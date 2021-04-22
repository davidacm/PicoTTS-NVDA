#synthDrivers/pico.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2010 Aleksey Sadovoy <lex@progger.ru>, Michael Curran <mick@kulgan.net>
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import ctypes, os, queue, threading
import config, nvwave, speech
from collections import OrderedDict
from io import BytesIO
from synthDriverHandler import synthDoneSpeaking, SynthDriver, synthIndexReached, VoiceInfo
from logHandler import log

# compatibility with nvda 2021.1 alpha versions.
try:
	from speech.commands import IndexCommand
except ImportError:
	from speech import IndexCommand

import addonHandler
addonHandler.initTranslation()

BASE_PATH=os.path.dirname(__file__)
SVOX_MEMORY_SIZE=3*1024**2

OUT_BUFFER_SIZE=4096 #it really generates 64 bytes at once

#from picoapi.h
pico_system = pico_resource = pico_engine = ctypes.c_void_p
PICO_STEP_IDLE = 200
PICO_STEP_BUSY = 201


class SynthDriver(SynthDriver):
	name = "pico"
	description = "Svox pico synthesizer"
	supportedSettings=(SynthDriver.VoiceSetting(),SynthDriver.RateSetting(),SynthDriver.PitchSetting(),SynthDriver.VolumeSetting())
	supportedCommands = {
		IndexCommand,
	}

	supportedNotifications = {synthIndexReached, synthDoneSpeaking}
	availableVoices=OrderedDict()
	availableVoices["en-us"] = VoiceInfo('en-us', _('American English'), "en-us")
	availableVoices["en-gb"] = VoiceInfo('en-gb', _('British English'), "en-gb")
	availableVoices["es"] = VoiceInfo('es', _('Spanish'), "es")
	availableVoices["fr"] = VoiceInfo('fr', _('French'), "fr")
	availableVoices["it"] = VoiceInfo('it', _('Italian'), "it")
	availableVoices["de"] = VoiceInfo('de', _('Deutch'), "de")
	_voice = 'en-us'
	pitch = 50
	rate = 50
	volume = 100

	#:tuples of (langName,langData,speakerData)
	voice_resources={
		'en-us': (b'American English', b'en-US_ta.bin', b'en-US_lh0_sg.bin'),
		'en-gb': (b'British English', b'en-GB_ta.bin', b'en-GB_kh0_sg.bin'),
		'es': (b'Spanish', b'es-ES_ta.bin', b'es-ES_zl0_sg.bin'),
		'fr': (b'French', b'fr-FR_ta.bin', b'fr-FR_nk0_sg.bin'),
		'it': (b'Italian', b'it-IT_ta.bin', b'it-IT_cm0_sg.bin'),
		'de': (b'Deutch', b'de-DE_ta.bin', b'de-DE_gl0_sg.bin'),
	}

	@classmethod
	def check(cls):
		return os.path.isfile(os.path.join(BASE_PATH, "svox-pico.dll"))

	def pico_system_errcheck(self,result,func,args):
		if result!=0:
			message=ctypes.create_string_buffer(200)
			self.dll.pico_getSystemStatusMessage(self.pico_system,result,message)
			raise RuntimeError("error while calling '%s' with arguments %s. underlying API reports: '%s'"%(func.__name__,args,message.value))
		return result

	def pico_engine_errcheck(self,result,func,args):
		if result<0:
			message=ctypes.create_string_buffer(200)
			self.dll.pico_getEngineStatusMessage(self.pico_engine, result, message)
			raise RuntimeError("error while calling '%s' with arguments %s. underlying API reports: '%s'"%(func.__name__,args,message.value))
		return result

	def __init__(self):
		self.dll=ctypes.cdll.LoadLibrary(os.path.join(BASE_PATH, 'svox-pico.dll'))
		#prepare dll object
		system_functs = ('pico_initialize', 'pico_terminate', 'pico_getSystemStatusMessage', 'pico_getNrSystemWarnings',
		'pico_getSystemWarning', 'pico_loadResource', 'pico_unloadResource', 'pico_getResourceName', 'pico_createVoiceDefinition', 'pico_addResourceToVoiceDefinition',
		'pico_releaseVoiceDefinition', 'pico_newEngine', 'pico_disposeEngine')
		for func in system_functs:
			getattr(self.dll,func).errcheck=self.pico_system_errcheck
		engine_funcs = ('pico_putTextUtf8', 'pico_getData', 'pico_resetEngine', 'pico_getEngineStatusMessage', 'pico_getNrEngineWarnings', 'pico_getEngineWarning')
		for func in engine_funcs:
			getattr(self.dll, func).errcheck = self.pico_engine_errcheck
		#init pico system
		self._svox_memory = ctypes.create_string_buffer(SVOX_MEMORY_SIZE)
		self.pico_system = pico_system()
		self.dll.pico_initialize(self._svox_memory, SVOX_MEMORY_SIZE, ctypes.byref(self.pico_system))
		self.pico_engine = None
		self.player = nvwave.WavePlayer(channels=1, samplesPerSec=16000, bitsPerSample=16, outputDevice=config.conf["speech"]["outputDevice"])
		self.queue = queue.Queue()
		self.isSpeaking = False
		self.background_thread = threading.Thread(target=self.background_thread_func)
		self.background_thread.daemon  = True
		self.background_thread.start()
		self._set_voice("es")
		#log the version
		#version_string=ctypes.create_string_buffer(200)
		#self.dll.picoext_getVersionInfo(version_string,200)
		#log.info("Using pico version '%s'"%version_string.value)

	def load_resources(self, name, langData, speakerData):
		"""Loads lingware data, defines voice"""
		langRes = pico_resource()
		self.dll.pico_loadResource(self.pico_system, os.path.join(BASE_PATH.encode('mbcs'), b'svox-pico-data', langData), ctypes.byref(langRes))
		langResName=ctypes.create_string_buffer(200)
		self.dll.pico_getResourceName(self.pico_system, langRes, langResName)
		speakerRes = pico_resource()
		self.dll.pico_loadResource(self.pico_system, os.path.join(BASE_PATH.encode('mbcs'), b'svox-pico-data', speakerData), ctypes.byref(speakerRes))
		speakerResName=ctypes.create_string_buffer(200)
		self.dll.pico_getResourceName(self.pico_system, speakerRes, speakerResName)
		self.dll.pico_createVoiceDefinition(self.pico_system, name)
		self.dll.pico_addResourceToVoiceDefinition(self.pico_system, name, langResName)
		self.dll.pico_addResourceToVoiceDefinition(self.pico_system, name, speakerResName)
		self._resources = (name, langRes, speakerRes)

	def free_resources(self):
		if not self._resources: return
		self.dll.pico_releaseVoiceDefinition(self.pico_system,self._resources[0])
		self.dll.pico_unloadResource(self.pico_system,ctypes.byref(self._resources[1]))
		self.dll.pico_unloadResource(self.pico_system,ctypes.byref(self._resources[2]))
		self._resources=None

	def terminate(self):
		self.cancel()
		self.queue.put((None,None))
		self.background_thread.join()
		self.player.close()
		self.player=None
		if self.pico_engine:
			self.dll.pico_disposeEngine(self.pico_system,ctypes.byref(self.pico_engine))
		self.free_resources()
		self.dll.pico_terminate(ctypes.byref(self.pico_system))
		self.pico_system=None
		del self.dll

	def _get_voice(self):
		return self._voice

	def _set_voice(self,value):
		name = self.voice_resources[value][0]
		if self.pico_engine:
			self.cancel()
			self.queue.join()
			self.dll.pico_disposeEngine(self.pico_system,ctypes.byref(self.pico_engine))
			self.free_resources()
		self.load_resources(*self.voice_resources[value])
		self.pico_engine = pico_engine()
		self.dll.pico_newEngine(self.pico_system,  name, ctypes.byref(self.pico_engine))
		self._voice = value

	def build_string(self,s):
		"""applies voice parameters"""
		pitch=self.pitch+50 if self.pitch<=50 else self.pitch*2
		speed = int(20 +(self.rate/50.0) *80) if self.rate<=50 else 100 +(self.rate-50)*8
		volume = self.volume*0.7
		return ('<pitch level="%d"><speed level="%d"><volume level="%d">%s</volume></speed></pitch>' %(pitch, speed, volume, s)).encode('utf-8')

	def background_thread_func(self):
		bytes_sent=ctypes.c_int16()
		out_buffer=ctypes.create_string_buffer(OUT_BUFFER_SIZE)
		bytes_received=ctypes.c_int16()
		data_type=ctypes.c_int16()
		while True:
			data, index = self.queue.get()
			if data is None:
				break
			synthIndexReached.notify(synth=self, index=index)
			remaining=len(data)+1
			while remaining and self.isSpeaking:
				self.dll.pico_putTextUtf8(self.pico_engine, data, remaining, ctypes.byref(bytes_sent))
				remaining-=bytes_sent.value
				data=data[bytes_sent.value:]
				status=PICO_STEP_BUSY
				buf=BytesIO()
				while self.isSpeaking and status==PICO_STEP_BUSY:
					status=self.dll.pico_getData(self.pico_engine, out_buffer, OUT_BUFFER_SIZE, ctypes.byref(bytes_received), ctypes.byref(data_type))
					if status==PICO_STEP_BUSY:
						buf.write(ctypes.string_at(out_buffer, bytes_received.value))
						if buf.tell() >= 4096:
							self.player.feed(buf.getvalue())
							buf.seek(0)
							buf.truncate(0)
					else:
						if buf.tell():
							self.player.feed(buf.getvalue())
						synthDoneSpeaking.notify(synth=self)
						self.player.idle()
				if not self.isSpeaking: #stop requested during playback
					self.dll.pico_resetEngine(self.pico_engine,0)
			self.lastIndex=None
			self.queue.task_done()

	def cancel(self):
		#clear queue
		try:
			while True:
				self.queue.get_nowait()
				self.queue.task_done()
		except queue.Empty:
			pass
		self.isSpeaking=False
		self.player.stop()
		self.lastIndex=None

	def speak(self,speechSequence):
		self.isSpeaking=True
		textList=[]
		index=None
		for item in speechSequence:
			if isinstance(item, str):
				textList.append(item)
			elif isinstance(item,IndexCommand):
				index=item.index
		text = " ".join(textList)
		if text:
			self.queue.put((self.build_string(text), index))

	def pause(self,switch):
		self.player.pause(switch)

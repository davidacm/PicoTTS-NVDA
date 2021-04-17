# svox-pico driver for NVDA.
  This add-on implements NVDA compatibility with the svox-pico synthesizer.  
  The pico-tts binaries for Windows are included in this repo.
  If you want to improve this driver, feel free to send your pull requests!  

# Download.
The latest release is available to [download in this link](https://davidacm.github.io/getlatest/gh/davidacm/PicoTTS-NVDA)

You can change the voice language, rate, pitch and volume from NVDA's voice settings.
Currently this driver doesn't support realtime changing parameters.

# Requirements.
You need to use aNVDA version with python 3.7, this driver is not compatible with python 2 versions. It has been tested with NVDA 2021 alpha version and the 2020.4 stable version.

# Installation.
  Just install it as an NVDA add-on.

# Packaging it for distribution.
  Open the command line, change to the Add-on root folder  and run the scons command. The created add-on, if there were no errors, is placed in the root directory.

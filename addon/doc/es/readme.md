# Controlador svox-pico para NVDA.
    Este complemento implementa la compatibilidad de NVDA con el sintetizador svox-pico.  
  El binario pico-tts  para Windows está incluido en este repositorio.
  Si deseas contribuir a mejorar este controlador ¡siéntete libre de enviar tus aportes vía un pull requests!  

# Descargar.
La última versión está disponible para  [descargar desde este enlace](https://davidacm.github.io/getlatest/gh/davidacm/PicoTTS-NVDA)

Puedes cambiar el idioma de voz, velocidad, tono y volumen  en la categoría Opciones de voz de NVDA.
Actualmente, este controlador no admite los parámetros que cambian en tiempo real.

# Requisitos.
Debes usar una versión  de NVDA con Python 3.7, este controlador no es compatible con las versiones  de Python 2. Se ha probado con la versión alfa de NVDA 2021 y la versión estable 2020.4.

  # Instalación.
  Simplemente instálelo como cualquier otro complemento de NVDA.
  
  # Empaquetar el complemento para su distribución.
  Abra una línea de comandos, cambie al directorio raíz del complemento y ejecute el comando scons. El complemento creado, si no hay errores, será puesto en la carpeta raíz del complemento.
  
# Colaborando a este proyecto.
## Donaciones.
  Si te gusta mi proyecto o este software es útil para  ti en tu vida diaria y te gustaría contribuir de alguna manera, puede donar a través de paypal en el
  [enlace donar.](https://paypal.me/davicm)

  déjame saber si deseas escribir un mensaje o promover un enlace en la sección colaboración.

## Aviso importante.
Este controlador se bifurcó desde una versión anterior desarrollada por los autores de NVDA. Lamentablemente, no pude obtener el repositorio oficial.

## Corrección de errores y nuevas características.
  Si deseas solucionar un error o agregar una nueva característica, deberás   hacer un fork de este repositorio.

  ### Bifurcando el repositorio.
  Si esta es tu primera contribución, primero deberás hacer un "fork" del repositorio "PicoTTS-NVDA" en GitHub:

  1. Hacer un fork de este repositorio en tu cuenta de GitHub.
  2. Clona el repositorio una vez que has hecho  la bifurcación localmente: "git clone yourRepoUrl".
  3. Añade este repositorio en tu repositorio bifurcado desde una línea de comandos:  
  "git remote add davidacm https://github.com/davidacm/PicoTTS-NVDA.git".
  4. fetch para recuperar mis ramas:  
  "git fetch davidacm".
  5. Saltar a la rama master   local: "git checkout master".
  6. Ajustar  el master local para usar el  master davidacm como su upstream:  
  "git branch -u davidacm/master".  

### Pasos antes de la codificación.
  Debes usar una rama "tema" por separado para cada incidencia o característica. Todo el código generalmente debe basarse en el último commit en la rama master oficial en el momento en que comienzas el trabajo.
  Entonces, antes de comenzar a trabajar, haz lo siguiente:

  1. Recuerda los pasos de la sección "Bifurcando el repositorio".
  2. Checkout para saltar a la rama master: "git checkout master".
  3. Actualizar el master local: "git pull".
  4. Crear una nueva rama basada en la   rama master actualizada: "git checkout -b TuNuevaRama".
  5. Escribe tu código.
  6. Añade tu trabajo  para tu próxima confirmación (commited) (limpiar archivos no deseados primero): git "add ."
  7. Crear una confirmación (commit): "git commit" y escribe el mensaje del commit.
  8. Enviar (push) tu rama en tu repositorio: "git push". Si la rama no existe, Git te dirá cómo lidiar con esto.
  9. Solicitud de integración (Pull Request) en mi repositorio.


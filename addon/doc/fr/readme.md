# Pilote  svox-pico pour NVDA.
    Cette extension implémente la compatibilité NVDA avec le synthétiseur svox-pico.  
  Le binaire pico-tts pour Windows est inclus dans ce dépôt.
  Si vous souhaitez améliorer ce pilote, n'hésitez pas à envoyer librement vos pull requests!  

# Télécharger.
La dernière version est disponible  pour son [téléchargement à partir de ce lien](https://davidacm.github.io/getlatest/gh/davidacm/PicoTTS-NVDA)

Vous pouvez changer la langue de la voix, débit, hauteur et volume dans la catégorie Parole de NVDA.
Actuellement, ce pilote ne prend pas en charge les paramètres qui changent en temps réel.

# Exigences.
Vous devez utiliser une version NVDA avec Python 3.7, ce pilote n'est pas compatible avec les versions de Python 2. Il a été testé avec la version alpha de NVDA 2021 et la version stable 2020.4.

  # Installation.
  Installez-le simplement comme n'importe quel extension NVDA.
  
  # Empaquetage de l'extension pour sa distribution.
  Ouvrez une ligne de commande, changer le dossier racine de l'extension et exécutez la commande scons. L'extension créée, s'il n'y a pas d'erreur, sera placée dans le dossier racine de l'extension.
  
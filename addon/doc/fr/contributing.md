# Collaborer sur ce projet.
## Faire un don.
  Si vous aimez mon projet ou que ce logiciel vous est utile dans votre vie quotidienne et que vous souhaitez contribuer d'une manière ou d'une autre, vous pouvez faire un don via PayPal sur le
  [lien Faire un don.](https://paypal.me/davicm)

  Faites-moi savoir si vous souhaitez écrire un message ou promouvoir un lien dans la section Collaborer .

## Avis important.
Ce pilote a été dupliqué d'une version antérieure développée par les auteurs de NVDA. Malheureusement, je n'ai pas pu obtenir le dépôt officiel.

## Correction des erreurs et de nouvelles fonctionnalités.
  Si vous souhaitez résoudre une erreur ou ajouter une nouvelle fonctionnalité, vous devez faire  un fork de ce dépôt.

  ### Obtenir une copie du dépôt.
  S'il s'agit de votre première contribution, vous devez d'abord créer un "fork" du dépôt "PicoTTS-NVDA" sur GitHub:
1. Faire un fork de ce  dépôt dans votre compte  GitHub.
  2. Cloner le dépôt une fois que vous avez fait   la bifurcation localement: "git clone yourRepoUrl".
  3. Ajouter ce dépôt dans votre dépôt dupliqué à partir d'une ligne de commande:  
  "git remote add davidacm https://github.com/davidacm/PicoTTS-NVDA.git".
  4. fetch pour récupérer mes branches:  
  "git fetch davidacm".
  5. Aller à la branche master locale: "git checkout master".
  6. Ajuster le master locale pour utiliser le master davidacm comme son upstream:  
  "git branch -u davidacm/master".  

### Étapes avant le codage.
  Vous devez utiliser une branche "thématique " séparément pour chaque incidence ou caractéristique. Tout le code doit généralement être basé sur le dernier commit sur la branche master officielle au moment où le travail commence.
  Ensuite, avant de commencer à travailler, procédez comme suit:

  1. Rappelez-vous les étapes de la section "Obtenir une copie du dépôt".
  2. Checkout pour aller à la branche master: "git checkout master".
  3. Mettre à jour le master locale: "git pull".
  4. Créer une nouvelle branche basé sur la branche master mis à jour: "git checkout -b VotreNouvelleBranche".
  5. Ecrivez votre code.
  6. Ajouter votre travail pour la prochaine validation (commited) (nettoyer les fichiers indésirables d'abord): git "add ."
  7. Créer une validation (commit): "git commit" et saisissez un message de commit.
  8. Pousser (push) votre branche sur votre dépôt: "git push". Si la branche n'existe pas, GIT vous dira comment traiter cela.
  9. Requêtes de tirage  (Pull Request) sur mon dépôt.

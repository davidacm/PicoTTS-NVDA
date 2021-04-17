# svox-pico driver for NVDA.
  This add-on implements NVDA compatibility with the svox-pico synthesizer.  
  The pico-tts binaries for Windows are included in this repo.
  If you want to improve this driver, feel free to send your pull requests!  

# Download.
The latest release is available to [download in this link](https://davidacm.github.io/getlatest/gh/davidacm/PicoTTS-NVDA)

You can change the voice language, rate, pitch and volume from NVDA's voice settings.
Currently this driver doesn't support realtime changing parameters.

This driver was forked from an older version developed by NVDA's authors. Sadly, I was unable to get the oficial repository.

# Contributing to this project.
## Donations.
  If you like my project or this software is useful for you in your daily life and you would like to contribute in some way, you can donate via paypal in the
  [donate link.](https://paypal.me/davicm)

  let me know if you want to write a message or promote a link in the collaboration section.

## fixing bugs and new features.
  If you want to fix a bug or add new feature, You will need to fork this repository.

  ### Forking the repository.
  If this is your first contribution, you will first need to "fork" the "PicoTTS-NVDA" repository on GitHub:

  1. Fork this repo in your github account.
  2. Clone your forked repo locally: "git clone yourRepoUrl".
  3. Add this repo in your forked repo from the command line:  
  "git remote add davidacm https://github.com/davidacm/PicoTTS-NVDA.git".
  4. fetch my branches:  
  "git fetch davidacm".
  5. Switch to the local master branch: "git checkout master".
  6. Set the local master to use the davidacm  master as its upstream:  
  "git branch -u davidacm/master".  

### Steps before coding.
  You must use a separate "topic" branch for each issue or feature. All code should usually be based on the latest commit in the official master branch at the time you start the work.
  So, before begin to work, do the following:

  1. Remember the steps of "Forking the repository" section.
  2. Checkout to master branch: "git checkout master".
  3. Update the local master: "git pull".
  4. Create a new branch based on the updated master branch: "git checkout -b YourNewBranch".
  5. write your code.
  6. Add your work to be commited (clean unwanted files first): git "add ."
  7. create a commit: "git commit" and write the commit message.
  8. push your branch in your repository: "git push". if the branch doesn't exist, git will tell you how to deal with this.
  9. Request a pull request on my repository.

# Requirements.
You need to use aNVDA version with python 3.7, this driver is not compatible with python 2 versions. It has been tested with NVDA 2021 alpha version and the 2020.4 stable version.

# Installation.
  Just install it as an NVDA add-on.

# Packaging it for distribution.
  Open the command line, change to the Add-on root folder  and run the scons command. The created add-on, if there were no errors, is placed in the root directory.

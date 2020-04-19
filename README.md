# Ignition
Version 0.0.3 [![Build Status](https://travis-ci.org/Spiffily/ignition.svg?branch=master)](https://travis-ci.org/Spiffily/ignition)

Hit the ground running on your fresh Ubuntu installation.

Download for testing here:

<a href="https://snapcraft.io/ignition">
<img alt="Get it from the Snap Store" src="https://snapcraft.io/static/images/badges/en/snap-store-black.svg" />
</a>

(`sudo snap install ignition --edge --devmode` at the moment)

The Linux world is full of apps. You could be looking for an app that does something, only to find that there are literally hundreds of options. Ignition will show you common apps for certain categories and explain their little nuances in an easy format. Just choose the ones to install, and Ignition will start the engine.

  This app is still in `devel/alpha`. It isn't fully functional and should only be used for development and testing purposes.

  ## Status

  | Item    | Status     | Description |
  | ------- | ---------- | ---------- |
  | app     | pre-alpha  | -- |
  | run     | good       | `python3 ignition.py` |
  | build   | good       | Still confused about this process, but snapcraft builds it fine. |
  | publish | **error**  | Learn, debug, work - Error: `/snap/ignition/2/usr/bin/python3: can't open file 'ignition.py': [Errno 2] No such file or directory` |
  | backend | *rebuilding* | Thanks Byron! |
  | gui     | *rebuilding* | Rebuilding to consist of a better organized category system and a qeue. |
  | website | notstarted | To be made on github.io |


## Ideas

### Package Managers
The system would be divided into package manager options. The italicized options would be available right away:
- _apt_
- _snapd_
- _.deb_
- flatpak
- npm
- .AppImage
- _.sh_

### App Categories
App categories will be divided like this (maybe with some small revisions):
- Basics (and Personalization)
- Web Browsers and Communication
- Cloud and File Sharing
- Games (different from Gaming)
- Security
- Office
- Professional (I think this needs a different name)
  - Programming
  - Media Production
  - Gaming
  - Super User (aka Hacking tools)
  - Engineering
  - More...

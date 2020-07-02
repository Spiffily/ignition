<div align=center>
<img src="Armature.svg" width="100" />

# Ignition

  <a href="https://github.com/Spiffily/ignition">
  <img  alt="Version" src="https://img.shields.io/badge/version-0.0.4-blueviolet" />
  </a>
  <a href="https://github.com/Spiffily/ignition">
  <img  alt="Code Size" src="https://img.shields.io/badge/app%20size-63.9%C2%A0kB-yellowgreen" />
  </a>
  <a href="https://travis-ci.org/Spiffily/ignition">
  <img  alt="Build Status" src="https://travis-ci.org/Spiffily/ignition.svg?branch=master" />
  </a>
  <a href="https://gitter.im/Spiffily/ignition?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge">
  <img  alt="Join the chat at https://gitter.im/Spiffily/ignition" src="https://badges.gitter.im/Spiffily/ignition.svg" />
  </a>

<!-- [![Version](https://img.shields.io/badge/version-0.0.4-blueviolet)](https://github.com/Spiffily/ignition) [![Code Size](https://img.shields.io/badge/app%20size-63.9%C2%A0kB-yellowgreen)](https://github.com/Spiffily/ignition) [![Build Status](https://travis-ci.org/Spiffily/ignition.svg?branch=master)](https://travis-ci.org/Spiffily/ignition) [![Join the chat at https://gitter.im/Spiffily/ignition](https://badges.gitter.im/Spiffily/ignition.svg)](https://gitter.im/Spiffily/ignition?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) -->

Hit the ground running on your fresh Linux installation.

Download for testing here:

<a href="https://snapcraft.io/ignition">
<img alt="Get it from the Snap Store" src="https://snapcraft.io/static/images/badges/en/snap-store-black.svg" />
</a>

(`sudo snap install ignition --edge --devmode` at the moment)

The Linux world is full of apps. You could be looking for an app that does something, only to find that there are literally hundreds of options. Ignition will show you common apps for certain categories and explain their little nuances in an easy format. Just choose the ones to install, and Ignition will start the engine.

  This app is still in alpha. It isn't fully functional and should only be used for development and testing purposes.

## Status

| Item    | Status     | Description |
| ------- | ---------- | ---------- |
| app     | pre-alpha  | -- |
| run     | good       | `python3 ignition.py` or `./ignition.py` |
| build   | good       | Still confused about this process, but snapcraft builds it fine. |
| publish | **error**  | Learn, debug, work - Error: `/snap/ignition/2/usr/bin/python3: can't open file 'ignition.py': [Errno 2] No such file or directory` |
| backend | *rebuilding* | Rebuilding to use a flexible bash script-based backend. |
| gui     | *rebuilding* | Rebuilding to consist of a better organized category system and a qeue. |
| website | notstarted | To be made on github.io |


## Ideas

### Package Managers

<div align=left>

The system would be divided into package manager options. The italicized options would be available later:
- apt
- pacman *(pacman and aur both fall under this name)*
- snapd
- .deb
- flatpak
- .AppImage
- *.rpm*
- *dnf*
- .sh (Custom script)
- *npm*
- *apm*

</div>

### App Categories

<div align=left>

App categories will be divided like this (maybe with some small revisions):
- Personalization
- Internet
- Media
- Games (little desktop games like solitaire)
- Security
- Office
- Professional (I think this could use a different name)
  - Programming
  - Media Production
  - Gaming (this category is for more serious games like Minecraft and Steam)
  - Super User (aka hacking software and advanced tools)
  - Server (services that can do things for other computers)
  - Engineering
  - More...

</div>

  ## Other Useful Resources
  https://wiki.voidlinux.org/Rosetta_stone packagment command stuff.

</div>

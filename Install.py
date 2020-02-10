from os import * # Import bash run abilities
from os.path import expanduser
home = expanduser("~")

import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

class Install():
    def __init__(self):
        print("Installer Ready")
#  ____            _          
# | __ )  __ _ ___(_) ___ ___ 
# |  _ \ / _` / __| |/ __/ __|
# | |_) | (_| \__ \ | (__\__ \
# |____/ \__,_|___/_|\___|___/
    def allbasics(self, button):
        self.neofetch(button)
        self.gdebi(button)
        self.redshift(button)
        self.gnometweaks(button)
        self.baobab(button)
        self.wine(button)
        self.safeeyes(button)
        self.sl(button)

    def neofetch(self, button):
        print("Installing Neofetch via Aptitude")
        system("pkexec apt-get --yes install neofetch && exit")

    def redshift(self, button):
        print("Installing RedShift via Aptitude")
        system("pkexec apt-get --yes install redshift && exit")

    def baobab(self, button):
        print("Installing Baobab via Aptitude")

    def wine(self, button):
        print("Installing Wine Is Not an Emulator via Aptitude")

    def safeeyes(self, button):
        print("Installing Safe Eyes via Aptitude")
        system("pkexec apt-get --yes install safeeyes && exit")

    def sl(self, button):
        print("Installing Steamengine Locomotive via Aptitude")

    def gdebi(self, button):
        print("Installing Gdebi via Aptitude")
        system("pkexec apt-get --yes install gdebi && exit")

    def gnometweaks(self, button):
        print("Installing Gnome-Tweaks via Aptitude")
        system("pkexec apt-get --yes install gnome-tweaks && exit")

    def virtualbox(self, button):
        print("Installing Oracle VirtualBox via Aptitude")
#  _                           _                   
# | |    __ _ _   _ _ __   ___| |__   ___ _ __ ___ 
# | |   / _` | | | | '_ \ / __| '_ \ / _ \ '__/ __|
# | |__| (_| | |_| | | | | (__| | | |  __/ |  \__ \
# |_____\__,_|\__,_|_| |_|\___|_| |_|\___|_|  |___/

    def synapse(self, button):
        print("Installing Synapse via Aptitude")
        system("pkexec apt-get --yes install synapse && exit")

    def plank(self, button):
        print("Installing Plank dock via Aptitude")

    def ulauncher(self, button):
        print("Installing ULauncher via Gdebi")

    def cario(self, button):
        print("Installing Cario dock via Aptitude")
#  ____                                      
# | __ ) _ __ _____      _____  ___ _ __ ___ 
# |  _ \| '__/ _ \ \ /\ / / __|/ _ \ '__/ __|
# | |_) | | | (_) \ V  V /\__ \  __/ |  \__ \
# |____/|_|  \___/ \_/\_/ |___/\___|_|  |___/

    def chromiumapt(self, button):
        print("Installing Chromium via Aptitude")
        system("pkexec apt-get --yes install chromium-browser chromium-chromedriver chromium-codecs-ffmpeg chromium-bsu && exit")

    def chromium(self, button):
        print("Installing Chromium via snapd")
        system("pkexec snap install chromium && exit")

    def firefox(self, button):
        print("Installing Firefox via Aptitude")
        system("pkexec apt-get --yes install firefox firefoxdriver firefox-globalmenu && exit")

    def thunderbird(self, button):
        print("Installing Thunderbird local email client via Aptitude")

    def mailspring(self, button):
        print("Installing Mailspring via Snapd")

    def midori(self, button):
        print("Installing Midori via snapd")
        system("pkexec snap install midori && exit")

    def googleearth(self, button):
        print("Installing Google Earth via Aptitude")
#   ____ _                 _ 
#  / ___| | ___  _   _  __| |
# | |   | |/ _ \| | | |/ _` |
# | |___| | (_) | |_| | (_| |
#  \____|_|\___/ \__,_|\__,_|

    def googletools(self, button):
        print("Installing Google Tools Desktop via Snapd")

    def yakyak(self, button):
        print("Installing YakYak via Snapd")

    def ggmail(self, button):
        print("Installing Gnome Gmail via Snapd")

    def insync3(self, button):
        print("Installing Insync 3 via Gdebi")
#   ____                           
#  / ___| __ _ _ __ ___   ___  ___ 
# | |  _ / _` | '_ ` _ \ / _ \/ __|
# | |_| | (_| | | | | | |  __/\__ \
#  \____|\__,_|_| |_| |_|\___||___/

    def ggames(self, button):
        print("Installing the Gnome Games Suite via Aptitude")
        system("pkexec apt-get --yes install gnome-games && exit")

    def steam(self, button):
        print("Installing Steam via wget and gdebi")
        system("wget https://steamcdn-a.akamaihd.net/client/installer/steam.deb && pkexec gdebi steam.deb && exit")

    def minecraft(self, button):
        print("Installing Minecraft via wget and gdebi")
        system("wget https://launcher.mojang.com/download/Minecraft.deb && pkexec gdebi Minecraft.deb && exit")

    def supertuxkart(self, button):
        print("Installing SuperTuxKart via snapd")
        system("pkexec snap install supertuxkart && exit")

    def gnomebreakout(self, button):
        print("Installing Gnome Breakout via Aptitude")
        system("pkexec apt-get --yes install gnome-breakout && exit")
    
    def ggamesapp(self, button):
        print("Installing the Gnome Games App via Aptitude")
        system("pkexec apt-get --yes install gnome-games-app && exit")

#   ___   __  __ _          
#  / _ \ / _|/ _(_) ___ ___ 
# | | | | |_| |_| |/ __/ _ \
# | |_| |  _|  _| | (_|  __/
#  \___/|_| |_| |_|\___\___|

    def libreofficeall(self, button):
        print("Installing full LibreOffice suite and accessories via Aptitude")
        print()
        self.libreoffice(button)
        self.libreofficeext(button)

    def libreoffice(self, button):
        print("Installing full LibreOffice suite via Aptitude")
        system("pkexec apt-get --yes install libreoffice-common libreoffice-writer libreoffice-impress libreoffice-base libreoffice-calc libreoffice-math libreoffice-draw && exit")

    def libreofficeext(self, button):
        print("Installing LibreOffice suite accessories via Aptitude")
        system("pkexec apt-get --yes install libreoffice-style-sifr libreoffice-java-common libreoffice-pdfimport libreoffice-systray && exit")

    def openofficedesktopeditors(self, button):
        print("Installing OPENOFFICE Desktop Editors via Snapd")

    def abiword(self, button):
        print("Installing Abiword via Aptitude")

    def gnumeric(self, button):
        print("Installing Gnumeric via Aptitude")

    # def googletools()

    def micropad(self, button):
        print("Installing microPad via Snapd")

    def p3xonenote(self, button):
        print("Installing P3X-Onenote")
        system("pkexec snap install p3x-onenote && exit")

    def apacheopenoffice(self, button):
        print("Installing Apache Open Office suite via Gdebi")

    def projectlibre(self, button):
        print("Installing Project Libre via Snapd")
#  _____ _                              
# |_   _| |__   ___ _ __ ___   ___  ___ 
#   | | | '_ \ / _ \ '_ ` _ \ / _ \/ __|
#   | | | | | |  __/ | | | | |  __/\__ \
#   |_| |_| |_|\___|_| |_| |_|\___||___/
    def papirus(self, button):
        print("Installing Papirus Icon Theme via Aptitude")
        system("pkexec apt-get --yes install papirus-icon-theme && exit")

    def pocillo(self, button):
        print("Installing Pocillo Icon Theme via Aptitude")
        system("pkexec apt-get --yes install pocillo-icon-theme && exit")

    def faenza(self, button):
        print("Installing Faenza Icon Theme via Aptitude")
        system("pkexec apt-get --yes install faenza-icon-theme && exit")

    def pling(self, button):
        print("Installing the Pling Store by this process:")
        print("    1.Download PlingStore_______.AppImage via wget")
        print("    2.Move it to /usr/share/")
        print("    3.Mark it as executable by chmod 777")
        print("    4.Add a .desktop file generated by Ignition to /usr/share/applications/")
        print()

    def xscreensaver(self, button):
        print("Installing XScreenSaver v_____ and all screensavers via Aptitude")

#  __  __          _ _       
# |  \/  | ___  __| (_) __ _ 
# | |\/| |/ _ \/ _` | |/ _` |
# | |  | |  __/ (_| | | (_| |
# |_|  |_|\___|\__,_|_|\__,_|

    def vlc(self, button):
        print("Installing VLC Media Player and DVD (.VOB) support via Aptitude")

    def rhythmbox(self, button):
        print("Installing Rhythmbox and all plugins via Aptitude")

    def spotify(self, button):
        print("Installing Spotify via Snapd")

    def pavucontrol(self, button):
        print("Installing Pulse Audio VolUme Control via Aptitude")

    def gstreamer(self, button):
        print("Installing all GStreamer Audio Codecs via Aptitude")

    def flashplayer(self, button):
        print("Installing Adobe Flash Player support for Chromium and Firefox via Aptitude")

    def gimageviewer(self, button):
        print("Installing Gnome Image Viewer via Aptitude")

    def totem(self, button):
        print("Installing Totem (Gnome Videos) via Aptitude")
#  _____               
# |_   _|__  _   _ ___ 
#   | |/ _ \| | | / __|
#   | | (_) | |_| \__ \
#   |_|\___/ \__, |___/
#            |___/     
    def bb(self, button):
        print("Installing BB from AA via Aptitude")

    def libaabin(self, button):
        print("Installing the AA Binary Executable Library from AA via Aptitude")

#  _____                   _             _     
# |_   _|__ _ __ _ __ ___ (_)_ __   __ _| |___ 
#   | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | / __|
#   | |  __/ |  | | | | | | | | | | (_| | \__ \
#   |_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_|___/

    def tilix(self, button):
        print("Installing Tilix via Aptitude")
        system("pkexec apt-get --yes install tilix && exit")

    def terminator(self, button):
        print("Installing Terminator via Aptitude")

    def gterminal(self, button):
        print("Installing Gnome Terminal via Aptitude")

    def xfceterminal(self, button):
        print("Installing Xfce4 Terminal via Aptitude")

    def lxterminal(self, button):
        print("Installing Lxterminal via Aptitude")

    def xterm(self, button):
        print("Installing XTerm via Aptitude")

    def mateterminal(self, button):
        print("Installing MATE Terminal via Aptitude")

    def konsole(self, button):
        print("Installing Konsole from KDE via Aptitude")
#  ____                                                _             
# |  _ \ _ __ ___   __ _ _ __ __ _ _ __ ___  _ __ ___ (_)_ __   __ _ 
# | |_) | '__/ _ \ / _` | '__/ _` | '_ ` _ \| '_ ` _ \| | '_ \ / _` |
# |  __/| | | (_) | (_| | | | (_| | | | | | | | | | | | | | | | (_| |
# |_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|_| |_| |_|_|_| |_|\__, |
#                  |___/                                       |___/ 
    def git(self, button):
        print("Installing Git Source Control Management via Aptitude")
        system("pkexec apt-get --yes install git && exit")

    def code(self, button):
        print("Installing VS Code IDE via snapd")
        system("pkexec snap install code --classic && exit")

    def atom(self, button):
        print("Installing Atom IDE via snapd")
        system("pkexec snap install atom --classic && exit")

    def sublime(self, button):
        print("Installing Sublime Text IDE (Trial version) via Snapd")

    def androidstudio(self, button):
        print("Installing Android Studio from Google via Snapd")

    def gedit(self, button):
        print("Installing Gedit via Aptitude")

    def mousepad(self, button):
        print("Installing Lxterminal via Aptitude")

    def eclipse(self, button):
        print("Installing Eclipse IDE via snapd")
        system("pkexec snap install eclipse --classic && exit")
#  __  __          _ _         ____                _            _   _             
# |  \/  | ___  __| (_) __ _  |  _ \ _ __ ___   __| |_   _  ___| |_(_) ___  _ __  
# | |\/| |/ _ \/ _` | |/ _` | | |_) | '__/ _ \ / _` | | | |/ __| __| |/ _ \| '_ \ 
# | |  | |  __/ (_| | | (_| | |  __/| | | (_) | (_| | |_| | (__| |_| | (_) | | | |
# |_|  |_|\___|\__,_|_|\__,_| |_|   |_|  \___/ \__,_|\__,_|\___|\__|_|\___/|_| |_|
    def gimp(self, button):
        print("Installing GIMP via Snapd")
    
    def blender(self, button):
        print("Installing Blender via Snapd")

    def inkscape(self, button):
        print("Installing Inkscape via Snapd")

    def openshot(self, button):
        print("Installing Open Shot media editor via Aptitude")

    def kdenlive(self, button):
        print("Installing Kdenlive media editor from KDE via Snapd")

    def krita(self, button):
        print("Installing Krita via Snapd")

    def ubuntustudio(self, button):
        print("Installing Ubuntu Studio Installer via Aptitude")
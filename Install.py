from os import * # Import bash run abilities
from os.path import expanduser
home = expanduser("~")

import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

class Install():
    def __init__(self):
        print()
#  ____            _          
# | __ )  __ _ ___(_) ___ ___ 
# |  _ \ / _` / __| |/ __/ __|
# | |_) | (_| \__ \ | (__\__ \
# |____/ \__,_|___/_|\___|___/

    def neofetch(self, button):
        print("Installing Neofetch via Aptitude")
        system("pkexec apt-get --yes install neofetch && exit")

    def redshift(self, button):
        print("Installing RedShift via Aptitude")
        system("pkexec apt-get --yes install redshift && exit")

    def safeeyes(self, button):
        print("Installing Safe Eyes via Aptitude")
        system("pkexec apt-get --yes install safeeyes && exit")

    def gdebi(self, button):
        print("Installing Gdebi via Aptitude")
        system("pkexec apt-get --yes install gdebi && exit")

    def gnometweaks(self, button):
        print("Installing Gnome-Tweaks via Aptitude")
        system("pkexec apt-get --yes install gnome-tweaks && exit")
#  _                           _                   
# | |    __ _ _   _ _ __   ___| |__   ___ _ __ ___ 
# | |   / _` | | | | '_ \ / __| '_ \ / _ \ '__/ __|
# | |__| (_| | |_| | | | | (__| | | |  __/ |  \__ \
# |_____\__,_|\__,_|_| |_|\___|_| |_|\___|_|  |___/

    def synapse(self, button):
        print("Installing Synapse via Aptitude")
        system("pkexec apt-get --yes install synapse && exit")
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

    def midori(self, button):
        print("Installing Midori via snapd")
        system("pkexec snap install midori && exit")

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

    def libreoffice(self, button):
        print("Installing full LibreOffice suite via Aptitude")
        system("pkexec apt-get --yes install libreoffice-common libreoffice-writer libreoffice-impress libreoffice-base libreoffice-calc libreoffice-math libreoffice-draw && exit")

    def libreofficeext(self, button):
        print("Installing LibreOffice suite accessories via Aptitude")
        system("pkexec apt-get --yes install libreoffice-style-sifr libreoffice-java-common libreoffice-pdfimport libreoffice-systray && exit")

    def p3xonenote(self, button):
        print("Installing P3X-Onenote")
        system("pkexec snap install p3x-onenote && exit")
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

#  __  __          _ _       
# |  \/  | ___  __| (_) __ _ 
# | |\/| |/ _ \/ _` | |/ _` |
# | |  | |  __/ (_| | | (_| |
# |_|  |_|\___|\__,_|_|\__,_|

    def vlc(self, button):
        print("Installing VLC Media Player via Aptitude")
#  _____               
# |_   _|__  _   _ ___ 
#   | |/ _ \| | | / __|
#   | | (_) | |_| \__ \
#   |_|\___/ \__, |___/
#            |___/     
    def bb(self, button):
        print("Installing BB from AA via Aptitude")

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
#!/bin/env python3.7
from os import * # Import bash run abilities
from os.path import expanduser
home = expanduser("~")

import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

from Install import *

class HomeWindow(Gtk.ApplicationWindow):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ignition")
        system("mkdir ~/.local/share/ignition/")
        self.appdata = home+"/.local/share/ignition/"

        installer = Install()

        tabs = Gtk.Notebook.new()
        tabsnames = ["Basics", "Launchers", "Browsers", "Cloud", "Games", "Office", "Themes", "Media", "Toys", "Terminals", "Programming", "Media Production"]
        basicsnames = ["All", "Neofetch", "Gdebi", "Redshift", "Gnome Tweaks", "Baobab", "WINE", "Safe Eyes", "Steamengine Locomotive"]
        launchersnames = ["Synapse", "Plank", "ULauncher", "Cario"]
        browsersnames = ["Chromium", "Firefox", "Midori (Very Light)"]
        cloudnames = ["Google Tools", "YakYak", "Gnome Gmail"]
        gamesnames = ["Gnome Games", "Steam", "Minecraft", "Super Tux Kart"]
        officenames = ["Libreoffice", "OPENOFFICE Desktop Editors", "Abiword", "Gnumeric", "Google Tools", "OpenOffice", "ProjectLibre"]
        themesnames = ["Papirus Icon Theme", "Pocillo Icon Theme", "Faenza Icon Theme", "Pling Store", "XScreenSaver"]
        medianames = ["VLC Media Player", "Rhythmbox", "Spotify", "PAVU Control", "GStreamer Codecs", "Gnome Image Viewer", "Totem"]
        toysnames = ["BB", "AA Lib"]
        terminalsnames = ["Tilix", "Terminator", "Gnome Terminal", "Xfce Terminal", "LXTerminal", "XTerm", "MATE Terminal", "Konsole"]
        programmingnames = ["GIT SCM", "VS Code", "Atom", "Sublime", "Android Studio", "Gedit", "Mousepad"]
        mediaproductionnames = ["GIMP Photo Editor", "Blender", "Inkscape", "Open Shot", "Kdenlive", "Krita"]
        
        for i in tabsnames:
            tabgrid = i
            tabgrid = Gtk.Grid.new()
            tabs.insert_page(tabgrid, Gtk.Label.new(i), -1)

            # tabgrid.insert()

        self.add(tabs)
            
    def install(self, button, name):
        print("Install called")

win = HomeWindow()

win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
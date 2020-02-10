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
        # system("mkdir ~/.local/share/ignition/")
        # self.appdata = home+"/.local/share/ignition/"

        installer = Install()

        tabs = Gtk.Notebook.new()
        tabsnames = ["Basics", "Launchers", "Browsers", "Cloud", "Games", "Office", "Themes", "Media", "Toys", "Terminals", "Programming", "Media Production"]
        
        basicsnames = ["All", "Neofetch", "Gdebi", "Redshift", "Gnome Tweaks", "Baobab", "WINE", "Safe Eyes", "Steamengine Locomotive"]
        launchersnames = ["Synapse", "Plank", "ULauncher", "Cario"]
        browsersnames = ["Chromium", "Firefox", "Midori (Very Light)"]
        cloudnames = ["Google Tools", "YakYak", "Gnome Gmail"]
        gamesnames = ["Gnome Games App", "Steam", "Minecraft", "Gnome Games Suite", "Super Tux Kart", "Gnome Breakout"]
        officenames = ["Libreoffice", "OPENOFFICE Desktop Editors", "Abiword", "Gnumeric", "Google Tools", "microPad", "P3X Onenote", "OpenOffice", "ProjectLibre"]
        themesnames = ["Papirus Icon Theme", "Pocillo Icon Theme", "Faenza Icon Theme", "Pling Store", "XScreenSaver"]
        medianames = ["VLC Media Player", "Rhythmbox", "Spotify", "PAVU Control", "GStreamer Codecs", "Gnome Image Viewer", "Totem"]
        toysnames = ["BB", "AA Lib"]
        terminalsnames = ["Tilix", "Terminator", "Gnome Terminal", "Xfce Terminal", "LXTerminal", "XTerm", "MATE Terminal", "Konsole"]
        programmingnames = ["GIT SCM", "VS Code", "Atom", "Sublime", "Android Studio", "Gedit", "Mousepad"]
        mediaproductionnames = ["GIMP Photo Editor", "Blender", "Inkscape", "Open Shot", "Kdenlive", "Krita", "Ubuntu Studio"]
        gridlistlist = [basicsnames, launchersnames, browsersnames, cloudnames, gamesnames, officenames, themesnames, medianames, toysnames, terminalsnames, programmingnames, mediaproductionnames]
        allitems = []
        filler = Gtk.Button.new()
        allitemsmethods = ["allbasics(filler)", "neofetch(filler)", "gdebi(filler)", "redshift(filler)", "gnometweaks(filler)", "baobab(filler)", "wine(filler)", "safeeyes(filler)", "sl(filler)"", synapse(filler)", "plank(filler)", "ulauncher(filler)", "cario(filler)", "chromium(filler)", "firefox(filler)", "midori(filler)", "googletools(filler)", "yakyak(filler)", "ggmail(filler)", "ggamesapp(filler)", "steam(filler)", "minecraft(filler)", "ggames(filler)", "supertuxkart(filler)", "gnomebreakout(filler)", "libreofficeall(filler)", "openofficedesktopeditors(filler)", "abiword(filler)", "gnumeric(filler)", "googletools(filler)", "micropad(filler)", "p3xonenote(filler)", "apacheopenoffice(filler)", "projectlibre(filler)", "papirus(filler)", "pocillo(filler)", "faenza(filler)", "pling(filler)", "xscreensaver(filler)", "vlc(filler)", "rhythmbox(filler)", "spotify(filler)", "pavucontrol(filler)", "gstreamer(filler)", "gimageviewer(filler)", "totem(filler)", "bb(filler)", "aalibbin(filler)", "tilix(filler)", "terminator(filler)", "gterminal(filler)", "xfceterminal(filler)", "lxterminal(filler)", "xterm(filler)", "mateterminal(filler)", "konsole(filler)", "git(filler)", "code(filler)", "atom(filler)", "sublime(filler)", "androidstudio(filler)", "gedit(filler)", "mousepad(filler)", "eclipse(filler)", "gimp(filler)", "blender(filler)", "inkscape(filler)", "openshot(filler)", "kdenlive(filler)", "krita(filler)", "ubuntustudio(filler)"]
        
        for gridlist in gridlistlist:
            for item in gridlist:
                allitems.append(item)
        print(allitems)
        
        k = 0
        for gridlist in gridlistlist:
            name = tabsnames[k]
            tabgrid = name
            tabgrid = Gtk.Grid.new()

            # print(gridlist)

            row = 0
            col = 0

            for item in gridlist:

                button = Gtk.Button.new() 
                button.set_label(item)
                if col is 0:
                    # print("Attach")
                    tabgrid.attach(button, col, row, 2, 1)
                else:
                    # print("Attach Next To")
                    tabgrid.attach_next_to(button, prevbutton, Gtk.PositionType.RIGHT, 2, 1)

                prevbutton = button

                if col >= 7:
                    row = row + 1
                    col = 0
                else:
                    col = col + 1

            tabs.insert_page(tabgrid, Gtk.Label.new(name), -1)
            k = k + 1

        self.add(tabs)
            
    def install(self, button, name):
        print("Install called")

win = HomeWindow()

win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
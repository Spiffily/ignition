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
        
        basicsnames = ["All Basics", "Neofetch", "Gdebi", "Redshift", "Gnome Tweaks", "Baobab", "WINE", "Safe Eyes", "Steamengine Locomotive"]
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
        # filler = Gtk.Button.new()
        allitemsmethods = ["allbasics()", "neofetch()", "gdebi()", "redshift()", "gnometweaks()", "baobab()", "wine()", "safeeyes()", "sl()", "synapse()", "plank()", "ulauncher()", "cario()", "chromium()", "firefox()", "midori()", "googletools()", "yakyak()", "ggmail()", "ggamesapp()", "steam()", "minecraft()", "ggames()", "supertuxkart()", "gnomebreakout()", "libreofficeall()", "openofficedesktopeditors()", "abiword()", "gnumeric()", "googletools()", "micropad()", "p3xonenote()", "apacheopenoffice()", "projectlibre()", "papirus()", "pocillo()", "faenza()", "pling()", "xscreensaver()", "vlc()", "rhythmbox()", "spotify()", "pavucontrol()", "gstreamer()", "gimageviewer()", "totem()", "bb()", "aalibbin()", "tilix()", "terminator()", "gterminal()", "xfceterminal()", "lxterminal()", "xterm()", "mateterminal()", "konsole()", "git()", "code()", "atom()", "sublime()", "androidstudio()", "gedit()", "mousepad()", "eclipse()", "gimp()", "blender()", "inkscape()", "openshot()", "kdenlive()", "krita()", "ubuntustudio()"]
        
        for gridlist in gridlistlist:
            for item in gridlist:
                allitems.append(item)
        # print(allitems)
        # print(allitemsmethods)
        
        k = 0
        installapps = self.get_methods(installer)
        # print(installapps)
        for gridlist in gridlistlist:
            name = tabsnames[k]
            tabgrid = name
            tabgrid = Gtk.Grid.new()

            # print(gridlist)

            row = 0
            col = 0

            for item in gridlist:
                # allitemmethod = allitemsmethods[k]
                button = Gtk.Button.new() 
                button.set_label(item)
                # button.connect("clicked", installer.allitemmethod)
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

    def get_methods(self, object):
        spacing=20
        methodList = []
        for method_name in dir(object): 
            try: 
                if callable(getattr(object, method_name)): 
                    methodList.append(str(method_name)) 
            except: 
                print("")
                # methodList.append(str(method_name)) 
        processFunc = (lambda s: ' '.join(s.split())) or (lambda s: s) 
        for method in methodList: 
            try: 
                print(str(method.ljust(spacing)) + ' ' + 
                    processFunc(str(getattr(object, method).__doc__)[0:90])) 
            except: 
                print(method.ljust(spacing) + ' ' + ' getattr() failed')

        for method in methodList:
            if method.startswith('_'):
                methodList.remove(method)

        return methodList 

    # def install(self, button, name):
    #     print("Install called")

win = HomeWindow()

win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
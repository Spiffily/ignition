#!/usr/bin/env python3
from os import * # Import bash run abilities
from os.path import expanduser
home = expanduser("~")
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ListBoxWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Ignition Layout")
        self.set_border_width(10)
        self.set_size_request(720, 512)
        self.set_wmclass ("Ignition", "Ignition")
        self.set_icon_from_file(home+'/ignition/ignition/Armature.svg')

        
    # Apps are laid out like this: package_name = ['Nice Name', ['defaultsource', 'othersources'], 'extras_sh_name', 'command']
        #Personalization Apps
        ## Launchers
        synapse = ['Synapse', ['apt'], '']
        plank = ['Plank', ['apt'], '']
        
        ## Stores
        gnome_software = ['Gnome Software', ['apt'], '']

        #Internet Apps
        ## Browsers
        google_chrome = ['Google Chrome', ['deb'], '']
        chromium = ['Chromium', ['snap'], '']
        firefox = ['Firefox', ['apt'], '']
        midori = ['Midori', ['snap'], '']

        #Media Apps
        ## Players
        vlc = ['VLC Media Player', ['snap', 'apt'], '']

        ## Codecs
        gstreamer_codecs = ['GStreamer Codecs', ['apt'], '']
        
        #Personalization App Types
        personalizationtypelaunchers = ['App Launchers', synapse, plank]
        personalizationtypestores = ['Stores', gnome_software]

        #Internet App Types
        internettypebrowsers = ['Web Browsers', google_chrome, chromium, firefox, midori]

        #Media App Types
        mediatypeplayers = ['Media Players', vlc]
        mediatypecodecs = ['Media Codecs', gstreamer_codecs]

        #App Categories
        hometypes = ['Home']
        personalizationtypes = ['Personalization', personalizationtypelaunchers, personalizationtypestores]
        internettypes = ['Internet', internettypebrowsers]
        mediatypes = ['Media', mediatypeplayers, mediatypecodecs]
        # utilitiestypes = ['Nextcloud', 'Insync', 'Magic Wormhole', 'Barrier']
        # gamestypes = ['Gnome Games Collection', 'SuperTuxKart', 'Gnome Breakout', '0ad', 'GNU Jump', 'Micropolis']
        # securitytypes = ['Ufw', 'Canonical Livepatch', 'Macchanger', 'ClamTK', 'RKHunter']
        # officetypes = ['LibreOffice', 'ONLYOFFICE Desktop Editors', 'Abiword', 'Gnumeric', 'P3X Onenote']
        # categories = ['Home', 'Personalization', 'Internet', 'Utilities', 'Games', 'Security', 'Office']
        categories = [hometypes, personalizationtypes, internettypes, mediatypes]

        # box_home = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        categoryselect = Gtk.Notebook()
        #categoryselect.popup_enable()
        categoryselect.set_show_tabs(True)
        categoryselect.set_show_border(True)
        self.add(categoryselect)
        for appcategory in categories:
            categoryname = appcategory[0]
            box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
            categoryselect.insert_page(box, Gtk.Label(label=categoryname), -1)
            appcategory.remove(categoryname)
            # print(appcategory.lower()+'types')
            for apptype in appcategory:
                typebox = Gtk.ListBox()
                typebox.set_selection_mode(Gtk.SelectionMode.NONE) #(NONE, SINGLE, BROWSE, or MULTIPLE)
                typetitlerow = Gtk.ListBoxRow()
                typetitlerow.add(Gtk.Label(label=apptype[0]))
                apptype.remove(apptype[0])
                typebox.add(typetitlerow)
                print(apptype)
                for app in apptype:
                    # print(app)
                    try:
                        print(app)
                        appname = app[0]
                        appsources = app[1]
                        appextras = app[2]
                        print(appname)
                        print(appsources)
                        print(appextras)

                        row = Gtk.ListBoxRow()
                        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)
                        row.add(hbox)
                        to_install_switch = Gtk.Switch()
                        hbox.pack_start(to_install_switch, False, True, 0)
                        hbox.pack_start(Gtk.Label(label=appname), False, True, 0)

                        typebox.add(row)
                    except:
                        print('App not loaded')
                box.add(typebox)


            # listbox = Gtk.ListBox()
            # listbox.set_selection_mode(Gtk.SelectionMode.NONE) #(NONE, SINGLE, BROWSE, or MULTIPLE)
            # box_home.pack_start(listbox, True, True, 0)

            # row = Gtk.ListBoxRow()
            # hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)
            # row.add(hbox)
            # label = Gtk.Label(label="VLC Media Player")
            # check = Gtk.CheckButton()
            # hbox.pack_start(check, False, True, 0)
            # hbox.pack_start(label, False, True, 0)
            # # hbox.pack_start(Gtk.Widget(), True, False, 0)
            # combo = Gtk.ComboBoxText()
            # combo.insert(0, "0", "Aptitude")
            # combo.insert(1, "1", "Snappy")
            # combo.set_active(1)
            # # hbox.pack_start(Gtk.Label(label="Source:"), False, True, 0)
            # # hbox.pack_start(combo, False, True, 0)
            # # extraswitch = Gtk.Switch()
            # # hbox.pack_start(Gtk.Label(label="Extras:"), False, True, 0)
            # # hbox.pack_start(extraswitch, False, True, 0)

            # listbox.add(row)

        
win = ListBoxWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

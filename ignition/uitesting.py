#!/usr/bin/env python3
import os
from os import * # Import bash run abilities
from os.path import expanduser
home = expanduser("~")
path = os.getcwd()
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
import time


class ListBoxWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Ignition Layout")
        self.set_border_width(10)
        self.set_size_request(1024, 720)
        # self.set_wmclass ("Ignition", "Ignition") # Can be commented out while debuging, but should be uncommented for build
        self.set_icon_from_file(path+'/Armature.svg')
        
        apps_to_install = ['vlc', 'chrome'] # The master list of apps to be installed.
        head = Gtk.HeaderBar()
        self.set_titlebar(head)
        head.set_title('Ignition')
        head.set_show_close_button(True)
        install_button = Gtk.Button(label='Install')
        install_button.connect('clicked', self.install)
        # show_qeue_button = Gtk.Button(label='Qeue')
        head.pack_end(install_button) #pack Install button
        # head.pack_end(show_qeue_button) #pack Qeue button
        painsize = 610
        
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

        pains = Gtk.Paned()
        categoryselect = Gtk.Notebook()
        queue = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        pains.add1(categoryselect)
        # pains.add2(queue)
        pains.set_position(1024)
        pains.set_wide_handle(True)
        categoryselect.set_show_tabs(True)
        categoryselect.set_show_border(True)
        self.add(pains)
        # Draw the app selection part
        for appcategory in categories: # Make the App Category tabs at the top and fill them. (ex. Internet)
            categoryname = appcategory[0]
            box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
            categoryselect.insert_page(box, Gtk.Label(label=categoryname), -1)
            appcategory.remove(categoryname)
            # print(appcategory.lower()+'types')
            for apptype in appcategory: # Draw the subcategories of apps and fill them. (Ex. Browsers, Communication)
                typebox = Gtk.ListBox()
                typebox.set_selection_mode(Gtk.SelectionMode.NONE) #(NONE, SINGLE, BROWSE, or MULTIPLE)
                typetitlerow = Gtk.ListBoxRow()
                typetitlerow.add(Gtk.Label(label=apptype[0]))
                apptype.remove(apptype[0])
                typebox.add(typetitlerow)
                # print(apptype)
                for app in apptype: # Draw each app and all it's widgets. (Ex. Google Chrome, Chromium, Firefox)
                    # print(app)
                    try:
                        # print(app)
                        appname = app[0] # Set the appname from the lists
                        appsources = app[1] # Make a list of sources from the list
                        appextras = app[2] # If there's a bash script to install extras, set it's name from the list
                        # print(appname)
                        # print(appsources)
                        # print(appextras)

                        row = Gtk.ListBoxRow()
                        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)
                        row.add(hbox)
                        to_install_switch = Gtk.Switch()
                        hbox.pack_start(to_install_switch, False, True, 0)
                        hbox.pack_start(Gtk.Label(label=appname), False, True, 0)

                        typebox.add(row)
                    except:
                        print('ERROR: App not loaded')
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
            self.apps_to_install = apps_to_install

    def main(self):
        while(not Gtk.events_pending()):
            
            # winheight = 0
            # winwidth = 0
            winwidth = self.get_size()[0]
            time.sleep(1)
            print()
            print('Window width: ')
            print(winwidth)

    def install(self, button):
        print('Installing apps!')
        for app in self.apps_to_install:
            try:
                print('Installing app')

            except:
                print('ERROR: There was a problem installing this app.')

        
win = ListBoxWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
GLib.idle_add(win.main)
Gtk.main()

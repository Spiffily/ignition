#!/usr/bin/env python3
import os
from os import * # Import bash run abilities
from os.path import expanduser
home = expanduser("~")
path = os.getcwd()
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

data = home+'/.local/share/ignition/'
config = home+'/.config/ignition/'
system('mkdir '+data)
system('mkdir '+config)

class App():
    def __init__(self, package, name, sources, description):
        self.package = package
        self.script = data+'sh/'+package+'.sh'
        self.name = name
        self.sources = sources
        self.description = description
        # print(self.script)

    def row(self):
        switch = Gtk.Switch()
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        box.pack_start(switch, False, False, 2)
        box.pack_start(Gtk.Label(label=self.name), False, False, 0)

        return box

vlc = App('vlc', 'VLC', ['apt', 'snap', 'pacman'], 'A robust media player that will play pretty much anything.')

class AppList(Gtk.Notebook):
    def __init__(self):
        Gtk.Notebook.__init__(self)
        # Home
        catHome = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        catHome.pack_start(Gtk.Label(label='Hello!'), False, False, 1)

        # Personalization
        catPersonalization = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        launchers = Gtk.ListBox()
        launchers.set_selection_mode(Gtk.SelectionMode.BROWSE)
        # catPersonalization.pack_start(Gtk.Label(label='Launchers'), False, False, 0)
        catPersonalization.pack_start(launchers, False, False, 0)
        row = Gtk.ListBoxRow()
        row.add(Gtk.Label(label='Launchers'))
        row.set_selectable(False)
        launchers.add(row)
        row = Gtk.ListBoxRow()
        row.add(vlc.row())
        launchers.add(row)

        catInternet = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        catMedia = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        catGames = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        catSecurity = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        catOffice = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)

        catProgramming = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        catMediaProduction = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        catGaming = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        catSuperUser = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        catEngineering = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)

        

        # categories = Gtk.Notebook()
        self.insert_page(catHome, Gtk.Label(label='Home'), -1)
        self.insert_page(catPersonalization, Gtk.Label(label='Personalization'), -1)
        self.insert_page(catInternet, Gtk.Label(label='Internet'), -1)
        self.insert_page(catMedia, Gtk.Label(label='Media'), -1)
        self.insert_page(catGames, Gtk.Label(label='Games'), -1)
        self.insert_page(catSecurity, Gtk.Label(label='Security'), -1)
        self.insert_page(catOffice, Gtk.Label(label='Office'), -1)

        # self.insert(categories)

class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ignition Layout")
        self.set_border_width(10)
        self.set_size_request(1024, 720)
        # self.set_wmclass ("Ignition", "Ignition") # Can be commented out while debuging, but should be uncommented for build
        self.set_icon_from_file(path+'/Armature.svg')
        
        apps_to_install = [] # The master list of apps to be installed.
        head = Gtk.HeaderBar()
        self.set_titlebar(head)
        head.set_title('Ignition')
        head.set_show_close_button(True)
        install_button = Gtk.Button(label='Install')
        # install_button.connect('clicked', self.install)
        # show_qeue_button = Gtk.Button(label='Qeue')
        head.pack_end(install_button) #pack Install button
        # head.pack_end(show_qeue_button) #pack Qeue button
        painsize = 610

        pains = Gtk.Paned()
        categoryselect = Gtk.Notebook()
        queue = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        pains.add1(categoryselect)
        # pains.add2(queue)
        pains.set_position(1024)
        pains.set_wide_handle(True)
        categoryselect.set_show_tabs(True)
        categoryselect.set_show_border(True)
        # self.add(pains)

        categories = AppList()
        self.add(categories)


win = Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
# GLib.idle_add(win.main)
Gtk.main()
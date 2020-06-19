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

# Personalization
## Launchers
synapse = App('synapse', 'Synapse', ['apt', 'pacman'], 'Semantic app and file launcher. Good alternative to Spotlight.')
ulauncher = App('ulauncher', 'uLauncher', ['deb', 'pacman'], 'Modern and shiny launcher that provides fuzzy search, extensions, and themes.')
plank = App('plank', 'Plank', ['apt', 'pacman'], 'Stupidly simple.')
## App Centers
gnome_software = App('gnome-software', 'Gnome Software', ['apt', 'snap', 'pacman'], 'GNOME\'s graphical software management tool.')
pling = App('pling', 'Pling Store', ['appimage', 'deb'], '')
discover = App('discover', 'KDE Discover', ['apt', 'pacman'], 'Application Installer for the 22nd Century.')
software_boutique = App('software-boutique', 'Software Boutique', ['apt'], '')

# Internet
## Web Browsers
chrome = App('chrome', 'Google Chrome', ['deb', 'pacman', 'snap', 'apt'], '')
vivaldi = App('vivaldi', 'Vivaldi', ['deb', 'pacman'], '')
firefox = App('firefox', 'Firefox', ['apt','pacman', 'snap', 'flatpak', 'sh'], '')
epiphany = App('epiphany', 'GNOME Web', ['apt', 'flatpak', 'pacman', 'snap'], 'Simple web browser for GNOME. Similar to Apple\'s Safari.')
midori = App('midori', 'Midori', ['snap', 'pacman', 'apt', 'deb', 'flatpak'], '')
# opera = App('')
## Internet Messagers
discord = App('discord', 'Discord', ['apt', 'pacman', 'snap', 'flatpak', 'deb'], '')
yakyak = App('yakyak', 'YakYak', ['apt', 'snap', 'pacman', 'deb'], 'A desktop client for Google Hangouts. It\'s very light, stable, simple, and customizable.')
# pidgin
# hexchat
## File Syncing
insync = App('insync', 'Insync', ['deb', 'pacman'], '')
nextcloud_client = App('nextcloud-client', 'Nextcloud Sync', ['flatpak', 'pacman', 'apt', 'appimage'], '')
syncthing_gtk = App('syncthing-gtk', 'Syncthing GTK', ['apt', 'pacman', 'flatpak'], 'A window-based desktop syncthing client with system tray.')
syncthing = App('syncthing', 'Syncthing', ['apt', 'pacman', 'sh'], 'A light, stable peer-to-peer file syncing client. Uses a web-based UI. For a desktop UI, use Syncthing GTK instead.')
# owncloud_client = 
## File Sharing/Getting
wormhole = App('wormhole', 'Magic Wormhole', ['apt', 'pacman', 'snap'], 'A fast, efficient, and secure peer-to-peer file and text sharing app. Works anywhere, anytime, over any distance.')
transporter = App('transporter', 'Transporter', ['snap', 'pacman'], 'A GUI frontend for Magic Wormhole.')
transmission_gtk = App('transmission-gtk', 'Transmission', ['apt', 'pacman', 'flatpak'], 'A simple and very popular BitTorrent client.')
kTorrent = App('ktorrent', 'kTorrent', ['apt', 'pacman', 'A KDE BitTorrent client.'], '')
onionshare = App('onionshare', 'OnionShare', ['apt', 'pacman'], 'Securely send any file with many layers of encryption and without leaving a trace.')

# Media
## Music Players
rhythmbox = App('rhythmbox', 'Rhythmbox', ['apt', 'pacman', 'flatpak'], 'A simple, popular music player.')
spotify = App('spotify', 'Spotify', ['snap', 'pacman', 'flatpak'], 'An online music streaming service and local music player.')

## Video Players
vlc = App('vlc', 'VLC', ['apt', 'snap', 'pacman'], 'Robust media player that will play pretty much anything.')

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
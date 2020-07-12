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
desktop_session = os.environ['XDG_CURRENT_DESKTOP'].lower()
# desktop_session = 'gnome'
system('mkdir '+data)
system('mkdir '+config)
labelpadding = 3

apps_to_install = ["vlc", "vivaldi"] # The master list of apps to be installed.

class App():
    def __init__(self, package, name, sources, description):
        self.package = package
        self.script = data+'sh/'+package+'.sh'
        self.name = name
        self.sources = sources
        self.description = description
        # print(self.script)

    def row(self):
        row = Gtk.ListBoxRow()
        switch = Gtk.Switch()
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        box.pack_start(switch, False, False, 2)
        box.pack_start(Gtk.Label(label=self.name), False, False, 0)
        row.add(box)

        return row

# Personalization
## Launchers
synapse = App('synapse', 'Synapse', ['apt', 'pacman'], 'Semantic app and file launcher. Good alternative to Spotlight.')
ulauncher = App('ulauncher', 'uLauncher', ['deb', 'pacman'], 'Modern and shiny launcher that provides fuzzy search, extensions, and themes.')
plank = App('plank', 'Plank', ['apt', 'pacman'], 'Stupidly simple.')
gnome_pie = App('gnome-pie', 'GNOME Pie', ['apt', 'pacman'], '')
## App Centers
gnome_software = App('gnome-software', 'Gnome Software', ['apt', 'pacman'], 'GNOME\'s graphical software management tool.')
pling = App('pling', 'Pling Store', ['appimage', 'deb'], '')
discover = App('discover', 'KDE Discover', ['apt', 'pacman'], 'Application Installer for the 22nd Century.')
snap_store = App('snap_store', 'Snap Store', ['snap'], 'The graphical desktop store for the snappy package manager. This app is based on GNOME Software and is optimized for snap, but will also show apps from other GNOME Software sources.')
software_boutique = App('software-boutique', 'Software Boutique', ['apt'], '')

# Internet
## Web Browsers
chrome = App('chrome', 'Google Chrome', ['deb', 'pacman', 'snap', 'apt'], '')
vivaldi = App('vivaldi', 'Vivaldi', ['deb', 'pacman'], '')
firefox = App('firefox', 'Firefox', ['apt','pacman', 'snap', 'flatpak', 'sh'], '')
epiphany = App('epiphany', 'GNOME Web', ['apt', 'flatpak', 'pacman', 'snap'], 'Simple web browser for GNOME. Similar to Apple\'s Safari.')
midori = App('midori', 'Midori', ['snap', 'pacman', 'apt', 'deb', 'flatpak'], '')
# opera = App('')
## Internet Messengers
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
ktorrent = App('ktorrent', 'kTorrent', ['apt', 'pacman', 'A KDE BitTorrent client.'], '')
fragments = App('fragments', 'Fragments', ['snap', 'pacman', 'flatpak'], 'A simple GTK BitTorrent client.')
onionshare = App('onionshare', 'OnionShare', ['apt', 'pacman'], 'Securely send any file with many layers of encryption and without leaving a trace.')

# Media
## Multimedia Players
vlc = App('vlc', 'VLC', ['apt', 'snap', 'pacman'], 'Robust media player that will play pretty much anything you throw at it.')
parole = App('parole', 'Parole', ['apt', ''], 'Modern and simple media player. Very light.')
celluloid = App('celluloid', 'Celluloid', ['apt', 'pacman'], 'Simple GTK+ frontend for mpv.')
mpv = App('mpv', 'mpv Media Player', ['apt', 'pacman'], 'A versatile media player backend. Can be operated from the command line or with a frontend like Celluloid.')

## Music Players
lollypop = App('lollypop', 'Lollypop', ['apt', 'pacman', 'flatpak'], 'An all-in-one music playing and streaming service. With a layout similar to Microsoft\'s Groove Music, this powerful yet simple app can stream from YouTube, Spotify and more, or play local files. It also has a builtin album cover detection service and even a lyric detection service.')
rhythmbox = App('rhythmbox', 'Rhythmbox', ['apt', 'pacman', 'flatpak'], 'A simple, popular music player.')
spotify = App('spotify', 'Spotify', ['snap', 'pacman', 'flatpak'], 'An online music streaming service and local music player.')
audacious = App('audacious', 'Audacious', ['apt', 'pacman'], 'A light, basic playlist based music player.')
clementine = App('clementine', 'Clementine', ['apt', 'pacman', 'snap', 'flatpak'], 'Plays music files and Internet radio.')

## Video Players
totem = App('totem', 'GNOME Videos', ['apt', 'pacman', 'flatpak'], 'Play movies.')
dragon = App('dragonplayer', 'Dragon Player', ['apt', 'pacman', 'snap'], 'A KDE side video player with focus on simplicity.')
slowmovideo = App('slowmovideo', 'slowmoUI', ['apt', 'pacman'], 'Slow Motion Video')
stretchplayer = App('stretchplayer', 'StretchPlayer', ['apt', 'pacman'], 'Audio file player with time stretch.')

## Discs (Compact Discs, Digital Video Discs, etc.)
brasero = App('brasero', 'Brasero', ['apt', 'pacman'], 'A stable and powerful disc manipulation tool.')
asunder = App('asunder', 'Asunder CD Ripper', ['apt', 'pacman'], 'An application to save tracks from an Audio CD as WAV, MP3, OGG, FLAC, and/or Wavpack.')



class AppList(Gtk.Notebook):
    def __init__(self):
        Gtk.Notebook.__init__(self)
        # STANDARD CATEGORIES
        ## Home
        catHome = Gtk.ListBox()
        catHome.set_selection_mode(Gtk.SelectionMode.BROWSE)
        row = Gtk.ListBoxRow()
        row.add(Gtk.Label(label='Welcome!'))
        row.set_selectable(False)
        catHome.add(row)
        row = Gtk.ListBoxRow()
        row.add(Gtk.Label(label='The app does stuff now, but still needs the rest of the apps and a qeue.'))
        row.set_selectable(False)
        catHome.add(row)

        catHomeScroll = Gtk.ScrolledWindow(child=catHome)

        ## Personalization
        catPersonalization = Gtk.ListBox()
        catPersonalization.set_selection_mode(Gtk.SelectionMode.BROWSE)
        row = Gtk.ListBoxRow()
        row.add(Gtk.Label(label='Launchers'))
        row.set_selectable(False)
        catPersonalization.add(row)
        catPersonalization.add(synapse.row())
        catPersonalization.add(ulauncher.row())
        catPersonalization.add(plank.row())
        catPersonalization.add(gnome_pie.row())

        row = Gtk.ListBoxRow()
        row.add(Gtk.Label(label='App Centers'))
        row.set_selectable(False)
        catPersonalization.add(row)
        catPersonalization.add(gnome_software.row())
        catPersonalization.add(pling.row())
        catPersonalization.add(discover.row())
        catPersonalization.add(snap_store.row())
        catPersonalization.add(software_boutique.row())

        catPersonalizationScroll = Gtk.ScrolledWindow(child=catPersonalization)

        ## Internet
        catInternet = Gtk.ListBox()
        catPersonalization.set_selection_mode(Gtk.SelectionMode.BROWSE)
        row = Gtk.ListBoxRow()
        row.add(Gtk.Label(label='Browsers'))
        row.set_selectable(False)
        catInternet.add(row)
        catInternet.add(chrome.row())
        catInternet.add(vivaldi.row())
        catInternet.add(firefox.row())
        catInternet.add(epiphany.row())
        catInternet.add(midori.row())

        row = Gtk.ListBoxRow()
        row.add(Gtk.Label(label='Internet Messengers'))
        row.set_selectable(False)
        catInternet.add(row)
        catInternet.add(discord.row())
        catInternet.add(yakyak.row())
        # catPersonalization.add(firefox.row()) #OTHERS...
        # catPersonalization.add(epiphany.row())
        # catPersonalization.add(midori.row())

        row = Gtk.ListBoxRow()
        row.add(Gtk.Label(label='File Syncing'))
        row.set_selectable(False)
        catInternet.add(row)
        catInternet.add(insync.row())
        catInternet.add(nextcloud_client.row())
        catInternet.add(syncthing.row())
        catInternet.add(syncthing_gtk.row())
        # catPersonalization.add(owncloud_client.row())

        row = Gtk.ListBoxRow()
        row.add(Gtk.Label(label='File Sharing (and Getting)'))
        row.set_selectable(False)
        catInternet.add(row)
        catInternet.add(wormhole.row())
        catInternet.add(transporter.row())
        catInternet.add(transmission_gtk.row())
        catInternet.add(ktorrent.row())
        catInternet.add(onionshare.row())

        catInternetScroll = Gtk.ScrolledWindow(child=catInternet)

        ## Media
        catMedia = Gtk.ListBox()
        catMedia.set_selection_mode(Gtk.SelectionMode.BROWSE)
        catMediaScroll = Gtk.ScrolledWindow(child=catMedia)

        row = Gtk.ListBoxRow()
        row.add(Gtk.Label(label='Music Players'))
        row.set_selectable(False)
        catMedia.add(row)
        catMedia.add(rhythmbox.row())
        catMedia.add(spotify.row())
        # catPersonalization.add(transmission_gtk.row())
        # catPersonalization.add(ktorrent.row())
        # catPersonalization.add(onionshare.row())

        ## Games
        catGames = Gtk.ListBox()
        catGames.set_selection_mode(Gtk.SelectionMode.BROWSE)
        catGamesScroll = Gtk.ScrolledWindow(child=catGames)

        ## Security
        catSecurity = Gtk.ListBox()
        catSecurity.set_selection_mode(Gtk.SelectionMode.BROWSE)
        catSecurityScroll = Gtk.ScrolledWindow(child=catSecurity)

        ## Office
        catOffice = Gtk.ListBox()
        catOffice.set_selection_mode(Gtk.SelectionMode.BROWSE)
        catOfficeScroll = Gtk.ScrolledWindow(child=catOffice)

        # PROFESSIONAL CATEGORIES
        catProfessional = Gtk.Notebook()

        ## Programming
        catProgramming = Gtk.ListBox()
        catProgramming.set_selection_mode(Gtk.SelectionMode.BROWSE)
        catProgrammingScroll = Gtk.ScrolledWindow(child=catProgramming)



        ## Media Production
        catMediaProduction = Gtk.ListBox()
        catMediaProduction.set_selection_mode(Gtk.SelectionMode.BROWSE)
        catMediaProductionScroll = Gtk.ScrolledWindow(child=catMediaProduction)

        ## Gaming
        catGaming = Gtk.ListBox()
        catGaming.set_selection_mode(Gtk.SelectionMode.BROWSE)
        catGamingScroll = Gtk.ScrolledWindow(child=catGaming)

        ## SuperUser
        catSuperUser = Gtk.ListBox()
        catSuperUser.set_selection_mode(Gtk.SelectionMode.BROWSE)
        catSuperUserScroll = Gtk.ScrolledWindow(child=catSuperUser)

        ## Server
        catServer = Gtk.ListBox()
        catServer.set_selection_mode(Gtk.SelectionMode.BROWSE)
        catServerScroll = Gtk.ScrolledWindow(child=catServer)

        ## Engineering
        catEngineering = Gtk.ListBox()
        catEngineering.set_selection_mode(Gtk.SelectionMode.BROWSE)
        catEngineeringScroll = Gtk.ScrolledWindow(child=catEngineering)

        # Add pages to Notebook
        self.insert_page(catHomeScroll, Gtk.Label(label='Home'), -1)
        self.insert_page(catPersonalizationScroll, Gtk.Label(label='Personalization'), -1)
        self.insert_page(catInternetScroll, Gtk.Label(label='Internet'), -1)
        self.insert_page(catMediaScroll, Gtk.Label(label='Media'), -1)
        self.insert_page(catGamesScroll, Gtk.Label(label='Games'), -1)
        self.insert_page(catSecurityScroll, Gtk.Label(label='Security'), -1)
        self.insert_page(catOfficeScroll, Gtk.Label(label='Office'), -1)
        self.insert_page(catProfessional, Gtk.Label(label='Professional'), -1)

        catProfessional.insert_page(catProgrammingScroll, Gtk.Label(label='Programming'), -1)
        catProfessional.insert_page(catMediaProductionScroll, Gtk.Label(label='Media Production'), -1)
        catProfessional.insert_page(catGamingScroll, Gtk.Label(label='Gaming'), -1)
        catProfessional.insert_page(catSuperUserScroll, Gtk.Label(label='Super User'), -1)
        catProfessional.insert_page(catServerScroll, Gtk.Label(label='Server'), -1)
        catProfessional.insert_page(catEngineeringScroll, Gtk.Label(label='Engineering'), -1)

class Queue(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)

        list = Gtk.ListBox()
        hi = Gtk.Label(label="Hello")
        self.pack_start(list, True, True, 0)

        # for app in apps_to_install:
        #     list.add(app.row())

        # self.pack_start(list, True, True, 0)


class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ignition")
        self.set_border_width(3)
        self.set_size_request(720, 512)
        # self.set_wmclass ("Ignition", "Ignition") # Can be commented out while debuging, but should be uncommented for build
        self.set_icon_from_file(path+'/Armature.svg')

        categories = AppList()
        queue = Queue()
        # queue = Gtk.Label(label="Qeeew")

        # toggle = Gtk.ComboBox()   # TODO: In future, I want this to look more like the 'Songs/Categories' toggle in Rhythmbox.
        # menu_selection_button = Gtk.ToggleButton.new_with_label("Main")
        # menu_switcher = Gtk.ToggleButton(label="Qeue")
        menu_switcher = Gtk.Stack()
        menu_switcher.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        menu_switcher.set_transition_duration(1000)
        menu_switcher.add_titled(categories, "box", "Apps")
        menu_switcher.add_titled(queue, "label", "Queue")
        menu_switcher_button = Gtk.StackSwitcher()
        menu_switcher_button.set_stack(menu_switcher)

        install_button = Gtk.Button(label="Install")
        # install_button.connect('clicked', self.install)

        print("Desktop Environment: "+desktop_session)
        if ("gnome" in desktop_session):
            head = Gtk.HeaderBar()
            self.set_titlebar(head)
            head.set_title("Ignition")
            head.set_show_close_button(True)

            head.pack_start(menu_switcher_button)
            head.pack_end(install_button) #pack Install button

            self.add(menu_switcher)
        else:
            head = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, )
            head.pack_start(menu_switcher_button, False, False, 0)
            head.pack_end(install_button, False, False, 0)

            body = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            body.pack_start(head, False, False, 0)
            body.pack_end(menu_switcher, True, True, 0)

            self.add(body)

        painsize = 610

        # pains = Gtk.Paned()
        # categoryselect = Gtk.Notebook()
        # queue = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        # pains.add1(categoryselect)
        # # pains.add2(queue)
        # pains.set_position(1024)
        # pains.set_wide_handle(True)
        # categoryselect.set_show_tabs(True)
        # categoryselect.set_show_border(True)
        # # self.add(pains)



win = Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
# GLib.idle_add(win.main)
Gtk.main()

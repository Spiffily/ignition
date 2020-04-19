#!/usr/bin/env python3
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ListBoxRowWithData(Gtk.ListBoxRow):
    def __init__(self, data):
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        self.add(Gtk.Label(data))

class ListBoxWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Ignition Layout")
        self.set_border_width(10)
        self.set_size_request(512, 256)
        self.set_wmclass ("Ignition", "Ignition")
        self.set_icon_from_file('/home/josh/ignition/Armature.svg')

        categories = {'Home', 'Personalization', 'Internet', 'File Management', 'Games', 'Security', 'Office', 'Professional'}
        
        box_home = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        categoryselect = Gtk.Notebook()
        #categoryselect.popup_enable()
        categoryselect.set_show_tabs(True)
        categoryselect.set_show_border(True)
        for categoryname in categories:
            box = 'box_'+categoryname
            box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            categoryselect.insert_page(box_home, Gtk.Label(label=categoryname), -1)

        self.add(categoryselect)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE) #(NONE, SINGLE, BROWSE, or MULTIPLE)
        box_home.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)
        row.add(hbox)
        label = Gtk.Label(label="VS Code")
        check = Gtk.CheckButton()
        hbox.pack_start(check, False, True, 0)
        hbox.pack_start(label, False, True, 0)
        

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)
        row.add(hbox)
        label = Gtk.Label(label="VLC Media Player")
        check = Gtk.CheckButton()
        hbox.pack_start(check, False, True, 0)
        hbox.pack_start(label, False, True, 0)
        # hbox.pack_start(Gtk.Widget(), True, False, 0)
        combo = Gtk.ComboBoxText()
        combo.insert(0, "0", "Aptitude")
        combo.insert(1, "1", "Snappy")
        combo.set_active(1)
        hbox.pack_start(Gtk.Label(label="Source:"), False, True, 0)
        hbox.pack_start(combo, False, True, 0)
        extraswitch = Gtk.Switch()
        hbox.pack_start(Gtk.Label(label="Extras:"), False, True, 0)
        hbox.pack_start(extraswitch, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)
        row.add(hbox)
        label = Gtk.Label(label="Pling Store")
        check = Gtk.CheckButton()
        hbox.pack_start(check, False, True, 0)
        hbox.pack_start(label, False, True, 0)


        listbox.add(row)
        
win = ListBoxWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

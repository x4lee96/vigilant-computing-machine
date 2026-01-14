#!/usr/bin/env python3

# requires nautilus, nautilus-python
# put in ~/.local/share/nautilus-python/extensions/
#     or /usr/share/nautilus-python/extensions/

TERMINAL_NAME='kitty'
TERMINAL_ARGS=[]

from gi import require_version
try:
    # nautilus 43+
    require_version('Gtk', '4.0')
    require_version('Nautilus', '4.0')
except ValueError:
    require_version('Gtk', '3.0')
    require_version('Nautilus', '3.0')

from gi.repository import Nautilus, GObject, Gio
import subprocess

def launch_terminal(path):
    subprocess.Popen([TERMINAL_NAME] + TERMINAL_ARGS, cwd=path, shell=False)

class TerminalExtension(Nautilus.MenuProvider, GObject.GObject):
    def __init__(self):
        pass

    def activate_terminal(self, menu: Nautilus.MenuItem, files):
        for f in files:
            if f.get_file_type() == Gio.FileType.DIRECTORY:
                launch_terminal(f.get_location().get_path())
            else:
                launch_terminal(f.get_parent_location().get_path())

    def get_file_items(self, *args):
        # `args` will be `[files: [Nautilus.FileInfo]]` in Nautilus 4.0 API
        # `args` will be `[window: Gtk.Widget, files: [Nautilus.FileInfo]]` in Nautilus 3.0 API

        item = Nautilus.MenuItem(name='TerminalFile', label='Open in Terminal')
        item.connect('activate', self.activate_terminal, args[-1])
        return [item]

    def get_background_items(self, *args):
        # `args` will be `[folder: Nautilus.FileInfo]` in Nautilus 4.0 API
        # `args` will be `[window: Gtk.Widget, file: Nautilus.FileInfo]` in Nautilus 3.0 API

        item = Nautilus.MenuItem(name='TerminalBackground', label='Open in Terminal')
        item.connect('activate', self.activate_terminal, [args[-1]])
        return [item]

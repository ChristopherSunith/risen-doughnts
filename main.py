import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

if __name__ == '__main__':
    print("Hello World\n")
    builder = Gtk.Builder()
    builder.add_from_file("./ui/mainscreen.glade")
    window = builder.get_object("window1")
    window.show_all()
    Gtk.main()

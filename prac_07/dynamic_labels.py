"""This Kivy App displays a list of names as individual labels"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class ListNames(App):
    """ Main program - Kivy App to list names """

    def __init__(self, **kwargs):
        """ Construct main app """
        super().__init__(**kwargs)
        self.names = ["Susan", "Mike", "Ben", "Mark"]

    def build(self):
        """ Build the Kivy GUI from kv file """
        self.title = "List Names"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.list_names()
        return self.root

    def list_names(self):
        """ Create labels using the names from 'names' list and add them to the GUI. """
        for name in self.names:
            temp_label = Label(text=name)
            # add the label to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_label)


ListNames().run()

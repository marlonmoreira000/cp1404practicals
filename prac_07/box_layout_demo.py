""" This Kivy GUI allows a user to enter their name.
 It then displays a greeting message if 'Greet' button is clicked """
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """ Construct main app """
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file("box_layout.kv")
        return self.root

    def handle_greet(self):
        """ Display greeting message on GUI """
        print("test")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def clear_field(self):
        """ Clear GUI fields """
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()

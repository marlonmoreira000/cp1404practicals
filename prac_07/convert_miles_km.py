""" This is a program that generates a GUI to convert miles to km """
from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

MILES_TO_KM = 1.609


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """ convert miles to km and display result """
        value = self.get_validated_miles()
        self.message = str(value * MILES_TO_KM)

    def handle_increment(self, change):
        """ increment the user_input value upp or down by a fixed number """
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """ get user_input text and convert to float if valid """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()

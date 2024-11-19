"""
CP1404 Practical
Kivy GUI program convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder


class MilesToKilometresConverter(App):
    """MilesToKilometresConverter is a Kivy App for converting miles to kilometres"""

    FORMULA = 1.609  # Conversion factor: 1 mile = 1.609 km

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Miles To Kilometres Converter"
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root

    def increment_miles(self, direction):
        """increment the miles by the given direction"""
        miles = self.validate_miles()
        miles += direction
        self.root.ids.input_miles.text = str(miles)

    def convert_miles(self):
        """Calculate the conversion from miles to kilometres"""
        miles = self.validate_miles()
        km = miles * self.FORMULA
        self.root.ids.output_label.text = str(km)

    def validate_miles(self):
        """Validate the miles input"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesToKilometresConverter().run()

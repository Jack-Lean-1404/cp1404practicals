"""
CP1404 Practical
Kivy GUI program convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder


class MilesToKilometresConverter(App):
    """MilesToKilometresConverter is a Kivy App for converting miles to kilometres"""
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Miles To Kilometres Converter"
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root

    # def handle_calculate(self, value):
    #     """ handle calculation (could be button press or other call), output result to label widget """
    #     try:
    #         result = float(value) ** 2
    #         self.root.ids.output_label.text = str(result)
    #     except ValueError:
    #         pass

    def increment_miles(self, direction):
        """increment the miles by the given direction"""
        miles = float(self.root.ids.input_miles.text)
        miles += direction
        self.root.ids.input_miles.text = str(miles)

    def convert_miles(self):
        """Calculate the conversion from miles to kilometres"""
        miles = float(self.root.ids.input_miles.text)
        km = miles * 1.609
        self.root.ids.output_label.text = str(km)


MilesToKilometresConverter().run()

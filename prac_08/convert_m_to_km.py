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


MilesToKilometresConverter().run()

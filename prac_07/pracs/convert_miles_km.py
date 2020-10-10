"""
CP1404/CP5632 Practical
m to km
Daniel Mackenzie
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

FACTOR_M_TO_KM = 1.609


class ConvertMilesKmApp(App):
    output = StringProperty()

    def build(self):
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, value):
        miles = self.convert_to_number(text) + value
        self.root.ids.input_m.text = str(miles)

    def update_result(self, miles):
        self.output = str(miles * FACTOR_M_TO_KM)

    @staticmethod
    def convert_to_number(text):
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesKmApp().run()


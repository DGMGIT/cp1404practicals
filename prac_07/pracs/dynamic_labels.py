"""
CP1404/CP5632 Practical
m to km
Daniel Mackenzie
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = {"Bob Brown", "Cat Cyan", "Oren Ochre", "sam sandwich"}

    def build(self):
        self.title = 'dynamic_labels'
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_labels = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_labels)


DynamicLabelsApp().run()

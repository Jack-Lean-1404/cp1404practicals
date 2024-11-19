from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App to dynamically create labels."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Plz", "No", "Uni", "Work", "Lindsay"]

    def build(self):
        """Build the Kivy app and dynamically add Labels."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Dynamically create the Labels."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabelsApp().run()

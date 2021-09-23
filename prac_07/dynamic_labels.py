from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        # TODO: After running it, add another entry to the dictionary and see how the layout changes
        self.list_of_names = {"Bob Brown", "Cat Cyan", "Oren Ochre", "John Doe"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.list_of_names:
            temp_label = Button(text=name)
            self.root.ids.entries_box.add_widget(temp_label)



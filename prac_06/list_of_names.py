from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class SimpleApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Jason Aprilio", "Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        self.title = "List of Names"
        self.root = Builder.load_file('list_of_names.kv')
        self.create_label()
        return self.root

    def create_label(self):
        for name in self.names:
            self.status_text = "{}".format(name)

SimpleApp().run()

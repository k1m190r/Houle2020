from pathlib import Path as P

from kivy.app import App
from kivy.lang import Builder

root = Builder.load_file("kivy_5.kv")

class APP(App):
    def build(self):
        return root

APP().run()
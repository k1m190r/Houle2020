from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file("kivy_7.kv")

class RootWidget(BoxLayout):
    pass

class CustomLayout(FloatLayout):
    pass

class APP(App):
    def build(self):
        return RootWidget()

APP().run()
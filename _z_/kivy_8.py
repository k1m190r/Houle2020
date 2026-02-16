from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_file("kivy_8.kv")

class RootWidget(FloatLayout):
    pass

class APP(App):
    def build(self):
        return RootWidget()
    

APP().run()
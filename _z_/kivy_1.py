import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require("2.3.1")

class App1(App):
    def build(self):
        return Label(text="hello")


App1().run()
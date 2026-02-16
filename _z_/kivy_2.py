import os

os.environ["KIVY_TEXT"] = "pil"

from kivy import Logger
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):
    def __init__(self, **kw):
        super(LoginScreen, self).__init__(**kw)
        s = self
        s.cols = 2
        s.add_widget(Label(text="USER"))
        s.username = TextInput(multiline=False)
        s.add_widget(s.username)
        s.add_widget(Label(text="PWD"))
        s.password = TextInput(password=True, multiline=False)
        s.add_widget(self.password)


class APP(App):
    def build(self):
        return LoginScreen()


APP().run()

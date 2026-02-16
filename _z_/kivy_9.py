from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file("kivy_9.kv")


class CustomLayout(GridLayout):
    im_url = r"im\button_white_animated.zip"
    background_image = ObjectProperty(Image(source=im_url, anim_delay=0.1))

class RootWidget(FloatLayout):
    pass

class APP(App):
    def build(self):
        return RootWidget()


APP().run()
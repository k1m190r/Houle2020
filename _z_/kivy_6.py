from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage


class ROOT(BoxLayout):
    pass


class CustLayout(FloatLayout):
    def __init__(self, **kw):
        s = self
        super(CustLayout, s).__init__(**kw)
        with s.canvas.before:
            Color(0, 1, 0, 1)
            s.rect = Rectangle(size=s.size, pos=s.pos)

        s.bind(size=s._update_rect, pos=s._update_rect)

    def _update_rect(self, inst, v):
        s = self
        s.rect.pos = inst.pos
        s.rect.size = inst.size


class APP(App):
    def build(self):
        r = ROOT()

        c = CustLayout()
        im_url1 = "https://i.imgur.com/pWewhaG.jpeg"
        c.add_widget(
            AsyncImage(
                source=im_url1,
                size_hint=(1, 0.5),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        r.add_widget(c)

        im_url2 = "https://i.imgur.com/NFdc6NF.png"
        c = CustLayout()
        c.add_widget(
            AsyncImage(
                source=im_url2,
                size_hint=(1, 0.5),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        r.add_widget(c)
        return r

APP().run()

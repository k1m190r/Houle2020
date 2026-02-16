from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class ROOT(FloatLayout):
    def __init__(self, **kw):
        sf = self
        super(ROOT, sf).__init__(**kw)
        btn = Button(
            text="Hello Button",
            size_hint=(0.5, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        sf.add_widget(btn)


class APP(App):
    def build(self):
        sf = self
        sf.root = root = ROOT()
        root.bind(size=sf._update_rect, pos=sf._update_rect)

        with root.canvas.before:
            Color(0, 1, 0, 1)
            sf.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, inst, value):
        sf = self
        sf.rect.pos = inst.pos
        sf.rect.size = inst.size


APP().run()

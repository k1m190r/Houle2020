from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
import numpy as np

rand = np.random.rand


class PaintWidget(Widget):
    def clear_canvas(self):
        self.ids.id_paint.canvas.clear()

    def on_touch_down(self, touch):
        for child in self.children:
            if child.dispatch("on_touch_down", touch):
                return True

        c = (rand(), 1, 1)
        with self.ids.id_paint.canvas:
            Color(*c, mode="hsv")
            t, d = touch, 6.0
            e_pos = (t.x - d / 2, t.y - d / 2)
            Ellipse(pos=e_pos, size=(d, d))
            t.ud["line"] = Line(points=(t.x, t.y))

        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        t = touch
        if "line" in t.ud:
            t.ud["line"].points += [t.x, t.y]


class PaintApp(App):
    def build(self):
        return PaintWidget()


PaintApp().run()

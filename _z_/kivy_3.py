from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty


class RootWidget(BoxLayout):
    def __init__(self, **kw):
        super(RootWidget, self).__init__(**kw)
        s = self

        s.padding = 10

        s.add_widget(Button(text="Button 1"))

        cb = CustomBtm()
        cb.bind(pressed=s.btn_pressed)
        s.add_widget(cb)

        self.bt2 = Button(text="Button 2")
        s.add_widget(self.bt2)

    def btn_pressed(self, instance, pos):
        print(f"pos: printed from root widget: {pos}")
        # self.remove_widget(self.bt2)
        # self.clear_widgets()
        for child in self.children:
            print(child)


class CustomBtm(Widget):
    pressed = ListProperty([0, 0])

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            return True  # consume
        return super(CustomBtm, self).on_touch_down(touch)

    def on_pressed(self, instance, pos):
        print(f"pressed at {pos}")


class APP(App):
    def build(self):
        return RootWidget()


APP().run()

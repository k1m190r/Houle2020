from pathlib import Path as P
from vispy import app, gloo
from vispy.gloo import Program

vertex = P("vertex.glsl").read_text()
fragment = P("fragment.glsl").read_text()


class Canvas(app.Canvas):
    def __init__(self):

        # init
        super().__init__(
            size=(512, 512),
            title="rotating quad",
            keys="interactive",
        )

        # program
        self.program = Program(vertex, fragment, count=4)
        self.program["color"] = [
            (1, 0, 0, 1),
            (0, 1, 0, 1),
            (0, 0, 1, 1),
            (1, 1, 0, 1),
        ]
        self.program["pos"] = [
            (-1, -1),
            (-1, +1),
            (+1, -1),
            (+1, +1),
        ]
        self.program["theta"] = 0.0

        # viewport
        gloo.set_viewport(0, 0, *self.physical_size)
        gloo.set_clear_color("white")

        # timer 
        self.timer = app.Timer("auto", self.on_timer)
        self.clock = 0
        self.timer.start()

        self.show()

    def on_draw(self, event):
        gloo.clear()
        self.program.draw("triangle_strip")

    def on_resize(self, event):
        gloo.set_viewport(0, 0, *event.physical_size)

    def on_timer(self, event):
        self.clock += 0.001 * 1000.0 / 60.0
        self.program["theta"] = self.clock
        self.update()
    
    def on_key_press(self, event):
        if event.text == " ":
            if self.timer.running:
                self.timer.stop()
            else:
                self.timer.start()


if __name__ == "__main__":
    c = Canvas()
    app.run()

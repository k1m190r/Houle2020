import vispy
from pathlib import Path as P
from vispy import app, gloo, visuals, scene
import numpy as np

vertex_shader = P("vertex.glsl").read_text()
fragment_shader = P("fragment.glsl").read_text()

vispy.use("glfw")


class RectVisual(visuals.Visual):
    def __init__(self):
        visuals.Visual.__init__(self, vertex_shader, fragment_shader)
        a = [[-1, -1], [1, -1], [1, 1], [-1, -1], [1, 1], [-1, 1]]
        self.vbo = gloo.VertexBuffer(np.array(a, dtype=np.float32))
        self.shared_program.vert["position"] = self.vbo
        self.set_gl_state(cull_face=False)
        self._draw_mode = "triangle_fan"

    def _prepare_transforms(self, view):
        tr = view.transforms.get_transform("framebuffer", "visual")
        view.view_program.frag["fb_to_visual"] = tr


Rect = scene.visuals.create_visual_node(RectVisual)

canvas = scene.SceneCanvas(keys="interactive", show=True)

view = canvas.central_widget.add_view()
view.camera = "panzoom"
view.camera.rect = (0, 0, 800, 800)

vis = Rect()
view.add(vis)


text = scene.visuals.Text(
    "Drag right mouse button to zoom.",
    color="w",
    anchor_x="left",
    font_size=18,
    face="Consolas",
    parent=view,
    pos=(20, 30),
)


if __name__ == "__main__":
    import sys

    if sys.flags.interactive != 1:
        app.run()

import vispy
from pathlib import Path as P
from vispy import app, gloo, visuals, scene
import numpy as np

vertex_shader = P("vertex.glsl").read_text()
fragment_shader = P("fragment.glsl").read_text()

vispy.use("Glfw")


class RectVisual(visuals.Visual):
    def __init__(self, x, y, w, h, weight=5.0):
        self.weight = weight
        visuals.Visual.__init__(self, vertex_shader, fragment_shader)

        self.vert_buffer = gloo.VertexBuffer(
            np.array(
                [
                    [x, y],
                    [x, y],
                    [x + w, y],
                    [x + w, y],
                    [x + w, y + h],
                    [x + w, y + h],
                    [x, y + h],
                    [x, y + h],
                    [x, y],
                    [x, y],
                ],
                dtype=np.float32,
            )
        )

        self.adj_buffer = gloo.VertexBuffer(
            np.array(
                [
                    [0, 0],
                    [1, 1],
                    [0, 0],
                    [-1, 1],
                    [0, 0],
                    [-1, -1],
                    [0, 0],
                    [1, -1],
                    [0, 0],
                    [1, 1],
                ],
                dtype=np.float32,
            )
        )

        self.shared_program.vert["position"] = self.vert_buffer
        self.shared_program.vert["adjust_dir"] = self.adj_buffer

        self.shared_program.vert["line_width"] = weight + 1
        self.shared_program.frag["color"] = (1, 0, 0, 1)
        self._draw_mode = "triangle_strip"
        self.set_gl_state(cull_face=False)

    def _prepare_transforms(self, view):
        tr = view.transforms
        view_vert = view.view_program.vert
        view_vert["visual_to_doc"] = tr.get_transform("visual", "document")
        view_vert["doc_to_render"] = tr.get_transform("document", "render")

        doc_to_fb = tr.get_transform("document", "framebuffer")
        fbs = np.linalg.norm(doc_to_fb.map([1, 0]) - doc_to_fb.map([0, 0]))
        view_frag = view.view_program.frag
        view_frag["doc_fb_scale"] = fbs
        view_frag["line_width"] = (self.weight + 1) * fbs


Rect = scene.visuals.create_visual_node(RectVisual)

canvas = scene.SceneCanvas(keys="interactive", show=True)

view = canvas.central_widget.add_view()
view.camera = "panzoom"
view.camera.rect = (0, 0, 800, 800)

rects = [
    Rect(x=100, y=100, w=200, h=300, parent=view.scene),
    Rect(x=500, y=100, w=200, h=300, parent=view.scene),
]

tr = visuals.transforms.MatrixTransform()
tr.rotate(25, (0, 0, 1))
rects[1].transform = tr

text = scene.visuals.Text(
    "Drag right mouse button to zoom.",
    color="w",
    anchor_x="left",
    font_size=18,
    face="Consolas",
    parent=view,
    pos=(20, 30),
)

text2 = scene.visuals.Text(
    "Drag right mouse button to zoom.",
    color="w",
    anchor_x="left",
    font_size=18,
    face="Consolas",
    parent=view,
    pos=(20, 45),
)


if __name__ == "__main__":
    import sys

    if sys.flags.interactive != 1:
        app.run()

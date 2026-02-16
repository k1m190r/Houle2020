uniform float theta;
attribute vec4 color;
attribute vec2 pos;
varying vec4 v_color;

void main() {
    float ct = cos(theta);
    float st = sin(theta);
    float x = 0.75 * (pos.x * ct - pos.y * st);
    float y = 0.75 * (pos.x * st + pos.y * ct);
    gl_Position = vec4(x, y, 0.0, 1.0);
    v_color = color;
}
void main() {
  vec4 pos = $fb_to_visual(gl_FragCoord);
  gl_FragColor = vec4(sin(pos.x / 10.), sin(pos.y / 10.), 0, 1);
}
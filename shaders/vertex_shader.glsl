#version 120

attribute vec2 a_position;
attribute vec2 a_tex_coord;
varying vec2 tex_coord;

void main() {
    gl_Position = vec4(a_position, 0.0, 1.0);
    tex_coord = a_tex_coord;
}
#version 120

attribute vec2 a_position;
attribute vec2 a_tex_coord;
varying vec2 tex_coord;

---VERTEX SHADER---
void main() {
    gl_Position = vec4(a_position, 0.0, 1.0);
    tex_coord = a_tex_coord;
}

---FRAGMENT SHADER---
void main() {
    vec4 color = texture2D(texture, tex_coord);
    float intensity = color.r;
    vec4 result_color;

    if (intensity < 0.5) {
        result_color = mix(gradient[0], gradient[1], intensity * 2.0);
    } else {
        result_color = mix(gradient[1], gradient[2], (intensity - 0.5) * 2.0);
    }

    gl_FragColor = result_color;
}
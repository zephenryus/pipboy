#version 120

uniform sampler2D texture;
uniform vec4 gradient[3];
varying vec2 tex_coord;

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
import os

from kivy import Config
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Line, Fbo, BindTexture, ClearColor, ClearBuffers, RenderContext
from kivy.properties import ListProperty, StringProperty, NumericProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, NoTransition

scale = 2

Config.set('graphics', 'width', 480 * scale)
Config.set('graphics', 'height', 320 * scale)
Config.set('graphics', 'resizable', False)

if not Config.has_section('interface'):
    Config.add_section('interface')
Config.set('interface', 'color', '0.25, 0.88, 0.5686, 1')
Config.set('interface', 'color_rgb', '40E191')
Config.set('interface', 'scale', scale)


# Config.set('graphics', 'fullscreen', 'auto')


class PipBoyWidget(FloatLayout):
    pass


class StatsHeader(Screen):
    pass


class Footer(FloatLayout):
    pass


class SpecialScreen(Screen):
    pass


class StatusScreen(Screen):
    pass


class ClickableLabel(ButtonBehavior, Label):
    pass


class GradientMap(FloatLayout):
    def __init__(self, **kwargs):
        super(GradientMap, self).__init__(**kwargs)
        self.fbo = Fbo(size=self.size, with_stencilbuffer=True)
        with self.fbo:
            ClearColor(0, 0, 0, 0)
            ClearBuffers()
            self.rect = Rectangle(size=self.size, texture=self.fbo.texture)

        self.render_context = RenderContext(compute_normal_mat=True)
        self.load_shaders()
        self.canvas = self.render_context
        self.render_context['texture1'] = 1
        self.render_context['texture2'] = 2

    def load_shaders(self):
        with open(os.path.join(os.path.dirname(__file__), "shaders/vertex_shader.glsl"), "r") as vs_file:
            vertex_shader = vs_file.read()

        self.canvas.source = os.path.join(os.path.dirname(__file__), "shaders/fragment_shader.glsl")
        # self.render_context.shader.link()

        # self.fbo.shader.varyings = ['tex_coord']
        # self.fbo.shader.uniforms['gradient'] = [
        #     (0.0, 0.0, 0.0, 1.0),
        #     (0.0, 0.5, 0.0, 1.0),
        #     (0.0, 1.0, 0.0, 1.0),
        # ]

    def update_texture(self, texture):
        with self.canvas:
            self.rect.texture = texture
            self.fbo.shader.uniforms['texture'] = texture

    def capture_screen(self):
        self.fbo.bind()
        self.fbo.clear_buffer()
        self.canvas.ask_update()
        self.fbo.release()

        grayscale_texture = self.fbo.texture
        return grayscale_texture


class PipBoyApp(App):
    color = ListProperty([float(x) for x in Config.get('interface', 'color').split(',')])
    color_rgb = StringProperty(Config.get('interface', 'color_rgb'))
    scale = NumericProperty(Config.get('interface', 'scale'))

    def build(self):
        pipboy_widget = PipBoyWidget()
        gradient_map = GradientMap(size=(480 * scale, 320 * scale))
        pipboy_widget.add_widget(gradient_map)
        pipboy_widget.ids.content_manager.transition = NoTransition()
        pipboy_widget.ids.header_manager.transition = NoTransition()
        Clock.schedule_once(lambda dt: self.apply_gradient_map(gradient_map), 0)

        return pipboy_widget

    def switch_screen(self, screen_name):
        self.root.ids.content_manager.current = screen_name

    def color_opacity(self, color, opacity=1):
        return [color[0], color[1], color[2], opacity]

    def pad_label(self, size, pad_x=10, pad_y=10):
        width, height = size
        return width + 2 * pad_x, height + 2 * pad_y

    def pad_x(self, size, padding=10):
        return size[0] + 2 * padding

    def pad_y(self, size, padding=10):
        return size[1] + 2 * padding

    def apply_gradient_map(self, gradient_map):
        grayscale_texture = gradient_map.capture_screen()
        gradient_map.update_texture(grayscale_texture)


if __name__ == '__main__':
    PipBoyApp().run()

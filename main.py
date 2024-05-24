from kivy import Config
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Line
from kivy.properties import ListProperty, StringProperty, NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen

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


class PipBoyApp(App):
    color = ListProperty([float(x) for x in Config.get('interface', 'color').split(',')])
    color_rgb = StringProperty(Config.get('interface', 'color_rgb'))
    scale = NumericProperty(Config.get('interface', 'scale'))

    def build(self):
        return PipBoyWidget()

    def color_opacity(self, color, opacity=1):
        return [color[0], color[1], color[2], opacity]

    def pad_label(self, size, pad_x=10, pad_y=10):
        width, height = size
        return width + 2 * pad_x, height + 2 * pad_y

    def pad_x(self, size, padding=10):
        return size[0] + 2 * padding

    def pad_y(self, size, padding=10):
        return size[1] + 2 * padding


if __name__ == '__main__':
    PipBoyApp().run()

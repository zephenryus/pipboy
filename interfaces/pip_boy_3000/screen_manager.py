from kivy.uix.screenmanager import ScreenManager

from interfaces.pip_boy_3000.screens.stats.special_screen import SpecialScreen
from interfaces.pip_boy_3000.screens.stats.status_screen import StatusScreen


class PipBoyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(PipBoyScreenManager, self).__init__(**kwargs)
        self.add_widget(StatusScreen(name="status"))
        self.add_widget(SpecialScreen(name="special"))
        self.current = "status"


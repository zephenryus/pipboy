from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

from utils.kv_loader import load_kv


class StatusScreen(Screen):
    def __init__(self, **kwargs):
        super(StatusScreen, self).__init__(**kwargs)
        load_kv(self)
        self.current_button_index = 0
        Window.bind(on_key_down=self.on_key_down)
        Clock.schedule_once(self.delayed_init, 0)

    def delayed_init(self, dt):
        print(f"Delayed init: {self.ids}")
        self.update_focus()

    def on_key_down(self, window, key, *args):
        if key == 276:  # Left arrow key
            self.move_focus_left()
        elif key == 275:  # Right arrow key
            self.move_focus_right()
        elif key == 13:  # Enter key
            self.select_current_button()

    def move_focus_left(self):
        self.current_button_index = (self.current_button_index - 1) % 5
        self.update_focus()

    def move_focus_right(self):
        self.current_button_index = (self.current_button_index + 1) % 5
        self.update_focus()

    def update_focus(self):
        print(f"Current IDs: {self.ids}")
        if not hasattr(self, 'ids'):
            print('IDs are not yet available.')
            return

        buttons = self.ids.button_container.children[::-1]
        for i, button in enumerate(buttons):
            button.background_color = (1, 1, 1, 1) if i == self.current_button_index else (1, 1, 1, 0.5)

    def select_current_button(self):
        buttons = self.ids.button_container.children[::-1]
        if self.current_button_index < len(buttons):
            buttons[self.current_button_index].trigger_action(duration=0)

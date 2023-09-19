from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        bg_image = Image(source='ui/plain_blue.jpg', allow_stretch=True, keep_ratio=False)
        bg_image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        layout.add_widget(bg_image)

        fg_image = Image(source='ui/cd_foreground.png', allow_stretch=True, keep_ratio=True)
        fg_image.pos_hint = {'center_x': 0.5, 'center_y': 0.7}
        fg_image.size_hint_x = 0.5
        layout.add_widget(fg_image)

        game_rules = Label(
            text="[b]Guess the song's artist within 10 seconds to score points![/b]",
            markup=True,
            font_size=20,
            halign='center',
            pos_hint={'center_x': 0.5, 'center_y': 0.3}
        )

        start_button = Button(
            text="Start Game",
            size_hint=(1, 0.2),
            background_color=(1, 0.41, 0.71, 1)
        )
        start_button.bind(on_press=self.switch_to_gameplay)

        layout.add_widget(game_rules)
        layout.add_widget(start_button)
        self.add_widget(layout)

    def switch_to_gameplay(self, instance):
        self.manager.current = 'gameplay'

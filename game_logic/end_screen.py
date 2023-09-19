from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
import datetime

class EndScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = FloatLayout()
        self.end_label = Label(text="Game Over!", font_size=50, pos_hint={'center_x': 0.5, 'center_y': 0.8})
        self.add_widget(self.layout)

    def on_enter(self):
        self.layout.clear_widgets()
        bg_image = Image(source='ui/plain_blue.jpg', allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(bg_image)

        logo_image = Image(source='ui/cd_foreground.png', size_hint=(0.2, 0.2), pos_hint={'top': 1, 'right': 1})
        self.layout.add_widget(logo_image)

        self.layout.add_widget(self.end_label)

        score_label = Label(text=f"Final Score: {self.final_score}", font_size=40)
        self.layout.add_widget(score_label)

        self.save_score(self.final_score)

        buttons_layout = BoxLayout(spacing=10, size_hint=(1, 0.2))

        play_again_button = Button(text="Play Again", size_hint=(.33, 1), background_color=(1, 0.41, 0.71, 1))
        play_again_button.bind(on_press=self.play_again)

        view_high_scores_button = Button(text="View High Scores", size_hint=(.33, 1), background_color=(1, 0.41, 0.71, 1))
        view_high_scores_button.bind(on_press=self.view_high_scores)

        end_game_button = Button(text="End Game", size_hint=(.33, 1), background_color=(1, 0.41, 0.71, 1))
        end_game_button.bind(on_press=self.end_game)

        buttons_layout.add_widget(play_again_button)
        buttons_layout.add_widget(view_high_scores_button)
        buttons_layout.add_widget(end_game_button)

        self.layout.add_widget(buttons_layout)

    def play_again(self, instance):
        self.manager.current = 'gameplay'

    def view_high_scores(self, instance):
        self.manager.current = 'high_scores'

    def end_game(self, instance):
        App.get_running_app().stop()

    def save_score(self, score):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("flat_file_database/score_records.txt", "a") as score_file:
            score_file.write(f"{timestamp}: {score}\n")

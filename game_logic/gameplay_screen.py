from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from game_logic.song_data import SongData
import requests
from kivy.uix.screenmanager import Screen

class GameplayScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical")
        self.add_widget(self.layout)
        self.song_data_instance = SongData("2mdnbXPiAYIDZZlQmahyTQ")
        self.score = 0
        self.current_song_index = 0
        self.audio = None

    def on_enter(self):
        self.layout.clear_widgets()
        self.play_game()
        self.score = 0

    def play_game(self):
        Clock.unschedule(self.time_up)
        self.layout.clear_widgets()

        if self.current_song_index < 5:
            self.current_song_data = self.song_data_instance.get_random_song_data()

            if self.current_song_data is None:
                self.layout.add_widget(Label(text="No more songs with audio available. Game over."))
                return

            song_title = self.current_song_data["title"]
            correct_artist = self.current_song_data["artist"]
            options = self.current_song_data["options"]

            self.layout.add_widget(Label(text=song_title))

            for option in options:
                button = Button(text=option, size_hint=(1, 0.2))
                button.bind(on_press=self.check_answer)
                self.layout.add_widget(button)

            self.play_song(self.current_song_data["preview_url"])
            Clock.schedule_once(self.time_up, 10)
            self.current_song_index += 1

        else:
            self.switch_to_end(None)

    def check_answer(self, instance):
        Clock.unschedule(self.time_up)
        selected_option = instance.text
        correct_artist = self.current_song_data["artist"]

        if selected_option == correct_artist:
            self.score += 10
            instance.background_color = [0, 1, 0, 1]
        else:
            instance.background_color = [1, 0, 0, 1]

        if self.audio is not None:
            self.audio.stop()

        Clock.schedule_once(lambda dt: self.play_game(), 1)

    def play_song(self, preview_url):
        if self.audio is not None:
            self.audio.stop()

        audio_response = requests.get(preview_url)
        audio_file_path = "resources/audio_preview.mp3"
        with open(audio_file_path, "wb") as audio_file:
            audio_file.write(audio_response.content)

        self.audio = SoundLoader.load(audio_file_path)

        if self.audio:
            self.audio.play()

    def time_up(self, dt):
        if self.audio is not None and self.audio.state == 'play':
            self.audio.stop()
            Clock.schedule_once(lambda dt: self.play_game(), 1)

    def switch_to_end(self, instance):
        end_screen = self.manager.get_screen('end')
        end_screen.final_score = self.score
        self.current_song_index = 0
        self.manager.current = 'end'

from game_logic.start_screen import StartScreen
from game_logic.gameplay_screen import GameplayScreen
from game_logic.end_screen import EndScreen
from game_logic.view_high_scores_screen import ViewHighScoresScreen
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition

class GuessTheSongApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(GameplayScreen(name='gameplay'))
        sm.add_widget(EndScreen(name='end'))
        sm.add_widget(ViewHighScoresScreen(name='high_scores'))
        return sm


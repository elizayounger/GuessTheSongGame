import unittest
from unittest.mock import MagicMock, Mock, patch, call
from kivy.clock import Clock
from kivy.base import EventLoop
from ..game_logic.game_manager import GuessTheSongApp
from ..game_logic.game_manager import ViewHighScoresScreen
from ..game_logic.game_manager import EndScreen
from ..game_logic.game_manager import GameplayScreen
from ..game_logic.game_manager import StartScreen

class TestGameplayScreen(unittest.TestCase):

    def setUp(self):
        self.instance = GameplayScreen()
        self.instance.song_data_instance = MagicMock()
        self.instance.current_song_data = {"artist": "Correct Artist"}
        self.instance.audio = MagicMock()
        self.instance.audio.stop = MagicMock()
        self.instance.play_game = MagicMock(return_value=None)

    def test_correct_answer(self):
        instance = MagicMock()
        instance.text = "Correct Artist"
        initial_score = self.instance.score

        self.instance.check_answer(instance)
        self.advance_clock()

        self.assertEqual(self.instance.score, initial_score + 10)
        self.assertEqual(instance.background_color, [0, 1, 0, 1])
        self.instance.audio.stop.assert_called_once()
        self.instance.play_game.assert_called_with()

    def test_incorrect_answer(self):
        instance = MagicMock()
        instance.text = "Incorrect Artist"
        initial_score = self.instance.score

        self.instance.check_answer(instance)
        self.advance_clock()

        self.assertEqual(self.instance.score, initial_score)
        self.assertEqual(instance.background_color, [1, 0, 0, 1])
        self.instance.audio.stop.assert_called_once()

    def advance_clock(self):
        # Simulate processing of scheduled events
        for i in range(11):
            Clock.tick()
            EventLoop.idle()


if __name__ == '__main__':
    unittest.main()

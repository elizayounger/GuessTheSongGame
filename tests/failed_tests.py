import unittest
from unittest.mock import MagicMock, patch
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from game_logic.game_manager import GuessTheSongApp

class TestGuessTheSongApp(unittest.TestCase):

    def setUp(self):
        self.app = GuessTheSongApp()

    def test_start_game(self):
        start_button = Button(text="Start Game")
        self.app.layout.add_widget(start_button)

        # Mocking the behavior of play_game
        self.app.play_game = MagicMock()

        self.app.start_game(start_button)

        self.assertEqual(len(self.app.layout.children), 0)
        self.app.play_game.assert_called_once()

    @patch('game_logic.song_data')
    @patch('game_logic.SoundLoader')
    @patch('game.logic.requests.get')
    def test_play_song(self, mock_get, mock_sound_loader, mock_song_data):
        mock_response = MagicMock()
        mock_response.content = b'Some audio data'
        mock_get.return_value = mock_response

        mock_sound = MagicMock()
        mock_sound_loader.load.return_value = mock_sound

        preview_url = "http://example.com/audio_preview.mp3"
        self.app.play_song(preview_url)

        mock_get.assert_called_once_with(preview_url)
        mock_sound_loader.load.assert_called_once()
        mock_sound.play.assert_called_once()

    def test_check_answer_correct(self):
        mock_button = MagicMock()
        mock_button.text = "Correct Artist"
        self.app.audio = MagicMock()

        self.app.current_song_data = {"artist": "Correct Artist"}
        self.app.check_answer(mock_button)

        self.assertEqual(self.app.score, 10)
        mock_button.background_color == [0, 1, 0, 1]
        self.app.audio.stop.assert_called_once()
        Clock.schedule_once.assert_called_once()

    def test_check_answer_wrong(self):
        mock_button = MagicMock()
        mock_button.text = "Wrong Artist"
        self.app.audio = MagicMock()

        self.app.current_song_data = {"artist": "Correct Artist"}
        self.app.check_answer(mock_button)

        self.assertEqual(self.app.score, 0)
        mock_button.background_color == [1, 0, 0, 1]
        self.app.audio.stop.assert_called_once()
        Clock.schedule_once.assert_called_once()

if __name__ == '__main__':
    unittest.main()

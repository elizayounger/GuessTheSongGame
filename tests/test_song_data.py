import unittest
from unittest.mock import Mock, MagicMock, patch
import os
import sys
from ..game_logic.song_data import SongData

class TestSongData(unittest.TestCase):

    @patch('spotipy.Spotify')
    def setUp(self, mock_spotify):
        self.song_data = SongData("2mdnbXPiAYIDZZlQmahyTQ")
        self.song_data.sp = mock_spotify

    def test_init(self):
        self.assertEqual(self.song_data.playlist_id, "2mdnbXPiAYIDZZlQmahyTQ")

    def test_get_random_song_data_no_tracks(self):
        self.song_data.sp.playlist_tracks.return_value = {'items': []}
        song_data = self.song_data.get_random_song_data()
        self.assertIsNone(song_data)

    def test_get_random_song_data_one_track(self):
        mock_track = MagicMock()
        mock_track.configure_mock(**{
            'track.preview_url': 'http://preview.url',
            'track.name': 'Test Song',
            'track.artists': [{'name': 'Test Artist'}],
            'track.id': '1'
        })
        self.song_data.sp.playlist_tracks.return_value = {'items': [mock_track]}
        song_data = self.song_data.get_random_song_data()
        self.assertEqual(len(song_data['options']), 1)

    @patch("spotipy.Spotify")
    @patch("random.shuffle")
    def test_get_random_song_data_all_tracks(self, mock_shuffle, mock_spotify):
        # Create a mock Spotify instance
        mock_sp = Mock()
        mock_sp.playlist_tracks.return_value = {
            "items": [
                {"track": {"name": "fukumean", "artists": [{"name": "Gunna"}], "id": '2hLmm7s2ICUXOLVIhVFLZQ', "preview_url": 'https://p.scdn.co/mp3-preview/f237ab921af697ba9b49e12fa167c2ce1a82d6b4?cid=e0b89c9d4cb34de482b5299ff8bb7b91'}},
                {"track": {"name": "2 Be Loved (Am I Ready)", "artists": [{"name": "Lizzo"}], "id": "56oDRnqbIiwx4mymNEv7dS", "preview_url": 'https://p.scdn.co/mp3-preview/d8547bb88b7fff366d43a27961d772c105d934e4?cid=e0b89c9d4cb34de482b5299ff8bb7b91'}},
                {"track": {"name": "Call On Me", "artists": [{"name": "Bebe Rexha"}], "id": "64M6ah0SkkRsnPGtGiRAbb", "preview_url": 'https://p.scdn.co/mp3-preview/c641f959b91bf987ea7e2cde6c3f87330988c330?cid=e0b89c9d4cb34de482b5299ff8bb7b91'}},
                {"track": {"name": "10:35", "artists": [{"name": "Tiësto"}], "id": "2o5jDhtHVPhrJdv3cEQ99Z", "preview_url": 'https://p.scdn.co/mp3-preview/6e88ed9108e2c0c493903a7d280183d6d6855272?cid=e0b89c9d4cb34de482b5299ff8bb7b91'}}
            ]
        }
        mock_spotify.return_value = mock_sp

        # Create an instance of SongData
        song_data_instance = SongData("2mdnbXPiAYIDZZlQmahyTQ")
        # Call the method being tested
        song_data = song_data_instance.get_random_song_data()

        expected = {'artist': 'Gunna', 'options': ['Gunna', 'Lizzo', 'Bebe Rexha', 'Tiësto'], 'preview_url': 'https://p.scdn.co/mp3-preview/f237ab921af697ba9b49e12fa167c2ce1a82d6b4?cid=e0b89c9d4cb34de482b5299ff8bb7b91', 'title': 'fukumean'}
        self.assertEqual(song_data, expected)


if __name__ == '__main__':
    unittest.main()

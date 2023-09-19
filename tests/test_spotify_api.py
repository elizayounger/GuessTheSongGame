import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
from game_logic.spotify_api import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_id = '2mdnbXPiAYIDZZlQmahyTQ'
try:
    # Get the playlist information
    playlist = sp.playlist(playlist_id)
    print("Successfully fetched playlist!")
except spotipy.SpotifyException as e:
    print("Error fetching playlist:", e)

# Status code 200
response = requests.get(f"https://api.spotify.com/v1/playlists/{playlist_id}", headers=sp._auth_headers())
print("Response status code:", response.status_code)


import unittest
from ..game_logic.spotify_api import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

class TestSpotifyApi(unittest.TestCase):
    def test_spotify_api_pass(self):
        self.assertIn("e0b89c9d4cb34de482b5299ff8bb7b91", SPOTIFY_CLIENT_ID)
        self.assertIn("7d48fcfc3fde4666b73090606e35804c", SPOTIFY_CLIENT_SECRET)


if __name__ == '__main__':
    unittest.main()

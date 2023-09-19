import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
from game_logic.spotify_api import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

class SongData:
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                                        client_secret=SPOTIFY_CLIENT_SECRET))

    def get_random_song_data(self):
        playlist_tracks = self.sp.playlist_tracks(self.playlist_id)
        random.shuffle(playlist_tracks["items"])

        selected_song = None

        for track in playlist_tracks["items"]:
            if track["track"]["preview_url"]:
                selected_song = track["track"]
                break

        if selected_song is None:
            return None

        song_data = {}
        song_data["title"] = selected_song["name"]
        song_data["artist"] = selected_song["artists"][0]["name"]

        options = [song_data["artist"]]

        for track in playlist_tracks["items"]:
            if track["track"]["id"] != selected_song["id"]:
                options.append(track["track"]["artists"][0]["name"])
                if len(options) >= 4:
                    break

        random.shuffle(options)
        song_data["options"] = options
        song_data["preview_url"] = selected_song["preview_url"]

        return song_data

song_data_instance = SongData("2mdnbXPiAYIDZZlQmahyTQ")

print("Playlist ID:", song_data_instance.playlist_id)

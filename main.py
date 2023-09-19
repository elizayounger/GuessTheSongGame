from game_logic.game_manager import GuessTheSongApp
import kivy
import logging
logging.getLogger("spotipy").setLevel(logging.WARNING)

# Disable Kivy logging
kivy.logger.disabled = True
logging.getLogger("kivy").disabled = True

kivy.require("1.11.1")

kivy.logger.disabled = True
logging.getLogger("kivy").disabled = True

if __name__ == "__main__":
    GuessTheSongApp().run()

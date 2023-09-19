from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

class ViewHighScoresScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.high_scores_label = Label(text="", size_hint=(1, 0.9), markup=True)
        self.add_widget(self.layout)

    def on_enter(self):
        self.layout.clear_widgets()
        self.layout.add_widget(self.high_scores_label)
        self.display_top_scores()

        back_button = Button(text="Back", size_hint=(1, 0.1), background_color=(1, 0.41, 0.71, 1))
        back_button.bind(on_press=self.switch_to_end)
        self.layout.add_widget(back_button)

    def display_top_scores(self):
        try:
            with open("flat_file_database/score_records.txt", "r") as score_file:
                scores = score_file.readlines()

            score_entries = [score.strip() for score in scores]
            score_entries = [entry.split(": ") for entry in score_entries]
            score_entries = [(entry[0], int(entry[1])) for entry in score_entries]

            top_scores = sorted(score_entries, key=lambda x: x[1], reverse=True)[:10]

            scores_text = "[size=40]High scores[/size]\n\n"
            scores_text += "{:<20} {}\n".format("Score", "Date")

            for timestamp, score in top_scores:
                formatted_entry = "{:<20} {}\n".format(score, timestamp)
                scores_text += formatted_entry

            self.high_scores_label.text = scores_text
        except FileNotFoundError:
            self.high_scores_label.text = "No top scores available."

    def switch_to_end(self, instance):
        self.manager.current = 'end'

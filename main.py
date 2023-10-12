import random
import rumps
import subprocess, time

# playlist = [
#     "Sunday Bloody Sunday🎵",
#     "New Year's Day",
#     "40",
#     "The Miracle (Of Joey Ramone)",
#     "Every Breaking Wave",
#     "Song for Someone",
#     "With or Without You",
#     "Where The Streets Have No Name"
# ]
# with open ('music_playlist.txt', 'r') as music_file:
#     playlist = music_file.read().splitlines()
    # print(playlist)
    # for i in playlist:
    #     print(i)
class RecommendedSong(object):
    def __init__(self):
        self.config = {
            "app_name": "RecommendedMusic",
            "recommend_song_now": "Recommend Song",
            "playlist_file": "Open Playlist",
            "config_file": "Config",
            "interval": 3
        }
        self.app = rumps.App(self.config["app_name"])
        self.interval = self.config["interval"]
        self.set_up_menu()
        self.start_timer()
        self.recommend_song_button = rumps.MenuItem(title=self.config["recommend_song_now"], callback=self.notify_song)
        self.music_playlist_file = rumps.MenuItem(title=self.config["playlist_file"], callback=self.open_file)
        self.config_file_button = rumps.MenuItem(title=self.config["config_file"], callback=self.open_conf_file)
        self.app.menu = [self.recommend_song_button, self.music_playlist_file, self.config_file_button]

    def open_file(self, sender):
        subprocess.call(['open', '-t', 'music_playlist.txt'])

    def open_conf_file(self, sender):
        subprocess.call(['open', '-t', 'config.txt'])


    def set_up_menu(self):
        self.app.title = "🎵"

    def get_playlist_file(self, file):
        # time.sleep(1)
        while True:
            with open('music_playlist.txt', 'r') as file:
                music = file.read().splitlines()
                print(music)
            return music


    def get_config_file(self, sender):
        while True:
            with open('config.txt', 'r') as file:
                config_file = file.read().splitlines()
                print(config_file)
                config_file_data = float(config_file[0])
            return config_file_data

    def start_timer(self):
        # interval = self.get_config_file(self)
        @rumps.timer(self.get_config_file(self))
        def time(sender):
            self.notify_song(self)


    def notify_song(self, sender):
        recommended_song = random.choice(self.get_playlist_file(self))
        self.get_config_file(self)
        rumps.notification(title="Recommended Song",
                           subtitle=f"You should listen to: {recommended_song}",
                           message=''
                           )

    def run(self):
        self.app.run()

if __name__ == "__main__":
    app = RecommendedSong()
    app.run()
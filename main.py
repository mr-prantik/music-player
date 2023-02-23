#sample code using the PyQt5 framework to play an MP3 file:
import spotipy
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QSlider, QAction
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from spotipy.oauth2 import SpotifyClientCredentials

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the music player
        self.player = QMediaPlayer()

        # Add the slider for volume control
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setFixedWidth(100)
        self.volume_slider.setValue(self.player.volume())
        self.volume_slider.valueChanged.connect(self.player.setVolume)

        # Add the "Open" action to the file menu
        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)

        # Create the menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(open_action)

        # Add the volume slider to the status bar
        self.statusBar().addPermanentWidget(self.volume_slider)

        # Set the main window properties
        self.setWindowTitle('Music Player')
        self.setGeometry(100, 100, 600, 400)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', '', 'Music Files (*.mp3)')
        if file_path != '':
            self.player.setMedia(QMediaContent(file_path))
            self.player.play()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec_())


#fetching musics online
#scope = "user-library-read"

#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
#results = sp.current_user_saved_tracks()


spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Radiohead'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])


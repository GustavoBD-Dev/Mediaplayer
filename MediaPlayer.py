from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self) 
        
        # Configuramos el controlador del reproductor de multimedia 
        self.player = QMediaPlayer() 
        self.player.error.connect(self.erroralert)
        self.player.play()
        self.playlist = QMediaPlaylist()
        self.player.setPlaylist(self.playlist) 
        
        # agregamos el visor de video para la reproduccion 
        videoWidget = QVideoWidget()     
        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        self.widget.setLayout(layout)
        self.player.setVideoOutput(videoWidget)
        
        # conectamos los controles de botones y deslizadores para el reproductor
        self.fileButton.pressed.connect(self.open_file)
        self.playButton.pressed.connect(self.player.play)
        self.pauseButton.pressed.connect(self.player.pause)
        self.previousButton.pressed.connect(self.playlist.previous)
        self.nextButton.pressed.connect(self.playlist.next)
        self.volumeSlider.valueChanged.connect(self.player.setVolume)
        self.timeSlider.valueChanged.connect(self.player.setPosition)
        self.player.durationChanged.connect(self.update_duration)
        self.player.positionChanged.connect(self.update_position)

        # paramos la lista de reproduccion al reproductor 
        self.model = PlaylistModel(self.playlist)
        self.playlistView.setModel(self.model)
        self.playlist.currentMediaChanged.connect(self.songChanged)
        self.playlist.currentIndexChanged.connect(self.playlist_position_changed)
        selection_model = self.playlistView.selectionModel()
        selection_model.selectionChanged.connect(self.playlist_selection_changed)
        
        self.setAcceptDrops(True) # acepta archivos arrastrados
        self.show() # muestra la ventana 
        
    def update_duration(self, duration):
        self.timeSlider.setMaximum(duration)
        if duration >= 0:
            self.totalTimeLabel.setText(hhmmss(duration))
            
    def update_position(self, position):
        if position >= 0:
            self.currentTimeLabel.setText(hhmmss(position))
        self.timeSlider.blockSignals(True)
        self.timeSlider.setValue(position)
        self.timeSlider.blockSignals(False)
        
    def playlist_selection_changed(self, ix):
        # We receive a QItemSelection from selectionChanged.
        i = ix.indexes()[0].row()
        self.playlist.setCurrentIndex(i)
                
    def playlist_position_changed(self, i):
        if i > -1:
            ix = self.model.index(i)
            self.playlistView.setCurrentIndex(ix)
            
    def songChanged(self, media):
        if not media.isNull():
            self.nameFileLabel.setText(media.canonicalUrl().fileName())
        if media.canonicalUrl().fileName().endswith(".mp4"):
            self.widget.show()
        else:
            self.widget.hide()
            
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()

    def dropEvent(self, e):
        for url in e.mimeData().urls():
            self.playlist.addMedia(QMediaContent(url))
        self.model.layoutChanged.emit()
        if self.player.state() != QMediaPlayer.PlayingState:
            i = self.playlist.mediaCount() - len(e.mimeData().urls())
            self.playlist.setCurrentIndex(i)
            self.player.play()
    
    def open_file(self):
        path, _ = QFileDialog.getOpenFileNames(
            self, 
            "Open file", 
            "", 
            "mp3 Audio (*.mp3);mp4 Video (*.mp4);Movie files (*.mov);All files (*.*)")
        for i in path:
            self.playlist.addMedia(
                QMediaContent(
                    QUrl.fromLocalFile(i)
                ))
            self.model.layoutChanged.emit()
            
    def erroralert(self, *args):
        print(args)


class PlaylistModel(QAbstractListModel):
    def __init__(self, playlist, *args, **kwargs):
        super(PlaylistModel, self).__init__(*args, **kwargs)
        self.playlist = playlist

    def data(self, index, role):
        if role == Qt.DisplayRole:
            media = self.playlist.media(index.row())
            return media.canonicalUrl().fileName()

    def rowCount(self, index):
        return self.playlist.mediaCount()
    
    
class ViewerWindow(QMainWindow):
    state = pyqtSignal(bool)
    def closeEvent(self, e):
        # Emit the window state, to update the viewer toggle button.
        self.state.emit(False)
        
def hhmmss(ms):
    """ # s = 1000
    # m = 60000
    # h = 360000 """
    h, r = divmod(ms, 36000)
    m, r = divmod(r, 60000)
    s, _ = divmod(r, 1000)
    return ("%d:%02d:%02d" % (h,m,s)) if h else ("%d:%02d" % (m,s))

if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Media Player")
    app.setStyle("Fusion")
    # estilos a la ventana 
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
    window = MainWindow()
    app.exec()


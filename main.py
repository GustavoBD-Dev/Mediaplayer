from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Only needed for acces to commando line arguments 
import sys

# Subclass QMainWindow to customise your application´s main window
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("My Awesome App")
        
        label = QLabel("THIS IS AWESOME!!!")
        
        label.setAlignment(Qt.AlignCenter)
        
        self.setCentralWidget(label)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(746, 416)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/control.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.previousButton = QtWidgets.QPushButton(self.centralwidget)
        self.previousButton.setGeometry(QtCore.QRect(190, 370, 31, 24))
        self.previousButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/control-skip-180.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previousButton.setIcon(icon1)
        self.previousButton.setObjectName("previousButton")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(230, 370, 31, 24))
        self.playButton.setText("")
        self.playButton.setIcon(icon)
        self.playButton.setObjectName("playButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(310, 370, 31, 24))
        self.nextButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/control-skip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon2)
        self.nextButton.setObjectName("nextButton")
        self.playlistView = QtWidgets.QListView(self.centralwidget)
        self.playlistView.setGeometry(QtCore.QRect(470, 10, 271, 381))
        self.playlistView.setAcceptDrops(True)
        self.playlistView.setProperty("showDropIndicator", True)
        self.playlistView.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.playlistView.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.playlistView.setAlternatingRowColors(True)
        self.playlistView.setUniformItemSizes(True)
        self.playlistView.setObjectName("playlistView")
        self.timeSlider = QtWidgets.QSlider(self.centralwidget)
        self.timeSlider.setGeometry(QtCore.QRect(70, 330, 321, 22))
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.currentTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentTimeLabel.setGeometry(QtCore.QRect(30, 330, 31, 21))
        self.currentTimeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.currentTimeLabel.setObjectName("currentTimeLabel")
        self.totalTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalTimeLabel.setGeometry(QtCore.QRect(400, 330, 31, 21))
        self.totalTimeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.totalTimeLabel.setObjectName("totalTimeLabel")
        self.volumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.volumeSlider.setGeometry(QtCore.QRect(30, 370, 121, 22))
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setProperty("value", 100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 370, 16, 24))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/speaker-volume.png"))
        self.label.setObjectName("label")
        self.fileButton = QtWidgets.QPushButton(self.centralwidget)
        self.fileButton.setGeometry(QtCore.QRect(350, 370, 28, 24))
        self.fileButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/application-image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileButton.setIcon(icon3)
        self.fileButton.setCheckable(True)
        self.fileButton.setObjectName("fileButton")
        self.nameFileLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameFileLabel.setGeometry(QtCore.QRect(80, 300, 301, 20))
        self.nameFileLabel.setObjectName("nameFileLabel")
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(270, 370, 31, 24))
        self.pauseButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/control-pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon4)
        self.pauseButton.setObjectName("pauseButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 20, 451, 271))
        self.widget.setObjectName("widget")
        self.fontMusic = QtWidgets.QLabel(self.widget)
        self.fontMusic.setGeometry(QtCore.QRect(150, 50, 161, 151))
        self.fontMusic.setText("")
        self.fontMusic.setPixmap(QtGui.QPixmap("images/audio.png"))
        self.fontMusic.setScaledContents(True)
        self.fontMusic.setObjectName("fontMusic")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Media Player"))
        self.currentTimeLabel.setText(_translate("MainWindow", "0:00"))
        self.totalTimeLabel.setText(_translate("MainWindow", "0:00"))
        self.nameFileLabel.setText(_translate("MainWindow", "---"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog


class FileOperations():
    def render(self):
        # fileOptTab_imageBox
        self.fileOptTab_imageBox = self.findChild(
            QtWidgets.QLabel, 'fileOptTab_imageBox')
        # self.fileOptTab_imageBox.setScaledContents(True)  # scratches the image

        # Load/Read Button
        self.loadBtn = self.findChild(
            QtWidgets.QPushButton, 'loadBtn')
        self.loadBtn.clicked.connect(
            lambda: FileOperations.loadBtnClicked(self))

    def loadBtnClicked(self):
        self.fileName = QFileDialog.getOpenFileName(
            self, 'Open file', self.path, "Image files (*.jpg *.gif *.png)")[0]
        pixmap = QPixmap(self.fileName)
        self.fileOptTab_imageBox.setPixmap(pixmap)
        self.imageEnchTab.setEnabled(True)
        self.cannyBtn.setEnabled(True)
        self.morphologicalOptsTab.setEnabled(True)
        self.binaryErosionBtn.setEnabled(True)

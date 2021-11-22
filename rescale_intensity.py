from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog


class RescaleIntensity:
    def render(self):
        # Rescale Intensity Button
        self.rescaleIntensityBtn = self.findChild(
            QtWidgets.QPushButton, 'rescaleIntensityBtn')
        self.rescaleIntensityBtn.clicked.connect(
            lambda: RescaleIntensity.rescaleIntensityBtnClicked(self))

        self.rescaleMinInput = self.findChild(
            QtWidgets.QLineEdit, 'rescaleMinInput')
        self.rescaleMaxInput = self.findChild(
            QtWidgets.QLineEdit, 'rescaleMaxInput')

    def rescaleIntensityBtnClicked(self):
        print('Rescale Intensity Button Clicked')
        print('Rescale Min: ' + self.rescaleMinInput.text())
        print('Rescale Max: ' + self.rescaleMaxInput.text())

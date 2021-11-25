from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
import cv2
from matplotlib import pyplot as plt
from skimage.exposure.exposure import rescale_intensity
from skimage.io import imshow


class RescaleIntensity:
    def render(self):
        # Rescale Intensity Button
        self.rescaleIntensityBtn = self.findChild(
            QtWidgets.QPushButton, 'rescaleIntensityBtn')
        self.rescaleIntensityBtn.clicked.connect(
            lambda: RescaleIntensity.rescaleIntensityBtnClicked(self, self.fileName))

        self.rescaleMinInput = self.findChild(
            QtWidgets.QLineEdit, 'rescaleMinInput')
        self.rescaleMaxInput = self.findChild(
            QtWidgets.QLineEdit, 'rescaleMaxInput')

    def rescaleIntensityBtnClicked(self, fileName):
        image = cv2.imread(fileName)

        image_resint = rescale_intensity(image, in_range=(
            int(self.rescaleMinInput.text()), int(self.rescaleMaxInput.text())))

        imshow(image_resint)
        plt.show()

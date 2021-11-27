import cv2
from PyQt5 import QtWidgets
import numpy as np
from skimage.transform import resize, rescale, rotate, swirl
from matplotlib import pyplot as plt
from skimage import color
from skimage.io import imread, imshow


class Transform():
    def render(self):
        self.resizeMaxBtn = self.findChild(
            QtWidgets.QPushButton, 'resizeMaxBtn')
        self.resizeMaxBtn.clicked.connect(
            lambda: Transform.resizeMaxBtnClicked(self.fileName))

        self.resizeMediumBtn = self.findChild(
            QtWidgets.QPushButton, 'resizeMediumBtn')
        self.resizeMediumBtn.clicked.connect(
            lambda: Transform.resizeMediumBtnClicked(self.fileName))

        self.resizeMinBtn = self.findChild(
            QtWidgets.QPushButton, 'resizeMinBtn')
        self.resizeMinBtn.clicked.connect(
            lambda: Transform.resizeMinBtnClicked(self.fileName))

        self.rescaleBtn = self.findChild(
            QtWidgets.QPushButton, 'rescaleBtn')
        self.rescaleBtn.clicked.connect(
            lambda: Transform.rescaleBtnClicked(self, self.fileName))
        self.rescaleRatioInput = self.findChild(
            QtWidgets.QLineEdit, 'rescaleRatioInput')

        self.rotateBtn = self.findChild(
            QtWidgets.QPushButton, 'rotateBtn')
        self.rotateBtn.clicked.connect(
            lambda: Transform.rotateBtnClicked(self, self.fileName))
        self.rotateDegreeInput = self.findChild(
            QtWidgets.QLineEdit, 'rotateDegreeInput')

        self.rotateDegreeInput = self.findChild(
            QtWidgets.QLineEdit, 'rotateDegreeInput')

        self.mirrorHorizontalBtn = self.findChild(
            QtWidgets.QPushButton, 'mirrorHorizontalBtn')
        self.mirrorHorizontalBtn.clicked.connect(
            lambda: Transform.mirrorHorizontalBtnClicked(self.fileName))

        self.mirrorVeticalBtn = self.findChild(
            QtWidgets.QPushButton, 'mirrorVeticalBtn')
        self.mirrorVeticalBtn.clicked.connect(
            lambda: Transform.mirrorVeticalBtnClicked(self.fileName))

        self.swirlBtn = self.findChild(
            QtWidgets.QPushButton, 'swirlBtn')
        self.swirlBtn.clicked.connect(
            lambda: Transform.swirlBtnClicked(self, self.fileName))
        self.swrilXInput = self.findChild(
            QtWidgets.QLineEdit, 'swrilXInput')
        self.swrilYInput = self.findChild(
            QtWidgets.QLineEdit, 'swrilYInput')
        self.swirlStrengthInput = self.findChild(
            QtWidgets.QLineEdit, 'swirlStrengthInput')
        self.swirlRadiusInput = self.findChild(
            QtWidgets.QLineEdit, 'swirlRadiusInput')

    def resizeMaxBtnClicked(fileName):
        image = imread(fileName)
        resizedImage = resize(image, output_shape=(1080, 1920))
        imshow(resizedImage)
        plt.show()

    def resizeMediumBtnClicked(fileName):
        image = imread(fileName)
        resizedImage = resize(image, output_shape=(720, 1280))
        imshow(resizedImage)
        plt.show()

    def resizeMinBtnClicked(fileName):
        image = imread(fileName)
        resizedImage = resize(image, output_shape=(480, 640))
        imshow(resizedImage)
        plt.show()

    def rescaleBtnClicked(self, fileName):
        image = imread(fileName)
        if image.ndim == 3:
            rescaledImage = rescale(
                image, scale=float(self.rescaleRatioInput.text()), multichannel=True)
        else:
            rescaledImage = rescale(image, scale=float(
                self.rescaleRatioInput.text()))

        imshow(rescaledImage)
        plt.show()

    def rotateBtnClicked(self, fileName):
        image = imread(fileName)
        rotatedImage = rotate(
            image, float(self.rotateDegreeInput.text()) * -1)
        imshow(rotatedImage)
        plt.show()

    def swirlBtnClicked(self, fileName):
        image = imread(fileName)
        swirledImage = swirl(
            image,
            center=(float(self.swrilXInput.text()),
                    float(self.swrilYInput.text())),
            strength=float(self.swirlStrengthInput.text()),
            radius=float(self.swirlRadiusInput.text()))

        imshow(swirledImage)
        plt.show()

    def mirrorHorizontalBtnClicked(fileName):
        image = cv2.imread(fileName)
        image_mirror_h = np.fliplr(image)
        cv2.imshow("horizontal", image_mirror_h)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def mirrorVeticalBtnClicked(fileName):
        image = cv2.imread(fileName)
        image_mirror_v = np.flipud(image)
        cv2.imshow("vertical", image_mirror_v)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

import cv2
import numpy as np
from matplotlib import pyplot as plt
from PyQt5 import QtWidgets
from skimage import morphology
from PIL import Image


class MorphologicalOperations():
    def render(self):
        # Binary Erosion Button
        self.binaryErosionBtn = self.findChild(
            QtWidgets.QPushButton, 'binaryErosionBtn')
        self.binaryErosionBtn.clicked.connect(
            lambda: MorphologicalOperations.binaryErosionBtnClicked(self.fileName))

        # Medial Axis Button
        self.medialAxisBtn = self.findChild(
            QtWidgets.QPushButton, 'medialAxisBtn')
        self.medialAxisBtn.clicked.connect(
            lambda: MorphologicalOperations.medialAxisBtnClicked(self.fileName))

        # White Top Hat Button
        self.whiteTopHatBtn = self.findChild(
            QtWidgets.QPushButton, 'whiteTopHatBtn')
        self.whiteTopHatBtn.clicked.connect(
            lambda: MorphologicalOperations.whiteTopHatBtnClicked(self.fileName))

        # Opening Button
        self.openingBtn = self.findChild(
            QtWidgets.QPushButton, 'openingBtn')
        self.openingBtn.clicked.connect(
            lambda: MorphologicalOperations.openingBtnClicked(self.fileName))

        # Skeletonize- 3D Button
        self.skeletonizeBtn = self.findChild(
            QtWidgets.QPushButton, 'skeletonizeBtn')
        self.skeletonizeBtn.clicked.connect(
            lambda: MorphologicalOperations.skeletonizeBtnClicked(self.fileName))

        # Area Opening Button
        self.areaOpeningBtn = self.findChild(
            QtWidgets.QPushButton, 'areaOpeningBtn')
        self.areaOpeningBtn.clicked.connect(
            lambda: MorphologicalOperations.areaOpeningBtnClicked(self.fileName))

        # Binary Dilation Button
        self.binaryDilationBtn = self.findChild(
            QtWidgets.QPushButton, 'binaryDilationBtn')
        self.binaryDilationBtn.clicked.connect(
            lambda: MorphologicalOperations.binaryDilationBtnClicked(self.fileName))

        # Convex Hull Button
        self.diameterOpeningBtn = self.findChild(
            QtWidgets.QPushButton, 'diameterOpeningBtn')
        self.diameterOpeningBtn.clicked.connect(
            lambda: MorphologicalOperations.diameterOpeningBtnClicked(self.fileName))

        # Flood Fill Button
        self.floodFillBtn = self.findChild(
            QtWidgets.QPushButton, 'floodFillBtn')
        self.floodFillBtn.clicked.connect(
            lambda: MorphologicalOperations.floodFillBtnClicked(self.fileName))

        # Local Maxima Button
        self.localMaximaBtn = self.findChild(
            QtWidgets.QPushButton, 'localMaximaBtn')
        self.localMaximaBtn.clicked.connect(
            lambda: MorphologicalOperations.localMaximaBtnClicked(self.fileName))

    def binaryErosionBtnClicked(fileName):
        image = cv2.imread(fileName, 2)
        ret, bw_img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        # converting to its binary form
        bw = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        filteredImage = morphology.binary_erosion(image)
        plt.imshow(filteredImage)
        plt.show()

    def medialAxisBtnClicked(fileName):
        image = cv2.imread(fileName, 0)
        filteredImage = morphology.medial_axis(image)
        plt.imshow(filteredImage)
        plt.show()

    def whiteTopHatBtnClicked(fileName):
        image = cv2.imread(fileName, 0)
        filteredImage = morphology.white_tophat(image)
        plt.imshow(filteredImage)
        plt.show()

    def openingBtnClicked(fileName):
        image = cv2.imread(fileName, 0)
        filteredImage = morphology.opening(image)
        plt.imshow(filteredImage)
        plt.show()

    def skeletonizeBtnClicked(fileName):
        image = cv2.imread(fileName, 0)
        filteredImage = morphology.skeletonize_3d(image)
        plt.imshow(filteredImage)
        plt.show()

    def areaOpeningBtnClicked(fileName):
        image = cv2.imread(fileName, 0)
        filteredImage = morphology.area_opening(image)
        plt.imshow(filteredImage)
        plt.show()

    def binaryDilationBtnClicked(fileName):
        image = cv2.imread(fileName, 2)
        ret, bw_img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        filteredImage = morphology.binary_dilation(bw_img)
        plt.imshow(filteredImage)
        plt.show()

    def diameterOpeningBtnClicked(fileName):
        image = cv2.imread(fileName, 0)
        filteredImage = morphology.diameter_opening(image)
        plt.imshow(filteredImage)
        plt.show()

    def floodFillBtnClicked(fileName):
        image = cv2.imread(fileName, 2)
        ret, bw_img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        filteredImage = morphology.flood_fill(bw_img, (4, 2), 3)
        plt.imshow(filteredImage)
        plt.show()

    def localMaximaBtnClicked(fileName):
        image = cv2.imread(fileName, 0)
        filteredImage = morphology.local_maxima(image)
        plt.imshow(filteredImage)
        plt.show()

import cv2
import numpy as np
from matplotlib import pyplot as plt
from PyQt5 import QtWidgets
from skimage import filters


class ImageEnhancement():
    def render(self):
        # Canny Effect Button
        self.cannyBtn = self.findChild(
            QtWidgets.QPushButton, 'cannyBtn')
        self.cannyBtn.clicked.connect(
            lambda: ImageEnhancement.cannyBtnClicked(self.fileName))

        # Sobel Effect Button
        self.sobelBtn = self.findChild(
            QtWidgets.QPushButton, 'sobelBtn')
        self.sobelBtn.clicked.connect(
            lambda: ImageEnhancement.sobelBtnClicked(self.fileName))

        # Median Effect Button
        self.medianBtn = self.findChild(
            QtWidgets.QPushButton, 'medianBtn')
        self.medianBtn.clicked.connect(
            lambda: ImageEnhancement.medianBtnClicked(self.fileName))

        # Gauss Effect Button
        self.gaussBtn = self.findChild(
            QtWidgets.QPushButton, 'gaussBtn')
        self.gaussBtn.clicked.connect(
            lambda: ImageEnhancement.gaussBtnClicked(self.fileName))

        # Emboss Effect Button
        self.embossBtn = self.findChild(
            QtWidgets.QPushButton, 'embossBtn')
        self.embossBtn.clicked.connect(
            lambda: ImageEnhancement.embossBtnClicked(self.fileName))

        # Sharpen Effect Button
        self.sharpenBtn = self.findChild(
            QtWidgets.QPushButton, 'sharpenBtn')
        self.sharpenBtn.clicked.connect(
            lambda: ImageEnhancement.sharpenBtnClicked(self.fileName))

        # Sepia Effect Button
        self.sepiaBtn = self.findChild(
            QtWidgets.QPushButton, 'sepiaBtn')
        self.sepiaBtn.clicked.connect(
            lambda: ImageEnhancement.sepiaBtnClicked(self.fileName))

        # Blur Effect Button
        self.blurBtn = self.findChild(
            QtWidgets.QPushButton, 'blurBtn')
        self.blurBtn.clicked.connect(
            lambda: ImageEnhancement.blurBtnClicked(self.fileName))

        # Heisan Effect Button
        self.heisanBtn = self.findChild(
            QtWidgets.QPushButton, 'heisanBtn')
        self.heisanBtn.clicked.connect(
            lambda: ImageEnhancement.heisanBtnClicked(self.fileName))

        # Laplace Effect Button
        self.laplaceBtn = self.findChild(
            QtWidgets.QPushButton, 'laplaceBtn')
        self.laplaceBtn.clicked.connect(
            lambda: ImageEnhancement.laplaceBtnClicked(self.fileName))

    def cannyBtnClicked(fileName):
        img = cv2.imread(fileName, 0)
        edges = cv2.Canny(img, 50, 150)

        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Orjinal'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Canny'), plt.xticks([]), plt.yticks([])

        plt.show()

    def sobelBtnClicked(fileName):
        image = cv2.imread(fileName)
        effectedImage = cv2.Sobel(image, cv2.CV_8U, 1, 0, ksize=5)
        cv2.imshow("sobel", effectedImage)

    def medianBtnClicked(fileName):
        image = cv2.imread(fileName)
        effectedImage = cv2.medianBlur(image, 3)
        cv2.imshow("median dilter", effectedImage)

    def gaussBtnClicked(fileName):
        image = cv2.imread(fileName)
        effectedImage = cv2.GaussianBlur(image, (3, 3), 0)
        cv2.imshow("gaus filter", effectedImage)

    def embossBtnClicked(fileName):
        image = cv2.imread(fileName)
        Emboss_Kernel = np.array([[0, -1, -1], [1, 0, -1], [1, 1, 0]])
        Emboss_Effect_Img = cv2.filter2D(
            src=image, kernel=Emboss_Kernel, ddepth=-1)
        plt.figure(figsize=(8, 8))
        plt.imshow(Emboss_Effect_Img, cmap="gray")
        plt.title('Emboss')
        plt.axis("off")
        plt.show()

    def sharpenBtnClicked(fileName):
        image = cv2.imread(fileName)
        Sharpen_Kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        Sharpen_Effect_Img = cv2.filter2D(
            src=image, kernel=Sharpen_Kernel, ddepth=-1)
        plt.figure(figsize=(8, 8))
        plt.imshow(Sharpen_Effect_Img, cmap="gray")
        plt.title('Sharpen')
        plt.axis("off")
        plt.show()

    def sepiaBtnClicked(fileName):
        image = cv2.imread(fileName)
        Sepia_Kernel = np.array(
            [[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]])
        Sepia_Effect_Img = cv2.filter2D(
            src=image, kernel=Sepia_Kernel, ddepth=-1)
        plt.figure(figsize=(8, 8))
        plt.imshow(Sepia_Effect_Img, cmap="gray")
        plt.title('Sepia')
        plt.axis("off")
        plt.show()

    def blurBtnClicked(fileName):
        image = cv2.imread(fileName)
        Blur_Effect_Img = cv2.GaussianBlur(image, (35, 35), 0)
        plt.figure(figsize=(8, 8))
        plt.imshow(Blur_Effect_Img, cmap="gray")
        plt.title('Blur')
        plt.axis("off")
        plt.show()

    def heisanBtnClicked(fileName):
        image = cv2.imread(fileName, 0)
        hesian = filters.hessian(image)
        plt.imshow(hesian)
        plt.show()

    def laplaceBtnClicked(fileName):
        image = cv2.imread(fileName)
        effectedImage = cv2.Laplacian(image, cv2.CV_64F)
        cv2.imshow("laplace", effectedImage)

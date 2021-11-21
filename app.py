from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QFileDialog
import sys
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('user_interface.ui', self)
        self.path = os.path.join(os.path.expandvars(
            "%userprofile%"), "Downloads")
        self.fileName = ""

        # File Operations elements
        self.fileOperationsBlock()

        # Image Enhancement elements
        self.imageEnhancementBlock()

        # Rescale Intensity elements
        self.rescaleIntensityBlock()

        self.show()

    def fileOperationsBlock(self):
        # fileOptTab_imageBox
        self.fileOptTab_imageBox = self.findChild(
            QtWidgets.QLabel, 'fileOptTab_imageBox')
        # self.fileOptTab_imageBox.setScaledContents(True)  # scratches the image

        # Load/Read Button
        self.loadBtn = self.findChild(
            QtWidgets.QPushButton, 'loadBtn')
        self.loadBtn.clicked.connect(self.loadBtnClicked)

    def loadBtnClicked(self):
        self.fileName = QFileDialog.getOpenFileName(
            self, 'Open file', self.path, "Image files (*.jpg *.gif *.png)")[0]
        pixmap = QPixmap(self.fileName)
        self.fileOptTab_imageBox.setPixmap(pixmap)
        self.imageEnchTab.setEnabled(True)
        # SAKIN SİLME LÜTFEN KALSIN
        self.cannyBtn.setEnabled(True)

    def imageEnhancementBlock(self):
        # cannyBtn
        self.cannyBtn = self.findChild(
            QtWidgets.QPushButton, 'cannyBtn')
        self.cannyBtn.clicked.connect(self.cannyBtnClicked)

        # sobelBtn
        self.sobelBtn = self.findChild(
            QtWidgets.QPushButton, 'sobelBtn')
        self.sobelBtn.clicked.connect(self.sobelBtnClicked)

        # medianBtn
        self.medianBtn = self.findChild(
            QtWidgets.QPushButton, 'medianBtn')
        self.medianBtn.clicked.connect(self.medianBtnClicked)

        # gaussBtn
        self.gaussBtn = self.findChild(
            QtWidgets.QPushButton, 'gaussBtn')
        self.gaussBtn.clicked.connect(self.gaussBtnClicked)

        # embossBtn
        self.embossBtn = self.findChild(
            QtWidgets.QPushButton, 'embossBtn')
        self.embossBtn.clicked.connect(self.embossBtnClicked)

        # sharpenBtn
        self.sharpenBtn = self.findChild(
            QtWidgets.QPushButton, 'sharpenBtn')
        self.sharpenBtn.clicked.connect(self.sharpenBtnClicked)

        # sepiaBtn
        self.sepiaBtn = self.findChild(
            QtWidgets.QPushButton, 'sepiaBtn')
        self.sepiaBtn.clicked.connect(self.sepiaBtnClicked)

        # blurBtn
        self.blurBtn = self.findChild(
            QtWidgets.QPushButton, 'blurBtn')
        self.blurBtn.clicked.connect(self.blurBtnClicked)

        # heissanBtn
        self.heisanBtn = self.findChild(
            QtWidgets.QPushButton, 'heisanBtn')
        self.heisanBtn.clicked.connect(self.heisanBtnClicked)

        # laplaceBtn
        self.laplaceBtn = self.findChild(
            QtWidgets.QPushButton, 'laplaceBtn')
        self.laplaceBtn.clicked.connect(self.laplaceBtnClicked)

    def cannyBtnClicked(self):
        img = cv2.imread(self.fileName, 0)
        edges = cv2.Canny(img, 50, 150)

        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Orjinal'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Canny'), plt.xticks([]), plt.yticks([])

        plt.show()

    def sobelBtnClicked(self):
        cikisGoruntu = cv2.Sobel(cv2.imread(
            self.fileName), cv2.CV_8U, 1, 0, ksize=5)
        cv2.imshow("sobel", cikisGoruntu)

    def medianBtnClicked(self):
        # daha net olur orjinalik korunur
        medianFilter = cv2.medianBlur(cv2.imread(self.fileName), 3)
        cv2.imshow("median dilter", medianFilter)

    def gaussBtnClicked(self):
        gausFilter = cv2.GaussianBlur(cv2.imread(self.fileName), (3, 3), 0)
        cv2.imshow("gaus filter", gausFilter)

    def embossBtnClicked(self):
        Emboss_Kernel = np.array([[0, -1, -1], [1, 0, -1], [1, 1, 0]])
        Emboss_Effect_Img = cv2.filter2D(
            src=cv2.imread(self.fileName), kernel=Emboss_Kernel, ddepth=-1)
        plt.figure(figsize=(8, 8))
        plt.imshow(Emboss_Effect_Img, cmap="gray")
        plt.title('Emboss')
        plt.axis("off")
        plt.show()

    def sharpenBtnClicked(self):
        Sharpen_Kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        Sharpen_Effect_Img = cv2.filter2D(
            src=cv2.imread(self.fileName), kernel=Sharpen_Kernel, ddepth=-1)
        plt.figure(figsize=(8, 8))
        plt.imshow(Sharpen_Effect_Img, cmap="gray")
        plt.title('Sharpen')
        plt.axis("off")
        plt.show()

    def sepiaBtnClicked(self):
        Sepia_Kernel = np.array(
            [[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]])
        Sepia_Effect_Img = cv2.filter2D(
            src=cv2.imread(self.fileName), kernel=Sepia_Kernel, ddepth=-1)
        plt.figure(figsize=(8, 8))
        plt.imshow(Sepia_Effect_Img, cmap="gray")
        plt.title('Sepia')
        plt.axis("off")
        plt.show()

    def blurBtnClicked(self):
        Blur_Effect_Img = cv2.GaussianBlur(
            cv2.imread(self.fileName), (35, 35), 0)
        plt.figure(figsize=(8, 8))
        plt.imshow(Blur_Effect_Img, cmap="gray")
        plt.title('Blur')
        plt.axis("off")
        plt.show()

    def heisanBtnClicked(self):
        print("heisanBtnClicked")

    def laplaceBtnClicked(self):
        hedefGoruntu = cv2.Laplacian(cv2.imread(self.fileName), cv2.CV_64F)
        cv2.imshow("laplace", hedefGoruntu)

    def rescaleIntensityBlock(self):
        print("")


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

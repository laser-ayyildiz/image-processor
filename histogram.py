from PyQt5 import QtWidgets
import cv2
import matplotlib.pyplot as plt
from skimage.filters import threshold_mean
from skimage import data, color
import numpy as np
from skimage.io import imread


class Histogram():
    def render(self):

        # Draw Histogram Button
        self.histogramBtn = self.findChild(
            QtWidgets.QPushButton, 'histogramBtn')
        self.histogramBtn.clicked.connect(
            lambda: Histogram.histogramBtnClicked(self.fileName))

        # Draw Histogram Button
        self.thresholdBtn = self.findChild(
            QtWidgets.QPushButton, 'thresholdBtn')
        self.thresholdBtn.clicked.connect(
            lambda: Histogram.thresholdBtnClicked(self.fileName))

    def histogramBtnClicked(fileName):
        image = cv2.imread(fileName)
        if image.ndim == 3:
            plt.hist(image.ravel(), bins=256, color='gray', )
            plt.hist(image[:, :, 0].ravel(), bins=256, color='red', alpha=0.5)
            plt.hist(image[:, :, 1].ravel(), bins=256,
                     color='Green', alpha=0.5)
            plt.hist(image[:, :, 2].ravel(), bins=256, color='Blue', alpha=0.5)
            plt.xlabel('Intensity')
            plt.ylabel('Count')
            plt.legend(['All', 'Red', 'Green', 'Blue'])
            plt.show()
        else:
            ax = plt.hist(image.ravel(), bins=256)
            plt.xlabel('Intensity')
            plt.ylabel('Count')
            plt.legend('All')
            plt.show()

    def thresholdBtnClicked(fileName):
        image = color.rgb2gray(imread(fileName))*255
        image = np.array(image, dtype=np.uint8)

        thresh = threshold_mean(image)
        binary = image > thresh

        fig, axes = plt.subplots(ncols=2, figsize=(8, 3))
        ax = axes.ravel()

        ax[0].imshow(image, cmap=plt.cm.gray)
        ax[0].set_title('Original image')

        ax[1].imshow(binary, cmap=plt.cm.gray)
        ax[1].set_title('Result')

        for a in ax:
            a.axis('off')

        plt.show()

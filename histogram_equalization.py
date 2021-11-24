import matplotlib.pyplot as plt
from skimage import data, io
from skimage import exposure
from skimage.exposure import match_histograms
from skimage import data, exposure, img_as_float
from skimage.util import img_as_ubyte
from skimage.exposure import histogram
import numpy as np

class HistogramEqualization():
    def render(self):

        I = data.moon() 

        io.imshow(I)
        io.show()
        """ 
        TODO: yukarıda resmi okuyup değişkene atacaz
        """
        I_eq = exposure.equalize_hist(I)

        io.imshow(I_eq)
        io.show()

        noisy_image = img_as_ubyte(I)
        hist, hist_centers = histogram(noisy_image)

        fig, ax = plt.subplots(ncols=2, figsize=(10, 5))

        ax[0].imshow(noisy_image, cmap=plt.cm.gray)
        ax[0].axis('off')

        ax[1].plot(hist_centers, hist, lw=2)
        ax[1].set_title('Before Histogram Gray-level histogram')

        plt.tight_layout()

        noisy_image = img_as_ubyte(I_eq)
        hist, hist_centers = histogram(noisy_image)

        fig, ax = plt.subplots(ncols=2, figsize=(10, 5))

        ax[0].imshow(noisy_image, cmap=plt.cm.gray)
        ax[0].axis('off')

        ax[1].plot(hist_centers, hist, lw=2)
        ax[1].set_title('After Histogram Gray-level histogram')

        plt.tight_layout()
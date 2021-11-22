from PyQt5 import QtWidgets, uic
import sys
import os
from file_operations import FileOperations
from image_enhancement import ImageEnhancement
from rescale_intensity import RescaleIntensity
from morphological_operations import MorphologicalOperations


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('user_interface.ui', self)
        self.path = os.path.join(os.path.expandvars(
            "%userprofile%"), "Downloads")

        # File Operations elements
        FileOperations.render(self)

        # Image Enhancement elements
        ImageEnhancement.render(self)

        # Rescale Intensity elements
        RescaleIntensity.render(self)

        # Morphological Operations elements
        MorphologicalOperations.render(self)

        self.show()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

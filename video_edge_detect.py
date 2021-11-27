
from PyQt5 import QtWidgets
import cv2


class VideoEdgeDetect():
    def render(self):
        # detectEdgesBtn
        self.detectEdgesBtn = self.findChild(
            QtWidgets.QPushButton, 'detectEdgesBtn')
        self.detectEdgesBtn.clicked.connect(
            lambda: VideoEdgeDetect.detectEdgesBtnClicked())

    def detectEdgesBtnClicked():
        cap = cv2.VideoCapture(0)
        while True:
            ret, image = cap.read()

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            canny = cv2.Canny(blur, 10, 70)
            ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)
            cv2.imshow('Press Q to exit', mask)
            # Introduce 20 milisecond delay. press q to exit.
            if cv2.waitKey(10) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

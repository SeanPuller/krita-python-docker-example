from PyQt5.QtWidgets import *
from krita import *

class docker_example(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Docker Example")

    def canvasChanged(self, canvas):
        pass
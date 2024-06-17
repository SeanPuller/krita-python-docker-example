from PyQt5.QtWidgets import *
from krita import *

class docker_example(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Docker Example")
        mainWidget = QWidget(self)
        self.setWidget(mainWidget)
        
        exampleButton = QPushButton("Example Button",mainWidget)
        exampleButton.clicked.connect(self.popup)
        
        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(exampleButton)
        
    def popup(self):
              QMessageBox.information(QWidget(), "Docker Example", "This example button works")
              
    def canvasChanged(self, canvas):
        pass
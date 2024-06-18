from PyQt5.QtWidgets import *
from PyQt5 import Qt

#this is for development autocomplete
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .PyKrita import *
else:
    from krita import *

class docker_example(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Docker Example")
        mainWidget = QWidget(self)
        self.setWidget(mainWidget)
        
        exampleButton = QPushButton("Example Button",mainWidget)
        exampleButton.clicked.connect(self.popup)
        
        slider = QSlider(Qt.Horizontal, self)
        
        
        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(exampleButton)
        mainWidget.layout().addWidget(slider)
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:
            mainWidget.layout().addWidget(w())
        
    def popup(self):
              QMessageBox.information(QWidget(), "Docker Example", "This example button works")
              
    def canvasChanged(self, canvas):
        pass
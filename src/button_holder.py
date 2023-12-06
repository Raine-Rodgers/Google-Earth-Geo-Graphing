from PySide6.QtWidgets import QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Google Earth Graphing")
        button = QPushButton("press me")
        
        self.setCentralWidget(button)
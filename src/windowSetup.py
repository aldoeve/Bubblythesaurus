from PyQt6.QtWidgets import QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bubbly T")
        button = QPushButton("YEPPERS")

        self.setCentralWidget(button)
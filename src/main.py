from PyQt6.QtWidgets import QApplication, QWidget
from windowSetup import MainWindow

app = QApplication([])

window = MainWindow()
window.show()

app.exec()

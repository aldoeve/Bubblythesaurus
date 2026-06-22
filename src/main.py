from PyQt6.QtWidgets import QApplication
from window.bubblyWindow import BubblyWindow

app = QApplication([])

window = BubblyWindow()
window.show()

app.exec()

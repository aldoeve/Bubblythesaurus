from PyQt6.QtWidgets import QMainWindow, QPushButton
from PyQt6.QtCore import Qt, QTimer

from config.application import APP_TITLE
from utility.bubbleMovement import figureOutNextXnY

#-------------------------------------------
# This file contains the main windoes setup.
#-------------------------------------------

class BubblyWindow(QMainWindow):
   def __init__(self):
      super().__init__()
      
      self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
      
      self.showMaximized()
   
      self.setWindowTitle(APP_TITLE)

      self.button = QPushButton("Press me", self)
      self.button.show()

      self.mainBubbleMovementTimer = QTimer(self)
      self.mainBubbleMovementTimer.timeout.connect(self.shiftMainBubble)
      self.mainBubbleMovementTimer.start(500)

   def shiftMainBubble(self):
      screenW, screenH = self.width(), self.height()

      buttonW, buttonH = self.button.width(), self.button.height()

      buttonPos = self.button.pos()
      
      usableDistW = screenW - buttonW
      usableDistH = screenH - buttonH

      nextPos = figureOutNextXnY(buttonPos, usableDistW, usableDistH)

      self.button.move(nextPos[0], nextPos[1])



      

      

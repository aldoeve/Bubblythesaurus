from PyQt6.QtCore import QPoint
import random

#------------------------------------------------------
# This fille contains code that helps move the bubbles.
#------------------------------------------------------

def figureOutNextXnY(currentLocation: QPoint, maxX:int, maxY:int) -> tuple[int, int]:
    DEFAULT_SHIFT = 1
    xShift, yShift = random.randint(-DEFAULT_SHIFT, DEFAULT_SHIFT), random.randint(-DEFAULT_SHIFT, DEFAULT_SHIFT)

    if xShift == 0 and yShift == 0 :
        if random.choice([True, False]):
            xShift = DEFAULT_SHIFT
        else:
            yShift = DEFAULT_SHIFT

    finalX, finalY = currentLocation.x(), currentLocation.y()
    
    potentialX = finalX + xShift
    potentialY = finalY + yShift

    isLocationFine = lambda position, maxVal:(0 > position or position > maxVal)

    finalX = potentialX if isLocationFine(potentialX, maxX) else finalX - xShift
    finalY = potentialY if isLocationFine(potentialY, maxY) else finalY - yShift

    return finalX,finalY
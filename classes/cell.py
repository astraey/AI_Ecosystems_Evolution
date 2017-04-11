class Cell:

    def __init__(self, xIndex, yIndex, xPos, yPos):
        self.xIndex = xIndex
        self.yIndex = yIndex
        self.xPos = xPos
        self.yPos = yPos
        self.occupant = 0

    def printer(self):
        print("I am at ("+str(self.xPos)+", "+str(self.yPos)+")\n")

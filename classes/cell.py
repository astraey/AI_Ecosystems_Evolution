class Cell:

    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.occupant = 0

    def printer(self):
        print("I am at ("+str(self.xPos)+", "+str(self.yPos)+")\n")

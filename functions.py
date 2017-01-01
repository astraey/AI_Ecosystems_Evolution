from classes import *


def tester():
    print("WORKS")


def addplant(plantlist, x, y):
    plantlist.append(Plant(x, y))


def addpredator(predatorlist, x, y):
    predatorlist.append(Predator(x, y))


def predatorgenerator(predatorlist):

    addpredator(predatorlist, 400, 400)


def plantgenerator(plantlist):

    # for i in range(0, 1):
    #     self.plantsList.append(Plant(50*i + 100, 50*i + 100))

    # self.plantsList.append(Plant(0, 0))
    # self.plantsList.append(Plant(self.width - 10, 0))
    # self.plantsList.append(Plant(0, self.height - 10))
    # self.plantsList.append(Plant(self.width - 10, self.height - 10))

    addplant(plantlist, 350, 350)
    addplant(plantlist, 350, 400)
    addplant(plantlist, 400, 350)
    addplant(plantlist, 350, 450)
    addplant(plantlist, 450, 350)
    addplant(plantlist, 350, 450)
    addplant(plantlist, 550, 550)
    addplant(plantlist, 300, 450)
    addplant(plantlist, 200, 200)
    addplant(plantlist, 500, 200)


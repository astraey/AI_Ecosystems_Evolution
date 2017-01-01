from classes.plant import Plant
from classes.predator import Predator


def addplant(plantlist, x, y):
    plantlist.append(Plant(x, y))


def addpredator(predatorlist, x, y, color):
    predatorlist.append(Predator(x, y, color))


def predatorgenerator(predatorlist):

    addpredator(predatorlist, 400, 400, (255, 0, 0))
    addpredator(predatorlist, 250, 250, (0, 0, 255))


def plantgenerator(plantlist):

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


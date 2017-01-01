from plant import Plant
from predator import Predator


def addplant(plantlist, x, y):
    plantlist.append(Plant(x, y))


def addpredator(predatorlist, x, y):
    predatorlist.append(Predator(x, y))


def predatorgenerator(predatorlist):

    addpredator(predatorlist, 400, 400)


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


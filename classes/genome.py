from random import randint

class Genome:

    #The key would be that there was a method that generated a genome randomly, and the mutate_genome,
    #which returned a mutated version of the current one. This could be achieved by making a plane
    #Constructor, that made all the atributes 0, and an extra method, that returned the genome filled with all
    #of the randomly generated atributes.

    #Constructor, called when instanciating the class.
    def __init__(self, randomlyGenerated):

        #print("A genome has been instanciated")


        self.plantsDir = (False, False, False, False)
        self.predatorsDir = (False, False, False, False)
        self.nothingDetected = False

        #Mutation Factor, in %
        self.mutationFactor = 5
        self.mutationChance = 100
        self.valueScale = 100

        self.randomCounterCompass = 0
        self.randomDirectionCompass = randint(0,4)

        #Variables that reflect the agent's behaviour towards plants and predators.
        #Varies from 1 to 100

        if randomlyGenerated:
            self.plantNorthBehaviour = randint(-100,100)
            self.plantSouthBehaviour = randint(-100,100)
            self.plantEastBehaviour = randint(-100,100)
            self.plantWestBehaviour = randint(-100,100)

            self.predatorNorthBehaviour = randint(-100,100)
            self.predatorSouthBehaviour = randint(-100,100)
            self.predatorEastBehaviour = randint(-100,100)
            self.predatorWestBehaviour = randint(-100,100)

            self.notMovePlantDetected = randint(0,100)
            self.notMovePredatorDetected = randint(0,100)

        else:
            self.plantNorthBehaviour = 0
            self.plantSouthBehaviour = 0
            self.plantEastBehaviour = 0
            self.plantWestBehaviour = 0

            self.predatorNorthBehaviour = 0
            self.predatorSouthBehaviour = 0
            self.predatorEastBehaviour = 0
            self.predatorWestBehaviour = 0

            self.notMovePlantDetected = 0
            self.notMovePredatorDetected = 0


        #print("Generated predator with attributes: ")
        #print("["+str(self.plantNorthBehaviour)+", "+str(self.plantSouthBehaviour)+", "+str(self.plantEastBehaviour)+", "+str(self.plantWestBehaviour)+"]")
        #print("["+str(self.predatorNorthBehaviour)+", "+str(self.predatorSouthBehaviour)+", "+str(self.predatorEastBehaviour)+", "+str(self.predatorWestBehaviour)+"]")
        #print("["+str(self.nothingDetectedBeaviour)+", "+str(self.notMovePlantDetected)+", "+str(self.notMovePredatorDetected)+"]\n")


    #Genome's Logic
    def get_move(self):

        plantDir = self.get_direction_plant()
        predatorDir = self.get_direction_predator()
        valuePlant = self.value_for_direction_plant(plantDir)
        valuePredator = self.value_for_direction_predator(predatorDir)

        #Direction = -1 and value = 999 mean that no plant/predator was detected
        plantResult = self.direction_corrector(plantDir, valuePlant)
        predatorResult = self.direction_corrector(predatorDir, valuePredator)


        #print(plantDir, predatorDir, valuePlant, valuePredator)
        #print(plantResult, predatorResult)
        #print("************")


        ###################################################
        #Behaviour for the situations when not plants nor predators are detected.
        #At the moment, just

        #Add some randomness to the mix to make sure that the entity won't get stuck.
        #Currently, the entity adopts a random behaviour in case that it doens't detect anything or once every 20 moves
        if 0 != randint(0,30):
            if plantResult[0] == -1 and predatorResult[0] == -1:
                #print("RANDOM MOVE")
                #print("************")
                return self.random_movement()

            if plantResult[0] != -1 and predatorResult[0] == -1:
                #print("Move made depending on plant")
                #print("************")

                total = plantResult[1] + self.notMovePlantDetected
                randomNum = randint(0, total)

                if randomNum <= plantResult[1]:
                    #We follow the plant behaviour
                    return plantResult[0]

                if plantResult[1] < randomNum <= total:
                    #We follow the predator behaviour
                    return 4


            if plantResult[0] == -1 and predatorResult[0] != -1:
                #print("Move made depending on predator")
                #print("************")

                total = predatorResult[1] + self.notMovePredatorDetected
                randomNum = randint(0, total)

                if randomNum <= predatorResult[1]:
                    #We follow the plant behaviour
                    return predatorResult[0]

                if predatorResult[1] < randomNum <= total:
                    #We follow the predator behaviour
                    return 4


            if plantResult[0] != -1 and predatorResult[0] != -1:
                #print("MOVE MADE DEPENDING ON BOTH PLANTS AND PREDATORS")
                #print("************")

                total = plantResult[1] + predatorResult[1] + self.notMovePlantDetected + self.notMovePredatorDetected
                total = 100
                randomNum = randint(0, total)

                if randomNum <= plantResult[1]:
                    #We follow the plant behaviour
                    return plantResult[0]

                if plantResult[1] < randomNum <= plantResult[1] + predatorResult[1]:
                    #We follow the predator behaviour
                    return predatorResult[0]

                if plantResult[1] + predatorResult[1] < randomNum <= plantResult[1] + predatorResult[1] + self.notMovePlantDetected:
                    #We follow the stop Plant behaviour
                    return 4

                if  plantResult[1] + predatorResult[1] + self.notMovePlantDetected < randomNum <= total:
                    #We follow the stop Predator behaviour
                    return 4

        else:
            return self.random_movement()



    #Function used to pass down the mutated genome to the next generation
    def mutate_genome(self):
        #print("A genome has been mutated")

        #We generate a genome not randomly generated
        mutated_genome = Genome(False)

        if self.mutationChance >= randint(0,100):

            #We mutate the genome's atributes based on the mutationFactor
            mutated_genome.plantNorthBehaviour = self.plantNorthBehaviour + randint(-self.mutationFactor,self.mutationFactor)
            mutated_genome.plantSouthBehaviour = self.plantNorthBehaviour + randint(-self.mutationFactor,self.mutationFactor)
            mutated_genome.plantEastBehaviour = self.plantNorthBehaviour + randint(-self.mutationFactor,self.mutationFactor)
            mutated_genome.plantWestBehaviour = self.plantNorthBehaviour + randint(-self.mutationFactor,self.mutationFactor)

            mutated_genome.predatorNorthBehaviour = self.predatorNorthBehaviour + randint(-self.mutationFactor,self.mutationFactor)
            mutated_genome.predatorSouthBehaviour = self.predatorNorthBehaviour + randint(-self.mutationFactor,self.mutationFactor)
            mutated_genome.predatorEastBehaviour = self.predatorNorthBehaviour + randint(-self.mutationFactor,self.mutationFactor)
            mutated_genome.predatorWestBehaviour = self.predatorNorthBehaviour + randint(-self.mutationFactor,self.mutationFactor)

            mutated_genome.notMovePlantDetected = self.notMovePlantDetected + randint(-self.mutationFactor,self.mutationFactor)
            mutated_genome.notMovePredatorDetected = self.notMovePredatorDetected + randint(-self.mutationFactor,self.mutationFactor)


            mutated_genome.plantNorthBehaviour = self.mutation_corrector(mutated_genome.plantNorthBehaviour)
            mutated_genome.plantSouthBehaviour = self.mutation_corrector(mutated_genome.plantSouthBehaviour)
            mutated_genome.plantEastBehaviour = self.mutation_corrector(mutated_genome.plantEastBehaviour)
            mutated_genome.plantWestBehaviour = self.mutation_corrector(mutated_genome.plantWestBehaviour)

            mutated_genome.predatorNorthBehaviour = self.mutation_corrector(mutated_genome.predatorNorthBehaviour)
            mutated_genome.predatorSouthBehaviour = self.mutation_corrector(mutated_genome.predatorSouthBehaviour)
            mutated_genome.predatorEastBehaviour = self.mutation_corrector(mutated_genome.predatorEastBehaviour)
            mutated_genome.predatorWestBehaviour = self.mutation_corrector(mutated_genome.predatorWestBehaviour)


            mutated_genome.notMovePlantDetected = self.mutation_corrector_positives(mutated_genome.notMovePlantDetected)
            mutated_genome.notMovePredatorDetected = self.mutation_corrector_positives(mutated_genome.notMovePredatorDetected)


            print("Generated predator with attributes: ")
            print("["+str(mutated_genome.plantNorthBehaviour)+", "+str(mutated_genome.plantSouthBehaviour)+", "+str(mutated_genome.plantEastBehaviour)+", "+str(mutated_genome.plantWestBehaviour)+"]")
            print("["+str(mutated_genome.predatorNorthBehaviour)+", "+str(mutated_genome.predatorSouthBehaviour)+", "+str(mutated_genome.predatorEastBehaviour)+", "+str(mutated_genome.predatorWestBehaviour)+"]")
            print("["+str(mutated_genome.notMovePlantDetected)+", "+str(mutated_genome.notMovePredatorDetected)+"]\n")

        else:

            #The genome is passed down to the next generation without mutating it
            mutated_genome.plantNorthBehaviour = self.plantNorthBehaviour
            mutated_genome.plantSouthBehaviour = self.plantNorthBehaviour
            mutated_genome.plantEastBehaviour = self.plantNorthBehaviour
            mutated_genome.plantWestBehaviour = self.plantNorthBehaviour

            mutated_genome.predatorNorthBehaviour = self.predatorNorthBehaviour
            mutated_genome.predatorSouthBehaviour = self.predatorNorthBehaviour
            mutated_genome.predatorEastBehaviour = self.predatorNorthBehaviour
            mutated_genome.predatorWestBehaviour = self.predatorNorthBehaviour

            mutated_genome.notMovePlantDetected = self.notMovePlantDetected
            mutated_genome.notMovePredatorDetected = self.notMovePredatorDetected

            #print("Same genome has been passed down to the next generation")



        return mutated_genome

    def mutation_corrector(self,value):

        if value < - self.valueScale:
            return - self.valueScale
        if value > self.valueScale:
            return self.valueScale

        return value

    def mutation_corrector_positives(self,value):

        if value < 0:
            return 0
        if value > self.valueScale:
            return self.valueScale

        return value

    #When a negative value is passed as a parameter, it returns the oposite direction
    #and turns the value positive
    def direction_corrector(self, direction, value):

        if value < 0:
            value = abs(value)

            if direction == 0:
                newDirection = 1
            if direction == 1:
                newDirection = 0
            if direction == 2:
                newDirection = 3
            if direction == 3:
                newDirection = 2

            return (newDirection, value)

        return (direction, value)



    def get_direction_plant(self):

        #North
        if self.plantsDir[0]:
            return 0
        #South
        if self.plantsDir[1]:
            return 1
        #East
        if self.plantsDir[2]:
            return 2
        #West
        if self.plantsDir[3]:
            return 3

        return -1

    def get_direction_predator(self):

        #North
        if self.predatorsDir[0]:
            return 0
        #South
        if self.predatorsDir[1]:
            return 1
        #East
        if self.predatorsDir[2]:
            return 2
        #West
        if self.predatorsDir[3]:
            return 3

        return -1


    def value_for_direction_plant(self, direction):

        if direction == 0:
            return self.plantNorthBehaviour
        if direction == 1:
            return self.plantSouthBehaviour
        if direction == 2:
            return self.plantEastBehaviour
        if direction == 3:
            return self.plantWestBehaviour

        return 999

    def value_for_direction_predator(self, direction):

        if direction == 0:
            return self.predatorNorthBehaviour
        if direction == 1:
            return self.predatorSouthBehaviour
        if direction == 2:
            return self.predatorEastBehaviour
        if direction == 3:
            return self.predatorWestBehaviour

        return 999

    def random_movement(self):

        if self.randomCounterCompass < 250:
            self.randomCounterCompass += self.randomCounterCompass
            temp = randint(0,4)
            if temp != self.randomDirectionCompass:
                return randint(0,4)
            return temp

        else:
            self.randomDirectionCompass = randing(0,4)
            self.randomCounterCompass = 0

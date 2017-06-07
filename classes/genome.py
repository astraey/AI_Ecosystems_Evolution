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
        self.animalsDir = (False, False, False, False)
        self.nothingDetected = False

        #Mutation Factor, in %
        self.mutationFactor = 5

        #There is a 1% chance that the genome mutates
        self.mutationChance = 1
        self.valueScale = 100

        self.randomCounterCompass = 0
        self.randomDirectionCompass = randint(0,4)

        #Variables that reflect the agent's behaviour towards plants and animals.
        #Varies from 1 to 100

        if randomlyGenerated:
            self.plantNorthBehaviour = randint(-100,100)
            self.plantSouthBehaviour = randint(-100,100)
            self.plantEastBehaviour = randint(-100,100)
            self.plantWestBehaviour = randint(-100,100)

            self.animalNorthBehaviour = randint(-100,100)
            self.animalSouthBehaviour = randint(-100,100)
            self.animalEastBehaviour = randint(-100,100)
            self.animalWestBehaviour = randint(-100,100)

            self.notMovePlantDetected = randint(0,100)
            self.notMoveAnimalDetected = randint(0,100)

        else:
            self.plantNorthBehaviour = 0
            self.plantSouthBehaviour = 0
            self.plantEastBehaviour = 0
            self.plantWestBehaviour = 0

            self.animalNorthBehaviour = 0
            self.animalSouthBehaviour = 0
            self.animalEastBehaviour = 0
            self.animalWestBehaviour = 0

            self.notMovePlantDetected = 0
            self.notMoveAnimalDetected = 0


        #print("Generated animal with attributes: ")
        #print("["+str(self.plantNorthBehaviour)+", "+str(self.plantSouthBehaviour)+", "+str(self.plantEastBehaviour)+", "+str(self.plantWestBehaviour)+"]")
        #print("["+str(self.animalNorthBehaviour)+", "+str(self.animalSouthBehaviour)+", "+str(self.animalEastBehaviour)+", "+str(self.animalWestBehaviour)+"]")
        #print("["+str(self.nothingDetectedBeaviour)+", "+str(self.notMovePlantDetected)+", "+str(self.notMoveAnimalDetected)+"]\n")


    #Genome's Logic
    def get_move(self):

        plantDir = self.get_direction_plant()
        animalDir = self.get_direction_animal()
        valuePlant = self.value_for_direction_plant(plantDir)
        valueAnimal = self.value_for_direction_animal(animalDir)

        #Direction = -1 and value = 999 mean that no plant/animal was detected
        plantResult = self.direction_corrector(plantDir, valuePlant)
        animalResult = self.direction_corrector(animalDir, valueAnimal)


        #print(plantDir, animalDir, valuePlant, valueAnimal)
        #print(plantResult, animalResult)
        #print("************")


        ###################################################
        #Behaviour for the situations when not plants nor animals are detected.
        #At the moment, just

        #Add some randomness to the mix to make sure that the entity won't get stuck.
        #Currently, the entity adopts a random behaviour in case that it doens't detect anything or once every 20 moves
        if 0 != randint(0,30):
            if plantResult[0] == -1 and animalResult[0] == -1:
                #print("RANDOM MOVE")
                #print("************")
                return self.random_movement()

            if plantResult[0] != -1 and animalResult[0] == -1:
                #print("Move made depending on plant")
                #print("************")

                total = plantResult[1] + self.notMovePlantDetected
                randomNum = randint(0, total)

                if randomNum <= plantResult[1]:
                    #We follow the plant behaviour
                    return plantResult[0]

                if plantResult[1] < randomNum <= total:
                    #We follow the animal behaviour
                    return 4


            if plantResult[0] == -1 and animalResult[0] != -1:
                #print("Move made depending on animal")
                #print("************")

                total = animalResult[1] + self.notMoveAnimalDetected
                randomNum = randint(0, total)

                if randomNum <= animalResult[1]:
                    #We follow the plant behaviour
                    return animalResult[0]

                if animalResult[1] < randomNum <= total:
                    #We follow the animal behaviour
                    return 4


            if plantResult[0] != -1 and animalResult[0] != -1:
                #print("MOVE MADE DEPENDING ON BOTH PLANTS AND ANIMALS")
                #print("************")

                total = plantResult[1] + animalResult[1] + self.notMovePlantDetected + self.notMoveAnimalDetected
                total = 100
                randomNum = randint(0, total)

                if randomNum <= plantResult[1]:
                    #We follow the plant behaviour
                    return plantResult[0]

                if plantResult[1] < randomNum <= plantResult[1] + animalResult[1]:
                    #We follow the animal behaviour
                    return animalResult[0]

                if plantResult[1] + animalResult[1] < randomNum <= plantResult[1] + animalResult[1] + self.notMovePlantDetected:
                    #We follow the stop Plant behaviour
                    return 4

                if  plantResult[1] + animalResult[1] + self.notMovePlantDetected < randomNum <= total:
                    #We follow the stop Animal behaviour
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

            mutated_genome.animalNorthBehaviour = self.animalNorthBehaviour + randint(-self.mutationFactor,self.mutationFactor)
            mutated_genome.animalSouthBehaviour = self.animalNorthBehaviour + randint(-self.mutationFactor,self.mutationFactor)
            mutated_genome.animalEastBehaviour = self.animalNorthBehaviour + randint(-self.mutationFactor,self.mutationFactor)
            mutated_genome.animalWestBehaviour = self.animalNorthBehaviour + randint(-self.mutationFactor,self.mutationFactor)

            mutated_genome.notMovePlantDetected = self.notMovePlantDetected + randint(-self.mutationFactor,self.mutationFactor)
            mutated_genome.notMoveAnimalDetected = self.notMoveAnimalDetected + randint(-self.mutationFactor,self.mutationFactor)


            mutated_genome.plantNorthBehaviour = self.mutation_corrector(mutated_genome.plantNorthBehaviour)
            mutated_genome.plantSouthBehaviour = self.mutation_corrector(mutated_genome.plantSouthBehaviour)
            mutated_genome.plantEastBehaviour = self.mutation_corrector(mutated_genome.plantEastBehaviour)
            mutated_genome.plantWestBehaviour = self.mutation_corrector(mutated_genome.plantWestBehaviour)

            mutated_genome.animalNorthBehaviour = self.mutation_corrector(mutated_genome.animalNorthBehaviour)
            mutated_genome.animalSouthBehaviour = self.mutation_corrector(mutated_genome.animalSouthBehaviour)
            mutated_genome.animalEastBehaviour = self.mutation_corrector(mutated_genome.animalEastBehaviour)
            mutated_genome.animalWestBehaviour = self.mutation_corrector(mutated_genome.animalWestBehaviour)


            mutated_genome.notMovePlantDetected = self.mutation_corrector_positives(mutated_genome.notMovePlantDetected)
            mutated_genome.notMoveAnimalDetected = self.mutation_corrector_positives(mutated_genome.notMoveAnimalDetected)


            print("Generated animal with attributes: ")
            print("["+str(mutated_genome.plantNorthBehaviour)+", "+str(mutated_genome.plantSouthBehaviour)+", "+str(mutated_genome.plantEastBehaviour)+", "+str(mutated_genome.plantWestBehaviour)+"]")
            print("["+str(mutated_genome.animalNorthBehaviour)+", "+str(mutated_genome.animalSouthBehaviour)+", "+str(mutated_genome.animalEastBehaviour)+", "+str(mutated_genome.animalWestBehaviour)+"]")
            print("["+str(mutated_genome.notMovePlantDetected)+", "+str(mutated_genome.notMoveAnimalDetected)+"]")

        else:

            #The genome is passed down to the next generation without mutating it
            mutated_genome.plantNorthBehaviour = self.plantNorthBehaviour
            mutated_genome.plantSouthBehaviour = self.plantNorthBehaviour
            mutated_genome.plantEastBehaviour = self.plantNorthBehaviour
            mutated_genome.plantWestBehaviour = self.plantNorthBehaviour

            mutated_genome.animalNorthBehaviour = self.animalNorthBehaviour
            mutated_genome.animalSouthBehaviour = self.animalNorthBehaviour
            mutated_genome.animalEastBehaviour = self.animalNorthBehaviour
            mutated_genome.animalWestBehaviour = self.animalNorthBehaviour

            mutated_genome.notMovePlantDetected = self.notMovePlantDetected
            mutated_genome.notMoveAnimalDetected = self.notMoveAnimalDetected

            #print("Same genome has been passed down to the next generation")



        return mutated_genome

    def mutation_corrector(self, value):

        if value < - self.valueScale:
            return - self.valueScale
        if value > self.valueScale:
            return self.valueScale

        return value

    def mutation_corrector_positives(self, value):

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

    def get_direction_animal(self):

        #North
        if self.animalsDir[0]:
            return 0
        #South
        if self.animalsDir[1]:
            return 1
        #East
        if self.animalsDir[2]:
            return 2
        #West
        if self.animalsDir[3]:
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

    def value_for_direction_animal(self, direction):

        if direction == 0:
            return self.animalNorthBehaviour
        if direction == 1:
            return self.animalSouthBehaviour
        if direction == 2:
            return self.animalEastBehaviour
        if direction == 3:
            return self.animalWestBehaviour

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

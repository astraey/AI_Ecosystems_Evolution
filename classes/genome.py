
class Genome:

    #Constructor, called when instanciating the class.
    def __init__(self):

        #print("A genome has been instanciated")


        self.plantsDir = (False, False, False, False)
        self.predatorsDir = (False, False, False, False)

        #Mutation Factor
        self.mutationFactor = 0.05


    #Update environment information
    def update_environment_information(self, plantsDir, predatorsDir):

        self.plantsDir = plantsDir
        self.predatorsDir = predatorsDir

    #Function used to pass down the mutated genome to the next generation
    def mutate_genome(self):
        #print("A genome has been mutated")
        return Genome()

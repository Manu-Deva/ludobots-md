from solution import SOLUTION
import constants as c
import copy
import os


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for x in range(0, c.populationSize):
            self.parents[x] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        self.data = [0] * c.numberOfGenerations

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration)

        # self.parent.Evaluate("DIRECT")
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()
    def Evolve_For_One_Generation(self, currentGeneration):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select(currentGeneration)

    def Spawn(self):
        self.children = {}
        for i in (self.parents.keys()):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Select(self, currentGeneration):
        for i in self.parents.keys():
            if self.parents[i].fitness < self.children[i].fitness:
                self.parents[i] = self.children[i]

        bestFitness = 0
        for i in (self.parents.keys()):
            if (self.parents[i].fitness > bestFitness):
                bestFitness = self.parents[i].fitness

        self.data[currentGeneration] = bestFitness

    def Mutate(self):
        for i in self.children.keys():
            self.children[i].Mutate()

    def Print(self):
        for i in self.parents.keys():
            print(str(self.parents[i].fitness) +
                  ", " + str(self.children[i].fitness))

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")

        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()

    def Show_Best(self):
        fit = self.parents[0].fitness
        j = 0
        for i in self.parents.keys():
            if self.parents[i].fitness > fit:
                fit = self.parents[i].fitness
                j = i

                # with open("file5.npy", "wb") as f:
        #     np.save(f,np.array(self.data))

        self.parents[j].Start_Simulation("GUI")

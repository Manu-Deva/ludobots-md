from solution import SOLUTION
import constants as c
import copy


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        for x in range(0, c.populationSize):
            self.parents[x] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

        # self.parent.Evaluate("DIRECT")
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        # self.child = copy.deepcopy(self.parent)
        # self.child.Set_ID()
        # self.nextAvailableID += 1
        self.children = {}
        for i in range(len(self.parents)):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Select(self):
        # if (self.parent.fitness < self.child.fitness):
        #     self.parent = self.child
        for i in self.parents.keys():
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()

    def Print(self):
        for i in self.parents.keys():
            print(str(self.parents[i].fitness) +
                  ", " + str(self.children[i].fitness))

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("GUI")

        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()

    def Show_Best(self):
        fit = self.parents[0].fitness
        j = 0
        for i in self.parents.keys():
            if self.parents[i].fitness < fit:
                fit = self.parents[i].fitness
                j = i
        self.parents[j].Start_Simulation("GUI")

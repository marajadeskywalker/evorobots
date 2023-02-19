import constants as c
from solution import SOLUTION

class PARALLEL_HILLCLIMBER:
    def __init__(self):
        c.os.system("rm brain*.nndf")
        c.os.system("rm fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evaluate(self, solutions):
        for solution in solutions:
            solutions[solution].Start_Simulation("DIRECT")
        for solution in solutions:
            solutions[solution].Wait_For_Simulation_To_End()
    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(0, c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()


    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            self.children[parent] = c.copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
    def Mutate(self):
        for parent in self.parents:
            self.children[parent].Mutate()
    def Select(self):
        for solution in self.parents:
            if self.parents[solution].fitness > self.children[solution].fitness:
                self.parents[solution] = self.children[solution]
    def Print(self):
        print("")
        for solution in self.parents:
            print(f"Fitness of Child: {str(self.children[solution].fitness)}" + f" Fitness of Parent: {str(self.parents[solution].fitness)}")
        print("")

    def Show_Best(self):
        lowest_so_far = 0
        for solution in self.parents:
            if self.parents[solution].fitness < self.parents[solution].fitness:
                lowest_so_far = solution
        self.parents[lowest_so_far].Start_Simulation("GUI")

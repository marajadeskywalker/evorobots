import constants as c
from solution import SOLUTION
from operator import itemgetter

class PARALLEL_HILLCLIMBER:
    def __init__(self):
        c.os.system("rm brain*.nndf")
        c.os.system("rm fitness*.txt")
        self.generation = 0
        self.parents = {}
        self.unevolved = {}
        #self.evolved = []
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
        if self.generation == 0:
            for parent in self.parents:
                self.unevolved[parent] = c.copy.deepcopy(self.parents[parent])
        self.generation += 1



    def Get_Fitness(self, item):
        return item.fitness

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
        # self.parents.update(self.children)
        # sortedTotal = sorted(self.parents.items(), key=lambda item: item[1].fitness)
        # self.parents = dict(sortedTotal[0:c.populationSize])
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
            if self.parents[solution].fitness < self.parents[lowest_so_far].fitness:
                lowest_so_far = solution
        self.parents[lowest_so_far].Start_Simulation("GUI")
        #Display many hillclimbers version
        # lowest_so_far_unevolved = [0, 0, 0, 0, 0]
        # lowest_values_unevolved = [999, 999, 999, 999, 999]
        # for solution in self.unevolved:
        #     for i in range(0, 5):
        #         if self.unevolved[solution].fitness < lowest_values_unevolved[i]:
        #             lowest_so_far_unevolved[i] = solution
        #             lowest_values_unevolved[i] = self.unevolved[solution].fitness
        #             break
        # for i in range(0, 5):
        #     self.unevolved[lowest_so_far_unevolved[i]].Start_Simulation("GUI")
        #     c.time.sleep(65)
        #
        # lowest_so_far_evolved = [0, 0, 0, 0, 0]
        # lowest_values_evolved = [999, 999, 999, 990, 999]
        # for solution in self.parents:
        #     for i in range(0, 5):
        #         if self.parents[solution].fitness < lowest_values_evolved[i]:
        #             lowest_so_far_evolved[i] = solution
        #             lowest_values_evolved[i] = self.parents[solution].fitness
        #             break
        # for i in range(0, 5):
        #     self.parents[lowest_so_far_evolved[i]].Start_Simulation("GUI")
        #     c.time.sleep(65)

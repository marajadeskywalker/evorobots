import constants as c
class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = c.numpy.random.rand(3, 2)
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableID

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        c.os.system("python3 simulate.py " + directOrGUI + f" {str(self.myID)} " + " &")

    def Wait_For_Simulation_To_End(self):
        while not c.os.path.exists(f"fitness{str(self.myID)}.txt"):
            c.time.sleep(1)
        fitnessFile = open(f"fitness{str(self.myID)}.txt", "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()
        c.os.system(f"rm fitness{str(self.myID)}.txt")

    def Mutate(self):
        randomRow = c.random.randint(0, 2)
        randomColumn = c.random.randint(0, 1)
        self.weights[randomRow,randomColumn] = c.random.random() * 2 - 1.

    def Create_World(self):
        c.pyrosim.Start_SDF("world.sdf")
        c.pyrosim.Send_Cube(name="Box", pos=[0, 3, 0.5], size=[1, 1, 1])
        c.pyrosim.End()

    def Create_Body(self):
        c.pyrosim.Start_URDF("body.urdf")
        c.pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[1, 1, 1])
        c.pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[-0.5, 0, 1])
        c.pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0.5, 0, 1])
        c.pyrosim.Send_Cube(name="FrontLeg", pos=[-0.5, 0, -0.5], size=[1,1,1])
        c.pyrosim.Send_Cube(name="BackLeg", pos=[0.5, 0, -0.5], size=[1,1,1])
        c.pyrosim.End()

    def Create_Brain(self):
        c.pyrosim.Start_NeuralNetwork(f"brain{str(self.myID)}.nndf")
        c.pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        c.pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        c.pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        c.pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        c.pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        for currentRow in range(0, 3):
            for currentColumn in range(0, 2):
                c.pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+3, weight = self.weights[currentRow][currentColumn])
        c.pyrosim.End()

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

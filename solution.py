import constants as c
class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = c.numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableID

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        c.os.system("python3 simulate.py " + directOrGUI + f" {str(self.myID)} 2&>1 &")

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
        c.pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])

        c.pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0.5, 1], jointAxis = "1 0 0")
        c.pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 1], jointAxis = "1 0 0")
        c.pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position=[0.5, 0, 1], jointAxis = "0 1 0")
        c.pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[-0.5, 0, 1], jointAxis = "0 1 0")

        c.pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
        c.pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2,1,0.2])
        c.pyrosim.Send_Cube(name="LeftLeg", pos=[0.5, 0, 0], size=[1.0,0.2,0.2])
        c.pyrosim.Send_Cube(name="RightLeg", pos=[-0.5, 0, 0], size=[1.0,0.2,0.2])

        c.pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute", position=[0, 1, 0], jointAxis = "1 0 0")
        c.pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute", position=[0, -1, 0], jointAxis = "1 0 0")
        c.pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute", position=[1, 0, 0], jointAxis = "0 1 0")
        c.pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute", position=[-1, 0, 0], jointAxis = "0 1 0")

        c.pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        c.pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2,0.2,1])
        c.pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2,0.2,1])
        c.pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2,0.2,1])
        c.pyrosim.End()

    def Create_Brain(self):
        c.pyrosim.Start_NeuralNetwork(f"brain{str(self.myID)}.nndf")
        c.pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        c.pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        c.pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        c.pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        c.pyrosim.Send_Sensor_Neuron(name = 4, linkName = "RightLeg")
        c.pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "BackLowerLeg")
        c.pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "FrontLowerLeg")
        c.pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftLowerLeg")
        c.pyrosim.Send_Sensor_Neuron(name = 8, linkName = "RightLowerLeg")

        c.pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_BackLeg")
        c.pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_FrontLeg")
        c.pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_LeftLeg")
        c.pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_RightLeg")
        c.pyrosim.Send_Motor_Neuron( name = 13 , jointName = "BackLeg_BackLowerLeg")
        c.pyrosim.Send_Motor_Neuron( name = 14 , jointName = "FrontLeg_FrontLowerLeg")
        c.pyrosim.Send_Motor_Neuron( name = 15 , jointName = "LeftLeg_LeftLowerLeg")
        c.pyrosim.Send_Motor_Neuron( name = 16 , jointName = "RightLeg_RightLowerLeg")

        for currentRow in range(0, c.numSensorNeurons):
            for currentColumn in range(0, c.numMotorNeurons):
                c.pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])
        c.pyrosim.End()

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

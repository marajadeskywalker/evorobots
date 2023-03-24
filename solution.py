import constants as c
class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = 2*c.numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)-1
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
        randomRow = c.random.randint(0, 10)
        randomColumn = c.random.randint(0, 12)
        self.weights[randomRow,randomColumn] = c.random.random() * 2 - 1

    def Create_World(self):
        c.pyrosim.Start_SDF("world.sdf")
        #c.pyrosim.Send_Cube(name="Box", pos=[-5, 0, 1], size=[2, 2, 2])
        #for i in range(0, 5):
        #    for j in range(0, 5):
        #        if i % 2 == 0:
        #            c.pyrosim.Send_Cube(name=f"Box{i}{j}", pos=[3*i+3, -5+3*j, 0.5], size=[1, 1, 1])
        #        else:
        #            c.pyrosim.Send_Cube(name=f"Box{i}{j}", pos=[3*i+3, -3+3*j, 0.5], size=[1, 1, 1])
        c.pyrosim.End()

    def Create_Body(self):
        c.pyrosim.Start_URDF("body.urdf")
        c.pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])

        #Create "shoulder" joints that will enable legs to rotate sideways as well as up and down
        c.pyrosim.Send_Joint(name="Torso_FrontShoulder", parent="Torso", child="FrontShoulder", type="revolute", position=[0, 0.5, 1], jointAxis="0 0 1")
        c.pyrosim.Send_Joint(name="Torso_BackShoulder", parent="Torso", child="BackShoulder", type="revolute", position=[0, -0.5, 1], jointAxis="0 0 1")
        c.pyrosim.Send_Joint(name="Torso_LeftShoulder", parent="Torso", child="LeftShoulder", type="revolute", position=[0.5, 0, 1], jointAxis="0 0 1")
        c.pyrosim.Send_Joint(name="Torso_RightShoulder", parent="Torso", child="RightShoulder", type="revolute", position=[-0.5, 0, 1], jointAxis="0 0 1")

        #Create the shoulders
        c.pyrosim.Send_Cube(name="FrontShoulder", pos=[0, 0.125, 0], size=[0.25, 0.25, 0.25])
        c.pyrosim.Send_Cube(name="BackShoulder", pos=[0, -0.125, 0], size=[0.25, 0.25, 0.25])
        c.pyrosim.Send_Cube(name="LeftShoulder", pos=[0.125, 0, 0], size=[0.25, 0.25, 0.25])
        c.pyrosim.Send_Cube(name="RightShoulder", pos=[-0.125, 0, 0], size=[0.25, 0.25, 0.25])

        #Create the joints that enable up and down motion for the upper legs.
        c.pyrosim.Send_Joint(name="FrontShoulder_FrontUpperLeg", parent="FrontShoulder", child="FrontUpperLeg", type="revolute", position=[0, 0.125, 0], jointAxis="1 0 0")
        c.pyrosim.Send_Joint(name="BackShoulder_BackUpperLeg", parent="BackShoulder", child="BackUpperLeg", type="revolute", position=[0, -0.125, 0], jointAxis="1 0 0")
        c.pyrosim.Send_Joint(name="LeftShoulder_LeftUpperLeg", parent="LeftShoulder", child="LeftUpperLeg", type="revolute", position=[0.125, 0, 0], jointAxis="0 1 0")
        c.pyrosim.Send_Joint(name="RightShoulder_RightUpperLeg", parent="RightShoulder", child="RightUpperLeg", type="revolute", position=[-0.125, 0, 0], jointAxis="0 1 0")

        #Create the upper legs
        c.pyrosim.Send_Cube(name="FrontUpperLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
        c.pyrosim.Send_Cube(name="BackUpperLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
        c.pyrosim.Send_Cube(name="LeftUpperLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
        c.pyrosim.Send_Cube(name="RightUpperLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])

        #Create the "knees" connecting upper and lower legs
        c.pyrosim.Send_Joint(name="FrontUpperLeg_FrontLowerLeg", parent="FrontUpperLeg", child="FrontLowerLeg", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")
        c.pyrosim.Send_Joint(name="BackUpperLeg_BackLowerLeg", parent="BackUpperLeg", child="BackLowerLeg", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")
        c.pyrosim.Send_Joint(name="LeftUpperLeg_LeftLowerLeg", parent="LeftUpperLeg", child="LeftLowerLeg", type="revolute", position=[1, 0, 0], jointAxis="0 1 0")
        c.pyrosim.Send_Joint(name="RightUpperLeg_RightLowerLeg", parent="RightUpperLeg", child="RightLowerLeg", type="revolute", position=[-1, 0, 0], jointAxis="0 1 0")

        # c.pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0.5, 1], jointAxis = "1 0 0")
        # c.pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 1], jointAxis = "1 0 0")
        # c.pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position=[0.5, 0, 1], jointAxis = "0 1 0")
        # c.pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[-0.5, 0, 1], jointAxis = "0 1 0")
        #
        # c.pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
        # c.pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2,1,0.2])
        # c.pyrosim.Send_Cube(name="LeftLeg", pos=[0.5, 0, 0], size=[1.0,0.2,0.2])
        # c.pyrosim.Send_Cube(name="RightLeg", pos=[-0.5, 0, 0], size=[1.0,0.2,0.2])

        # c.pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute", position=[0, 1, 0], jointAxis = "1 0 0")
        # c.pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute", position=[0, -1, 0], jointAxis = "1 0 0")
        # c.pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute", position=[1, 0, 0], jointAxis = "0 1 0")
        # c.pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute", position=[-1, 0, 0], jointAxis = "0 1 0")

        #Create the lower legs
        c.pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        c.pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2,0.2,1])
        c.pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2,0.2,1])
        c.pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2,0.2,1])

        #Create the beam's shoulder joint
        c.pyrosim.Send_Joint(name="Torso_BeamShoulder", parent="Torso", child="BeamShoulder", type="revolute", position=[0, 0, 1.5], jointAxis="0 0 1")
        #Create the beam
        c.pyrosim.Send_Cube(name="BeamShoulder", pos=[0, 0, 0.125], size=[0.25, 0.25, 0.25])
        c.pyrosim.Send_Joint(name="BeamShoulder_Beam", parent="BeamShoulder", child="Beam", type="revolute", position=[0, 0, 0.25], jointAxis="0 0 1")
        c.pyrosim.Send_Cube(name="Beam", pos=[-1.5, 0, 0], size=[3, 0.2, 0.2])
        c.pyrosim.End()

    def Create_Brain(self):
        c.pyrosim.Start_NeuralNetwork(f"brain{str(self.myID)}.nndf")

        c.pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        c.pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontShoulder")
        c.pyrosim.Send_Sensor_Neuron(name=2, linkName="BackShoulder")
        c.pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftShoulder")
        c.pyrosim.Send_Sensor_Neuron(name=4, linkName="RightShoulder")
        c.pyrosim.Send_Sensor_Neuron(name=5, linkName="BeamShoulder")
        c.pyrosim.Send_Sensor_Neuron(name=6, linkName="FrontLowerLeg")
        c.pyrosim.Send_Sensor_Neuron(name=7, linkName="BackLowerLeg")
        c.pyrosim.Send_Sensor_Neuron(name=8, linkName="LeftLowerLeg")
        c.pyrosim.Send_Sensor_Neuron(name=9, linkName="RightLowerLeg")
        c.pyrosim.Send_Sensor_Neuron(name=10, linkName="Beam")

        c.pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_FrontShoulder")
        c.pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_BackShoulder")
        c.pyrosim.Send_Motor_Neuron(name=13, jointName="Torso_LeftShoulder")
        c.pyrosim.Send_Motor_Neuron(name=14, jointName="Torso_RightShoulder")
        c.pyrosim.Send_Motor_Neuron(name=15, jointName="FrontShoulder_FrontUpperLeg")
        c.pyrosim.Send_Motor_Neuron(name=16, jointName="BackShoulder_BackUpperLeg")
        c.pyrosim.Send_Motor_Neuron(name=17, jointName="LeftShoulder_LeftUpperLeg")
        c.pyrosim.Send_Motor_Neuron(name=18, jointName="RightShoulder_RightUpperLeg")
        c.pyrosim.Send_Motor_Neuron(name=19, jointName="FrontUpperLeg_FrontLowerLeg")
        c.pyrosim.Send_Motor_Neuron(name=20, jointName="BackUpperLeg_BackLowerLeg")
        c.pyrosim.Send_Motor_Neuron(name=21, jointName="LeftUpperLeg_LeftLowerLeg")
        c.pyrosim.Send_Motor_Neuron(name=22, jointName="RightUpperLeg_RightLowerLeg")
        c.pyrosim.Send_Motor_Neuron(name=23, jointName="BeamShoulder_Beam")

        # c.pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        # c.pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        # c.pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        # c.pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        # c.pyrosim.Send_Sensor_Neuron(name = 4, linkName = "RightLeg")
        # c.pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "BackLowerLeg")
        # c.pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "FrontLowerLeg")
        # c.pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftLowerLeg")
        # c.pyrosim.Send_Sensor_Neuron(name = 8, linkName = "RightLowerLeg")
        #
        # c.pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_BackLeg")
        # c.pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_FrontLeg")
        # c.pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_LeftLeg")
        # c.pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_RightLeg")
        # c.pyrosim.Send_Motor_Neuron( name = 13 , jointName = "BackLeg_BackLowerLeg")
        # c.pyrosim.Send_Motor_Neuron( name = 14 , jointName = "FrontLeg_FrontLowerLeg")
        # c.pyrosim.Send_Motor_Neuron( name = 15 , jointName = "LeftLeg_LeftLowerLeg")
        # c.pyrosim.Send_Motor_Neuron( name = 16 , jointName = "RightLeg_RightLowerLeg")

        for currentRow in range(0, c.numSensorNeurons):
            for currentColumn in range(0, c.numMotorNeurons):
                c.pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])
        c.pyrosim.End()

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

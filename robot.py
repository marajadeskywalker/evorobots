import constants as c
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self, solutionID):
        self.robotId = c.p.loadURDF("body.urdf")
        c.pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.solutionID = solutionID
        self.nn = c.NEURAL_NETWORK(f"brain{str(solutionID)}.nndf")
        c.os.system(f"rm brain{str(solutionID)}.nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in c.pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    def Sense(self, x):
        for linkName in self.sensors:
            self.sensors[linkName].Get_Value(x)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in c.pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    def Act(self, robot, x):

        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(robot, desiredAngle)

    def Get_Fitness(self):
        stateOfLinkZero = c.p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open(f"tmp{str(self.solutionID)}.txt", "w")
        c.os.system(f"mv tmp{str(self.solutionID)}.txt fitness{str(self.solutionID)}.txt")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        exit()

    def Think(self):
        self.nn.Update()

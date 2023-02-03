import constants as c
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self):
        self.robotId = c.p.loadURDF("body.urdf")
        c.pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

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
        for jointName in self.motors:
            self.motors[jointName].Set_Value(robot, x)

import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.offset
        if self.jointName == "Torso_BackLeg":
            self.frequency = c.frequency / 2
        else:
            self.frequency = c.frequency

        self.motorValues = self.amplitude*c.numpy.sin(self.frequency*c.numpy.linspace(0, self.frequency*c.numpy.pi, 1000)+self.offset)
        c.numpy.save(c.Path(f'/Users/Max/Documents/Academia/CS206/evorobots/data/{self.jointName}MotorValues.npy'), self.motorValues)
    def Set_Value(self, robot, x):
        c.pyrosim.Set_Motor_For_Joint(bodyIndex = robot.robotId, jointName = self.jointName, controlMode = c.p.POSITION_CONTROL, targetPosition = self.motorValues[x], maxForce = 50)

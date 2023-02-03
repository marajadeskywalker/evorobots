import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

    def Set_Value(self, robot, desiredAngle):
        c.pyrosim.Set_Motor_For_Joint(bodyIndex = robot.robotId, jointName = self.jointName, controlMode = c.p.POSITION_CONTROL, targetPosition = desiredAngle, maxForce = 50)

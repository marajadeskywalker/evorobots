from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR
import constants as c

class SIMULATION:
    def __init__(self):
        self.physicsClient = c.p.connect(c.p.GUI)
        c.p.setAdditionalSearchPath(c.pybullet_data.getDataPath())
        self.world = WORLD()
        self.robot = ROBOT()
        c.p.setGravity(0,0,-9.8)


    def Run(self):
        for x in range(1000):
            c.time.sleep(float(1)/240)
            c.p.stepSimulation()
            self.robot.Sense(x)
            self.robot.Think()
            self.robot.Act(self.robot, x)

    def __del__(self):
        c.p.disconnect()

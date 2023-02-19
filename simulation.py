from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR
import constants as c

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        if directOrGUI == "DIRECT":
            self.physicsClient = c.p.connect(c.p.DIRECT)
        else:
            self.physicsClient = c.p.connect(c.p.GUI)
        c.p.setAdditionalSearchPath(c.pybullet_data.getDataPath())
        self.directOrGUI = directOrGUI
        self.world = WORLD()
        self.robot = ROBOT(solutionID)
        c.p.setGravity(0,0,-9.8)

    def Get_Fitness(self):
        self.robot.Get_Fitness()
    def Run(self):
        for x in range(500):
            if self.directOrGUI == "GUI":
                c.time.sleep(float(1)/240)
            c.p.stepSimulation()
            self.robot.Sense(x)
            self.robot.Think()
            self.robot.Act(self.robot, x)

    def __del__(self):
        c.p.disconnect()

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
from pathlib import Path
import random

backLegAmplitude = numpy.pi/3
backLegFrequency = 4
backLegPhaseOffset = numpy.pi/4

frontLegAmplitude = numpy.pi/4
frontLegFrequency = 4
frontLegPhaseOffset = 0

frontY = numpy.linspace(0, frontLegFrequency*numpy.pi, 1000)
backY = numpy.linspace(0, backLegFrequency*numpy.pi, 1000)
frontLegTargetAngles = frontLegAmplitude*numpy.sin(frontLegFrequency*frontY+frontLegPhaseOffset)
backLegTargetAngles = backLegAmplitude*numpy.sin(backLegFrequency*backY+backLegPhaseOffset)
numpy.save(Path("/Users/Max/Documents/Academia/CS206/evorobots/data/frontLegTargetAngles.npy"), frontLegTargetAngles)
numpy.save(Path("/Users/Max/Documents/Academia/CS206/evorobots/data/backLegTargetAngles.npy"), backLegTargetAngles)

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
for x in range(1000):
    time.sleep(float(1)/240)
    p.stepSimulation()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_FrontLeg", controlMode = p.POSITION_CONTROL, targetPosition = frontLegTargetAngles[x], maxForce = 50)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = backLegTargetAngles[x], maxForce = 50)
p.disconnect()

print(backLegSensorValues)
numpy.save(Path("/Users/Max/Documents/Academia/CS206/evorobots/data/backLegSensorValues.npy"), backLegSensorValues)
numpy.save(Path("/Users/Max/Documents/Academia/CS206/evorobots/data/frontLegSensorValues.npy"), frontLegSensorValues)

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
from pathlib import Path

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(200)
frontLegSensorValues = numpy.zeros(200)
for x in range(200):
    time.sleep(float(1)/60)
    p.stepSimulation()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
p.disconnect()

print(backLegSensorValues)
numpy.save(Path("/Users/Max/Documents/Academia/CS206/evorobots/data/backLegSensorValues.npy"), backLegSensorValues)
numpy.save(Path("/Users/Max/Documents/Academia/CS206/evorobots/data/frontLegSensorValues.npy"), frontLegSensorValues)

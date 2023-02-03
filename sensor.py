import constants as c
class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.values = c.numpy.zeros(1000)

    def Get_Value(self, x):
        self.values[x] = c.pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if x==999:
            c.numpy.save(c.Path(f'/Users/Max/Documents/Academia/CS206/evorobots/data/{self.linkName}SensorValues.npy'), self.values)

import numpy
import matplotlib.pyplot
from pathlib import Path

#backLegSensorValues = numpy.load(Path("/Users/Max/Documents/Academia/CS206/evorobots/data/backLegSensorValues.npy"))
#frontLegSensorValues = numpy.load(Path("/Users/Max/Documents/Academia/CS206/evorobots/data/frontLegSensorValues.npy"))
targetAngles = numpy.load(Path("/Users/Max/Documents/Academia/CS206/evorobots/data/targetAngles.npy"))
matplotlib.pyplot.plot(targetAngles)
matplotlib.pyplot.show()

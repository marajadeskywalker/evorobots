import numpy
import matplotlib.pyplot
from pathlib import Path

backLegSensorValues = numpy.load(Path("/Users/Max/Documents/Academia/CS206/evorobots/data/backLegSensorValues.npy"))
frontLegSensorValues = numpy.load(Path("/Users/Max/Documents/Academia/CS206/evorobots/data/frontLegSensorValues.npy"))

matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=3)
matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

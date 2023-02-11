import pybullet as p
import numpy
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
from pathlib import Path
from pyrosim.neuralNetwork import NEURAL_NETWORK
import random
import os
import copy


amplitude = numpy.pi/3
frequency = 4
offset = numpy.pi/4
numberOfGenerations = 10

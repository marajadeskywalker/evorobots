# import os
# for i in range(0, 5):
#     os.system("python generate.py")
#     os.system("python simulate.py")
from parallelHillClimber import PARALLEL_HILLCLIMBER
phc = PARALLEL_HILLCLIMBER()
phc.Evolve()
phc.Show_Best()

# import os
# for i in range(0, 5):
#     os.system("python generate.py")
#     os.system("python simulate.py")
from hillclimber import HILLCLIMBER
hc = HILLCLIMBER()
hc.Evolve()
hc.Show_Best()


from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, str(0))
simulation.Run()
simulation.Get_Fitness()

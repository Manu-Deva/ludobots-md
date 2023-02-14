import constants as c
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import math
import random

from world import WORLD
from robot import ROBOT


class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        if (self.directOrGUI == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def Run(self):
        for t in range(1000):
            p.stepSimulation()
            if (self.directOrGUI == "GUI"):
                time.sleep(1/60)
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)

    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()

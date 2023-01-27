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
    def __init__(self, directOrGUI):
        self.directOrGUI = directOrGUI
        if (self.directOrGUI == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for t in range(1000):
            # print(t)
            time.sleep(1/60)
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)

    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()

        # pyrosim.Set_Motor_For_Joint(
        #     bodyIndex=robotId,
        #     jointName='Torso_BackLeg',
        #     controlMode=p.POSITION_CONTROL,
        #     targetPosition=backTargetAngles[x],
        #     maxForce=c.force
        # )
        # pyrosim.Set_Motor_For_Joint(
        #     bodyIndex=robotId,
        #     jointName='Torso_FrontLeg',
        #     controlMode=p.POSITION_CONTROL,
        #     targetPosition=frontTargetAngles[x],
        #     maxForce=c.force
        # )

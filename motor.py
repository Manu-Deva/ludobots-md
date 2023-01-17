import constants as c
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import math
import random
from sensor import SENSOR


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_to_Act()

    def Prepare_to_Act(self):
        match self.jointName:
            case "Torso_FrontLeg":
                self.frequency = c.LegFrequency
            case _:
                self.frequency = c.LegFrequency/2
        self.amplitude = c.LegAmplitude
        self.offset = c.LegPhaseOffset
        self.targetValues = np.linspace(0, 2*np.pi, 1000)
        self.motorValues = self.amplitude * \
            np.sin(self.frequency * (self.targetValues + self.offset))

    def Set_Value(self, robotID, t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotID,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],
            maxForce=c.force
        )

    def Save_Values(self):
        np.save('data/motorValues', self.motorValues)

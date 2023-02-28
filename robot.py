import constants as c
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import math
import random
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR
import os


class ROBOT:
    def __init__(self, solutionID):
        self.motors = {}
        self.robotId = p.loadURDF("body" + str(solutionID) + ".urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        self.Prepare_to_Sense()
        self.Prepare_to_Act()
        self.solutionID = solutionID

        os.system("del brain" + str(solutionID) + ".nndf")

    def Prepare_to_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            if linkName in self.nn.Generate_List_Of_Sensor_Neurons():
                self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(t)

    def Prepare_to_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(
                    neuronName)*c.motorJointRange
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open("tmp" + self.solutionID + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.rename("tmp"+str(self.solutionID)+".txt",
                  "fitness"+str(self.solutionID)+".txt")

    def Think(self):
        self.nn.Update()
        # self.nn.Print()

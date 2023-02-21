import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time


class LINK:
    def __init__(self):
        self.d = random.randint(1, 6)
        self.c = random.randint(0, 1)
        self.x = random.randint(8, 15)

        self.links = {}
        for i in range(0, self.x):
            self.links["Link" + str(i)] = self.Create_Random_Size()
        self.linkNames = list(self.links.keys())
        self.selectedLinks = [None] * len(self.links)
        self.linkPositions = {}
        self.selectedJoints = [None] * len(self.links)

    def Create_Random_Size(self):
        return [random.uniform(0.5, 1.5), random.uniform(1.0, 1.5), random.uniform(1.0, 1.5)]

    def Connect_Links(self):
        for i in range(len(self.linkNames)):
            z = random.randint(0, i)
            if (i == len(self.linkNames) - 1):
                initiaLink = self.linkNames[z]
                self.selectedLinks[i] = initiaLink
                break
            initialLink = self.linkNames[z]
            self.selectedLinks[i] = initialLink
            if (i == 0):
                self.linkPositions[initialLink] = [0, 0, 0.5]
            currLink = self.linkNames[i+1]
            self.selectedLinks[i+1] = currLink

            randomJointName = initialLink + "_" + currLink
            self.selectedJoints[i] = randomJointName

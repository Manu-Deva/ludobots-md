import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time


class LINK:
    def __init__(self):
        self.d = random.randint(1, 6)
        self.x = random.randint(8, 15)

        self.links = {}
        for i in range(0, self.x):
            self.links["Link" + str(i)] = self.Create_Random_Size()
        self.linkNames = list(self.links.keys())

        self.connectedLinks = {}
        self.connectingJoints = {}
        self.initialLinks = list(range(len(self.linkNames)))

        self.Connect_Links()

        self.connectedLinkKeys = list(range(len(self.connectedLinks)))
        self.rootLink = self.connectedLinkKeys[0]

        self.linkDictionary = {}

    def Create_Random_Size(self):
        return [random.random()+0.5, random.random(), random.random()+0.10]

    def Create_Random_Pos(self):
        return [random.randint(0, 5), random.uniform(0, 5), random.uniform(0, 5)]

    # def Connect_Links(self):
    #     random.shuffle(self.linkNames)
    #     initialLink = self.linkNames[1]

    #     for i in range(1, len(self.linkNames)):
    #         prevLink = self.linkNames[i-1]
    #         currLink = self.linkNames[i]

    #         self.connectedLinks[prevLink] = currLink

    #         jointName = prevLink + "_" + currLink
    #         self.connectingJoints[prevLink] = jointName

    #         # Set the position of the current link to a random value
    #         self.linkPositions[currLink] = self.Create_Random_Pos()
    #     print(self.connectedLinks)
    #     print(self.connectingJoints)

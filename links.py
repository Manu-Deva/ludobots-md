import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time


class LINK:
    def __init__(self):
        self.d = random.randint(1, 6)
        self.x = random.randint(4, 8)

        self.linkDictionary = {}
        for i in range(0, self.x):
            self.c = random.randint(0, 1)
            self.linkDictionary[i] = {}
            self.linkDictionary[i]["connections"] = []
            self.linkDictionary[i]["size"] = self.Create_Random_Size()
            if (self.c == 0):
                self.linkDictionary[i]["cString"] = '    <color rgba="0.0 1.0 0.0 1.0"/>'
                self.linkDictionary[i]["cName"] = "Green"
            else:
                self.linkDictionary[i]["cString"] = '    <color rgba="0.0 0.0 1.0 1.0"/>'
                self.linkDictionary[i]["cName"] = "Blue"
            self.linkDictionary[i]["randomAxis"] = random.randint(0, 2)
            self.linkDictionary[i]["direction"] = random.randint(0, 1)
        self.linkNames = list(self.linkDictionary.keys())
        self.poolLinks = list()

        # self.connectedLinks = {}
        # self.connectingJoints = {}
        # self.initialLinks = list(range(len(self.linkNames)))

        self.Connect_Links()
        self.rootLink = "Link"+str(0)

        # self.connectedLinkKeys = list(range(len(self.connectedLinks)))
        # self.rootLink = self.connectedLinkKeys[0]

    def Create_Random_Size(self):
        return [random.random()+0.1, random.random()+0.1, random.random()+0.1]

    def Create_Random_Pos(self):
        return [random.randint(0, 5), random.uniform(0, 5), random.uniform(0, 5)]

    def Connect_Links(self):
        for i in range(1, self.x):
            self.poolLinks.append(i-1)
            # for num in range(random.randint(1, i)):
            randomConnection = random.choice(self.poolLinks)
            if randomConnection not in self.linkDictionary[i]["connections"]:
                self.linkDictionary[i]["connections"].append(
                    randomConnection)
        print(self.linkDictionary)

    #         self.connectedLinks[prevLink] = currLink
    #     print(self.connectedLinks)
    #     print(self.connectingJoints)

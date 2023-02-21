import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time


class LINK:
    def __init__(self):
        self.numLinks = random.randint(5, 10)
        self.connectLinks = {}
        for i in range(self.numLinks-1):
            self.connectLinks["Link" + str(i)] = self.Create_Random_Size()

        self.connectLinksKeys = list(self.connectLinks.keys())


randLegs = random.randint(3, 6)
randLinks = random.randint(3, 7)
linkNames = {}
for i in range(0, randLegs):
    linkNames["Leg" + str(i)] = i
for i in range(len(linkNames)):
    linkNames["Leg" + str(i)] = {}
    for j in range(0, randLinks):
        linkNames["Leg" + str(i)]["Link" + str(j)] = self.Create_Random_Size()


self.linkNames = [None] * self.randLegs
for i in range(self.linkNames.size()):
    self.linkNames[i] = self.temp
for i in range(len(linkNames)):
    linkNames[i] =
for j in range(self.randLegs)
self.randLeg1 = random.randint(3, 7)
self.randLeg1 = random.randint(3, 7)
self.randLeg1 = random.randint(3, 7)
self.randLeg1 = random.randint(3, 7)

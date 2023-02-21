import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time


class SOLUTION:

    def __init__(self, nextAvailableID) -> None:
        self.myID = nextAvailableID
        self.numLinks = random.randint(5, 10)
        self.randomLink = random.randint(1, self.numLinks - 3)
        self.connectLinks = {}
        for i in range(self.numLinks-1):
            self.connectLinks["Link" + str(i)] = self.Create_Random_Size()
        self.connectLinksKeys = list(self.connectLinks.keys())

        self.randLegs = random.randint(3, 6)
        self.randLinks = random.randint(3, 7)
        self.linkNames = {}
        self.count = 0
        for i in range(0, self.randLegs):
            self.linkNames["Leg" + str(i)] = i
        for i in range(len(self.linkNames)):
            self.linkNames["Leg" + str(i)] = {}
            for j in range(0, self.randLinks):
                self.count += 1
                self.linkNames["Leg" + str(i)]["Link" +
                                               str(self.count)] = self.Create_Random_Size()

        self.numMotors = self.randLinks - 1
        self.joints = list(range(self.numMotors))

        self.sensors = list(range(self.randLinks))

        self.counter = 0
        for i in range(len(self.sensors)):
            self.sensors[i] = random.randint(0, 1)
            if self.sensors[i] == 1:
                self.counter += 1

        self.links_with_sensors = list(range(self.counter))

        self.weights = (np.random.rand(
            len(self.links_with_sensors)-1, self.numMotors-2)*2) - 1

    def Evaluate(self, directOrGUI):
        self.Create_Body()
        self.Create_Brain()
        self.Create_World()
        os.system("start /B python simulate.py " +
                  "GUI" + " " + str(self.myID))
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-5.5, 10, 0.5], size=[1, 1, 1])
        pyrosim.End()

    def Create_Random_Size(self):
        return [random.uniform(0.5, 1.5), random.uniform(1.0, 1.5), random.uniform(1.0, 1.5)]

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        print(self.numLinks)
        link_size = [1, 1, 1]
        for i in range(0, self.randLegs+1):
            currLink = "Link" + str(i)
            nextLink = "Link" + str(i+1)
            currJointName = currLink + "_" + nextLink
            direction = random.randint(1, 6)
            if (i == 0):
                if self.sensors[i] == 0:
                    pyrosim.Send_Cube(name=currLink, pos=[
                        2.5, 0, 2.5], size=link_size, colorString='    <color rgba="0.0 0.0 1.0 1.0"/>', colorName='Blue')

                if self.sensors[i] == 1:
                    pyrosim.Send_Cube(name=currLink, pos=[
                        2.5, 0, 2.5], size=link_size, colorString='    <color rgba="0.0 1.0 0.0 1.0"/>', colorName='Green')

                if direction == 1:
                    pyrosim.Send_Joint(name=currJointName, parent=currLink,
                                       child=nextLink, type="revolute", position=[3.0, 0, 2.5])  # x
                if direction == 2:
                    pyrosim.Send_Joint(name=currJointName, parent=currLink,
                                       child=nextLink, type="revolute", position=[2.5, 0.5, 2.5])  # y
                if direction == 3:
                    pyrosim.Send_Joint(name=currJointName, parent=currLink,
                                       child=nextLink, type="revolute", position=[2.5, 0, 3.0])  # z
                if direction == 4:
                    pyrosim.Send_Joint(name=currJointName, parent=currLink,
                                       child=nextLink, type="revolute", position=[2.0, 0, 2.5])  # -x
                if direction == 5:
                    pyrosim.Send_Joint(name=currJointName, parent=currLink,
                                       child=nextLink, type="revolute", position=[2.5, -0.5, 2.5])  # -y
                if direction == 6:
                    pyrosim.Send_Joint(name=currJointName, parent=currLink,
                                       child=nextLink, type="revolute", position=[2.5, 0, 2.0])  # -z

            else:
                if
                currLeg = "Leg"+str(i-1)
                currLink = (i-1)+1
                nextLink = (i-1)+2
                moreNextLink = (i-1)+3
                if self.sensors[i] == 0:
                    incrementer = 0
                    if direction == 1:

                        if (incrementer != 3):
                            pyrosim.Send_Cube(name=currLink, pos=[self.linkNames[currLeg].get(currLink)[0]/2, 0, 0
                                                                  ], size=self.linkNames[currLeg].get(currLink), colorString='    <color rgba="0.0 0.0 1.0 1.0"/>', colorName='Blue')
                            pyrosim.Send_Joint(name=currJointName, parent=currLink, child=nextLink, type="revolute", position=[
                                self.linkNames[currLeg].get(currLink)[0], 0, 0])
                            pyrosim.Send_Cube(name=nextLink, pos=[self.linkNames[currLeg].get(nextLink)[0]/2, 0, 0
                                                                  ], size=self.linkNames[currLeg].get(currLink), colorString='    <color rgba="0.0 0.0 1.0 1.0"/>', colorName='Blue')
                            incrementer += 4
                        if (incrementer == 4):
                            pyrosim.Send_Joint(name=currJointName, parent=currLink, child=nextLink, type="revolute", position=[
                                self.linkNames[currLeg].get(currLink)[0]/2, 0, -self.linkNames[currLeg].get(currLink)[2]/2])
                            incrementer += 1
                        if (incrementer < 4):
                            pyrosim.Send_Cube(name=currLink, pos=[0, 0, -self.linkNames[currLeg].get(currLink)[2]/2
                                                                  ], size=self.linkNames[currLeg].get(currLink), colorString='    <color rgba="0.0 0.0 1.0 1.0"/>', colorName='Blue')
                            if (j != self.randLinks):
                                pyrosim.Send_Joint(name=currJointName, parent=currLink, child=nextLink, type="revolute", position=[
                                    self.linkNames[currLeg].get(currLink)[0]/2, 0, -self.linkNames[currLeg].get(currLink)[2]/2])

                    if direction == 2:
                        for j in range(0, self.randLinks):
                            pyrosim.Send_Cube(name=currLink, pos=[0, self.linkNames[currLeg].get(currLink)[0]/2, 0
                                                                  ], size=self.linkNames[currLeg].get(currLink), colorString='    <color rgba="0.0 0.0 1.0 1.0"/>', colorName='Blue')
                            pyrosim.Send_Joint(name=currJointName, parent=currLink, child=nextLink, type="revolute", position=[
                                               0, self.linkNames[currLeg].get(currLink)[0], 0])

                    if direction == 4:
                        for j in range(0, self.randLinks):
                            pyrosim.Send_Cube(name=currLink, pos=[-self.linkNames[currLeg].get(currLink)[0]/2, 0, 0
                                                                  ], size=self.linkNames[currLeg].get(currLink), colorString='    <color rgba="0.0 0.0 1.0 1.0"/>', colorName='Blue')
                            pyrosim.Send_Joint(name=currJointName, parent=currLink, child=nextLink, type="revolute", position=[
                                               -self.linkNames[currLeg].get(currLink)[0], 0, 0])

                    if direction == 5:
                        for j in range(0, self.randLinks):
                            pyrosim.Send_Cube(name=currLink, pos=[0, -self.linkNames[currLeg].get(currLink)[0]/2, 0
                                                                  ], size=self.linkNames[currLeg].get(currLink), colorString='    <color rgba="0.0 0.0 1.0 1.0"/>', colorName='Blue')
                            pyrosim.Send_Joint(name=currJointName, parent=currLink, child=nextLink, type="revolute", position=[
                                               0, -self.linkNames[currLeg].get(currLink)[0], 0])

                    if direction == 5:
                        for j in range(0, self.randLinks):
                            pyrosim.Send_Cube(name=currLink, pos=[self.linkNames[currLeg].get(currLink)[0]/2, 0, 0
                                                                  ], size=self.linkNames[currLeg].get(currLink), colorString='    <color rgba="0.0 0.0 1.0 1.0"/>', colorName='Blue')
                            pyrosim.Send_Joint(name=currJointName, parent=currLink, child=nextLink, type="revolute", position=[
                                               self.linkNames[currLeg].get(currLink)[0], 0, 0])

                    if direction == 6:
                        for j in range(0, self.randLinks):
                            pyrosim.Send_Cube(name=currLink, pos=[self.linkNames[currLeg].get(currLink)[0]/2, 0, 0
                                                                  ], size=self.linkNames[currLeg].get(currLink), colorString='    <color rgba="0.0 0.0 1.0 1.0"/>', colorName='Blue')
                            pyrosim.Send_Joint(name=currJointName, parent=currLink, child=nextLink, type="revolute", position=[
                                               self.linkNames[currLeg].get(currLink)[0], 0, 0])

                if self.sensors[i] == 1:
                    if direction == 1:
                        pyrosim.Send_Cube(name=self.connectLinksKeys[i], pos=[
                            self.connectLinks[self.connectLinksKeys[i]][0]/2, 0, 0], size=self.connectLinks[self.connectLinksKeys[i]], colorString='    <color rgba="0.0 1.0 0.0 1.0"/>', colorName='Green')
                    if direction == 2:
                        pyrosim.Send_Cube(name=self.connectLinksKeys[i], pos=[
                            0, self.connectLinks[self.connectLinksKeys[i]][1]/2, 0], size=self.connectLinks[self.connectLinksKeys[i]], colorString='    <color rgba="0.0 1.0 0.0 1.0"/>', colorName='Green')
                    if direction == 3:
                        pyrosim.Send_Cube(name=self.connectLinksKeys[i], pos=[
                            0, 0, self.connectLinks[self.connectLinksKeys[i]][2]/2], size=self.connectLinks[self.connectLinksKeys[i]], colorString='    <color rgba="0.0 1.0 0.0 1.0"/>', colorName='Green')
                    if direction == 4:
                        pyrosim.Send_Cube(name=self.connectLinksKeys[i], pos=[
                            -self.connectLinks[self.connectLinksKeys[i]][0]/2, 0, 0], size=self.connectLinks[self.connectLinksKeys[i]], colorString='    <color rgba="0.0 1.0 0.0 1.0"/>', colorName='Green')
                    if direction == 5:
                        pyrosim.Send_Cube(name=self.connectLinksKeys[i], pos=[
                            0, -self.connectLinks[self.connectLinksKeys[i]][1]/2, 0], size=self.connectLinks[self.connectLinksKeys[i]], colorString='    <color rgba="0.0 1.0 0.0 1.0"/>', colorName='Green')
                    if direction == 6:
                        pyrosim.Send_Cube(name=self.connectLinksKeys[i], pos=[
                            0, 0, -self.connectLinks[self.connectLinksKeys[i]][2]/2], size=self.connectLinks[self.connectLinksKeys[i]], colorString='    <color rgba="0.0 1.0 0.0 1.0"/>', colorName='Green')
                    self.sensors[i] = linkName

                if (i < self.numLinks-2):
                    if direction == 1:
                        pyrosim.Send_Joint(name=currJointName, parent=linkName,
                                           child=nextLinkName, type="revolute", position=[self.connectLinks[self.connectLinksKeys[i+1]][0], 0, 0])
                    if direction == 2:
                        pyrosim.Send_Joint(name=currJointName, parent=linkName,
                                           child=nextLinkName, type="revolute", position=[0, self.connectLinks[self.connectLinksKeys[i+1]][1], 0])
                    if direction == 3:
                        pyrosim.Send_Joint(name=currJointName, parent=linkName,
                                           child=nextLinkName, type="revolute", position=[0, 0, self.connectLinks[self.connectLinksKeys[i+1]][2]])
                    if direction == 4:
                        pyrosim.Send_Joint(name=currJointName, parent=linkName,
                                           child=nextLinkName, type="revolute", position=[-self.connectLinks[self.connectLinksKeys[i+1]][0], 0, 0])
                    if direction == 5:
                        pyrosim.Send_Joint(name=currJointName, parent=linkName,
                                           child=nextLinkName, type="revolute", position=[0, -self.connectLinks[self.connectLinksKeys[i+1]][1], 0])
                    if direction == 6:
                        pyrosim.Send_Joint(name=currJointName, parent=linkName,
                                           child=nextLinkName, type="revolute", position=[0, 0, -self.connectLinks[self.connectLinksKeys[i+1]][2]])
                    self.joints[i] = currJointName

        print(self.joints)
        self.joints = self.joints[:-1]
        print(self.joints)

        pyrosim.End()

    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        # for i in range(0, len(self.sensors)):
        #     if self.sensors[i] == "Link" + str(i):
        #         pyrosim.Send_Sensor_Neuron(
        #             name=i, linkName=str(self.sensors[i]))

        # for i in range(0, self.numMotors-1):
        #     if i < len(self.joints):
        #         pyrosim.Send_Motor_Neuron(
        #             name=self.numLinks+i, jointName=str(self.joints[i]))

        # for currentRow in range(len(self.sensors)):
        #     if self.sensors[currentRow] == "Link" + str(currentRow):
        #         for currentColumn in range(self.numMotors):
        #             pyrosim.Send_Synapse(currentRow, currentColumn +
        #                                  len(self.sensors)-1, 1)
        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0, len(self.weights) - 1)
        randomColumn = random.randint(0, len(self.weights[0]) - 1)
        self.weights[randomRow, randomColumn] = (random.random() * 2) - 1

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python simulate.py " +
                  "GUI" + " " + str(1))

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()
        os.system("del fitness" + str(self.myID) + ".txt")

    def Set_ID(self, ID):
        self.myID = ID

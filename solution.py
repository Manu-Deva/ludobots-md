import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time
from links import LINK


class SOLUTION:

    def __init__(self, nextAvailableID) -> None:
        self.myID = nextAvailableID
        self.link = LINK()
        self.numMotors = self.link.x - 1
        self.joints = list(range(self.numMotors))
        self.randomPos = self.link.linkPos

        self.sensors = list(range(self.link.x))

        self.counter = 0
        for i in range(len(self.sensors)):
            self.sensors[i] = random.randint(0, 1)
            if self.sensors[i] == 1:
                self.counter += 1

        self.links_with_sensors = list(range(self.counter))

        self.colors = {0: {"colorString": '    <color rgba="0.0 0.0 1.0 1.0"/>',
                           "color": "Blue"},
                       1: {"colorString": '    <color rgba="0.0 1.0 0.0 1.0"/>',
                           "color": "Green"}
                       }

        self.generatedLinks = {self.link.rootLink}

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
        prevd = 1
        for link in self.link.connectedLinks:
            self.d = random.randint(1, 6)
            opposite_directions = {1: 4, 2: 5, 3: 6, 4: 1, 5: 2, 6: 3}
            while self.d == opposite_directions[prevd]:
                self.d = random.randint(1, 6)
            self.c = random.randint(0, 1)
            currLinkName = str(link)
            nextLinkName = str(self.link.connectedLinks[currLinkName])
            currLinkSize = self.link.links[currLinkName]
            if (self.link.connectedLinks[currLinkName] is not None):
                nextLinkSize = self.link.links[nextLinkName]

            currJointName = currLinkName + "_" + nextLinkName
            if self.d == 1:
                # dist = sum([abs(nextLinkPos[i] - currLinkPos[i])
                #             for i in range(3)]) - sum([currLinkSize[i] for i in range(3)])

                # while dist < 0.5*sum(nextLinkSize) + 0.5*sum(currLinkSize):
                #     self.d = random.randint(1, 6)
                match prevd:
                    case 0:
                        jointMovement = [currLinkSize[0], 0, 0]
                    case 1:
                        jointMovement = [currLinkSize[0], 0, 0]
                    case 2:
                        jointMovement = [0.5*currLinkSize[0],
                                         0.5*currLinkSize[1], 0]
                    case 3:
                        jointMovement = [0.5*currLinkSize[0],
                                         0, 0.5*currLinkSize[2]]
                    case 4:
                        jointMovement = [currLinkSize[0], 0, 0]
                    case 5:
                        jointMovement = [0.5*currLinkSize[0],
                                         -0.5*currLinkSize[1], 0]
                    case 6:
                        jointMovement = [
                            0.5*currLinkSize[0], 0, -0.5*currLinkSize[2]]

                currLinkPos = [0.5*currLinkSize[0], 0, 0]
                nextLinkPos = [0.5*nextLinkSize[0], 0, 0]

                if currLinkName not in self.generatedLinks:
                    pyrosim.Send_Cube(name=currLinkName, pos=currLinkPos, size=currLinkSize,
                                      colorString=self.colors[self.c]["colorString"], colorName=self.colors[self.c]["color"])
                    self.generatedLinks.add(currLinkName)

                if (self.link.connectedLinks[currLinkName] is None):
                    break

                while (nextLinkPos[0] - currLinkPos[0] <= 0 and nextLinkPos[1] - currLinkPos[1] <= 0 and nextLinkPos[2] - currLinkPos[2] <= 0):
                    nextLinkPos[0] += 0.01*nextLinkSize[0]
                    nextLinkPos[1] += 0.01*nextLinkSize[1]
                    nextLinkPos[2] += 0.01*nextLinkSize[2]

                pyrosim.Send_Joint(
                    name=currJointName, parent=currLinkName, child=nextLinkName,
                    type="revolute", position=jointMovement)
                if nextLinkName not in self.generatedLinks:

                    self.c = random.randint(0, 1)

                    pyrosim.Send_Cube(name=nextLinkName, pos=nextLinkPos, size=nextLinkSize,
                                      colorString=self.colors[self.c]["colorString"], colorName=self.colors[self.c]["color"])
                    self.generatedLinks.add(nextLinkName)

                prevd = self.d

            if self.d == 2:
                match prevd:
                    case 0:
                        jointMovement = [0, currLinkSize[1], 0]
                    case 1:
                        jointMovement = [0.5*currLinkSize[0],
                                         0.5*currLinkSize[1], 0]
                    case 2:
                        jointMovement = [0, currLinkSize[1], 0]
                    case 3:
                        jointMovement = [0,
                                         0.5*currLinkSize[1], 0.5*currLinkSize[2]]
                    case 4:
                        jointMovement = [-0.5*currLinkSize[0],
                                         0.5*currLinkSize[1], 0]
                    case 5:
                        jointMovement = [0, currLinkSize[1], 0]
                    case 6:
                        jointMovement = [
                            0, 0.5*currLinkSize[1], -0.5*currLinkSize[2]]
                currLinkPos = [0, 0.5*currLinkSize[1], 0]
                nextLinkPos = [0, 0.5*nextLinkSize[1], 0]
                if currLinkName not in self.generatedLinks:
                    pyrosim.Send_Cube(name=currLinkName, pos=currLinkPos, size=currLinkSize,
                                      colorString=self.colors[self.c]["colorString"], colorName=self.colors[self.c]["color"])
                    self.generatedLinks.add(currLinkName)

                if (self.link.connectedLinks[currLinkName] is None):
                    break

                while (nextLinkPos[0] - currLinkPos[0] <= 0 and nextLinkPos[1] - currLinkPos[1] <= 0 and nextLinkPos[2] - currLinkPos[2] <= 0):
                    nextLinkPos[0] += 0.01*nextLinkSize[0]
                    nextLinkPos[1] += 0.01*nextLinkSize[1]
                    nextLinkPos[2] += 0.01*nextLinkSize[2]

                pyrosim.Send_Joint(
                    name=currJointName, parent=currLinkName, child=nextLinkName,
                    type="revolute", position=jointMovement)
                if nextLinkName not in self.generatedLinks:

                    self.c = random.randint(0, 1)

                    pyrosim.Send_Cube(name=nextLinkName, pos=nextLinkPos, size=nextLinkSize,
                                      colorString=self.colors[self.c]["colorString"], colorName=self.colors[self.c]["color"])
                    self.generatedLinks.add(nextLinkName)

                prevd = self.d

            if self.d == 3:
                match prevd:
                    case 0:
                        jointMovement = [0, 0, currLinkSize[2]]
                    case 1:
                        jointMovement = [0.5*currLinkSize[0],
                                         0, 0.5*currLinkSize[2]]
                    case 2:
                        jointMovement = [
                            0, 0.5*currLinkSize[1], 0.5*currLinkSize[2]]
                    case 3:
                        jointMovement = [0, 0, currLinkSize[2]]
                    case 4:
                        jointMovement = [-0.5*currLinkSize[0],
                                         0, 0.5*currLinkSize[2]]
                    case 5:
                        jointMovement = [
                            0, -0.5*currLinkSize[1], 0.5*currLinkSize[2]]
                    case 6:
                        jointMovement = [0, 0, currLinkSize[2]]
                currLinkPos = [0, 0, 0.5*currLinkSize[2]]
                nextLinkPos = [0, 0, 0.5*nextLinkSize[2]]
                if currLinkName not in self.generatedLinks:
                    pyrosim.Send_Cube(name=currLinkName, pos=currLinkPos, size=currLinkSize,
                                      colorString=self.colors[self.c]["colorString"], colorName=self.colors[self.c]["color"])
                    self.generatedLinks.add(currLinkName)

                if (self.link.connectedLinks[currLinkName] is None):
                    break

                while (nextLinkPos[0] - currLinkPos[0] <= 0 and nextLinkPos[1] - currLinkPos[1] <= 0 and nextLinkPos[2] - currLinkPos[2] <= 0):
                    nextLinkPos[0] += 0.01*nextLinkSize[0]
                    nextLinkPos[1] += 0.01*nextLinkSize[1]
                    nextLinkPos[2] += 0.01*nextLinkSize[2]

                pyrosim.Send_Joint(
                    name=currJointName, parent=currLinkName, child=nextLinkName,
                    type="revolute", position=jointMovement)
                if nextLinkName not in self.generatedLinks:

                    self.c = random.randint(0, 1)

                    pyrosim.Send_Cube(name=nextLinkName, pos=nextLinkPos, size=nextLinkSize,
                                      colorString=self.colors[self.c]["colorString"], colorName=self.colors[self.c]["color"])
                    self.generatedLinks.add(nextLinkName)

                prevd = self.d

            if self.d == 4:
                match prevd:
                    case 0:
                        jointMovement = [-currLinkSize[0], 0, 0]
                    case 1:
                        jointMovement = [-currLinkSize[0], 0, 0]
                    case 2:
                        jointMovement = [-0.5*currLinkSize[0],
                                         0.5*currLinkSize[1], 0]
                    case 3:
                        jointMovement = [-0.5*currLinkSize[0],
                                         0, 0.5*currLinkSize[2]]
                    case 4:
                        jointMovement = [-currLinkSize[0], 0, 0]
                    case 5:
                        jointMovement = [-0.5*currLinkSize[0],
                                         -0.5*currLinkSize[1], 0]
                    case 6:
                        jointMovement = [-0.5*currLinkSize[0],
                                         0, -0.5*currLinkSize[2]]
                currLinkPos = [-0.5*currLinkSize[0], 0, 0]
                nextLinkPos = [-0.5*nextLinkSize[0], 0, 0]
                if currLinkName not in self.generatedLinks:
                    pyrosim.Send_Cube(name=currLinkName, pos=currLinkPos, size=currLinkSize,
                                      colorString=self.colors[self.c]["colorString"], colorName=self.colors[self.c]["color"])
                    self.generatedLinks.add(currLinkName)

                if (self.link.connectedLinks[currLinkName] is None):
                    break

                while (nextLinkPos[0] - currLinkPos[0] <= 0 and nextLinkPos[1] - currLinkPos[1] <= 0 and nextLinkPos[2] - currLinkPos[2] <= 0):
                    nextLinkPos[0] += 0.01*nextLinkSize[0]
                    nextLinkPos[1] += 0.01*nextLinkSize[1]
                    nextLinkPos[2] += 0.01*nextLinkSize[2]

                pyrosim.Send_Joint(
                    name=currJointName, parent=currLinkName, child=nextLinkName,
                    type="revolute", position=jointMovement)
                if nextLinkName not in self.generatedLinks:

                    self.c = random.randint(0, 1)

                    pyrosim.Send_Cube(name=nextLinkName, pos=nextLinkPos, size=nextLinkSize,
                                      colorString=self.colors[self.c]["colorString"], colorName=self.colors[self.c]["color"])
                    self.generatedLinks.add(nextLinkName)

                prevd = self.d

            if self.d == 5:
                match prevd:
                    case 0:
                        jointMovement = [0, -currLinkSize[1], 0]
                    case 1:
                        jointMovement = [
                            0.5*currLinkSize[0], -0.5*currLinkSize[1], 0]
                    case 2:
                        jointMovement = [0, -currLinkSize[1], 0]
                    case 3:
                        jointMovement = [
                            0, -0.5*currLinkSize[1], 0.5*currLinkSize[2]]
                    case 4:
                        jointMovement = [-0.5*currLinkSize[0], -
                                         0.5*currLinkSize[1], 0]
                    case 5:
                        jointMovement = [0, -currLinkSize[1], 0]
                    case 6:
                        jointMovement = [
                            0, -0.5*currLinkSize[1], -0.5*currLinkSize[2]]
                currLinkPos = [0, -0.5*currLinkSize[1], 0]
                nextLinkPos = [0, -0.5*nextLinkSize[1], 0]
                if currLinkName not in self.generatedLinks:
                    pyrosim.Send_Cube(name=currLinkName, pos=currLinkPos, size=currLinkSize,
                                      colorString=self.colors[self.c]["colorString"], colorName=self.colors[self.c]["color"])
                    self.generatedLinks.add(currLinkName)

                if (self.link.connectedLinks[currLinkName] is None):
                    break

                while (nextLinkPos[0] - currLinkPos[0] <= 0 and nextLinkPos[1] - currLinkPos[1] <= 0 and nextLinkPos[2] - currLinkPos[2] <= 0):
                    nextLinkPos[0] += 0.01*nextLinkSize[0]
                    nextLinkPos[1] += 0.01*nextLinkSize[1]
                    nextLinkPos[2] += 0.01*nextLinkSize[2]

                pyrosim.Send_Joint(
                    name=currJointName, parent=currLinkName, child=nextLinkName,
                    type="revolute", position=jointMovement)
                if nextLinkName not in self.generatedLinks:

                    self.c = random.randint(0, 1)

                    pyrosim.Send_Cube(name=nextLinkName, pos=nextLinkPos, size=nextLinkSize,
                                      colorString=self.colors[self.c]["colorString"], colorName=self.colors[self.c]["color"])
                    self.generatedLinks.add(nextLinkName)

                prevd = self.d
            if self.d == 6:
                match prevd:
                    case 0:
                        jointMovement = [0, 0, -currLinkSize[2]]
                    case 1:
                        jointMovement = [0.5*currLinkSize[0],
                                         0, -0.5*currLinkSize[2]]
                    case 2:
                        jointMovement = [
                            0, 0.5*currLinkSize[1], -0.5*currLinkSize[2]]
                    case 3:
                        jointMovement = [0, 0, -currLinkSize[2]]
                    case 4:
                        jointMovement = [-0.5*currLinkSize[0],
                                         0, -0.5*currLinkSize[2]]
                    case 5:
                        jointMovement = [
                            0, -0.5*currLinkSize[1], -0.5*currLinkSize[2]]
                    case 6:
                        jointMovement = [0, 0, -currLinkSize[2]]
                currLinkPos = [0, 0, -0.5*currLinkSize[2]]
                nextLinkPos = [0, 0, -0.5*nextLinkSize[2]]
                if currLinkName not in self.generatedLinks:
                    pyrosim.Send_Cube(name=currLinkName, pos=currLinkPos, size=currLinkSize,
                                      colorString=self.colors[self.c]["colorString"], colorName=self.colors[self.c]["color"])
                    self.generatedLinks.add(currLinkName)

                if (self.link.connectedLinks[currLinkName] is None):
                    break

                while (nextLinkPos[0] - currLinkPos[0] <= 0 and nextLinkPos[1] - currLinkPos[1] <= 0 and nextLinkPos[2] - currLinkPos[2] <= 0):
                    nextLinkPos[0] += 0.01*nextLinkSize[0]
                    nextLinkPos[1] += 0.01*nextLinkSize[1]
                    nextLinkPos[2] += 0.01*nextLinkSize[2]

                pyrosim.Send_Joint(
                    name=currJointName, parent=currLinkName, child=nextLinkName,
                    type="revolute", position=jointMovement)
                if nextLinkName not in self.generatedLinks:

                    self.c = random.randint(0, 1)

                    pyrosim.Send_Cube(name=nextLinkName, pos=nextLinkPos, size=nextLinkSize,
                                      colorString=self.colors[self.c]["colorString"], colorName=self.colors[self.c]["color"])
                    self.generatedLinks.add(nextLinkName)

                prevd = self.d

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

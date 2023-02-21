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

    def Create_Random_Pos(self):
        return [random.randint(0, 5), random.uniform(0, 5), random.uniform(0, 5)]

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        randomPos = self.Create_Random_Pos()
        for i in range(0, self.link.x):
            if self.link.d == 1:
                if (i == self.link.x - 1):
                    pyrosim.Send_Cube(name=self.link.selectedLinks[i], pos=[randomPos], size=self.link.links[self.link.selectedLinks[i]],
                                      colorString=self.colors[self.link.c]["colorString"], colorString=self.colors[self.link.c]["color"])
                    break

                pyrosim.Send_Cube(name=self.link.selectedLinks[i], pos=[randomPos], size=self.link.links[self.link.selectedLinks[i]],
                                  colorString=self.colors[self.link.c]["colorString"], colorString=self.colors[self.link.c]["color"])
                pyrosim.Send_Joint(
                    name=self.link.selectedJoints[i], parent=self.link.selectedLinks[i], child=self.link.selectedLinks[i+1],
                    type="revolute", position=[randomPos[0]+(0.5*self.link.links[self.link.selectedLinks[i]][0]), 0, 0])
                # pyrosim.Send_Cube(name=self.link.selectedLinks[i+1], pos=[], size=self.link.links[self.link.selectedLinks[i+1]],
                #                   colorString=self.colors[self.link.c]["colorString"], colorString=self.colors[self.link.c]["color"])

            if self.link.d == 2:
                if (i == self.link.x - 1):
                    pyrosim.Send_Cube(name=self.link.selectedLinks[i], pos=[randomPos], size=self.link.links[self.link.selectedLinks[i]],
                                      colorString=self.colors[self.link.c]["colorString"], colorString=self.colors[self.link.c]["color"])
                    break
                pyrosim.Send_Cube(name=self.link.selectedLinks[i], pos=[randomPos], size=self.link.links[self.link.selectedLinks[i]],
                                  colorString=self.colors[self.link.c]["colorString"], colorString=self.colors[self.link.c]["color"])
                pyrosim.Send_Joint(
                    name=self.link.selectedJoints[i], parent=self.link.selectedLinks[i], child=self.link.selectedLinks[i+1],
                    type="revolute", position=[0, randomPos[0]+(0.5*self.link.links[self.link.selectedLinks[i]][0]), 0])
                # pyrosim.Send_Cube(name=self.link.selectedLinks[i+1], pos=[], size=self.link.links[self.link.selectedLinks[i+1]],
                #                   colorString=self.colors[self.link.c]["colorString"], colorString=self.colors[self.link.c]["color"])

            if self.link.d == 3:
                if (i == self.link.x - 1):
                    pyrosim.Send_Cube(name=self.link.selectedLinks[i], pos=[randomPos], size=self.link.links[self.link.selectedLinks[i]],
                                      colorString=self.colors[self.link.c]["colorString"], colorString=self.colors[self.link.c]["color"])
                    break
                pyrosim.Send_Cube(name=self.link.selectedLinks[i], pos=[randomPos], size=self.link.links[self.link.selectedLinks[i]],
                                  colorString=self.colors[self.link.c]["colorString"], colorString=self.colors[self.link.c]["color"])
                pyrosim.Send_Joint(
                    name=self.link.selectedJoints[i], parent=self.link.selectedLinks[i], child=self.link.selectedLinks[i+1],
                    type="revolute", position=[0, 0, randomPos[0]+(0.5*self.link.links[self.link.selectedLinks[i]][0])])
                # pyrosim.Send_Cube(name=self.link.selectedLinks[i+1], pos=[], size=self.link.links[self.link.selectedLinks[i+1]],
                #                   colorString=self.colors[self.link.c]["colorString"], colorString=self.colors[self.link.c]["color"])

            if self.link.d == 4:
                if (i == self.link.x - 1):
                    pyrosim.Send_Cube(name=self.link.selectedLinks[i], pos=[randomPos], size=self.link.links[self.link.selectedLinks[i]],
                                      colorString=self.colors[self.link.c]["colorString"], colorString=self.colors[self.link.c]["color"])
                    break
                pyrosim.Send_Cube(name=self.link.selectedLinks[i], pos=[randomPos], size=self.link.links[self.link.selectedLinks[i]],
                                  colorString=self.colors[self.link.c]["colorString"], colorString=self.colors[self.link.c]["color"])
                pyrosim.Send_Joint(
                    name=self.link.selectedJoints[i], parent=self.link.selectedLinks[i], child=self.link.selectedLinks[i+1],
                    type="revolute", position=[randomPos[0]-(0.5*self.link.links[self.link.selectedLinks[i]][0]), 0, 0])
                # pyrosim.Send_Cube(name=self.link.selectedLinks[i+1], pos=[], size=self.link.links[self.link.selectedLinks[i+1]],
                #                   colorString=self.colors[self.link.c]["colorString"], colorString=self.colors[self.link.c]["color"])

            if self.link.d == 5:
                if (i == self.link.x - 1):
                    pyrosim.Send_Cube(name=self.link.selectedLinks[i], pos=[randomPos], size=self.link.links[self.link.selectedLinks[i]],
                                      colorString=self.colors[self.link.c]["colorString"], colorString=self.colors[self.link.c]["color"])
                    break
                pyrosim.Send_Cube(name=self.link.selectedLinks[i], pos=[randomPos], size=self.link.links[self.link.selectedLinks[i]],
                                  colorString=self.colors[self.link.c]["colorString"], colorString=self.colors[self.link.c]["color"])
                pyrosim.Send_Joint(
                    name=self.link.selectedJoints[i], parent=self.link.selectedLinks[i], child=self.link.selectedLinks[i+1],
                    type="revolute", position=[0, randomPos[0]-(0.5*self.link.links[self.link.selectedLinks[i]][0]), 0])
                # pyrosim.Send_Cube(name=self.link.selectedLinks[i+1], pos=[], size=self.link.links[self.link.selectedLinks[i+1]],
                #                   colorString=self.colors[self.link.c]["colorString"], colorString=self.colors[self.link.c]["color"])

            if self.link.d == 6:
                if (i == self.link.x - 1):
                    pyrosim.Send_Cube(name=self.link.selectedLinks[i], pos=[randomPos], size=self.link.links[self.link.selectedLinks[i]],
                                      colorString=self.colors[self.link.c]["colorString"], colorString=self.colors[self.link.c]["color"])
                    break
                pyrosim.Send_Cube(name=self.link.selectedLinks[i], pos=[randomPos], size=self.link.links[self.link.selectedLinks[i]],
                                  colorString=self.colors[self.link.c]["colorString"], colorString=self.colors[self.link.c]["color"])
                pyrosim.Send_Joint(
                    name=self.link.selectedJoints[i], parent=self.link.selectedLinks[i], child=self.link.selectedLinks[i+1],
                    type="revolute", position=[0, 0, randomPos[0]-(0.5*self.link.links[self.link.selectedLinks[i]][0])])
                # pyrosim.Send_Cube(name=self.link.selectedLinks[i+1], pos=[], size=self.link.links[self.link.selectedLinks[i+1]],
                #                   colorString=self.colors[self.link.c]["colorString"], colorString=self.colors[self.link.c]["color"])

                if direction == 1:
                    pyrosim.Send_Joint(name=currJointName, parent=currLink,
                                       child=nextLink, type="revolute", position=[linkPos[0]+0.5*linkSize[0], 0, 2.5])  # x
                if direction == 2:
                    pyrosim.Send_Joint(name=currJointName, parent=currLink,
                                       child=nextLink, type="revolute", position=[2.5, linkPos[0]+0.5*linkSize[0], 2.5])  # y
                if direction == 3:
                    pyrosim.Send_Joint(name=currJointName, parent=currLink,
                                       child=nextLink, type="revolute", position=[2.5, 0, linkPos[0]+0.5*linkSize[0]])  # z
                if direction == 4:
                    pyrosim.Send_Joint(name=currJointName, parent=currLink,
                                       child=nextLink, type="revolute", position=[linkPos[0]-0.5*linkSize[0], 0, 2.5])  # -x
                if direction == 5:
                    pyrosim.Send_Joint(name=currJointName, parent=currLink,
                                       child=nextLink, type="revolute", position=[2.5, linkPos[0]-0.5*linkSize[0], 2.5])  # -y
                if direction == 6:
                    pyrosim.Send_Joint(name=currJointName, parent=currLink,
                                       child=nextLink, type="revolute", position=[2.5, 0, linkPos[0]-0.5*linkSize[0]])  # -z

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

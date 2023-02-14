import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time


class SOLUTION:
    def __init__(self, nextAvailableID) -> None:
        self.myID = nextAvailableID
        self.numLinks = random.randint(2, 8)

        self.numMotors = self.numLinks - 1
        self.joints = list(range(self.numMotors))

        self.sensors = list(range(self.numLinks))

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
        return [random.random()+0.5, random.random(), random.random()+0.10]

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        print(self.numLinks)
        for i in range(self.numLinks-1):

            linkName = "Link" + str(i)
            print(linkName)
            nextLinkName = "Link" + str(i+1)
            currJointName = "Link" + str(i) + "_" + "Link" + str(i+1)
            if (i == 0):
                if self.sensors[i] == 0:
                    pyrosim.Send_Cube(name=linkName, pos=[
                        0, 0, 0.5], size=self.Create_Random_Size(), colorString='    <color rgba="0.0 0.0 1.0 1.0"/>', colorName='Blue')

                if self.sensors[i] == 1:
                    pyrosim.Send_Cube(name=linkName, pos=[
                        0, 0, 0.5], size=self.Create_Random_Size(), colorString='    <color rgba="0.0 1.0 0.0 1.0"/>', colorName='Green')
                    self.sensors[i] = linkName

                if (i < self.numLinks-2):
                    pyrosim.Send_Joint(name=currJointName, parent=linkName,
                                       child=nextLinkName, type="revolute", position=[0.5, 0, 0.5])
                    self.joints[i] = currJointName

            else:

                if self.sensors[i] == 0:
                    pyrosim.Send_Cube(name=linkName, pos=[
                        0.5, 0, 0], size=self.Create_Random_Size(), colorString='    <color rgba="0.0 0.0 1.0 1.0"/>', colorName='Blue')

                if self.sensors[i] == 1:
                    pyrosim.Send_Cube(name=linkName, pos=[
                        0.5, 0, 0], size=self.Create_Random_Size(), colorString='    <color rgba="0.0 1.0 0.0 1.0"/>', colorName='Green')
                    self.sensors[i] = linkName

                if (i < self.numLinks-2):
                    pyrosim.Send_Joint(name=currJointName, parent=linkName,
                                       child=nextLinkName, type="revolute", position=[1, 0, 0])
                    self.joints[i] = currJointName

        print(self.joints)
        self.joints = self.joints[:-1]
        print(self.joints)

        pyrosim.End()

    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        for i in range(0, len(self.sensors)):
            if self.sensors[i] == "Link" + str(i):
                pyrosim.Send_Sensor_Neuron(
                    name=i, linkName=str(self.sensors[i]))

        for i in range(0, self.numMotors-1):
            if i < len(self.joints):
                pyrosim.Send_Motor_Neuron(
                    name=self.numLinks+i, jointName=str(self.joints[i]))

        for currentRow in range(len(self.sensors)):
            if self.sensors[currentRow] == "Link" + str(currentRow):
                for currentColumn in range(self.numMotors):
                    pyrosim.Send_Synapse(currentRow, currentColumn +
                                         len(self.sensors)-1, 1)
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

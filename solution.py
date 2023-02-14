import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time


class SOLUTION:
    def __init__(self, nextAvailableID) -> None:
        self.myID = nextAvailableID
        self.numLinks = random.randint(5, 15)
        self.numMotors = self.numLinks - 1
        # self.numSensors = random.randint(0, 1)
        self.sensors = list(range(self.numLinks))
        for i in range(len(self.sensors)):
            self.sensors[i] = random.randint(0, 1)
        self.links_with_sensors = list(range(20))
        self.joints = list(range(self.numLinks))
        self.weights = (np.random.rand(
            len(self.sensors), self.numMotors)*2) - 1

    def Evaluate(self, directOrGUI):
        self.Create_Body()
        self.Create_Brain()
        self.Create_World()
        os.system("start /B python simulate.py " +
                  directOrGUI + " " + str(self.myID))
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
        for i in range(self.numLinks-1):

            linkName = "Link" + str(i)
            print(linkName)

        if (i < self.numLinks-2):
            if (i == 0):
                if self.sensors[i] == 0:
                    pyrosim.Send_Cube(name=linkName, pos=[
                        0, 0, 0.5], size=self.Create_Random_Size(), colorString='    <color rgba="0.0 0.0 1.0 1.0"/>', colorName='Blue')

                pyrosim.Send_Joint(name="Link" + str(i) + "_" + "Link" + str(i+1), parent=linkName,
                                   child="Link" + str(i+1), type="revolute", position=[0.5, 0, 0.5])
                self.joints[i] = "Link" + \
                    str(i) + "_" + "Link" + str(i+1)

                if self.sensors[i] == 1:
                    pyrosim.Send_Cube(name=linkName, pos=[
                        0, 0, 0.5], size=self.Create_Random_Size(), colorString='    <color rgba="0.0 1.0 0.0 1.0"/>', colorName='Green')
                    self.links_with_sensors[i] = linkName

            else:

                if self.sensors[i] == 0:
                    pyrosim.Send_Cube(name=linkName, pos=[
                        0.5, 0, 0], size=self.Create_Random_Size(), colorString='    <color rgba="0.0 0.0 1.0 1.0"/>', colorName='Blue')

                currJointName = "Link" + str(i) + "_" + "Link" + str(i+1)
                self.joints[i] = currJointName
                pyrosim.Send_Joint(name=currJointName, parent=linkName,
                                   child="Link" + str(i+1), type="revolute", position=[1, 0, 0])

                if self.sensors[i] == 1:
                    pyrosim.Send_Cube(name=linkName, pos=[
                        0.5, 0, 0], size=self.Create_Random_Size(), colorString='    <color rgba="0.0 1.0 0.0 1.0"/>', colorName='Green')
                    self.links_with_sensors[i] = linkName

            print(self.joints)
            # print(currJointName)

            # print(self.joints)
        self.joints = self.joints[:-1]
        self.joints = self.joints[:-1]
        # print(self.joints)

        # pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[
        #     1, 1, 1])

        # pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso",
        #                    child="BackLeg", type="revolute", position=[0.5, 0, 1])

        # pyrosim.Send_Cube(
        #     name="BackLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

        # pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso",
        #                    child="FrontLeg", type="revolute", position=[-0.5, 0, 1])

        # pyrosim.Send_Cube(
        #     name="FrontLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

        # pyrosim.Send_Cube(name="Link1", pos=[
        #                   0, 0, 0.5], size=self.Create_Random_Size())

        # pyrosim.Send_Joint(name="Link1_Link2", parent="Link1",
        #                    child="Link2", type="revolute", position=[0.5, 0, 0.5])
        # pyrosim.Send_Cube(name="Link2", pos=[
        #                   0.5, 0, 0], size=self.Create_Random_Size())

        # pyrosim.Send_Joint(name="Link2_Link3", parent="Link2",
        #                    child="Link3", type="revolute", position=[1, 0, 0])
        # pyrosim.Send_Cube(name="Link3", pos=[
        #                   0.5, 0, 0], size=self.Create_Random_Size())

        # pyrosim.Send_Joint(name="Link3_Link4", parent="Link3",
        #                    child="Link4", type="revolute", position=[1, 0, 0])
        # pyrosim.Send_Cube(name="Link4",
        #                   pos=[0.5, 0, 0], size=self.Create_Random_Size())

        # pyrosim.Send_Joint(name="Link4_Link5", parent="Link4",
        #                    child="Link5", type="revolute", position=[1, 0, 0])
        # pyrosim.Send_Cube(name="Link5", pos=[
        #                   0.5, 0, 0], size=self.Create_Random_Size())

        pyrosim.End()

    def Create_Brain(self):
        # pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        # pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        # pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        # pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        # pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        # pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        for i in range(len(self.links_with_sensors)):
            if (self.links_with_sensors[i] == "Link" + str(i)):
                pyrosim.Send_Sensor_Neuron(
                    name=i, linkName=str(self.links_with_sensors[i]))
        for i in range(self.numMotors-1):
            pyrosim.Send_Motor_Neuron(
                name=self.numLinks+i, jointName=str(self.joints[i]))

        # pyrosim.Send_Sensor_Neuron(name=0, linkName="Link1")
        # pyrosim.Send_Sensor_Neuron(name=1, linkName="Link2")
        # pyrosim.Send_Sensor_Neuron(name=2, linkName="Link3")
        # pyrosim.Send_Sensor_Neuron(name=3, linkName="Link4")
        # pyrosim.Send_Sensor_Neuron(name=4, linkName="Link5")

        # pyrosim.Send_Motor_Neuron(name=5, jointName="Link1_Link2")
        # pyrosim.Send_Motor_Neuron(name=6, jointName="Link2_Link3")
        # pyrosim.Send_Motor_Neuron(name=7, jointName="Link3_Link4")
        # pyrosim.Send_Motor_Neuron(name=8, jointName="Link4_Link5")
        for currentRow in range(len(self.sensors)):
            for currentColumn in range(self.numMotors):
                pyrosim.Send_Synapse(currentRow, currentColumn +
                                     len(self.sensors), 1)
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
                  directOrGUI + " " + str(self.myID))

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

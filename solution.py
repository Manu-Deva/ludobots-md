import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c
from links import LINK


class SOLUTION:
    def __init__(self, nextAvailableID) -> None:
        self.link = LINK()
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
            c.numSensorNeurons, c.numMotorNeurons)*2) - 1

        self.allLinks = self.link.linkDictionary
        self.generatedLinks = {self.link.rootLink}

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
        pyrosim.Send_Cube(name="Box", pos=[-5.5, 10, 0.5], size=[0, 0, 0.01])
        pyrosim.End()

    def Create_Random_Size(self):
        return [random.random()+0.5, random.random(), random.random()+0.10]

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        torsoSize = [1, 1, 1]

        pyrosim.Send_Cube(name="Link0", pos=[0, 0, 5], size=torsoSize)
        print("THIS IS THE AXIS" + str(5))
        print(len(self.allLinks))
        for i in range(0, len(self.allLinks)):
            print("THIS IS THE AXIS" + str(i))
            for connection in self.allLinks[i]["connections"]:
                jointName = "Link"+str(connection)+"_"+"Link"+str(i)
                parentName = "Link"+str(connection)
                childName = "Link"+str(i)
                randomAxis = random.randint(0, 2)
                direction = random.randint(0, 1)
                print("THIS IS THE AXIS" + str(randomAxis))
                if randomAxis == 0:
                    randomJointAxis = "0 1 0"
                    if direction == 0:
                        pyrosim.Send_Joint(name=jointName, parent=parentName,
                                           child=childName, type="revolute", position=[self.allLinks[connection]["size"][randomAxis]/2,
                                                                                       self.allLinks[connection]["size"][1],
                                                                                       self.allLinks[connection]["size"][2]],
                                           jointAxis=randomJointAxis)
                        if (childName not in self.generatedLinks):
                            pyrosim.Send_Cube(name=childName, pos=[
                                self.allLinks[i]["size"][randomAxis]/2, 0, 0], size=self.allLinks[i]["size"],
                                colorString=self.allLinks[i]["cString"], colorName=self.allLinks[i]["cName"])
                            self.generatedLinks.add(childName)
                    if direction == 1:
                        pyrosim.Send_Joint(name=jointName, parent=parentName,
                                           child=childName, type="revolute", position=[-self.allLinks[connection]["size"][randomAxis]/2,
                                                                                       self.allLinks[connection]["size"][1],
                                                                                       self.allLinks[connection]["size"][2]],
                                           jointAxis=randomJointAxis)
                        if (childName not in self.generatedLinks):
                            pyrosim.Send_Cube(name=childName, pos=[
                                -self.allLinks[i]["size"][randomAxis]/2, 0, 0], size=self.allLinks[i]["size"],
                                colorString=self.allLinks[i]["cString"], colorName=self.allLinks[i]["cName"])
                            self.generatedLinks.add(childName)

                if randomAxis == 1:
                    randomJointAxis = "1 0 0"
                    if direction == 0:
                        pyrosim.Send_Joint(name=jointName, parent=parentName,
                                           child=childName, type="revolute", position=[self.allLinks[connection]["size"][0],
                                                                                       self.allLinks[connection]["size"][randomAxis]/2,
                                                                                       self.allLinks[connection]["size"][2]],
                                           jointAxis=randomJointAxis)
                        if (childName not in self.generatedLinks):
                            pyrosim.Send_Cube(name=childName, pos=[
                                0, self.allLinks[i]["size"][randomAxis]/2, 0], size=self.allLinks[i]["size"],
                                colorString=self.allLinks[i]["cString"], colorName=self.allLinks[i]["cName"])
                            self.generatedLinks.add(childName)
                    if direction == 1:
                        pyrosim.Send_Joint(name=jointName, parent=parentName,
                                           child=childName, type="revolute", position=[self.allLinks[connection]["size"][0],
                                                                                       -self.allLinks[connection]["size"][randomAxis]/2,
                                                                                       self.allLinks[connection]["size"][2]],
                                           jointAxis=randomJointAxis)
                        if (childName not in self.generatedLinks):
                            pyrosim.Send_Cube(name=childName, pos=[
                                0, -self.allLinks[i]["size"][randomAxis]/2, 0], size=self.allLinks[i]["size"],
                                colorString=self.allLinks[i]["cString"], colorName=self.allLinks[i]["cName"])
                            self.generatedLinks.add(childName)
                if randomAxis == 2:
                    randomJointAxis = "0 0 1"
                    if direction == 0:
                        pyrosim.Send_Joint(name=jointName, parent=parentName,
                                           child=childName, type="revolute", position=[self.allLinks[connection]["size"][0],
                                                                                       self.allLinks[connection]["size"][1],
                                                                                       self.allLinks[connection]["size"][randomAxis]/2],
                                           jointAxis=randomJointAxis)
                        if (childName not in self.generatedLinks):
                            pyrosim.Send_Cube(name=childName, pos=[
                                0, 0, self.allLinks[i]["size"][randomAxis]/2], size=self.allLinks[i]["size"],
                                colorString=self.allLinks[i]["cString"], colorName=self.allLinks[i]["cName"])
                            self.generatedLinks.add(childName)
                    if direction == 1:
                        pyrosim.Send_Joint(name=jointName, parent=parentName,
                                           child=childName, type="revolute", position=[self.allLinks[connection]["size"][0],
                                                                                       self.allLinks[connection]["size"][1],
                                                                                       -self.allLinks[connection]["size"][randomAxis]/2],
                                           jointAxis=randomJointAxis)
                        if (childName not in self.generatedLinks):
                            pyrosim.Send_Cube(name=childName, pos=[
                                0, 0, -self.allLinks[i]["size"][randomAxis]/2], size=self.allLinks[i]["size"],
                                colorString=self.allLinks[i]["cString"], colorName=self.allLinks[i]["cName"])
                            self.generatedLinks.add(childName)

        # "___________________________________________________________________________________________________-"

        # pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso",
        #                    child="BackLeg", type="revolute", position=[0, -torsoSize[1]/2, 1], jointAxis="1 0 0")
        # pyrosim.Send_Cube(name="BackLeg", pos=[
        #                   0, -backLegSize[1]/2, 0], size=backLegSize)

        # pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso",
        #                    child="FrontLeg", type="revolute", position=[0, torsoSize[1]/2, 1], jointAxis="1 0 0")
        # pyrosim.Send_Cube(name="FrontLeg", pos=[
        #                   0, frontLegSize[1]/2, 0], size=frontLegSize)

        # "___________________________________________________________________________________________________-"

        # pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso",
        #                    child="LeftLeg", type="revolute", position=[-torsoSize[0]/2, 0, 1], jointAxis="0 1 0")
        # pyrosim.Send_Cube(
        #     name="LeftLeg", pos=[-leftLegSize[0]/2, 0, 0], size=leftLegSize)

        # pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso",
        #                    child="RightLeg", type="revolute", position=[torsoSize[0]/2, 0, 1], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="RightLeg", pos=[
        #                   rightLegSize[0]/2, 0, 0], size=rightLegSize)

        # "___________________________________________________________________________________________________-"

        # pyrosim.Send_Joint(name="Torso_TopLeg", parent="Torso",
        #                    child="TopLeg", type="revolute", position=[0, 0, 1.5], jointAxis="0 0 1")
        # pyrosim.Send_Cube(name="TopLeg", pos=[
        #                   0, 0, topLegSize[2]/2], size=topLegSize)

        # pyrosim.Send_Joint(name="Torso_BottomLeg", parent="Torso",
        #                    child="BottomLeg", type="revolute", position=[0, 0, 0.5], jointAxis="0 0 1")
        # pyrosim.Send_Cube(name="BottomLeg", pos=[
        #                   0, 0, -bottomLegSize[2]/2], size=bottomLegSize)

        # "___________________________________________________________________________________________________-"

        # pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg",
        #                    child="FrontLowerLeg", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")
        # pyrosim.Send_Cube(name="FrontLowerLeg", pos=[
        #                   0, 0, -0.5], size=[0.2, 0.2, 1])

        # pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg",
        #                    child="BackLowerLeg", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")
        # pyrosim.Send_Cube(name="BackLowerLeg", pos=[
        #                   0, 0, -0.5], size=[0.2, 0.2, 1])

        # pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg",
        #                    child="LeftLowerLeg", type="revolute", position=[-1, 0, 0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="LeftLowerLeg", pos=[
        #                   0, 0, -0.5], size=[0.2, 0.2, 1])

        # pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg",
        #                    child="RightLowerLeg", type="revolute", position=[1, 0, 0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="RightLowerLeg", pos=[
        #                   0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        # pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        # pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        # pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        # pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        # pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
        # pyrosim.Send_Sensor_Neuron(name=5, linkName="LowerBackLeg")
        # pyrosim.Send_Sensor_Neuron(name=6, linkName="LowerFrontLeg")
        # pyrosim.Send_Sensor_Neuron(name=7, linkName="LowerLeftLeg")
        # pyrosim.Send_Sensor_Neuron(name=8, linkName="LowerRightLeg")

        # pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        # pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
        # pyrosim.Send_Motor_Neuron(name=5, jointName="Torso_LeftLeg")
        # pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_RightLeg")
        # pyrosim.Send_Motor_Neuron(name=7, jointName="FrontLeg_FrontLowerLeg")
        # pyrosim.Send_Motor_Neuron(name=8, jointName="BackLeg_BackLowerLeg")
        # pyrosim.Send_Motor_Neuron(name=9, jointName="LeftLeg_LeftLowerLeg")
        # pyrosim.Send_Motor_Neuron(name=10, jointName="RightLeg_RightLowerLeg")

        # for currentRow in range(c.numSensorNeurons):
        #     for currentColumn in range(c.numMotorNeurons):
        #         pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn +
        #                              c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])
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
                  "GUI" + " " + str(self.myID))

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

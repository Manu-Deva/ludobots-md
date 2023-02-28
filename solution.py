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
        self.listJointNames = []

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
        while True:
            try:
                f = open("fitness" + str(self.myID) + ".txt", "r")
                break
            except:
                pass
        self.fitness = float(f.read())
        f.close()
        os.system("del fitness" + str(self.myID) + ".txt")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-5.5, 10, 0.5], size=[0, 0, 0.01])
        pyrosim.End()

    # def Evaluate(self, directOrGUI):
    #     self.Create_Body()
    #     self.Create_Brain()
    #     self.Create_World()
    #     os.system("start /B python simulate.py " +
    #               "GUI" + " " + str(self.myID))
    #     fitnessFileName = "fitness" + str(self.myID) + ".txt"
    #     while not os.path.exists(fitnessFileName):
    #         time.sleep(0.01)
    #     f = open("fitness" + str(self.myID) + ".txt", "r")
    #     self.fitness = float(f.read())
    #     f.close()

    def Create_Random_Size(self):
        return [random.random()+0.5, random.random(), random.random()+0.10]

    def Create_Body(self):
        pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
        torsoSize = [1, 1, 1]

        pyrosim.Send_Cube(name="Link0", pos=[0, 0, 1.5], size=torsoSize)
        for i in range(0, len(self.allLinks)):
            for connection in self.allLinks[i]["connections"]:
                jointName = "Link"+str(connection)+"_"+"Link"+str(i)
                self.listJointNames.append(jointName)
                parentName = "Link"+str(connection)
                childName = "Link"+str(i)
                randomAxis = random.randint(0, 2)
                direction = random.randint(0, 1)
                if randomAxis == 0:
                    randomJointAxis = "0 1 0"
                    if direction == 0:
                        if parentName == "Link0":
                            pyrosim.Send_Joint(name=jointName, parent=parentName,
                                               child=childName, type="revolute", position=[0.5,
                                                                                           0,
                                                                                           1],
                                               jointAxis=randomJointAxis)
                        else:
                            pyrosim.Send_Joint(name=jointName, parent=parentName,
                                               child=childName, type="revolute", position=[self.allLinks[connection]["size"][randomAxis],
                                                                                           0,
                                                                                           0],
                                               jointAxis=randomJointAxis)
                        if (childName not in self.generatedLinks):
                            pyrosim.Send_Cube(name=childName, pos=[
                                self.allLinks[i]["size"][randomAxis]/2, 0, 0], size=self.allLinks[i]["size"],
                                colorString=self.allLinks[i]["cString"], colorName=self.allLinks[i]["cName"])
                            self.generatedLinks.add(childName)
                    if direction == 1:
                        if parentName == "Link0":
                            pyrosim.Send_Joint(name=jointName, parent=parentName,
                                               child=childName, type="revolute", position=[-0.5,
                                                                                           0,
                                                                                           1],
                                               jointAxis=randomJointAxis)
                        else:
                            pyrosim.Send_Joint(name=jointName, parent=parentName,
                                               child=childName, type="revolute", position=[-self.allLinks[connection]["size"][randomAxis],
                                                                                           0,
                                                                                           0],
                                               jointAxis=randomJointAxis)
                        if (childName not in self.generatedLinks):
                            pyrosim.Send_Cube(name=childName, pos=[
                                -self.allLinks[i]["size"][randomAxis]/2, 0, 0], size=self.allLinks[i]["size"],
                                colorString=self.allLinks[i]["cString"], colorName=self.allLinks[i]["cName"])
                            self.generatedLinks.add(childName)

                if randomAxis == 1:
                    randomJointAxis = "1 0 0"
                    if direction == 0:
                        if parentName == "Link0":
                            pyrosim.Send_Joint(name=jointName, parent=parentName,
                                               child=childName, type="revolute", position=[0,
                                                                                           0.5,
                                                                                           1],
                                               jointAxis=randomJointAxis)
                        else:
                            pyrosim.Send_Joint(name=jointName, parent=parentName,
                                               child=childName, type="revolute", position=[0,
                                                                                           self.allLinks[connection]["size"][randomAxis],
                                                                                           0],
                                               jointAxis=randomJointAxis)
                        if (childName not in self.generatedLinks):
                            pyrosim.Send_Cube(name=childName, pos=[
                                0, self.allLinks[i]["size"][randomAxis]/2, 0], size=self.allLinks[i]["size"],
                                colorString=self.allLinks[i]["cString"], colorName=self.allLinks[i]["cName"])
                            self.generatedLinks.add(childName)
                    if direction == 1:
                        if parentName == "Link0":
                            pyrosim.Send_Joint(name=jointName, parent=parentName,
                                               child=childName, type="revolute", position=[0,
                                                                                           -0.5,
                                                                                           1],
                                               jointAxis=randomJointAxis)
                        else:
                            pyrosim.Send_Joint(name=jointName, parent=parentName,
                                               child=childName, type="revolute", position=[0,
                                                                                           -self.allLinks[connection]["size"][randomAxis]/2,
                                                                                           0],
                                               jointAxis=randomJointAxis)

                        if (childName not in self.generatedLinks):
                            pyrosim.Send_Cube(name=childName, pos=[
                                0, -self.allLinks[i]["size"][randomAxis]/2, 0], size=self.allLinks[i]["size"],
                                colorString=self.allLinks[i]["cString"], colorName=self.allLinks[i]["cName"])
                            self.generatedLinks.add(childName)
                if randomAxis == 2:
                    randomJointAxis = "0 0 1"
                    if direction == 0:
                        if parentName == "Link0":
                            pyrosim.Send_Joint(name=jointName, parent=parentName,
                                               child=childName, type="revolute", position=[0,
                                                                                           0,
                                                                                           1.5],
                                               jointAxis=randomJointAxis)
                        else:
                            pyrosim.Send_Joint(name=jointName, parent=parentName,
                                               child=childName, type="revolute", position=[0,
                                                                                           0,
                                                                                           self.allLinks[connection]["size"][randomAxis]/2],
                                               jointAxis=randomJointAxis)
                        if (childName not in self.generatedLinks):
                            pyrosim.Send_Cube(name=childName, pos=[
                                0, 0, self.allLinks[i]["size"][randomAxis]/2], size=self.allLinks[i]["size"],
                                colorString=self.allLinks[i]["cString"], colorName=self.allLinks[i]["cName"])
                            self.generatedLinks.add(childName)
                    if direction == 1:
                        if parentName == "Link0":
                            pyrosim.Send_Joint(name=jointName, parent=parentName,
                                               child=childName, type="revolute", position=[0,
                                                                                           0,
                                                                                           0.5],
                                               jointAxis=randomJointAxis)
                        else:
                            pyrosim.Send_Joint(name=jointName, parent=parentName,
                                               child=childName, type="revolute", position=[0,
                                                                                           0,
                                                                                           -self.allLinks[connection]["size"][randomAxis]/2],
                                               jointAxis=randomJointAxis)
                        if (childName not in self.generatedLinks):
                            pyrosim.Send_Cube(name=childName, pos=[
                                0, 0, -self.allLinks[i]["size"][randomAxis]/2], size=self.allLinks[i]["size"],
                                colorString=self.allLinks[i]["cString"], colorName=self.allLinks[i]["cName"])
                            self.generatedLinks.add(childName)

        self.generatedLinks = {self.link.rootLink}

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        numSensorNeurons = 0
        numMotorNeurons = len(self.listJointNames)
        j = 0
        listSensorNeurons = []
        listMotorNeurons = []
        for i in range(0, len(self.allLinks)):
            if (self.allLinks[i]["cName"] == "Green"):
                pyrosim.Send_Sensor_Neuron(name=i, linkName="Link"+str(i))
                print(str(i) + "-" + "sensor")
                listSensorNeurons.append(i)
                numSensorNeurons += 1

        for ijointName in self.listJointNames:
            pyrosim.Send_Motor_Neuron(
                name=j+numSensorNeurons, jointName=ijointName)
            listMotorNeurons.append(j+numSensorNeurons)
            print(str(j+numSensorNeurons) + "-" + "motor")
            j += 1

        weights = (np.random.rand(
            numSensorNeurons, numMotorNeurons)*4) - 0.5

        for currentRow in listSensorNeurons:
            for currentColumn in listMotorNeurons:
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn,
                                     weight=weights[listSensorNeurons.index(currentRow)][listMotorNeurons.index(currentColumn)])

        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0, len(self.weights) - 1)
        randomColumn = random.randint(0, len(self.weights[0]) - 1)
        self.weights[randomRow, randomColumn] = (random.random() * 2) - 1

    def Set_ID(self, ID):
        self.myID = ID

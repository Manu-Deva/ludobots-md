import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os


class SOLUTION:
    def __init__(self) -> None:
        self.weights = (np.random.rand(3, 2)*2) - 1

    def Evaluate(self, directOrGUI):
        self.Create_World()
        os.system("python simulate.py " + directOrGUI)
        f = open("fitness.txt", "r")
        self.fitness = float(f.read())
        f.close()

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-5.5, 10, 0.5], size=[1, 1, 1])
        pyrosim.End()
        self.Create_Body()
        self.Create_Brain()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[
            1, 1, 1])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso",
                           child="BackLeg", type="revolute", position=[0.5, 0, 1])

        pyrosim.Send_Cube(
            name="BackLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso",
                           child="FrontLeg", type="revolute", position=[-0.5, 0, 1])

        pyrosim.Send_Cube(
            name="FrontLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(
                    sourceNeuronName=currentRow, targetNeuronName=currentColumn + 3, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0, len(self.weights) - 1)
        randomColumn = random.randint(0, len(self.weights[0]) - 1)
        self.weights[randomRow, randomColumn] = (random.random() * 2) - 1

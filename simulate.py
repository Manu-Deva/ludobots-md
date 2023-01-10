#!/usr/bin/python3.11
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

for x in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link(
        "FrontLeg")

    pyrosim.Set_Motor_For_Joint(
        bodyIndex="robot",
        jointName="Torso_BackLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=0.0,
        maxForce=500)

np.save('data/backLegSensorValues', backLegSensorValues)
np.save('data/frontLegSensorValues', frontLegSensorValues)
p.disconnect()

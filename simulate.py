#!/usr/bin/python3.11
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import math
import random

amplitude = np.pi/4
frequency = 1
phaseOffset = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)
targetValues = np.linspace(0, 2*np.pi, 1000)
targetValueSines = np.sin(targetValues)


for x in range(1000):
    time.sleep(1/60)
    p.stepSimulation()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link(
        "FrontLeg")

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName='Torso_BackLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetValueSines[x],
        maxForce=50
    )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName='Torso_FrontLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetValueSines[x],
        maxForce=50
    )

np.save('data/backLegSensorValues', backLegSensorValues)
np.save('data/frontLegSensorValues', frontLegSensorValues)
# np.save('data/targetValues', targetValues)
# np.save('data/targetValueSines', targetValueSines)

p.disconnect()
print(backLegSensorValues)

#!/usr/bin/python3.11
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import math

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
    time.sleep(1/90)
    p.stepSimulation()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link(
        "FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName='Torso_BackLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=math.pi/2,
        maxForce=500
    )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName='Torso_FrontLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=-math.pi/2,
        maxForce=500
    )


p.disconnect()
print(backLegSensorValues)

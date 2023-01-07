import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("boxes.sdf")

for x in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(x)
p.disconnect()

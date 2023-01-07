import pybullet as p
import time

physicsClient = p.connect(p.GUI)
p.loadSDF("box.sdf")
for x in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(x)
p.disconnect()

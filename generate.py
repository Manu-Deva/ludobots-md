import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0.5
z = 0
pyrosim.Send_Cube(name="Box", pos=[z, x, y], size=[length, width, height])
pyrosim.End()

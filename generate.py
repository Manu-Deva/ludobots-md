import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0.5
z = 0
n = 0
while n < 10:
    for p in range(5):
        pyrosim.Send_Cube(
            name="Box", pos=[z, x+p, y+n], size=[(0.9**n)*length, (0.9**n)*width, (0.9**n)*height])
    n += 1
pyrosim.End()

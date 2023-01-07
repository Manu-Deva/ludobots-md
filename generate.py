import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1
x = 0
y = 0.5
z = 0
n = 0


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(
        name="Box", pos=[z, x, y], size=[length, width, height])
    pyrosim.End()


def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Robot", pos=[z, x, y], size=[
                      length, width, height])
    pyrosim.End()


Create_World()
Create_Robot()

import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1
x = 0
y = 0.5
z = 0
n = 0

# [z,x,y]


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(
        name="Box", pos=[-10, -5, 1], size=[length, width, height])
    pyrosim.End()


def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    # pyrosim.Send_Cube(name="BackLeg", pos=[0, 0.5, 0.5], size=[
    #                   length, width, height])

    # pyrosim.Send_Joint(name="BackLeg_Torso", parent="BackLeg",
    #                    child="Torso", type="revolute", position=[0, 1, 1])

    # pyrosim.Send_Cube(
    #     name="Torso", pos=[0, 0.5, 0.5], size=[length, width, height])

    # pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso",
    #                    child="FrontLeg", type="revolute", position=[0, 1.0, 0])

    # pyrosim.Send_Cube(
    #     name="FrontLeg", pos=[0, 0.5, -0.5], size=[length, width, height])

    # pyrosim.End()
    pyrosim.Send_Cube(name="Torso", pos=[0, 1.5, 1.5], size=[
        length, width, height])

    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso",
                       child="BackLeg", type="revolute", position=[0, 1, 1])

    pyrosim.Send_Cube(
        name="BackLeg", pos=[0, -0.5, -0.5], size=[length, width, height])

    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso",
                       child="FrontLeg", type="revolute", position=[0, 1.0, 0])

    pyrosim.Send_Cube(
        name="FrontLeg", pos=[0, 0.5, -0.5], size=[length, width, height])

    pyrosim.End()


Create_World()
Create_Robot()


# green line x
# red line z

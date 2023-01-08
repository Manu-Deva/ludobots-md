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
    pyrosim.Send_Cube(name="BackLeg", pos=[0, 0.5, 0.5], size=[
                      length, width, height])

    pyrosim.Send_Joint(name="BackLeg_Torso", parent="BackLeg",
                       child="Torso", type="revolute", position=[0, 1, 1])

    pyrosim.Send_Cube(
        name="Torso", pos=[0, 0.5, 0.5], size=[length, width, height])

    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso",
                       child="FrontLeg", type="revolute", position=[0, 1.0, 0])

    pyrosim.Send_Cube(
        name="FrontLeg", pos=[0, 0.5, -0.5], size=[length, width, height])

    # pyrosim.Send_Joint(name="Link2_Link3", parent="Link2",
    #                    child="Link3", type="revolute", position=[0, 0.5, 0.5])

    # pyrosim.Send_Cube(
    #     name="Link3", pos=[0, 0.5, 0], size=[length, width, height])

    # pyrosim.Send_Joint(name="Link3_Link4", parent="Link3",
    #                    child="Link4", type="revolute", position=[0, 1, 0])

    # pyrosim.Send_Cube(
    #     name="Link4", pos=[0, 0.5, 0], size=[length, width, height])

    # pyrosim.Send_Joint(name="Link4_Link5", parent="Link4",
    #                    child="Link5", type="revolute", position=[0, 0.5, -0.5])

    # pyrosim.Send_Cube(
    #     name="Link5", pos=[0, 0, -0.5], size=[length, width, height])

    # pyrosim.Send_Joint(name="Link5_Link6", parent="Link5",
    #                    child="Link6", type="revolute", position=[0, 0, -1])

    # pyrosim.Send_Cube(
    #     name="Link6", pos=[0, 0, -0.5], size=[length, width, height])

    pyrosim.End()


Create_World()
Create_Robot()


# green line x
# red line z

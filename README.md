# Assignment 7 - 3D Creature Morphology CS396 Northwestern University

The pyrosim graphical interface, pybullet physics engine, and other python libraries were used in the codebase of this assignment. Special thanks to Campuswire for helping to debug.

In this assignment, a "creature" with 3D morphology is randomly generated in space, having 8-15 links in its body.
The body's individual links are randomly connected to each other through dictionaries in a function inside a separate LINK class, also recording the names of joints that connect them. Each link will have a randomly generated size as well.
This information is passed into the create_body function of SOLUTION, where a link's information is used to generate the entire body.

A morphospace of this creature includes the ability to grow in the +x/y/z and -x/y/z directions, building out from previous links. Each link is additionally selected with a 50% chance to be a motor or sensor, with corresponding color coordination.

There are multiple conditionals inside create_body that keep track of the previous direction that the creature was growing in, the current direction, and how to minimize overlapping between links.

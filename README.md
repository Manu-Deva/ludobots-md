# Assignment 7 - 3D Creature Morphology CS396 Northwestern University

Youtube Link - https://youtu.be/LmMJHOGKrx8

The pyrosim graphical interface, pybullet physics engine, and other python libraries were used in the codebase of this assignment. Special thanks to Campuswire for helping to debug.
Ludobots MOOC -  https://www.reddit.com/r/ludobots/
Pyrosim - https://github.com/jbongard/pyrosim.git

In this assignment, a "creature" with 3D morphology is generated with random size and connections in space, having 8-15 links in its body.
The body's individual links are randomly connected to each other through dictionaries in a function inside a separate LINK class.
This information is passed into the create_body function of SOLUTION, where a link's information is used to generate the entire body.

![IMG-0188](https://user-images.githubusercontent.com/94333898/220515842-16d943c7-13db-4a22-b4e9-9fc8f63a8485.jpg)


A morphospace of this creature includes the ability to grow in the +x/y/z and -x/y/z directions, building out from previous links by using a number 1-6 to track what direction it is growing in. This information determines where the joint will be created, using the size of a link to orient itself correctly. 

Each link is additionally selected with a 50% chance to be a motor or sensor, with corresponding color coordination.

There are multiple conditionals inside create_body that keep track of the previous direction that the creature was growing in, the current direction, and how to minimize overlapping between links.

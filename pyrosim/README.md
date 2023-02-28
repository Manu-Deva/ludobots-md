# Assignment 8 - Parallel Hill Climbing of 3D Creatures - CS396 Northwestern University

Youtube Link - https://youtu.be/LmMJHOGKrx8

The pyrosim graphical interface, pybullet physics engine, and other python libraries were used in the codebase of this assignment. Special thanks to Campuswire for helping to debug.
Ludobots MOOC -  https://www.reddit.com/r/ludobots/
Pyrosim - https://github.com/jbongard/pyrosim.git

To run this code, click "Run" in the top right corner and import the code to your computer

In this assignment, a "creature" with 3D morphology is generated with random size and connections in space, having 4-8 links in its body.
The body's individual links are randomly connected to each other through dictionaries in a function inside a separate LINK class.
This information is passed into the create_body function of SOLUTION, where a link's information is used to generate the entire body.
At initialization of each link in the LINK class, attributes including connections, size, color, joint axis, +/- direction of growth, and mass are recorded.

![Note Feb 21, 2023](https://user-images.githubusercontent.com/94333898/221752835-73d60c49-c3dc-4686-873c-5076998109a7.jpg)

A morphospace of this creature includes the ability to grow in the +x/y/z and -x/y/z directions, building out from previous links by using a random jointAxis and direction to track what direction it is growing in.

Each link is additionally selected with a 50% chance to be a motor or sensor, with corresponding color coordination.

During evolution, many attributes are mutated to optimize the ability of the creature to move in the x direction. These include regnerating the brain's synapses and altering the weights of each synapse in the matrix, giving a 30% chance of a neuron becoming a sensor neurons, a 50% chance of a link's size growing, a 50% chance of a link's mass increasing, and more.

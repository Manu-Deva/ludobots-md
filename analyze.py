import numpy as np
import matplotlib.pyplot as plt
import constants as c

# backLegSensorValues = np.load('data/backLegSensorValues.npy')
# backTargetAngles = np.load('data/backTargetAngles.npy')
# frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
# frontTargetAngles = np.load('data/frontTargetAngles.npy')

# plt.figure(0)
# plt.plot(backLegSensorValues, label="Back Leg Data", linewidth=5)
# plt.plot(frontLegSensorValues, label="Front Leg Data")

# plt.figure(1)
# plt.plot(backTargetAngles, label="Back Leg Target Angles", linewidth=4)
# plt.plot(frontTargetAngles, label="Front Leg Target Angles")

# plt.legend()
# plt.show()

array1 = np.load("file1.npy")
array2 = np.load("file2.npy")
array3 = np.load("file3.npy")
array4 = np.load("file4.npy")
array5 = np.load("file5.npy")

xArr = list(range(0, c.numberOfGenerations))
plt.plot(xArr, array1, color="red", label="Seed 1")
plt.plot(xArr, array2, color="blue", label="Seed 2")
plt.plot(xArr, array3, color="green", label="Seed 3")
plt.plot(xArr, array4, color="brown", label="Seed 4")
plt.plot(xArr, array5, color="purple", label="Seed 5")
plt.legend()
plt.show()

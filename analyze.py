import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load('data/backLegSensorValues.npy')
backTargetAngles = np.load('data/backTargetAngles.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
frontTargetAngles = np.load('data/frontTargetAngles.npy')

plt.figure(0)
plt.plot(backLegSensorValues, label="Back Leg Data", linewidth=5)
plt.plot(frontLegSensorValues, label="Front Leg Data")

plt.figure(1)
plt.plot(backTargetAngles, label="Back Leg Target Angles", linewidth=4)
plt.plot(frontTargetAngles, label="Front Leg Target Angles")

plt.legend()
plt.show()

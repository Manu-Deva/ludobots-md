import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
targetValues = np.load('data/targetValues.npy')
targetValueSines = np.load('data/targetValueSines.npy')

plt.figure(0)
plt.plot(backLegSensorValues, label="Back Leg Data", linewidth=5)
plt.plot(frontLegSensorValues, label="Front Leg Data")

plt.figure(1)
plt.plot(np.pi/4*(targetValueSines), label="Target Value Sines")

plt.legend()
plt.show()

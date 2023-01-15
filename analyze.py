import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')

plt.plot(backLegSensorValues, label="Back Leg Data", linewidth=5)
plt.plot(frontLegSensorValues, label="Front Leg Data")

plt.legend()
plt.show()

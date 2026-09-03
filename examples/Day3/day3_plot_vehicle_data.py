import numpy as np
import matplotlib.pyplot as plt

time = np.array([
    0.0,
    0.1,
    0.2,
    0.3,
    0.4,
    0.5
])

yaw_rate = np.array([
    0.05,
    0.08,
    0.12,
    0.20,
    0.15,
    0.10
])

plt.plot(time, yaw_rate)

plt.xlabel("Time (s)")
plt.ylabel("Yaw Rate (rad/s)")
plt.title("Vehicle Yaw Rate")

plt.grid(True)

plt.show()
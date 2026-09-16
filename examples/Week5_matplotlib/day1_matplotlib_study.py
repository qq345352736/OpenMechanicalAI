import matplotlib.pyplot as plt
import numpy as np

# Create some data
x=np.linspace(0,10,100)
y=np.sin(x)

# Create a figure and axis
plt.plot(x,y)
plt.show()
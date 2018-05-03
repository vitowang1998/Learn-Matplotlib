import matplotlib.pyplot as plt
import numpy as np

# %matplotlib inline                    if using jupyter notebook

# The more data x, y have, the more precise the graph will be.
x = np.linspace(0, 10, 100)
y = x ** 3



# Object-Oriented Method

# Create a figure object
fig = plt.figure()

# Add a new set of axes
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.set_xlabel('Time')
axes.set_ylabel('Distance')
axes.set_title('Time-Distance Graph')
axes.plot(x, y)
plt.show()

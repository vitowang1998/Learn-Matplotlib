import matplotlib.pyplot as plt
import numpy as np

# %matplotlib inline                    if using jupyter notebook

# The more pairs in x, y, the more precise the graph will be.
x = np.linspace(0, 10, 100)
y = x ** 3

# There are two ways of ploting a graph, one is to use function plt.plot(a, b)
plt.plot(x, y)
plt.xlabel('Time')
plt.ylabel('Distance')
plt.title('Time-Distance Graph')
plt.show()

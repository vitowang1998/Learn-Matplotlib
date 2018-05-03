import matplotlib.pyplot as plt
import numpy as np

# %matplotlib inline                    if using jupyter notebook

# The more data x, y have, the more precise the graph will be.
x = np.linspace(0, 10, 100)
y = x ** 3

fig = plt.figure()

# Since fig.add_axes is a method for "fig" object, it is clear that we can create multiple axes, namely, graphs, in one canvas.
axes1 = fig.add_axes([0.0, 0.0, 0.8, 0.8])
axes2 = fig.add_axes([0.12, 0.35, 0.38, 0.3])

axes1.set_xlabel('Time')
axes1.set_ylabel('Distance')
axes1.set_title('Time-Distance Graph')

axes2.set_xlabel('Time')
axes2.set_ylabel('Distance')
axes2.set_title('Time-Distance Graph')

axes1.plot(x, y)
axes2.plot(y, x)

plt.show()
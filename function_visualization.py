import matplotlib.pyplot as plt
import numpy as np


# The function
def f(x):
    return x**2

#limits
a = 0
b = 2

# Creating a range of values for x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Creating the plot
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

# Filling the area under the curve
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Set up the plot
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Adding integration limits and the titles
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


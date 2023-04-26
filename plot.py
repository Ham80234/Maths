import matplotlib.pyplot as plt
import numpy as np

n = 10000
r = np.linspace(0, 10, n)
x = 1e-5 * np.ones(n)
iterations = 1000
last = 100

for i in range(iterations):
    x = r * x * (1 - x/2) - (0.5*x)
    if i >= (iterations - last):
        plt.plot(r, x, ',k', alpha=1)

plt.show()
import matplotlib.pyplot as plt
import numpy as np

iterations = 1000
R=np.linspace(0,10,iterations)
N=0.5

X = []
Y = []

for u in R:
    X.append(u)
    m = np.random.random()
    for n in range(1001):
      m=(u*m)*(1-m/2) - (0.5 * m)
    for l in range(1051):
      m=(u*m)*(1-m/2) - (0.5 * m)
    Y.append(m)
plt.plot(X, Y, ',k', alpha=1 )
plt.show()
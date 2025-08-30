import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-8, 8, 400)
y = np.linspace(-8, 8, 400)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)

Z = np.sinc(R / np.pi)  

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none')
fig.colorbar(surf, shrink=0.5, aspect=10)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

fig.canvas.manager.set_window_title('Sinc Function')

plt.show()

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

num_blades = 500
x = np.random.uniform(0, 10, num_blades)
y = np.random.uniform(0, 10, num_blades)

def ground_height(x, y):
    return 0.2 * np.sin(x) * np.cos(y)

z = ground_height(x, y)

lengths = np.random.uniform(0.3, 1.0, num_blades)
angles_x = np.random.uniform(-0.3, 0.3, num_blades)
angles_y = np.random.uniform(-0.3, 0.3, num_blades)

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

X = np.linspace(0, 10, 50)
Y = np.linspace(0, 10, 50)
X, Y = np.meshgrid(X, Y)
Z = ground_height(X, Y)
ax.plot_surface(X, Y, Z, color='lightgreen', alpha=0.5)

for xi, yi, zi, l, axl, ayl in zip(x, y, z, lengths, angles_x, angles_y):
    x_end = xi + l * np.sin(axl)
    y_end = yi + l * np.sin(ayl)
    z_end = zi + l * np.cos(axl)
    ax.plot([xi, x_end], [yi, y_end], [zi, z_end], color='green')

    fig.canvas.manager.set_window_title("Grass")

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 2)
ax.set_axis_off()
ax.set_title("3B Grass")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5, 5, 300)
y = np.linspace(-5, 5, 300)
X, Y = np.meshgrid(x, y)

Z = np.exp(-0.1*(X**2 + Y**2)) * 10  
Z += np.sin(X*2) + np.cos(Y*2)       

colors = np.zeros((X.shape[0], X.shape[1], 3))

for i in range(X.shape[0]):
    for j in range(X.shape[1]):

        r = min(max(Z[i,j]/12 + np.random.rand()*0.2, 0), 1)
        g = min(max(Z[i,j]/15 + np.random.rand()*0.3, 0), 1)
        b = min(max(1 - Z[i,j]/15 + np.random.rand()*0.2, 0), 1)
        colors[i,j] = [r, g, b]


fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, facecolors=colors, linewidth=0, antialiased=True)

fig.canvas.manager.set_window_title("Mountain")  


ax.set_title("3B Mountain")
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.view_init(elev=60, azim=-60)  

plt.show()

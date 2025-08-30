import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

r = 1 
u = np.linspace(0, 2 * np.pi, 100)  
v = np.linspace(0, np.pi, 100)      

x = r * np.outer(np.cos(u), np.sin(v))
y = r * np.outer(np.sin(u), np.sin(v))
z = r * np.outer(np.ones(np.size(u)), np.cos(v))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='b', edgecolor='k')  


ax.set_box_aspect([1,1,1])

fig.canvas.manager.set_window_title('Ball')

plt.title("3B Ball")

plt.show()

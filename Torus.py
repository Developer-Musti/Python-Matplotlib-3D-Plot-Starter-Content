import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  


R = 3.0   
r = 1.0  

u = np.linspace(0, 2*np.pi, 200)
v = np.linspace(0, 2*np.pi, 60)
U, V = np.meshgrid(u, v)

X = (R + r * np.cos(V)) * np.cos(U)
Y = (R + r * np.cos(V)) * np.sin(U)
Z = r * np.sin(V)

fig = plt.figure(figsize=(9, 7))
fig.canvas.manager.set_window_title("Torus Geometry Node") 
ax = fig.add_subplot(111, projection='3d')


ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=True, alpha=0.9)


a = 1.0
cube_pts = np.array([
    [-a, -a, -a], [ a, -a, -a], [ a,  a, -a], [-a,  a, -a], 
    [-a, -a,  a], [ a, -a,  a], [ a,  a,  a], [-a,  a,  a]  
])

edges = [
    (0,1),(1,2),(2,3),(3,0),  
    (4,5),(5,6),(6,7),(7,4),   
    (0,4),(1,5),(2,6),(3,7)  
]

for i, j in edges:
    xi, yi, zi = cube_pts[i]
    xj, yj, zj = cube_pts[j]
    ax.plot([xi, xj], [yi, yj], [zi, zj], linewidth=1.5)

ax.set_box_aspect([1,1,1])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3B Torus Geometry Node")

ax.view_init(elev=25, azim=35)

plt.show()

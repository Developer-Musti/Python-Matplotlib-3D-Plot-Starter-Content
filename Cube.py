import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

a = 2.0  

cube_pts = np.array([
    [-a, -a, -a], [ a, -a, -a], [ a,  a, -a], [-a,  a, -a], 
    [-a, -a,  a], [ a, -a,  a], [ a,  a,  a], [-a,  a,  a]  
])

faces = [
    [cube_pts[0], cube_pts[1], cube_pts[2], cube_pts[3]],  
    [cube_pts[4], cube_pts[5], cube_pts[6], cube_pts[7]],  
    [cube_pts[0], cube_pts[1], cube_pts[5], cube_pts[4]],  
    [cube_pts[2], cube_pts[3], cube_pts[7], cube_pts[6]],  
    [cube_pts[1], cube_pts[2], cube_pts[6], cube_pts[5]],  
    [cube_pts[4], cube_pts[7], cube_pts[3], cube_pts[0]]   
]

fig = plt.figure(figsize=(7, 7))
fig.canvas.manager.set_window_title("Cube")  
ax = fig.add_subplot(111, projection='3d')

ax.add_collection3d(Poly3DCollection(faces,
                                     facecolors='skyblue',
                                     edgecolors='black',
                                     linewidths=1,
                                     alpha=0.8))

ax.set_box_aspect([1,1,1])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3B Cube")

plt.show()

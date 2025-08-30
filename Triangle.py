import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

vertices = [
    [0, 0, 0],  
    [1, 0, 0],    
    [0.5, 1, 0], 
    [0.5, 0.5, 1] 
]


faces = [
    [vertices[0], vertices[1], vertices[2]],  
    [vertices[0], vertices[1], vertices[3]], 
    [vertices[1], vertices[2], vertices[3]], 
    [vertices[2], vertices[0], vertices[3]]  
]


poly3d = Poly3DCollection(faces, facecolors='cyan', edgecolors='black', alpha=0.8)
ax.add_collection3d(poly3d)


ax.set_xlim([ -0.5, 1.5])
ax.set_ylim([ -0.5, 1.5])
ax.set_zlim([ -0.5, 1.5])


ax.set_title("3B Triangle")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

fig.canvas.manager.set_window_title("Triangle")

plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure(figsize=(8, 12))
fig.canvas.manager.set_window_title("Eiffel Tower")
ax = fig.add_subplot(111, projection="3d")

levels = [0, 3, 6, 9]   
sizes = [6, 4, 2, 1]    
colors = ["saddlebrown", "dimgray", "darkorange", "firebrick"]  

faces = []
for i in range(len(levels) - 1):
    z1, z2 = levels[i], levels[i+1]
    s1, s2 = sizes[i], sizes[i+1]

   
    bottom = np.array([
        [-s1, -s1, z1], [ s1, -s1, z1], [ s1,  s1, z1], [-s1,  s1, z1]
    ])
   
    top = np.array([
        [-s2, -s2, z2], [ s2, -s2, z2], [ s2,  s2, z2], [-s2,  s2, z2]
    ])

   
    for j in range(4):
        faces.append(( [bottom[j], bottom[(j+1)%4], top[(j+1)%4], top[j]], colors[i] ))

   
    faces.append((bottom, colors[i]))
    faces.append((top, colors[i]))


anten_height = 2
top_center = [0, 0, levels[-1]]
top_square = np.array([
    [-sizes[-1], -sizes[-1], levels[-1]], 
    [ sizes[-1], -sizes[-1], levels[-1]], 
    [ sizes[-1],  sizes[-1], levels[-1]], 
    [-sizes[-1],  sizes[-1], levels[-1]]
])
anten_tip = [0, 0, levels[-1] + anten_height]

faces.append(( [top_square[0], top_square[1], anten_tip], "gold" ))
faces.append(( [top_square[1], top_square[2], anten_tip], "gold" ))
faces.append(( [top_square[2], top_square[3], anten_tip], "gold" ))
faces.append(( [top_square[3], top_square[0], anten_tip], "gold" ))


for f, c in faces:
    ax.add_collection3d(Poly3DCollection([f],
                                         facecolors=c,
                                         edgecolors="black",
                                         linewidths=1,
                                         alpha=0.8))

ax.set_box_aspect([1,1,2.5]) 
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Eiffel Tower")

plt.show()

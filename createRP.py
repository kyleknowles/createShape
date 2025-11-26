import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


def add_RP(x,x_depth,y,y_depth,z,z_depth,colors, model):



    rp = np.array([
    [x,y,z], [x+x_depth,y,z], [x+x_depth,y+y_depth,z], [x,y+y_depth,z],
    [x,y,z+z_depth], [x + x_depth,y,z+z_depth], [x + x_depth,y+y_depth,z+z_depth], [x,y+y_depth,z+z_depth]
    ])

    # Cube faces
    faces = [
        [rp[0], rp[1], rp[2], rp[3]],
        [rp[4], rp[5], rp[6], rp[7]],
        [rp[0], rp[1], rp[5], rp[4]],
        [rp[2], rp[3], rp[7], rp[6]],
        [rp[1], rp[2], rp[6], rp[5]],
        [rp[4], rp[7], rp[3], rp[0]]
    ]

    # Different colors for each face

    # Add faces with unique colors
    poly = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='k', alpha=0.8)
    ax.add_collection3d(poly)
    return rp

def add_xz_rect(x, x_depth, y, z, z_depth):
    rect = np.array([
        [x, y, z],
        [x+x_depth, y, z],
        [x+x_depth, y, z+z_depth],
        [x, y, z+z_depth]
    ])
    rct = Poly3DCollection([rect], facecolors='cyan', edgecolor='black')
    ax.add_collection3d(rct)



'''
# Define cube vertices
cube = np.array([
    [0,0,0], [220,0,0], [220,240,0], [0,240,0],
    [0,0,490], [220,0,490], [220,240,490], [0,240,490]
])

# Cube faces
faces = [
    [cube[0], cube[1], cube[2], cube[3]],
    [cube[4], cube[5], cube[6], cube[7]],
    [cube[0], cube[1], cube[5], cube[4]],
    [cube[2], cube[3], cube[7], cube[6]],
    [cube[1], cube[2], cube[6], cube[5]],
    [cube[4], cube[7], cube[3], cube[0]]
]

# Different colors for each face
colors = ['gray', 'gray', 'darkgray', 'darkgray', 'lightgray', 'lightgray']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Add faces with unique colors
poly = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='k', alpha=0.8)
ax.add_collection3d(poly)

x = 22
x_depth = 4
y = 4
y_depth = 4
z = 40
z_depth = 5

'''

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#x, x_depth, y, y_depth, z, z_depth


colors = ['gray', 'gray', 'darkgray', 'darkgray', 'lightgray', 'lightgray']
colors2 = ['green','green','green','green','green','green']
model = []





model = add_RP(210,-90,240,11,375,-60,colors2, model)
model = add_RP(110,-40,240,11,355,-40,colors2, model)
model = add_RP(30,-20,240,11,375,-60,colors2, model)

model = add_RP(210, -60, 240, 11, 305, -35, colors2, model)
model = add_RP(95, -50, 240, 11, 280, -25, colors2, model)
model = add_RP(30, -20, 240, 11, 275, -80,colors2, model)

model = add_RP(95, -50, 240, 11, 220, -25, colors2, model)

model = add_RP(210, -50, 240, 11, 260, -120, colors2, model)

model = add_RP(90, -80, 240, 11, 185, -80, colors2, model)

model = add_RP(0,220,0,240,0,385,colors, model)
scale = model.flatten()
ax.auto_scale_xyz(scale, scale, scale)








# x, x_depth, y, z, z_depth





"""

center = np.array([11, 12])
radius = 10

# Generate circle points
theta = np.linspace(0, 2*np.pi, 100)
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)
z = np.zeros_like(x)     # Face at z = 0

# Stack into Nx3 array
circle_points = np.column_stack([x, y, z])


# Add circle as polygon
# Extrusion parameters
height = -3  # How high you want to extrude along z-axis
z_bottom = 0
z_top = z_bottom + height

# Bottom circle (already created)
bottom_circle = circle_points

# Top circle
top_circle = np.column_stack([x, y, np.full_like(x, z_top)])

# Side faces (connect each point on bottom circle to top circle)
side_faces = []
for i in range(len(bottom_circle)):
    j = (i + 1) % len(bottom_circle)  # wrap around
    quad = [
        bottom_circle[i],
        bottom_circle[j],
        top_circle[j],
        top_circle[i]
    ]
    side_faces.append(quad)

# Create 3D polygon collection for the extruded cylinder
cylinder_faces = side_faces + [bottom_circle, top_circle]

cylinder_poly = Poly3DCollection(cylinder_faces, 
                                 facecolor="cyan", 
                                 edgecolor=None, 
                                 alpha=0.8)
ax.add_collection3d(cylinder_poly)


center = np.array([11, 12])
radius = 10

# Generate circle points
theta = np.linspace(0, 2*np.pi, 100)
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)
z = np.zeros_like(x)     # Face at z = 0
circle_points = np.column_stack([x, y, z]) # Add circle as polygon 
circle_poly = Poly3DCollection([circle_points], facecolor="cyan", edgecolor="black", alpha=1.0) 
ax.add_collection3d(circle_poly)

"""

# Auto-scale


# Remove axis (optional)
ax.set_axis_off()

ax.view_init(elev=0, azim=90)




plt.savefig("proj.png")

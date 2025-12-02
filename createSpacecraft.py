import pyvista as pv
import math 

# create body 

cube_x = 220
cube_y = 240
cube_z = 380

spacecraft_color = "gray"

spacecraft = pv.Cube(center=(0,0,0), x_length=cube_x, y_length=cube_y, z_length=cube_z)

plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(spacecraft, show_edges=False, color=spacecraft_color, opacity=1)

# create solar panels

y_depth = 5
y = cube_y / 2 + y_depth /2

panel_color = "lightgray"

def createZX_Panel(x,y,z,x_dep,y_dep,z_dep):
    panel = pv.Cube(center=(cube_x/2-x_dep/2-x,y,cube_z/2-z_dep/2-z), x_length=x_dep, y_length=y_dep, z_length=z_dep)
    plotter.add_mesh(panel, show_edges=False, color="lightgray")

# row 1
createZX_Panel(10,y,10, 90,y_depth,60)
createZX_Panel(110,y,30, 40,y_depth,40)
createZX_Panel(190,y,10, 20,y_depth,60)
# row 2
createZX_Panel(10,y,75, 75,y_depth,45)
createZX_Panel(130,y,90, 50,y_depth,20)
createZX_Panel(190,y,95, 20,y_depth,60)
# row 3
createZX_Panel(130,y,135, 50,y_depth,20)
createZX_Panel(10,y,125, 60,y_depth,100)
# row 4
createZX_Panel(130,y,160, 80,y_depth,80)


# add antiena 
hole_height = 20
hole_outer_radius = 100
hole_inner_radius = 70

hole = pv.Cylinder(center=(0,0,-cube_z/2+hole_height/2-0.01), direction=(0,0,1), radius=hole_outer_radius, height=hole_height)
not_hole = pv.Cylinder(center=(0,0,-cube_z/2+hole_height/2-0.02), direction=(0,0,1), radius=hole_inner_radius, height=hole_height)

plotter.add_mesh(hole, show_edges=False, color="white", opacity=1)
plotter.add_mesh(not_hole, show_edges=False, color=spacecraft_color, opacity=1)

# add bottom panel thing
sphere = pv.Sphere(start_phi=0, end_phi=55, radius = 100, center=(0,0,-300))
sphere2 = pv.Sphere(start_phi=125, end_phi=180, radius = 100, center=(0,0,-185))

sphere = sphere.rotate_y(-30, point=(0,0,-300))
sphere2 = sphere2.rotate_y(-30, point=(0,0,-185))

sphere = sphere.translate([0,0,10])
sphere2 = sphere2.translate([-57,0,-5])

plotter.add_mesh(sphere, show_edges=False, color=spacecraft_color, opacity=1)
plotter.add_mesh(sphere2, show_edges=False, color=spacecraft_color, opacity=1)


# legs
leg_height = 225
leg_radius = 3
leg_offset = 0
leg_offset2 = cube_x / 2

# vertical legs
leg = pv.Cylinder(center=(cube_x/2-leg_radius-leg_offset, cube_y/2-leg_radius-leg_offset, -cube_z/2 - leg_height/2), direction=(0,0,1), radius=leg_radius, height=leg_height)
plotter.add_mesh(leg, show_edges=False, color="black", opacity=1)

leg = pv.Cylinder(center=(cube_x/2-leg_radius-leg_offset, -cube_y/2+leg_radius+leg_offset, -cube_z/2 - leg_height/2), direction=(0,0,1), radius=leg_radius, height=leg_height)
plotter.add_mesh(leg, show_edges=False, color="black", opacity=1)

# diagnol legs
leg = pv.Cylinder(center=(cube_x/2-cube_x/4,cube_y/2-cube_y/8,-cube_z/2 - leg_height/2), direction=(cube_x/4,cube_y/8,-leg_height/2), radius=leg_radius, height=math.sqrt(pow(cube_x/2-leg_offset,2) + pow(cube_y/4-leg_offset,2) + pow(leg_height,2)))
plotter.add_mesh(leg, show_edges=False, color="black", opacity=1)

leg = pv.Cylinder(center=(cube_x/2-cube_x/4,-cube_y/2+cube_y/8,-cube_z/2 - leg_height/2), direction=(cube_x/4,-cube_y/8,-leg_height/2), radius=leg_radius, height=math.sqrt(pow(cube_x/2-leg_offset,2) + pow(cube_y/4-leg_offset,2) + pow(leg_height,2)))
plotter.add_mesh(leg, show_edges=False, color="black", opacity=1)


leg = pv.Cylinder(center=(cube_x/2-cube_x/8,cube_y/2-cube_y/4,-cube_z/2 - leg_height/2), direction=(cube_x/8,cube_y/4,-leg_height/2), radius=leg_radius, height=math.sqrt(pow(cube_x/4-leg_offset,2) + pow(cube_y/2-leg_offset,2) + pow(leg_height,2)))
plotter.add_mesh(leg, show_edges=False, color="black", opacity=1)

leg = pv.Cylinder(center=(cube_x/2-cube_x/8,-cube_y/2+cube_y/4,-cube_z/2 - leg_height/2), direction=(cube_x/8,-cube_y/4,-leg_height/2), radius=leg_radius, height=math.sqrt(pow(cube_x/4-leg_offset,2) + pow(cube_y/2-leg_offset,2) + pow(leg_height,2)))
plotter.add_mesh(leg, show_edges=False, color="black", opacity=1)





z_offset = 50
hole = pv.Cube(center=(cube_x/2 - 5 + 1, 0, -cube_z/2 + 10 + z_offset), x_length = 10, y_length=cube_x/3, z_length=cube_x/6)
plotter.add_mesh(hole, show_edges=False, color="white", opacity=1)

# little instrument things
leg = pv.Cylinder(center=(cube_x/2 - 5 + 1, -16, -cube_z/2 + 10 + z_offset), direction=(1,0,0), radius=4, height=40)
plotter.add_mesh(leg, show_edges=False, color="lightgray", opacity=1)

leg = pv.Cylinder(center=(cube_x/2 - 5 + 1, 16, -cube_z/2 + 10 + z_offset), direction=(1,0,0), radius=4, height=40)
plotter.add_mesh(leg, show_edges=False, color="lightgray", opacity=1)

# top arm thing

# arm offset
arm_offset = 10
arm_length = 70
arm_width = 15

arm = pv.Cube(center=(cube_x/2 + arm_length/2,0,cube_z/2 - arm_offset), x_length=arm_length, y_length=arm_width, z_length=arm_width)
plotter.add_mesh(arm, show_edges=False, color="black", opacity=1)

arm_length2 = 35

arm2= pv.Cube(center=(cube_x/2 + arm_length+arm_length2/2,0,cube_z/2 - arm_offset), x_length=arm_length2, y_length=arm_width, z_length=arm_width)

arm2 = arm2.rotate_y(30, point=(cube_x/2 + arm_length,0,cube_z/2 - arm_offset))
arm2 = arm2.translate([-5,0,0])

plotter.add_mesh(arm2, show_edges=False, color="black", opacity=1)


# solar panels
y = -y

# row 1
box_size = 40
createZX_Panel(cube_x/2 - box_size - 5,y,10, box_size,y_depth,box_size)
createZX_Panel(cube_x/2 + 5,y,10, box_size,y_depth,box_size)


# row 2
createZX_Panel(10,y,box_size+30, 30,y_depth,60)
createZX_Panel(70,y,box_size+30, 30,y_depth,60)
createZX_Panel(130,y,box_size+30, 30,y_depth,60)
createZX_Panel(cube_x - 40,y,box_size+30, 30,y_depth,60)

# row 3
createZX_Panel(cube_x - 80,y,150, 50,y_depth,40)
createZX_Panel(-cube_x/2 + 160,y,150, 50,y_depth,40)

createZX_Panel(cube_x - 80,y,220, 50,y_depth,40)
createZX_Panel(-cube_x/2 + 160,y,220, 50,y_depth,40)


# other arm
arm = pv.Cube(center=(-(cube_x/2 + arm_length/2),0,cube_z/2 - arm_offset), x_length=arm_length, y_length=arm_width, z_length=arm_width)
plotter.add_mesh(arm, show_edges=False, color="black", opacity=1)


arm2= pv.Cube(center=(-(cube_x/2 + arm_length+arm_length2/2),0,cube_z/2 - arm_offset), x_length=arm_length2, y_length=arm_width, z_length=arm_width)

arm2 = arm2.rotate_y(-30, point=(-(cube_x/2 + arm_length),0,cube_z/2 - arm_offset))
arm2 = arm2.translate([5,0,0])
plotter.add_mesh(arm2, show_edges=False, color="black", opacity=1)

#createZX_Panel(10,y,10, 50,y_depth,50)

# Camera view
plotter.camera_position = 'iso'
plotter.camera.azimuth += 180
plotter.screenshot("psyche1.png")


plotter.camera_position = 'zy'


plotter.screenshot("psyche2.png")


plotter.camera_position = [
    (800, 800, 1100),
    (0, 0, 0),
    (0, 0, 1)
]

plotter.camera_position = 'yx'

plotter.screenshot("psyche3.png")

'''
pv.start_xvfb()
plotter.show()
input("Press Enter to exit...")
'''






import pyvista as pv


cube_x = 220
cube_y = 240
cube_z = 380

spacecraft = pv.Cube(center=(0,0,0), x_length=cube_x, y_length=cube_y, z_length=cube_z)

# Create a plotter
plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(spacecraft, show_edges=True, color="gray", opacity=1)

y_depth = 10
y = cube_y / 2 + y_depth /2

panel_color = "lightgray"

def createZX_Panel(x,y,z,x_dep,y_dep,z_dep):
    panel = pv.Cube(center=(cube_x/2-x_dep/2-x,y,cube_z/2-z_dep/2-z), x_length=x_dep, y_length=y_dep, z_length=z_dep)
    plotter.add_mesh(panel, show_edges=True, color=panel_color)

createZX_Panel(10,y,10, 90,y_depth,60)
createZX_Panel(110,y,30, 40,y_depth,40)
createZX_Panel(190,y,10, 20,y_depth,60)

createZX_Panel(10,y,75, 75,y_depth,45)
createZX_Panel(130,y,90, 50,y_depth,20)
createZX_Panel(190,y,95, 20,y_depth,60)

createZX_Panel(130,y,135, 50,y_depth,20)
createZX_Panel(10,y,125, 60,y_depth,100)

createZX_Panel(130,y,160, 80,y_depth,80)




#plotter.camera_position = 'iso'
#plotter.camera_position = 'zx'
#plotter.camera.roll += 90


plotter.camera_position = [
    (800, 800, 0),
    (0, 0, 0),
    (0, 0, 1)
]


plotter.screenshot("psyche.png")

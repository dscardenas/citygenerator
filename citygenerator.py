# city generator
# diego cardenas, january 15 2024

import bpy
import random

buildingnum = int(input('Enter # of desired buildings: '))

def get_boundaries(vertices):
    x1, y1, z = vertices[0]
    x2, y2, z = vertices[-1]
    xmin = (x1-x2)/2
    xmax = (abs(x1-x2))/2
    ymin = (y1-y2)/2
    ymax = (abs(y1-y2))/2
    return (xmin, xmax, ymin, ymax, z)


# coordinate selector
def select_coords(bounds):
    xmin, xmax, ymin, ymax, z = bounds
    coords = []
    for i in range(buildingnum):
        x = random.uniform(xmin, xmax)
        y = random.uniform(ymin, ymax)
        coords.append((x, y, z))
    print(coords)
    return coords

# get vertices from base
def get_vertices(mesh):
    
    vertices = []
    meshdata = mesh.data
    for vert in meshdata.vertices:
        (x, y, z) = vert.co
        vertices.append((x, y, z))
        
    if len(vertices) == 4:
        return(vertices)

def place_cubes(vertices):
    for vert in vertices:
        x, y, z = vert
        mscale = random.uniform(.5, 1)
        bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(x, y, z), scale=(random.uniform(.1, .2), random.uniform(.1, .2), mscale))
        cube = bpy.context.active_object
        dx, dy, dz = cube.dimensions
        z = dz/2
        cube.location = (x, y, z)

    
# add a plane
bpy.ops.mesh.primitive_plane_add(scale=(1.2,1.2,1.2))

# change plane name
base = bpy.context.active_object
base.name = "Base"

place_cubes(select_coords(get_boundaries(get_vertices(base))))
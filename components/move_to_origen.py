import rhinoscriptsyntax as rs
import ghpythonlib.components as gh
import ghpythonlib.treehelpers as gt
import Rhino as r
import rhinoscriptsyntax as rs

def move_to_origem(obj):
    box = rs.BoundingBox(obj)
    bbox =  r.Geometry.Box(r.Geometry.Plane.WorldZX,box)   
    point = gh.DeconstructBrep(bbox)[2][0]   
    vector = gh.Vector2Pt(point, gh.ConstructPoint(0,0,0), False)
    moved_objs = []
    for i in obj:
        moved_obj,_ = gh.Move(i,vector)
        moved_objs.append(moved_obj)
        print(point)
    return moved_objs
    
a = move_to_origem(A)
b = move_to_origem(B)
c = move_to_origem(C)
d = move_to_origem(D)
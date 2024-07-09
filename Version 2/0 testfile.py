from BuildingPy import *
import speckle

p1 = Point(1000,0,0)

v1 = Vector3(10,5,2)
v2 = Vector3.reverse(v1)

p2 = Point.translate(p1,v2)

print(p2)
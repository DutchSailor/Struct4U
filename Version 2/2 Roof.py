from BuildingPy import *
from speckle import *

TotalWidth = 7700
Height = 4000
Length = 5000
Spacing = 610

div = DivisionSystem().by_fixed_distance_equal_division(Length,Spacing,0)
lst = div.distances
lst.insert(0,0)
lst.append(Length)

proj = BuildingPy("Bedrijfswoning",2428)

HalfWidth = TotalWidth/2

prof = Rectangle("28x245",28,245)

for i in lst:
    proj.objects.append(Frame.by_startpoint_endpoint_profile(Point(i,0,0),Point(i,HalfWidth,Height),prof.curve,"spoor",BaseTimber))
    proj.objects.append(Frame.by_startpoint_endpoint_profile(Point(i, TotalWidth, 0), Point(i, HalfWidth, Height), prof.curve, "spoor",
                                             BaseTimber))

proj.objects.append(Frame.by_startpoint_endpoint_profile(Point(0,HalfWidth,Height),Point(HalfWidth,HalfWidth,Height),prof.curve,"spoor",BaseTimber))

)
    #proj.objects.append(Support.pinned(Point(0,0,0)))


proj.toSpeckle("657e01486d", "My shiny commit for the Betonvereniging ;-)")


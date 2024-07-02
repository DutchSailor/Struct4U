from BuildingPy import *
from speckle import *
from math import tan
import sys

TotalWidth = 7700
Height = 4000
Length = 5000 # tot de kilkeper
HoekKilkeperAansluitendDakvlak = 45
Spacing = 610

#DIVISION SYSTEM
div = DivisionSystem().by_fixed_distance_equal_division(Length,Spacing,0)
lst = div.distances
lst.insert(0,0)
lst.append(Length)

project = BuildingPy("Test project",00)

HalfWidth = TotalWidth/2

prof = Rectangle("28x245",28,245).curve

#FOR LOOP FOR MAIN STRUCTURE
for i in lst:
    project.objects.append(Frame.by_startpoint_endpoint_rect(Point(i,0,0),Point(i,HalfWidth,Height),28,245,"BB 28x245", 0, BaseTimber))
    project.objects.append(Frame.by_startpoint_endpoint_rect(Point(i, TotalWidth, 0), Point(i, HalfWidth, Height),28,245,"28x245", 0, BaseTimber))

project.objects.append(Frame.by_startpoint_endpoint_rect(Point(0,HalfWidth,Height),Point(Length,HalfWidth,Height),28,245,"28x245", 0, BaseTimber))
project.objects.append(Frame.by_startpoint_endpoint_rect(Point(0,0,0),Point(Length,0,0),28,245,"28x245", 0, BaseTimber))
project.objects.append(Frame.by_startpoint_endpoint_rect(Point(0,TotalWidth,0),Point(Length,TotalWidth,0),28,245,"28x245", 0, BaseTimber))

#KILKEPERS
verlenging_kil = Height/ tan(radians(HoekKilkeperAansluitendDakvlak))

#DIVISION SYSTEM IN KIL
div2 = DivisionSystem().by_fixed_distance_unequal_division(verlenging_kil,Spacing,Spacing,0)
lst2 = div2.distances
number_distances = verlenging_kil / Spacing

#zijde 1
project.objects.append(Frame.by_startpoint_endpoint_rect(Point(Length,0,0),Point(Length+verlenging_kil,HalfWidth,Height),28,245,"28x245", 0, BaseTimber))
project.objects.append(Frame.by_startpoint_endpoint_rect(Point(Length,HalfWidth,Height),Point(Length+verlenging_kil,HalfWidth,Height),28,245,"28x245", 0, BaseTimber))


y = 0
z = 0
ystep = HalfWidth / number_distances
zstep = Height / number_distances

for j in lst2:
    y = y + ystep
    z = z + zstep
    project.objects.append(
        Frame.by_startpoint_endpoint_rect(Point(Length + j, y, z), Point(Length + j, HalfWidth, Height),28,245,"28x245", 0, BaseTimber))
    project.objects.append(
        Frame.by_startpoint_endpoint_rect(Point(Length + j, y, z), Point(Length + verlenging_kil, y, Height),28,245,"28x245", 0, BaseTimber))

# KAP DE HOEK OM

#SEND TO STRUCT4U
pathxml = "C:/TEMP/test8.xml"
gridinput =  ["0 1000 1000",seqChar,"0 4x3600",seqNumber,"0"]

createXFEM4UXML(project,pathxml,gridinput)

project.toSpeckle("657e01486d", "My shiny commit for the Betonvereniging ;-)")
OpenXMLXFEM4U(pathxml)

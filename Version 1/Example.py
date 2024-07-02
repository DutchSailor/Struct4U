from bp_single_file import *

project = BuildingPy("Struct4U Example File", "0,")
#create a project with a name and project number

height = 2500
#In this example the height is variable.

#CREATE GRIDSYSTEM
gridinput = ["0 1000 1000", seqChar, "0 4x3600", seqNumber, "0"]
#This is the syntax for a grid system. The same syntax is used in XFEM4U.

#CONCRETE BEAMS
project.objects.append(Frame.byStartpointEndpoint(Point(0,0,0),Point(0,14400,0),Rectangle("350x500",350,500).curve,"BB 350x500",0,BaseConcrete))

project.objects.append(Frame.byStartpointEndpoint(Point(0,14400,0),Point(2000,14400,0),Rectangle("350x500",350,500).curve,"350x500",0,BaseConcrete))

#These are 2 concrete beams with a certain start and end point.

#STEEL COLUMNS

project.objects.append(Frame.byStartpointEndpointProfileNameShapevector(Point(2000,14400,0),Point(2000,14400,height),"HEA160","HEA160",Vector2(0,0),0,BaseSteel,"Frame"))

#Here we create a steel column. For a HEA160 you can use the syntax of 'HEA 160, HE160A, hea 280 etc.
#Other steelprofiles are HEB100, HEM100, IPE100, 100AA, HD260/54,1, DIN, DIE, DIR, DIL, UNP, B42.4/2.6, INP.
#For the full list of profiles see: https://github.com/3BMLabs/building.py/blob/main/library/profile_database/steelprofile.json
#Composite profiles are not yet implemented.

#STEEL FRAMES
x = 1000
y = 0
for i in range(5):
    project.objects.append(Frame.byStartpointEndpointProfileNameShapevector(Point(0,y,0),Point(0,y,height),"HEA180","HEA180",Vector2(0,0),90,BaseSteel,"Frame")) # column

    project.objects.append(
        Frame.byStartpointEndpointProfileNameShapevector(Point(0, y, height), Point(x, y, height), "HEA180", "HEA180",
                                                         Vector2(0, 0), 0, BaseSteel, "Frame"))  # beam
    x = x + 250
    y = y + 3600

#In this forloop we create the frames. The x and y coordinates increase by every step.

#PLATE IN XFEM4U
project.objects.append(Panel.byPolyCurveThickness(
    PolyCurve.byPoints(
        [Point(0,0,height),
         Point(0,14400,height),
         Point(2000,14400,height),
         Point(1000,0,height),
         Point(0,0,height)]),
    100,
    0,
    "Plate"
    ,BaseConcrete.colorint))

#This code is used to create a plate in XFEM4U based on a list of 5 points.


#SEND PROJECT TO SPECKLE
#project.toSpeckle("31d9948b31")
#It is possible to visualize the result of this parametric structure in Speckle.

#Create XML-file
pathxml = "C:/TEMP/test4.xml"
#This is the path were the temporary file is saved.

createXFEM4UXML(project,pathxml, gridinput)

OpenXMLXFEM4U(pathxml)
#This function will activate XFEM4U and open the parametric model.
from bp_single_file import *

project = BuildingPy("Struct4U Example file","0")

height = 3000

#CREATE GRIDSYSTEM
gridinput =  ["0 1000 1000",seqChar,"0 4x3600",seqNumber,"0"]

#CONCRETE BEAM
project.objects.append(Frame.byStartpointEndpoint(Point(0,0,0),Point(0,14400,0),Rectangle("350x500",350,500).curve,"350x500",0,BaseConcrete))
project.objects.append(Frame.byStartpointEndpoint(Point(0,14400,0),Point(2000,14400,0),Rectangle("350x500",350,500).curve,"350x500",0,BaseConcrete))

#STEEL COLUMN
project.objects.append(Frame.byStartpointEndpointProfileNameShapevector(Point(2000,14400,0),Point(2000,14400,height),"HEA160","HEA160",Vector2(0,0),0,BaseSteel,"Frame"))

#STEEL FRAMES
x = 1000
y = 0
for i in range(5):
    project.objects.append(Frame.byStartpointEndpointProfileNameShapevector(Point(0,y,0),Point(0,y,height),"HEA180","HEA180",Vector2(0,0),90,BaseSteel,"Frame")) # column
    project.objects.append(Frame.byStartpointEndpointProfileNameShapevector(Point(0,y,height),Point(x,y,height),"HEA180","HEA180",Vector2(0,0),0,BaseSteel,"Frame")) # beam
    x = x + 250
    y = y + 3600

#LOADS

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

#SEND PROJECT TO SPECKLE
#project.toSpeckle("31d9948b31")

#CREATE XML-FILE
pathxml = "C:/TEMP/test3.xml"
createXFEM4UXML(project, pathxml, gridinput)

#CHECK IF XFEM4U IS OPENED. IF NOT OPEN XFEM4U
if process_exists("wframe3d.exe") is True:
    pass
else:
    openXFEM4U()
    import time
    time.sleep(10)

#WRITE DIRECTCOMMANDS TO XFEM4U, THEN XML-FILE IS OPENED IN XFEM4U
writeDirectCommandsfile(pathxml)


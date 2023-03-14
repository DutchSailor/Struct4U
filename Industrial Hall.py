from objects.frame import *
from exchange.speckle import *
from objects.datum import *

# GridSystem
seqX = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z AA AB AC"
seqY = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24"
ext = 2500
spac = 5400 #stramienmaat

x = spac
y = spac*4 #breedte hal
z = 10000 #hoogte hal

spacX = "10x5400"
spacY = "4x5400"
grids = GridSystem(spacX,seqX,spacY,seqY,ext)
obj1 = grids[0] + grids[1]

KOLOM = "HEA200"
HOOFDLIGGER = "IPE600"
RANDLIGGER = "HEA140"
KOPPELLIGGER = "HEA100"
n = 9
#SPANTEN
for i in range(n):
    obj1.append(Frame.byStartpointEndpointProfileName(Point(x, 0, z), Point(x, y, z), HOOFDLIGGER, "Hoofdligger")) # dakligger
    obj1.append(Frame.byStartpointEndpointProfileName(Point(x, 0, 0), Point(x, 0, z), KOLOM, "Kolom 1")) # kolom 1
    obj1.append(Frame.byStartpointEndpointProfileName(Point(x, y, 0), Point(x, y, z), KOLOM, "Kolom 2"))  # kolom 2
    x = x + spac

#RANDLIGGERS & KOPPELKOKERS
x = 0
for i in range(n+1):
    obj1.append(Frame.byStartpointEndpointProfileName(Point(x, 0, z), Point(x+spac, 0, z), RANDLIGGER, "Randligger 1"))
    obj1.append(Frame.byStartpointEndpointProfileName(Point(x, y, z), Point(x+spac, y, z), RANDLIGGER, "Randligger 2"))
    obj1.append(Frame.byStartpointEndpointProfileName(Point(x, spac, z), Point(x+spac, spac, z), KOPPELLIGGER,"Koppelkoker 1"))
    obj1.append(Frame.byStartpointEndpointProfileName(Point(x, spac*2, z), Point(x+spac, spac*2, z), KOPPELLIGGER,"Koppelkoker 2"))
    obj1.append(Frame.byStartpointEndpointProfileName(Point(x, spac*3, z), Point(x+spac, spac*3, z), KOPPELLIGGER,"Koppelkoker 3"))
    x = x + spac

#WINDVERBANDEN DAK
x = 0
for i in range(n+1):
    obj1.append(Frame.byStartpointEndpointProfileName(Point(x, 0, z), Point(x+spac, 0, z), RANDLIGGER, "Randligger 1"))
    obj1.append(Frame.byStartpointEndpointProfileName(Point(x, y, z), Point(x+spac, y, z), RANDLIGGER, "Randligger 2"))
    obj1.append(Frame.byStartpointEndpointProfileName(Point(x, spac, z), Point(x+spac, spac, z), KOPPELLIGGER,"Koppelkoker 1"))
    obj1.append(Frame.byStartpointEndpointProfileName(Point(x, spac*2, z), Point(x+spac, spac*2, z), KOPPELLIGGER,"Koppelkoker 2"))
    obj1.append(Frame.byStartpointEndpointProfileName(Point(x, spac*3, z), Point(x+spac, spac*3, z), KOPPELLIGGER,"Koppelkoker 3"))
    x = x + spac


SpeckleObj = translateObjectsToSpeckleObjects(obj1)
Commit = TransportToSpeckle("3bm.exchange", "9eea7219e6", SpeckleObj, "building.py examples.py")
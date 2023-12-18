import simplekml
from polygontest import *


rowCount = 5 # change to recieve from gui 

objList = [None]*row

for i in range(row):
    objList[i] = CreateCoordinates(18.00, 18.00, 100, "test")

polCreate = MakeFile(objList, "test")

polCreate.makePolygon()

# make x dynamic
# make y dynamic
# make z dynamic
# make file name dynamic
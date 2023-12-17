import simplekml
from polygontest import *

row = 5

objList = [None]*row

for i in range(row):
    objList[i] = CreateCoordinates(18.00, 18.00, 100, "test")

polCreate = MakeFile(objList, "test")

polCreate.makePolygon()
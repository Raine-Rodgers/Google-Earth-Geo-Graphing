import simplekml

# make x dynamic
# make y dynamic
# make z dynamic
# make file name dynamic


# create an object with x, y, z values, a name for the polyogn. the z coordinate will represent the value of the polyogn
# ///////////////////////////////////////////////////////////////
class CreateCoordinates:
    def __init__(self, x, y, z, name):
        self.__name = name
        self.__x = x
        self.__y = y
        self.__z = z

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getZ(self):
        return self.__z
    
    def getName(self):
        return self.__name

# a class to create polygons and save the file
# ///////////////////////////////////////////////////////////////
class MakeFile:
    def __init__(self, coordObjList, fileName):
        self.__coordObjList = coordObjList # a list of coordinate objects created in the class above
        self.__fileName = fileName  # name of the file
        self.__kml = simplekml.Kml() # creat the kml variable to uses

    def saveFile(self):
        self.__kml.save(self.__fileName + ".kml") # saves file with a name stored in a variable

    def makePolygon(self):
        for i in range(len(self.__coordObjList)): # iterate through the list of coordinate objects
            pol = self.__kml.newpolygon(name=self.__coordObjList[i].getName(), outerboundaryis=[(self.__coordObjList[i].getX(), self.__coordObjList[i].getY(), self.__coordObjList[i].getZ()),
                                                                                                (self.__coordObjList[i].getX()+0.00039, self.__coordObjList[i].getY()-0.00019, self.__coordObjList[i].getZ()),
                                                                                                (self.__coordObjList[i].getX()+0.00062, self.__coordObjList[i].getY()+0.00013, self.__coordObjList[i].getZ()),
                                                                                                (self.__coordObjList[i].getX()+0.00023, self.__coordObjList[i].getY()+0.00033, self.__coordObjList[i].getZ()),
                                                                                                (self.__coordObjList[i].getX(), self.__coordObjList[i].getY(), self.__coordObjList[i].getZ()),]) # create new polygon with the oldest one being saved
                                                                                                # [(18.43348,-33.98985), 
                                                                                                # (18.43387,-33.99004),
                                                                                                # (18.43410,-33.98972), 
                                                                                                # (18.43371,-33.98952),
                                                                                                # (18.43348,-33.98985)])
            print(self.__coordObjList[i])
            pol.extrude = 1 # connect it to the roud
            pol.altitudemode = simplekml.AltitudeMode.relativetoground # set distance relative to ground to avoid clipping
import simplekml

# make x dynamic
# make y dynamic
# make z dynamic
# make file name dynamic


# create an object with x, y, z values, a name for the polyogn. the z coordinate will represent the value of the polyogn
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
class MakeFile:
    def __init__(self, coordObjList, fileName):
        self.__coordObjList = [coordObjList] # a list of coordinate objects created in the class above
        self.__fileName = fileName  # name of the file
        self.__kml = simplekml.Kml() # creat the kml variable to use

    def saveFile(self):
        self.kml.save(self.__fileName + ".kml") # saves file with a name stored in a variable

    def makePolygon(self):
        for i in self.__coordObjList: # iterate through the list of coordinate objects
            pol = self.__kml.newpolygon(name=self.__fileName, outerboundaryis=self.__coordObjList[i].getX()) # create new polygon with the oldest one being saved
            print(self.__coordObjList[coordObj])
            pol.extrude = 1 # connect it to the roud
            pol.altitudemode = simplekml.AltitudeMode.relativetoground # set distance relative to ground to avoid clipping
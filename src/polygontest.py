import simplekml

class CreateCoordinates:
    def __init__(self, x, y, z, name):
        self.__name = name
        self.__x = x
        self.__y = y
        self.__z = z

    def getX():
        return x
    
    def getY():
        return y
    
    def getZ():
        return z
    

    class MakeFile:
        kml = simplekml.Kml ()
        def __init__(self, coordObj, fileName):
            self.__coordObj = coordObj
            self.__fileName = fileName

        def saveFile():
            pol = kml.newpolygon(name=__fileName, outerboundaryis=coordObj)
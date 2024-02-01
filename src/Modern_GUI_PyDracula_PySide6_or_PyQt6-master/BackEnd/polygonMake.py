import colorsys
import simplekml
from pykml import parser
#TODO: use pykml to parse file and get coordinates

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
    def __init__(self, coordObjList, fileName, outlineIsChecked, filePath):
        self.__filePath = filePath
        self.__coordObjList = coordObjList # a list of coordinate objects created in the class above
        self.__fileName = fileName  # name of the file
        self.__kml = simplekml.Kml() # creat the kml variable to uses
        self.__outlineIsChecked = outlineIsChecked # if the outline is checked or not

    def convertToHex(self, color):
        # Convert color value to RGB
        r, g, b = colorsys.hsv_to_rgb(color / 360, 1, 1)
        
        # Convert RGB to hex code
        # for some reason its reversed and is registered as bgr instead of rgb
        hex_code = 'ff%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255))
        print(hex_code)
        
        return hex_code
    

    def saveFile(self):
        self.__kml.save(self.__filePath + "/" + self.__fileName + ".kml") # saves file with a name stored in a variable


    def makePolygon(self):
        for i in range(len(self.__coordObjList)): # iterate through the list of coordinate objects
            pol = self.__kml.newpolygon(name=self.__coordObjList[i].getName(), outerboundaryis=[(self.__coordObjList[i].getX(), self.__coordObjList[i].getY(), self.__coordObjList[i].getZ()),
                                                                                                (self.__coordObjList[i].getX()+0.00039, self.__coordObjList[i].getY()-0.00019, self.__coordObjList[i].getZ()),
                                                                                                (self.__coordObjList[i].getX()+0.00062, self.__coordObjList[i].getY()+0.00013, self.__coordObjList[i].getZ()),
                                                                                                (self.__coordObjList[i].getX()+0.00023, self.__coordObjList[i].getY()+0.00033, self.__coordObjList[i].getZ()),
                                                                                                (self.__coordObjList[i].getX(), self.__coordObjList[i].getY(), self.__coordObjList[i].getZ()),])
            print(self.__coordObjList[i])
            pol.extrude = 1 # connect it to the roud
            pol.altitudemode = simplekml.AltitudeMode.relativetoground # set distance relative to ground to avoid clipping
            pol.style.polystyle.color = self.convertToHex(1)#simplekml.Color.changealphaint(200, simplekml.Color.) # set color of polygonw // 
            if self.__outlineIsChecked: pol.style.polystyle.outline = 1
            else: pol.style.polystyle.outline = 0
            pol.style.polystyle.fill = 1 # set fill of polygon
            pol.style.polystyle.outline = simplekml.Color.changealphaint(200, simplekml.Color.green) # set outline color of polygon
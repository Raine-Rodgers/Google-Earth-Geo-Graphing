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
    def __init__(self, coordObjList, fileName, outlineIsChecked, barColor, filePath):
        self.__filePath = filePath
        self.__coordObjList = coordObjList # a list of coordinate objects created in the class above
        self.__fileName = fileName  # name of the file
        self.__kml = simplekml.Kml() # creat the kml variable to uses
        self.__outlineIsChecked = outlineIsChecked # if the outline is checked or not
        self.__barColor = barColor # color of the bar graph
        self.min = self.__coordObjList[0].getZ()
        self.max = self.__coordObjList[0].getZ()
        for i in range(len(self.__coordObjList)):
            if self.__coordObjList[i].getZ() < self.min: self.min = self.__coordObjList[i].getZ()
            if self.__coordObjList[i].getZ() > self.max: self.max = self.__coordObjList[i].getZ()

    def convertToHex(self, color):
        
        # Normalize the color value between 0 and 1
        normalized_color = (color - self.min) / (self.max - self.min)
        
        # Reverse the normalized color value
        reversed_color = 1 - normalized_color
        
        # Convert reversed normalized color value to RGB
        r, g, b = colorsys.hsv_to_rgb(reversed_color * 0.666, 1, 1)
        
        # Convert RGB to hex code
        # Reverse the order of RGB and convert to hex code
        hex_code = 'ff%02x%02x%02x' % (int(b * 255), int(g * 255), int(r * 255))
        
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
            if self.__barColor == "Na":
                pol.style.polystyle.color = self.convertToHex(self.__coordObjList[i].getZ())#simplekml.Color.changealphaint(200, simplekml.Color.) # set color of polygonw // 
            else:
                print(self.__barColor)
                pol.style.polystyle.color = self.__barColor
            if self.__outlineIsChecked: pol.style.polystyle.outline = 1
            else: pol.style.polystyle.outline = 0
            pol.style.polystyle.fill = 1 # set fill of polygon
            pol.style.polystyle.outline = simplekml.Color.changealphaint(200, simplekml.Color.green) # set outline color of polygon
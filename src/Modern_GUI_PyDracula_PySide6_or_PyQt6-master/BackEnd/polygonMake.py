import colorsys
import simplekml
from pykml import parser
import math
#TODO: use pykml to parse file and get coordinates

# create an object with x, y, z values, a name for the polyogn. the z coordinate will represent the value of the polyogn
# ///////////////////////////////////////////////////////////////
class CreateCoordinates: 
    def __init__(self, x, y, z, name, z2):
        self.__name = name
        self.__x = x
        self.__y = y
        self.__z = z
        self.__z2 = z2

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getZ(self):
        return self.__z
    
    def getZ2(self):
        return self.__z2
    
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
        self.__scaledValues = [] # a list of scaled values to be used for the bar graph
        self.__rawExtraValues = [] # a list of extra values to be used for the bar graph
        self.min = self.__coordObjList[0].getZ()
        self.max = self.__coordObjList[0].getZ()
        for i in range(len(self.__coordObjList)):
            if self.__coordObjList[i].getZ() < self.min: self.min = self.__coordObjList[i].getZ()
            if self.__coordObjList[i].getZ() > self.max: self.max = self.__coordObjList[i].getZ()
            if self.__coordObjList[i].getZ2() is None or self.__coordObjList[i].getZ2() == "":
                self.__rawExtraValues.append(0)
            else:
                self.__rawExtraValues.append(self.__coordObjList[i].getZ2())
    

    def convertToHex(self, color):
        
        # Normalize the color value between 0 and 1
        if self.min == self.max:
            normalized_color = 0
        else:
            normalized_color = (color - self.min) / (self.max - self.min)
        
        # Reverse the normalized color value
        reversed_color = 1 - normalized_color
        
        # Convert reversed normalized color value to RGB
        r, g, b = colorsys.hsv_to_rgb(reversed_color * 0.666, 1, 1)
        
        # Convert RGB to hex code
        # Reverse the order of RGB and convert to hex code
        hex_code = 'ff%02x%02x%02x' % (int(b * 255), int(g * 255), int(r * 255))
        
        return hex_code
    
    def normalizeExtraValues(self):
        a1_list = [10, 20, 30, 40, 50]  # Example inputs
        target_min = 0.00040  # New target min
        target_max = 0.00150  # New target max

        a1_min = min(self.__rawExtraValues)
        a1_max = max(self.__rawExtraValues)

        if a1_min == a1_max:
            a1_normalized = [0] * len(self.__rawExtraValues)  # Avoid division by zero
        else:
            # Normalize a1 values to [0,1]
            a1_normalized = [(x - a1_min) / (a1_max - a1_min) for x in self.__rawExtraValues]

        # Rescale normalized values to [target_min, target_max]
        self.__scaledValues = [x * (target_max - target_min) + target_min for x in a1_normalized]

        # Output the scaled values and the average b1 multiplier
        print("Scaled values:", self.__scaledValues)


    def saveFile(self):
        self.__kml.save(self.__filePath + "/" + self.__fileName + ".kml") # saves file with a name stored in a variable


    def makePolygon(self):
        for i in range(len(self.__coordObjList)):  # iterate through the list of coordinate objects
            x = self.__coordObjList[i].getX()
            y = self.__coordObjList[i].getY()

            # Adjust longitude offset based on latitude
            self.normalizeExtraValues()
            offset = self.__scaledValues[i]
            lon_offset = offset / abs(math.cos(math.radians(y)))

            barOffset = 0.0001
            barLon_offset = barOffset / abs(math.cos(math.radians(y)))

            pol = self.__kml.newpolygon(name=self.__coordObjList[i].getName(),
                outerboundaryis=[(x - barLon_offset, y - barOffset,  self.__coordObjList[i].getZ()),
                                (x + barLon_offset, y - barOffset,  self.__coordObjList[i].getZ()),
                                (x + barLon_offset, y + barOffset,  self.__coordObjList[i].getZ()),
                                (x - barLon_offset, y + barOffset,  self.__coordObjList[i].getZ()),
                                (x - barLon_offset, y - barOffset,   self.__coordObjList[i].getZ()),])
            print(self.__coordObjList[i])
            pol.extrude = 1  # connect it to the ground
            pol.altitudemode = simplekml.AltitudeMode.relativetoground  # set distance relative to ground to avoid clipping
            if self.__barColor == "Na":
                pol.style.polystyle.color = self.convertToHex(self.__coordObjList[i].getZ())
            else:
                print(self.__barColor)
                pol.style.polystyle.color = self.__barColor
            if self.__outlineIsChecked:
                pol.style.polystyle.outline = 1
            else:
                pol.style.polystyle.outline = 0
            pol.style.polystyle.fill = 1  # set fill of polygon
            pol.style.polystyle.outline = simplekml.Color.changealphaint(200, simplekml.Color.green)  # set outline color of polygon

            if self.__coordObjList[i].getZ2() != 0:
                
                # Define rectangle vertices using scaledValues as offsets
                

                pol2 = self.__kml.newpolygon(name=self.__coordObjList[i].getName() + "2",
                outerboundaryis=[
                    (x - lon_offset, y - offset, 5),  # Bottom-left corner
                    (x + lon_offset, y - offset, 5),  # Bottom-right corner
                    (x + lon_offset, y + offset, 5),  # Top-right corner
                    (x - lon_offset, y + offset, 5),  # Top-left corner
                    (x - lon_offset, y - offset, 5)   # Close the square
                ])

                print("Error: " + str(i))
                print(self.__scaledValues)
                print(self.__coordObjList[i])
                pol2.extrude = 1
                pol2.altitudemode = simplekml.AltitudeMode.relativetoground  # set distance relative to ground to avoid clipping
                pol2.style.polystyle.outline = 1
                pol2.style.polystyle.fill = 1  # set fill of polygon
                pol2.style.polystyle.color = simplekml.Color.changealphaint(200, simplekml.Color.blue)
                pol2.style.polystyle.outline = simplekml.Color.changealphaint(200, simplekml.Color.green)  # set outline color of polygon
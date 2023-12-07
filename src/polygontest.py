import simplekml

class MakeFile:
    def __init__(self):
        self.kml = simplekml.Kml()
        self.coords = []

# sets up coordinates
    def createCoords(self, x, y, z):
        self.coords.append((x, y, z))

# sets up and saves file
    def saveFile(self, filename, name, coordinates):
        if self.coords:
            pol = self.kml.newpolygon(name=name, outerboundaryis=coordinates)
            pol.extrude = 1
            pol.altitudemode = simplekml.AltitudeMode.relativetoground
            self.kml.save(filename + ".kml")
        else:
            print("No coordinates to save.")

    # pol = kml.newpolygon(name=name, outerboundaryis=coordinates)
    # # Set the polygon style
    # pol.extrude = 1
    # pol.altitudemode = simplekml.AltitudeMode.relativetoground
    # # Save the KML object to a file
    # kml.save("output.kml")

# Create a new polygon with the defined coordinates
    createCoords(3, 5, 10, 5)
    saveFile("Test", "Name", self.coords)
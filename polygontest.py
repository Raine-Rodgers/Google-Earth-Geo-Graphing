import simplekml

class MakeFile():
    def __init__(self, kml, fileName, XPreset, YPreset, ZPreset, coordinates):
        self.kml = simplekml.Kml() # Create a new KML object
        self.fileName = "polygon" # get name from title page
        self.XPreset = 8.47287495092937 # make sure these work for different scales
        self.YPreset = 50.2237550498698 # make sure these work for different scales
        self.ZPreset = 1000 # make sure these work for different scales
        self.coordinates = [[None]]

# sets up coordinates
def createCoords():
    coordinates = [
        (XPreset+0.0002, YPreset+0.0002, ZPreset),
        (XPreset-0.0002, YPreset+0.0002, ZPreset),
        (XPreset-0.0002, YPreset-0.0001, ZPreset),
        (XPreset+0.0002, YPreset-0.0001, ZPreset),
        (XPreset+0.0002, YPreset+0.0002, ZPreset)
    ]

# sets up and saves file
def saveFile(coordinates):
    pol = kml.newpolygon(name=name, outerboundaryis=coordinates)
    # Set the polygon style
    pol.extrude = 1
    pol.altitudemode = simplekml.AltitudeMode.relativetoground
    # Save the KML object to a file
    kml.save("output.kml")

# Create a new polygon with the defined coordinates
createCoords()

saveFile(coordinates)
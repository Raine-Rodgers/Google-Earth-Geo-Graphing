import simplekml

# Create a new KML object
kml = simplekml.Kml()

# get name from title page
name = "polygon"

# make sure these work for different scales
XPreset = 8.47287495092937
YPreset = 50.2237550498698
ZPreset = 1000

coordinates = [[None] * 4] * 3
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
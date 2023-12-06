import simplekml

# Create a new KML object
kml = simplekml.Kml()

name = "polygon"

XPreset = 8.47287495092937
YPreset = 50.2237550498698
ZPreset = 1000
def createCoords():
    coordinates = [
        (XPreset+0.0002, YPreset+0.0002, ZPreset),
        (XPreset-0.0002, YPreset+0.0002, ZPreset),
        (XPreset-0.0002, YPreset-0.0001, ZPreset),
        (XPreset+0.0002, YPreset-0.0001, ZPreset),
        (XPreset+0.0002, YPreset+0.0002, ZPreset)
    ]

createCoord()
# Create a new polygon with the defined coordinates
pol = kml.newpolygon(name=name, outerboundaryis=coordinates)

# Set the polygon style
pol.extrude = 1
pol.altitudemode = simplekml.AltitudeMode.relativetoground

# Save the KML object to a file
kml.save("output.kml")

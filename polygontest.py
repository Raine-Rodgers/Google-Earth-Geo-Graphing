import simplekml

# Create a new KML object
kml = simplekml.Kml()

name = "polygon"

x = 8.47287495092937
y = 50.2237550498698
z = 1000

coordinates = [
    (x+0.0002, y+0.0002, 1000),
    (x-0.0002, y+0.0002, 1000),
    (x-0.0002, y-0.0001, 1000),
    (x+0.0002, y-0.0001, 1000),
    (x+0.0002, y+0.0002, 1000)
]

# Create a new polygon with the defined coordinates
pol = kml.newpolygon(name=name, outerboundaryis=coordinates)

# Set the polygon style
pol.extrude = 1
pol.altitudemode = simplekml.AltitudeMode.relativetoground

# Save the KML object to a file
kml.save("output.kml")

import simplekml
kml = simplekml.Kml()
pol = kml.newpolygon(name='A Polygon')
pol.outerboundaryis = [(18.333868,-34.038274), (18.370618,-34.034421),
                       (18.350616,-34.051677),(18.333868,-34.038274)]
pol.altitudemode = simplekml.AltitudeMode.relativetoground
kml.save("Polygon.kml")
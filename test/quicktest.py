import simplekml

kml = simplekml.Kml()

pol = kml.newpolygon(name="numberOne", outerboundaryis=[(18.333868,-34.038274), (18.370618,-34.034421),
                                                        (18.350616,-34.051677),(18.333868,-34.038274)])

pol = kml.newpolygon(name="numberTwo", outerboundaryis=[(28.333868,-24.038274), (28.370618,-24.034421),
                                                        (28.350616,-24.051677),(28.333868,-24.038274)])
pol.extrude = 1
pol.altitudemode = simplekml.AltitudeMode.relativetoground

kml.save("testingFile.kml")
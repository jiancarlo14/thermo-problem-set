import numpy as np

constants = np.array([
    [13.8594, 2773.78, 220.07],
    [14.0098, 3103.01, 219.79],
    [14.0045, 3279.47, 213.20]
])

temperature = 110 #degC

A, B, C = constants[:, 0], constants[:, 1], constants[:, 2]

P = np.e**(A - B/(temperature + C)) #PSAT {1,2,3}

for i, p in enumerate(P, start=1):
    print(f"Species {i}: Vapor Pressure = {p:.2f} kPa")

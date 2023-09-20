import random
import json
import math

samples = []
no_of_samples = 20
pi = math.pi

def calculate_emf(n, b, r, w, R):
    r = r * (10 ** -2)
    A = pi * r * r
    e = n * w * b * A
    i = e / R
    p = (e * i) / 2
    return "{:.2e}".format(e), "{:.2e}".format(i), "{:.2e}".format(p)

for i in range(no_of_samples):
    b = random.randint(1, 100)
    b = round(b * 0.1, 1)
    w = random.randint(1, 100)
    n = random.randint(1, 20)
    R = random.randint(1, 10)
    r = random.randint(20, 40)
    q = "A circular coil of radius " + str(r) + " cm and " + str(n) + " turns is rotated about its vertical diameter with an angular speed of " + str(w) + " rad/s in a uniform horizontal magnetic field of magnitude " + str(b) + " T. Obtain the maximum and average emf induced in the coil. If a coil forms a closed loop of resistance " + str(R) + " ohm, what is the maximum current in the coil and average power loss due to joule heating?\n"
    a1, a2, a3 = calculate_emf(n, b, r, w, R)
    a = "maximum emf: " + a1 + " volt, average emf: 0 volts, maximum current: " + a2 + " amp, average power loss: " + a3 + " joule\n"

    sample = {
        'instruction': q,
        'input': "EMF = n * w * b * A, I = EMF / R, P = (EMF * I) / 2",
        'output': a + "\n\nThe maximum emf induced in the coil can be calculated using the formula EMF = n * w * b * A, where n is the number of turns, w is the angular speed, b is the magnetic field magnitude, and A is the area of the coil.\nThe maximum current in the coil can be calculated using the formula I = EMF / R, where R is the resistance of the coil.\nThe average power loss due to joule heating can be calculated using the formula P = (EMF * I) / 2."
    }
    samples.append(sample)

# Load existing JSON file
with open("science/ElectroMagneticInduction/emi.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save the updated JSON data
with open("science/ElectroMagneticInduction/emi.json", "w") as file:
    json.dump(existing_data, file, indent=4)

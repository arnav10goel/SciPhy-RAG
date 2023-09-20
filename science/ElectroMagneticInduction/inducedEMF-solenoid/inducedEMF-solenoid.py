import random
import json
import math

samples = []
no_of_samples = 20
mu0 = math.pi * 4 * (10 ** (-7))

def calculate_induced_emf(n, A, t, I1, I2):
    emf = (mu0 * A * 0.01 * n * I2) / t
    return "{:.2e}".format(emf)

for i in range(no_of_samples):
    n = random.randint(1, 30)
    A = random.randint(1, 30)
    t = round(random.randint(1, 30) / 100, 2)
    I1 = random.randint(1, 30)
    I2 = random.randint(1, 10)
    q = "A long solenoid with " + str(n) + " turns per cm has a small loop of area " + str(A) + " cm² placed inside the solenoid normal to its axis. If the current carried by the solenoid changes steadily from " + str(I1) + " A to " + str(I1 + I2) + " A in " + str(t) + " s, what is the induced emf in the loop while the current is changing?\n"
    a = "{:.2e} volt\n".format(float(calculate_induced_emf(n, A, t, I1, I2)))

    sample = {
        'instruction': q,
        'input': "EMF = (μ₀ * A * n * I₂) / t",
        'output': a + "\n\nThe induced electromotive force (EMF) can be calculated using the formula EMF = (μ₀ * A * n * I₂) / t, where μ₀ is the permeability of free space, A is the area of the loop, n is the number of turns per cm of the solenoid, I₂ is the change in current, and t is the time taken for the change."
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

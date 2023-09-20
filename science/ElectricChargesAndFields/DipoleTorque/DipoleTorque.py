import random
import math
import json

samples = []

no_of_samples = 20

for i in range(no_of_samples):
    sample = {}
    dipole = random.randint(1, 200)
    E = random.randint(1, 200)
    theta = random.randint(0, 179)
    q = "An Electric dipole with dipole moment " + str(dipole) + " x 10^(-9) C-m is aligned at " + str(
        theta) + " degrees with the direction of a uniform electric field of magnitude " + str(
        E) + " x 10^4 N C-1. Calculate the magnitude of torque acting on the dipole?\n"
    torque = dipole * E * math.sin(theta * (math.pi / 180))
    
    a = "The torque acting on an electric dipole in a uniform electric field can be calculated using the formula:\n"
    explanation = "Torque = dipole moment * electric field * sin(theta)\n"
    a += "Substituting the given values:\n"
    a += "Torque = " + str(dipole) + " x 10^(-9) C-m * " + str(E) + " x 10^4 N C-1 * sin(" + str(theta) + ")\n"
    a += "Torque = " + "{:.1e}".format(torque) + " newton-m\n"

    sample["instruction"] = q
    sample["input"] = explanation
    sample["output"] = a

    samples.append(sample)

# Load existing JSON file
with open("science/ElectricChargesAndFields/ecf.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/ElectricChargesAndFields/ecf.json", "w") as file:
    json.dump(existing_data, file, indent=4)

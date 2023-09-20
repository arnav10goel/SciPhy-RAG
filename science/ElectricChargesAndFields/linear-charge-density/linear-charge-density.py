import random
import json

samples = []

no_of_samples = 10

for i in range(no_of_samples):
    sample = {}
    E = random.randint(1000, 11000)
    d = random.randint(1, 400)
    q = "An infinite line charge produces a field of {} N/C at a distance of {} cm. Calculate the linear charge density.\n".format(E, d)
    a = "To calculate the linear charge density, we use the formula:\n"
    a += "Linear charge density = (Electric field * distance) / (18 * epsilon_0)\n"
    a += "Given electric field = {} N/C, distance = {} cm,\n".format(E, d)
    a += "Linear charge density = {:.2e} C/m\n".format((E * d * 0.01) / (18 * (10 ** 9)))
    input_formula = "Linear charge density = (Electric field * distance) / (18 * epsilon_0)"

    sample["instruction"] = q
    sample["input"] = input_formula
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

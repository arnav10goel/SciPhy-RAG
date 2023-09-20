import random
import json

samples = []

no_of_samples = 10

for i in range(no_of_samples):
    sample = {}
    q1 = random.randint(1, 50) * (10 ** (-6))
    q2 = random.randint(1, 50) * (10 ** (-6))
    if random.randint(0, 1):
        q1 = -q1
    if random.randint(0, 1):
        q2 = -q2
    d = random.randint(1, 50)
    r1 = random.randint(2, 5)
    r2 = random.randint(2, 5)
    d2 = random.randint(2, 5)
    q = "Two copper spheres A, B are separated by a distance " + str(d) + " cm. The force of repulsion if the charge on A is " + str(
        q1) + " C, and the charge on B is " + str(q2) + " C is F1. The force of repulsion if the charge on A becomes " + str(
        r1) + " times, the charge on B becomes " + str(r2) + " times, and the distance between them becomes " + str(
        d2) + " times is F2. Find F1/F2?\n"
    a = "{}/{}".format(d2 ** 2, r1 * r2)
    input_formula = "F1/F2 = (d2^2) / (r1 * r2)"

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

import random
import math
import json

samples = []

no_of_samples = 20

for i in range(no_of_samples):
    sample = {}
    q1 = random.randint(1, 200)
    q2 = random.randint(1, 200)
    d = random.randint(1, 200)
    if random.randint(0, 1):
        q1 = -q1
    if random.randint(0, 1):
        q2 = -q2
    q = "Two point charges q1 = " + str(q1) + " x 10^(-6)C and q2 = " + str(q2) + " x 10^(-6)C are located " + str(
        d) + " cm apart in vacuum. "
    types = random.randint(1, 5)
    E = (q1 - q2) * (10 ** (-6)) * (9 * (10 ** 9)) * (4 / (d * d * 0.0001))
    if types < 3:
        q = q + "What is the electric field at the midpoint O of the line joining two charges?\n"
        a = "To calculate the electric field at the midpoint O, we use the formula:\n"
        a += "Electric field = (q1 - q2) / (4 * pi * epsilon * r^2)\n"
        a += "Given q1 = " + str(q1) + " x 10^(-6)C, q2 = " + str(q2) + " x 10^(-6)C, and r = " + str(d) + " cm,\n"
        a += "Electric field = {:.2e} newton/coulomb\n".format(abs(E))
        input_formula = "Electric field = (q1 - q2) / (4 * pi * epsilon * r^2)"
    else:
        qmid = random.randint(-10, 10)
        while qmid == 0:
            qmid = random.randint(-10, 10)
        q = q + "What is the force on the test charge of " + str(qmid) + " x 10^(-6)C placed at the midpoint of the line joining two charges?\n"
        a = "To calculate the force on the test charge at the midpoint, we use the formula:\n"
        a += "Force = Electric field * test charge\n"
        a += "Given the electric field as calculated before and the test charge qmid = " + str(qmid) + " x 10^(-6)C,\n"
        a += "Force = {:.2e} newton\n".format(abs(E * qmid * (10 ** (-6))))
        input_formula = "Electric field = (q1 - q2) / (4 * pi * epsilon * r^2)\nForce = Electric field * test charge"
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

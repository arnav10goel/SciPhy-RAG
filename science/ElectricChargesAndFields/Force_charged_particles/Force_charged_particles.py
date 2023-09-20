import random
import json
import math

samples = []

no_of_samples = 20

for i in range(no_of_samples):
    sample = {}
    types = random.randint(0, 4)
    if types < 3:
        q1 = random.randint(1, 200) * (10 ** (-6))
        q2 = random.randint(1, 200) * (10 ** (-6))
        if random.randint(0, 1):
            q1 = -q1
        if random.randint(0, 1):
            q2 = -q2
        F = random.randint(1, 200)
        q = "The electrostatic force on a small sphere of charge " + str(q1) + " C due to another small charge of " + str(
            q2) + " C in air is " + str(F) + " N. "
        if types != 2:
            q += "What is the distance between the spheres?\n"
            r = math.sqrt(abs((q1 * q2 * (9 * (10 ** 9))) / F))
            a = "The distance between the spheres is {:.2e} m\n".format(r)
            input_formula = "r = sqrt(abs((q1 * q2 * k) / F))"
        else:
            q += "What is the force on the second sphere due to the first?\n"
            a = "The force on the second sphere due to the first is {} N\n".format(F)
            input_formula = "Force = F"
    else:
        q1 = random.randint(1, 200) * (10 ** (-6))
        q2 = random.randint(1, 200) * (10 ** (-6))
        if random.randint(0, 1):
            q1 = -q1
        if random.randint(0, 1):
            q2 = -q2
        d = random.randint(1, 100)
        F = (9 * (10 ** 9) * q1 * q2) / (d * d * 0.0001)
        q = "What is the force between two small charged spheres having charges " + str(q1) + " C and " + str(
            q2) + " C placed " + str(d) + " cm apart?\n"
        a = "The force between the two charged spheres is {:.2e} N\n".format(F)
        input_formula = "Force = (k * q1 * q2) / (d^2)"

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

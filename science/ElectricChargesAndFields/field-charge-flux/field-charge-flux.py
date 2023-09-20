import random
import json
import math

samples = []

no_of_samples = 40

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1, 6)
    if types < 3:
        d1 = random.randint(1, 100)
        d2 = random.randint(1, 100)
        E = random.randint(1, 800) * 10
        arr = ["inward", "outward"]
        arr2 = ["-", ""]
        types2 = types - 1
        q = "A sphere of radius " + str(d1) + " cm has an unknown charge. If the electric field at " + str(
            d1 + d2) + " cm from the center of the sphere is " + str(E) + " N/C and points radially " + arr[
                types2] + ", then what is the net charge on the sphere?\n"
        a = arr2[types2] + "To calculate the net charge on the sphere, we use the formula:\n"
        a += "Net charge = Electric field * (distance^2) * (1 / (4 * pi * epsilon_0))\n"
        a += "Given electric field = " + str(E) + " N/C, distance = " + str(d1 + d2) + " cm,\n"
        a += "Net charge = {:.2e} C\n".format(E * ((d1 + d2) ** 2) * (1 / (9 * (10 ** 9))))
        input_formula = "Net charge = Electric field * (distance^2) * (1 / (4 * pi * epsilon_0))"
    else:
        d = random.randint(1, 2000)
        D = random.randint(1, 2000)
        q = "A uniformly charged conducting sphere of " + str(d) + " cm diameter has a surface charge density of " + str(
            D) + " micro-C/m², then find the "
        if types < 5:
            q = q + "charge on the sphere?\n"
            a = "To determine the charge on the sphere, we use the formula:\n"
            a += "Charge = Surface charge density * Surface area\n"
            a += "Given surface charge density = " + str(D) + " micro-C/m², diameter = " + str(d) + " cm,\n"
            a += "Charge = {:.2e} C\n".format(D * 4 * math.pi * (d / 2) * (d / 2) * (10 ** (-10)))
            input_formula = "Charge = Surface charge density * Surface area"
        else:
            q = q + "electric flux leaving the sphere?\n"
            a = "To calculate the electric flux leaving the sphere, we use the formula:\n"
            a += "Electric flux = Surface charge density * Surface area * (1 / (4 * pi * epsilon_0))\n"
            a += "Given surface charge density = " + str(D) + " micro-C/m², diameter = " + str(d) + " cm,\n"
            a += "Electric flux = {:.2e} N·m²/C\n".format(
                D * 4 * math.pi * (d / 2) * (d / 2) * (10 ** (-10)) * (1 / (8.854 * (10 ** (-12)))))
            input_formula = "Electric flux = Surface charge density * Surface area * (1 / (4 * pi * epsilon_0))"
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

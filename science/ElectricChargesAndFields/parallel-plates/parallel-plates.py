import random
import json

samples = []

no_of_samples = 20

for i in range(no_of_samples):
    sample = {}
    sigma = random.randint(1, 2000000)
    q = "Two large thin metal plates are parallel and close to each other. On their inner faces, the plates have surface charge densities of opposite signs and of magnitude {} x 10^(-22) C/m². What is E:".format(sigma)
    types = random.randint(1, 12)
    if types <= 10:
        q += " between the plates?\n"
        a = "To calculate the electric field between the plates, we use the formula:\n"
        a += "Electric field (E) = surface charge density / (2 * epsilon_0)\n"
        a += "Given surface charge density = {} x 10^(-22) C/m²,\n".format(sigma)
        a += "Electric field (E) = {:.2e} N/C\n".format(sigma / (8.854 * (10 ** 10)))
        input_formula = "Electric field (E) = surface charge density / (2 * epsilon_0)"
    else:
        arr = ["first", "second"]
        q += " in the outer region of the {} plate?\n".format(arr[types - 11])
        a = "To calculate the electric field in the outer region of a plate, the electric field is zero.\n"
        input_formula = "Electric field = 0 N/C"

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

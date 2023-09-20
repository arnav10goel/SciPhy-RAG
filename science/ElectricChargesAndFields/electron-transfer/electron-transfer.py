import random
import json

samples = []

no_of_samples = 30

for i in range(no_of_samples):
    sample = {}
    q1 = random.randint(1, 2000000)
    q = "A polythene is rubbed with wool is found to have a negative charge of " + str(
        q1) + " x 10^(-12) C. "
    types = random.randint(1, 2)
    n = (q1 * (10 ** (-12))) / (1.6 * (10 ** (-19)))
    if types == 1:
        q = q + "Estimate the number of electrons transferred (from which to which)?\n"
        a = "To estimate the number of electrons transferred, we use the formula:\n"
        a += "Number of electrons = (charge / elementary charge)\n"
        a += "Given charge = " + str(q1) + " x 10^(-12) C and elementary charge = 1.6 x 10^(-19) C,\n"
        a += "Number of electrons = {:.3e} electrons transfered from wool to polythene\n".format(n)
        input_formula = "Number of electrons = (charge / elementary charge)"
    else:
        q = q + "Is there a transfer of mass from wool to polythene?\n"
        a = "To determine if there is a transfer of mass, we consider the mass associated with the number of electrons transferred:\n"
        a += "Mass = (number of electrons) * (mass of one electron)\n"
        a += "Given number of electrons = {:.3e}, mass of one electron = 9.1 x 10^(-31) kg,\n".format(n)
        a += "Mass = {:.3e} kg of mass is transferred\n".format(n * 9.1 * (10 ** (-31)))
        input_formula = "Mass = (number of electrons) * (mass of one electron)"
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

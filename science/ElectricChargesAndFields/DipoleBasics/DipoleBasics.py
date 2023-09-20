import random
import json

samples = []

no_of_samples = 20

for i in range(no_of_samples):
    sample = {}
    q1 = random.randint(1, 200)
    d1 = random.randint(1, 200)
    d2 = random.randint(-200, -1)
    q = "Two point charges q1 = " + str(q1) + " x 10^(-6)C and q2 = - " + str(q1) + " x 10^(-6)C are located at the points A:(0, 0, - " + str(d1) + " cm) and B:(0, 0, " + str(d2) + " cm), respectively. What are the total charge and electric dipole moment of the system?\n"
    d = d1 + abs(d2)
    p = q1 * d * (10 ** (-8))
    a = "The total charge of the system is 0 coulomb and the electric dipole moment is " + "{:.2e}".format(
        p) + " coulomb-m\n"
    input_formula = "Total charge = 0\nElectric dipole moment = q1 * d"
    
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

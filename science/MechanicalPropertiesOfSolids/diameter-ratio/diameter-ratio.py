import random
import math
import json

no_of_samples = 20

def calculate_diameter_ratio(Y1, Y2):
    ratio = math.sqrt(Y2/Y1)
    return ratio

def generate_question(m, l, Y1, Y2):
    return f"A rigid bar of mass {m} kg is supported symmetrically by three wires each {l} m long. Those at each end are of material-1 and the middle one is of material-2. Find ratios of their diameters all have the same tension (Young's modulus of material-1 is {Y1} x 10^9 Nm-2, material-2 is {Y2} x 10^9 Nm-2)."

samples = []

for i in range(no_of_samples):
    m = random.randint(1, 20)
    l = random.randint(1, 20)
    Y1 = random.randint(1, 200)
    Y2 = random.randint(1, 200)

    question = generate_question(m, l, Y1, Y2)
    diameter_ratio = calculate_diameter_ratio(Y1, Y2)
    input_formula = "diameter_ratio = sqrt(Y2 / Y1)"
    output = f"The ratio of their diameters is {diameter_ratio:.2f}."

    sample = {
        "instruction": question,
        "input": input_formula,
        "output": output
    }

    samples.append(sample)

# Read the existing JSON file
with open("science/MechanicalPropertiesOfSolids/mps.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/MechanicalPropertiesOfSolids/mps.json", "w") as file:
    json.dump(existing_data, file, indent=4)

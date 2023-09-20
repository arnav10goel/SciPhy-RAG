import random
import math
import json

no_of_samples = 20

def calculate_elongation(m1, m2, l1, l2, d, E):
    A = math.pi * d ** 2 * 10 ** (-8)
    if E == 2.0 * 10 ** 11:
        F = (m1 + m2) * 9.8
        elongation = (F * l1) / (A * E)
    elif E == 0.9 * 10 ** 11:
        F = m2 * 9.8
        elongation = (F * l2) / (A * E)
    return elongation

def generate_question(m1, m2, l1, l2, d, E, types):
    if types == 1:
        wire_type = "steel"
    elif types == 2:
        wire_type = "brass"
    return f"A body of mass {m1} kg is hanged from the roof with the help of a {wire_type} wire of length {l1} m. Another body of mass {m2} kg is hanged from the bottom of mass m1 with the help of a {wire_type} wire of length {l2} m. If the radius of both wires is {d} x 10^(-4) m, what is the elongation of the {wire_type} wire?"

samples = []

for i in range(no_of_samples):
    m1 = random.randint(1, 20)
    m2 = random.randint(1, 20)
    l1 = random.randint(1, 20)
    l2 = random.randint(1, 20)
    d = random.randint(1, 200)
    types = random.randint(1, 2)

    if types == 1:
        E = 2.0 * 10 ** 11
    elif types == 2:
        E = 0.9 * 10 ** 11

    question = generate_question(m1, m2, l1, l2, d, E, types)
    elongation = calculate_elongation(m1, m2, l1, l2, d, E)
    input_formula = "elongation = (F * l) / (A * E)"
    output = f"elongation = (F * l) / (A * E)\nThe elongation of the wire is {elongation:.1e} m."

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

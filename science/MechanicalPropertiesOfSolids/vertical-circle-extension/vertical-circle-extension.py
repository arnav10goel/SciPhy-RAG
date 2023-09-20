import random
import math
import json

no_of_samples = 20

def calculate_elongation(m, l, ang_v, A):
    F = m * (9.8 + l * math.pi * math.pi * ang_v * ang_v)
    elongation = (F * l) / ((A * (10 ** (-6))) * (2 * (10 ** 11)))
    return elongation * 100

def generate_question(m, l, ang_v, A):
    input_formula = f"elongation = (force * length) / (A * 10^(-6) * Y_steel)"
    return f"A {m} kg mass, fastened to the end of a steel wire of initial length {l} m, is whirled in a vertical circle with an angular velocity of {ang_v} rev/s at the bottom of the circle. The cross-sectional area of the wire is {A} mm^2. Calculate the elongation of the wire when the mass is at the lowest point of its path.", input_formula

samples = []

for i in range(no_of_samples):
    m = random.randint(20, 200)
    l = random.randint(10, 40)
    ang_v = random.randint(1, 10)
    A = random.randint(1, 100)
    question, input_formula = generate_question(m, l, ang_v, A)
    elongation = calculate_elongation(m, l, ang_v, A)
    explanation = f"To calculate the elongation, we use the formula:\n\n"
    explanation += f"elongation = (force * length) / (A * 10^(-6) * Y_steel)\n"
    explanation += f" = ({m} kg * (9.8 + {l} m * π^2 * {ang_v}^2) * {l} m) / ({A} mm^2 * 10^(-6) m^2 * (2 * 10^11 N/m^2))\n"
    explanation += f" = {elongation:.1f} cm."
    output = explanation

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

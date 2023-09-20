import random
import json
import math

no_of_samples = 20

pi = math.pi

def generate_question(n, r, i, b, v):
    return f"A circular coil of {n} turns and radius {r} cm carrying a current of {i} A rests with its plane normal to an external field of magnitude {b} T. The coil is free to turn about an axis in its plane perpendicular to the field direction. When the coil is turned slightly and released, it oscillates about its stable equilibrium with a frequency of {v} sec-1. What is the moment of inertia of the coil about its axis of rotation?"

def generate_input_formula(n, r, i, b, v):
    r = r * (10**-2)
    m = n * i * pi * r * r
    return f"(m * b) / (4 * pi^2 * v^2)"

def generate_output_explanation(n, r, i, b, v):
    r = r * (10**-2)
    m = n * i * pi * r * r
    inertia = (m * b) / (4 * pi * pi * v * v)
    return f"The moment of inertia of the coil about its axis of rotation can be calculated using the formula (m * b) / (4 * pi^2 * v^2), where 'm' is the mass of the coil given by n * i * pi * r^2, 'b' is the magnitude of the external magnetic field, 'v' is the frequency of oscillation. Substituting the given values, we have ({m} * {b}) / (4 * {pi}^2 * {v}^2) = {inertia} kgm^2."

samples = []

for i in range(no_of_samples):
    sample = {}
    n = random.randint(1, 50)
    r = random.randint(10, 20)
    i = random.randint(1, 50)
    b = round(random.randint(1, 100) * 0.01, 2)
    v = random.randint(1, 20)
    question = generate_question(n, r, i, b, v)
    input_formula = generate_input_formula(n, r, i, b, v)
    output_explanation = generate_output_explanation(n, r, i, b, v)

    sample["instruction"] = question
    sample["input"] = input_formula
    sample["output"] = output_explanation

    samples.append(sample)

# Read the existing JSON file
with open("science/MagnetismAndMatter/mam.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/MagnetismAndMatter/mam.json", "w") as file:
    json.dump(existing_data, file, indent=4)

import random
import math
import json

no_of_samples = 20

def calculate_compression_strain(m, num, r1, r2, Y):
    F = (m * 9.8) / num
    A = math.pi * (r2 ** 2 - r1 ** 2) * (10 ** (-4))
    strain = F / (A * (2 * (10 ** 11)))
    return strain

def generate_question(num, r1, r2, m):
    return f"{num} identical hollow cylindrical columns of mild steel support a big structure of mass {m} kg. The inner and outer radii of each column are {r1} cm and {r2} cm respectively. Calculate the compressional strain of each column."

samples = []

number = [4, 6, 9, 12, 15, 16]

for i in range(no_of_samples):
    num = number[random.randint(0, 5)]
    r1 = random.randint(10, 40)
    r2 = random.randint(r1 + 10, r1 + 40)
    m = random.randint(1000, 5000) * 10

    question = generate_question(num, r1, r2, m)
    strain = calculate_compression_strain(m, num, r1, r2, 2.0 * 10 ** 11)
    input_formula = "strain = F / (A * Y)"
    output = f"The compressional strain of each column is {strain:.1e}."

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

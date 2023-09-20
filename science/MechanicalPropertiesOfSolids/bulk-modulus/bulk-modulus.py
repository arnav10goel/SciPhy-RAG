import random
import math
import json

no_of_samples = 20

def calculate_bulk_modulus(initial_volume, pressure_increase, final_volume):
    B = (pressure_increase * 1.013 * (10 ** 8) * initial_volume) / (final_volume - initial_volume)
    return B

def generate_question(initial_volume, pressure_increase, final_volume):
    return f"Compute the bulk modulus of a material from the following data: Initial volume = {initial_volume} litre, Pressure increase = {pressure_increase} atm (1 atm = 1.013 x 10^5 Pa), volume increased = {final_volume - initial_volume} ml."

samples = []

for i in range(no_of_samples):
    initial_volume = random.randint(100, 300)
    pressure_increase = random.randint(100, 300)
    final_volume = random.randint(initial_volume + 1, initial_volume + 1000)

    question = generate_question(initial_volume, pressure_increase, final_volume)
    bulk_modulus = calculate_bulk_modulus(initial_volume, pressure_increase, final_volume)
    input_formula = "bulk modulus = (pressure_increase * 1.013 * (10 ** 8) * initial_volume) / (final_volume - initial_volume)"
    output = f"The bulk modulus of the material is {bulk_modulus:.2e}."

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

import random
import json

samples = []
no_of_samples = 20

def type1(R, n):
    instruction = f"A piece of wire of resistance {R} ohm is drawn out so that its length is increased {n} times. Calculate the resistance of the reformed wire?"
    input_formula = f"R = {R} ohm, n = {n}"
    resistance = R * n * n
    output = f"The resistance of the reformed wire is {resistance} ohm. It is calculated by multiplying the original resistance ({R} ohm) by the square of the length increase factor ({n})."
    return instruction, input_formula, output

def type2(R, n):
    instruction = f"A piece of wire of resistance {R} ohm is drawn out so that its cross-sectional area is increased {n} times. Calculate the resistance of the reformed wire?"
    input_formula = f"R = {R} ohm, n = {n}"
    resistance = round(R / (n ** 2), 1)
    output = f"The resistance of the reformed wire is {resistance} ohm. It is calculated by dividing the original resistance ({R} ohm) by the square of the area increase factor ({n})."
    return instruction, input_formula, output

for _ in range(no_of_samples):
    R = random.randint(10, 100010)
    n = random.randint(2, 11)
    types = random.randint(0, 2)
    if types == 0 or types == 1:
        instruction, input_formula, output = type1(R, n)
    elif types == 2:
        instruction, input_formula, output = type2(R, n)
    sample = {
        'instruction': instruction,
        'input': input_formula,
        'output': output,
    }
    samples.append(sample)

# Load existing JSON file
with open("science/Electricity/elec.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save the updated JSON data
with open("science/Electricity/elec.json", "w") as file:
    json.dump(existing_data, file, indent=4)

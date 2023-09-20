import random
import json

samples = []
no_of_samples = 40

def type1():
    R = random.randint(1, 100)
    A = random.randint(1, 100)
    rho = random.randint(1, 100)
    l = round((R * A) / rho, 1)
    instruction = f"A copper wire has a cross-sectional area of {A} m² and resistivity of {rho} ohm-m. What is the length of this wire that makes its resistance {R} ohm?"
    input_formula = f"R = {R} ohm, A = {A} m², rho = {rho} ohm-m"
    output = f"The length of the wire required to achieve a resistance of {R} ohm is {l} m. It is calculated by dividing the product of resistance and area ({R * A}) by the resistivity ({rho})."
    return instruction, input_formula, output

def type2():
    rho = random.randint(1, 100)
    l = random.randint(1, 100)
    R = random.randint(1, 100)
    A = round((rho * l) / R, 1)
    instruction = f"A copper wire has a length of {l} m and resistivity of {rho} ohm-m. What is the cross-sectional area of this wire that makes its resistance {R} ohm?"
    input_formula = f"R = {R} ohm, l = {l} m, rho = {rho} ohm-m"
    output = f"The cross-sectional area of the wire required to achieve a resistance of {R} ohm is {A} m². It is calculated by dividing the product of resistivity and length ({rho * l}) by the resistance."
    return instruction, input_formula, output

def type3():
    R = random.randint(1, 100)
    A = random.randint(1, 100)
    l = random.randint(1, 100)
    rho = round((R * A) / l, 1)
    instruction = f"A copper wire has a cross-sectional area of {A} m² and length of {l} m. What is the resistivity of this wire that makes its resistance {R} ohm?"
    input_formula = f"R = {R} ohm, A = {A} m², l = {l} m"
    output = f"The resistivity of the wire required to achieve a resistance of {R} ohm is {rho} ohm-m. It is calculated by dividing the product of resistance and area ({R * A}) by the length."
    return instruction, input_formula, output

def type4():
    rho = random.randint(1, 100)
    l = random.randint(1, 100)
    A = random.randint(1, 100)
    R = round((rho * l) / A, 1)
    instruction = f"A copper wire has a cross-sectional area of {A} m², length of {l} m, and resistivity of {rho} ohm-m. What is its resistance?"
    input_formula = f"rho = {rho} ohm-m, l = {l} m, A = {A} m²"
    output = f"The resistance of the wire is {R} ohm. It is calculated by dividing the product of resistivity and length ({rho * l}) by the area."
    return instruction, input_formula, output

for _ in range(no_of_samples):
    types = random.randint(0, 3)
    if types == 0:
        instruction, input_formula, output = type1()
    elif types == 1:
        instruction, input_formula, output = type2()
    elif types == 2:
        instruction, input_formula, output = type3()
    elif types == 3:
        instruction, input_formula, output = type4()
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

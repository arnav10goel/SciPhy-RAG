import random
import json

samples = []
no_of_samples = 2000000

def type1():
    R1 = random.randint(1, 10)
    R2 = random.randint(1, 10)
    rho1 = random.randint(1, 10)
    rho2 = random.randint(1, 10)
    A1 = random.randint(1, 10)
    A2 = random.randint(1, 10)
    instruction = f"A wire of material-1 has resistance of {R1} ohm, cross-sectional area of {A1} m², resistivity of {rho1} ohm-m, another wire of material-2 has resistance of {R2} ohm, cross-sectional area of {A2} m², resistivity of {rho2} ohm-m. Find the ratio of the length of the two wires."
    input_formula = f"R1 = {R1} ohm, R2 = {R2} ohm, rho1 = {rho1} ohm-m, rho2 = {rho2} ohm-m, A1 = {A1} m², A2 = {A2} m²"
    l_ratio = f"{R1 * A1 * rho2}/{R2 * A2 * rho1}"
    output = f"The ratio of the lengths of the two wires is {l_ratio}. It is calculated by taking the product of the resistance, cross-sectional area, and resistivity of wire-1 ({R1 * A1 * rho2}) and dividing it by the product of the resistance, cross-sectional area, and resistivity of wire-2 ({R2 * A2 * rho1})."
    return instruction, input_formula, output

def type2():
    R1 = random.randint(1, 10)
    R2 = random.randint(1, 10)
    l1 = random.randint(1, 10)
    l2 = random.randint(1, 10)
    rho1 = random.randint(1, 10)
    rho2 = random.randint(1, 10)
    instruction = f"A wire of material-1 has length of {l1} m, resistance of {R1} ohm, resistivity of {rho1} ohm-m, another wire of material-2 has length of {l2} m, resistance of {R2} ohm, resistivity of {rho2} ohm-m. Find the ratio of the cross-sectional area of the two wires."
    input_formula = f"R1 = {R1} ohm, R2 = {R2} ohm, l1 = {l1} m, l2 = {l2} m, rho1 = {rho1} ohm-m, rho2 = {rho2} ohm-m"
    A_ratio = f"{R2 * l1 * rho1}/{R1 * l2 * rho2}"
    output = f"The ratio of the cross-sectional areas of the two wires is {A_ratio}. It is calculated by taking the product of the resistance, length, and resistivity of wire-2 ({R2 * l1 * rho1}) and dividing it by the product of the resistance, length, and resistivity of wire-1 ({R1 * l2 * rho2})."
    return instruction, input_formula, output

def type3():
    R1 = random.randint(1, 10)
    R2 = random.randint(1, 10)
    l1 = random.randint(1, 10)
    l2 = random.randint(1, 10)
    A1 = random.randint(1, 10)
    A2 = random.randint(1, 10)
    instruction = f"A wire of material-1 has length of {l1} m, cross-sectional area of {A1} m², resistance of {R1} ohm, another wire of material-2 has length of {l2} m, cross-sectional area of {A2} m², resistance of {R2} ohm. Find the ratio of the resistivity of the two wires."
    input_formula = f"R1 = {R1} ohm, R2 = {R2} ohm, l1 = {l1} m, l2 = {l2} m, A1 = {A1} m², A2 = {A2} m²"
    rho_ratio = f"{R1 * A1 * l2}/{R2 * A2 * l1}"
    output = f"The ratio of the resistivities of the two wires is {rho_ratio}. It is calculated by taking the product of the resistance, length, and cross-sectional area of wire-1 ({R1 * A1 * l2}) and dividing it by the product of the resistance, length, and cross-sectional area of wire-2 ({R2 * A2 * l1})."
    return instruction, input_formula, output

def type4():
    l1 = random.randint(1, 10)
    l2 = random.randint(1, 10)
    rho1 = random.randint(1, 10)
    rho2 = random.randint(1, 10)
    A1 = random.randint(1, 10)
    A2 = random.randint(1, 10)
    instruction = f"A wire of material-1 has length of {l1} m, cross-sectional area of {A1} m², resistivity of {rho1} ohm-m, another wire of material-2 has length of {l2} m, cross-sectional area of {A2} m², resistivity of {rho2} ohm-m. Find the ratio of the resistance of the two wires."
    input_formula = f"l1 = {l1} m, l2 = {l2} m, rho1 = {rho1} ohm-m, rho2 = {rho2} ohm-m, A1 = {A1} m², A2 = {A2} m²"
    R_ratio = f"{A2 * l1 * rho1}/{A1 * l2 * rho2}"
    output = f"The ratio of the resistances of the two wires is {R_ratio}. It is calculated by taking the product of the cross-sectional area, length, and resistivity of wire-2 ({A2 * l1 * rho1}) and dividing it by the product of the cross-sectional area, length, and resistivity of wire-1 ({A1 * l2 * rho2})."
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
        'output': output
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



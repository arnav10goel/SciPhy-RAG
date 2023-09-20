import random
import json

samples = []
no_of_samples = 20

def determine_capacitance(A, d):
    return (8.854 * A * 6) / (d * 0.001)

def determine_charge(capacitance, V):
    return capacitance * V * (10**-12)

for i in range(no_of_samples):
    types = random.randint(1, 2)
    sample = {}

    A = round(random.randint(1, 2000) / 10000, 4)
    d = random.randint(1, 50)
    V = random.randint(1, 800)

    if types == 1:
        q = f"A capacitor with air between its parallel plates, each plate has an area of {A} m² and the distance between the plates is {d} mm. If this capacitor is connected to a {V} V supply and a {d} mm thick mica sheet is inserted between the plates, then what will happen?"
        input_formula = f"A = {A} m², d = {d} mm, V = {V} V"
        capacitance = determine_capacitance(A, d)
        charge = determine_charge(capacitance, V)
        output_formula = f"capacitance becomes = 6 * {capacitance/6:.2e} = {capacitance:.2e} pico-farad, charge = capacitance * V = {capacitance*(10**-12):.2e} * {V} = {charge:.2e} coulomb"
        explanation = "When the mica sheet is inserted between the plates, the effective capacitance of the capacitor changes, and the charge on the capacitor can be calculated using the formula Q = CV."

    elif types == 2:
        q = f"A capacitor with air between its parallel plates, each plate has an area of {A} m² and the distance between the plates is {d} mm. If this capacitor is connected to a {V} V supply and a {d} mm thick mica sheet is inserted between the plates and then the supply is disconnected, then what will happen?"
        input_formula = f"A = {A} m², d = {d} mm, V = {V} V"
        capacitance = determine_capacitance(A, d)
        charge = determine_charge(capacitance, V)
        output_formula = f"capacitance becomes = 6 * {capacitance/6:.2e} = {capacitance:.2e} pico-farad, charge remains = capacitance * V = {(capacitance/6)*(10**-12):.2e} * {V} = {charge:.2e} coulomb"
        explanation = "When the supply is disconnected after inserting the mica sheet, the capacitance of the capacitor remains the same, and the charge on the capacitor also remains the same."

    sample['instruction'] = q
    sample['input'] = input_formula
    sample['output'] = f"{output_formula}\n\n{explanation}"
    samples.append(sample)

# Load existing JSON file
with open("science/ElectroStaticPotentialAndCapacitance/esp.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save the updated JSON data
with open("science/ElectroStaticPotentialAndCapacitance/esp.json", "w") as file:
    json.dump(existing_data, file, indent=4)

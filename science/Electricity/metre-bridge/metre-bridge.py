import random
import json

samples = []
no_of_samples = 20

def calculate_resistance_of_X(balance_point, resistor_Y):
    resistance_X = ((1000 - balance_point) / balance_point) * resistor_Y
    return resistance_X

def interchange_X_and_Y(balance_point):
    new_balance_point = 1000 - balance_point
    return new_balance_point

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1, 5)
    balance_pt = random.randint(0, 1000)
    R1 = random.randint(1, 4000)
    q = "In a meter bridge, the balance point is found to be at " + str(balance_pt) + " mm from end A, when the resistor Y is of " + str(R1) + " ohm. "
    if types != 1:
        q = q + "Determine the resistance of X."
        input_formula = "Resistance of X = ((1000 - balance_point) / balance_point) * R1"
        explanation = "The resistance of X in the meter bridge can be calculated using the formula: Resistance of X = ((1000 - balance_point) / balance_point) * R1."
        a = str(round(calculate_resistance_of_X(balance_pt, R1), 1)) + " ohm\n\nExplanation: " + explanation
    else:
        q = q + "Determine the balance point of the bridge above if X and Y are interchanged."
        input_formula = "New balance point = 1000 - balance_point"
        explanation = "When X and Y are interchanged, the new balance point can be calculated by subtracting the current balance point from 1000."
        a = str(1000 - balance_pt) + " mm\n\nExplanation: " + explanation
    
    sample['instruction'] = q
    sample['input'] = input_formula
    sample['output'] = a
    samples.append(sample)

# Load existing JSON file
with open("science/Electricity/elec.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/Electricity/elec.json", "w") as file:
    json.dump(existing_data, file, indent=4)

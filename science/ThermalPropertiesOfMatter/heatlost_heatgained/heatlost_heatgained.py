import random
import json

no_of_samples = 20

def cal1(m, t1, s):
    return round((m * t1 * s) / 335, 1)

def generate_question_type1(m, t1, s):
    ice_melt = cal1(m, t1, s)
    question = f"A copper block of mass {m} g is heated in a furnace to a temperature of {t1} degree C and then placed on a large ice block. What is the maximum amount of ice that can melt? Specific heat of copper is {s} Jg-1°C-1. Heat of fusion of water = 335 Jg-1."
    input_formula = "Maximum amount of ice melted = (mass of block * temperature change * specific heat) / heat of fusion of water"
    output = f"To calculate the maximum amount of ice melted, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the maximum amount of ice that can melt is approximately {ice_melt} g."
    return question, input_formula, output

samples = []

for i in range(no_of_samples):
    m = random.randint(1000, 4000)
    t1 = random.randint(500, 1000)
    t = random.randint(1, 2)

    if t == 1:
        s = 0.39
        question, input_formula, output = generate_question_type1(m, t1, s)
    else:
        s = 0.91
        question, input_formula, output = generate_question_type1(m, t1, s)

    sample = {
        "instruction": question,
        "input": input_formula,
        "output": output
    }

    samples.append(sample)

# Load existing JSON file
with open("science/ThermalPropertiesOfMatter/tpm.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/ThermalPropertiesOfMatter/tpm.json", "w") as file:
    json.dump(existing_data, file, indent=4)

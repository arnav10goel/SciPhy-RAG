import random
import json

no_of_samples = 20

def calculate_liquid_height(d1, d2):
    return (1.01 * (10 ** 5)) / (d1 * 9.8)

def determine_suitability(P, p):
    if P <= p:
        return "no, it is not suitable"
    else:
        return "yes, it is suitable"

def generate_question_toricelli(d1, d2):
    return f"Toricelli\'s barometer used mercury. If someone duplicated it using some liquid of density {d1} kg/m3. Determine the height of the liquid column for normal atmospheric pressure (density of material of barometer is {d2} kg/m3)."

def generate_question_offshore(d, P):
    return f"A vertical off-shore structure is built to withstand a maximum stress of {P} Pa. Is the structure suitable for putting up on top of an oil well in the ocean? Take the depth of the ocean to be roughly {d} km, and ignore ocean currents?"

def generate_input_formula_toricelli(d1, d2):
    return f"(1.01 * (10 ** 5)) / ({d1} * 9.8)"

def generate_input_formula_offshore(d, P):
    return f"{d} * 1000 * 980"

samples = []

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1, 2)

    if types == 1:
        d1 = random.randint(100, 3000)
        d2 = random.randint(100, 3000)
        question = generate_question_toricelli(d1, d2)
        result = calculate_liquid_height(d1, d2)
        input_formula = generate_input_formula_toricelli(d1, d2)
    else:
        d = random.randint(1, 10)
        P = d * 1000 * 980
        question = generate_question_offshore(d, P)
        p = random.randint(P - 200000, P + 200000)
        result = determine_suitability(P, p)
        input_formula = generate_input_formula_offshore(d, P)

    sample["instruction"] = question
    sample["input"] = input_formula
    sample["output"] = result

    samples.append(sample)

# Read the existing JSON file
with open("science/MechanicalPropertiesOfLiquids/mpl.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/MechanicalPropertiesOfLiquids/mpl.json", "w") as file:
    json.dump(existing_data, file, indent=4)

import random
import json

no_of_samples = 30

def calculate_ratio(l1, l2, A1, A2):
    ratio = (l1 * A2) / (l2 * A1)
    return ratio

def generate_question_type1(l1, l2, A1, A2):
    input_formula = f"ratio = (l1 * A2) / (l2 * A1)"
    return f"A wire of material-1 of length {l1} m stretches by the same amount as a wire of material-2 of length {l2} m under a given load. What is the ratio of the Young’s modulus of material-1 to that of material-2, assuming the ratio of their cross-sectional areas is {A1}/{A2}?", input_formula

def generate_question_type2(l1, l2, A1, A2):
    input_formula = f"ratio = (l1 * A2) / (l2 * A1)"
    return f"A wire of material-1 of cross-sectional area {A1} x 10^(-6) m^2 stretches by the same amount as a wire of material-2 of cross-sectional area {A2} x 10^(-6) m^2 under a given load. What is the ratio of the Young’s modulus of material-1 to that of material-2, assuming the ratio of their lengths is {l1}/{l2}?", input_formula

def generate_question_type3(l1, l2, A1, A2):
    input_formula = f"ratio = (l1 * A2) / (l2 * A1)"
    return f"A wire of material-1 of length {l1} m and cross-sectional area {A1} x 10^(-6) m^2 stretches by the same amount as a wire of material-2 of length {l2} m and cross-sectional area {A2} x 10^(-6) m^2 under a given load. What is the ratio of the Young’s modulus of material-1 to that of material-2?", input_formula

samples = []

for i in range(no_of_samples):
    l1 = random.randint(1, 200)
    l2 = random.randint(1, 200)
    A1 = random.randint(1, 20)
    A2 = random.randint(1, 20)

    types = random.randint(1, 4)

    if types == 1:
        question, input_formula = generate_question_type1(l1, l2, A1, A2)
    elif types == 2:
        question, input_formula = generate_question_type2(l1, l2, A1, A2)
    else:
        question, input_formula = generate_question_type3(l1, l2, A1, A2)

    ratio = calculate_ratio(l1, l2, A1, A2)
    output = f"The ratio of the Young\'s modulus of material-1 to that of material-2 is approximately {ratio:.2f}. To calculate the ratio, we use the formula:\n\n{input_formula}"

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


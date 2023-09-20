import random
import json

no_of_samples = 20

def calculate_relative_density(l2, l1):
    return l2 / l1

def calculate_difference_in_levels(l1, l2, l3):
    h1 = l1 + l3
    h2 = l2 + l3
    relative_density = l2 / l1
    difference = (abs(h1 / 10 - relative_density * (h2 / 10))) / 13.6
    return difference

def generate_question_relative_density(l1, l2):
    return f"A U tube contains water and liquid separated by mercury. The mercury columns in the two arms are in level with {l1} mm of water in one arm and {l2} mm of liquid in the other. What is the relative density of the liquid?"

def generate_question_difference_in_levels(l1, l2, l3):
    return f"A U tube contains water and liquid separated by mercury. The mercury columns in the two arms are in level with {l1} mm of water in one arm and {l2} mm of liquid in the other. If {l3} mm of water and liquid each are further poured into the respective arms of the tube, what is the difference in the levels of mercury in the two arms?"

def generate_input_formula_relative_density():
    return "l2 / l1"

def generate_input_formula_difference_in_levels():
    return "abs((l1 + l3) / 10 - (l2 / l1) * (l2 + l3) / 10) / 13.6"

samples = []

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1, 3)
    l1 = random.randint(1, 2000)
    l2 = random.randint(1, 2000)

    if types == 1:
        question = generate_question_relative_density(l1, l2)
        relative_density = calculate_relative_density(l2, l1)
        input_formula = generate_input_formula_relative_density()
        output = f"The relative density of the liquid is {relative_density:.2f}."
    else:
        l3 = random.randint(1, 2000)
        question = generate_question_difference_in_levels(l1, l2, l3)
        difference = calculate_difference_in_levels(l1, l2, l3)
        input_formula = generate_input_formula_difference_in_levels()
        output = f"The difference in the levels of mercury in the two arms is {difference:.2e} mm."

    sample["instruction"] = question
    sample["input"] = input_formula
    sample["output"] = f"Output: {output}"

    samples.append(sample)

# Read the existing JSON file
with open("science/MechanicalPropertiesOfLiquids/mpl.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/MechanicalPropertiesOfLiquids/mpl.json", "w") as file:
    json.dump(existing_data, file, indent=4)

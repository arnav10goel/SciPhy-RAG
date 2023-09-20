import random
import json

no_of_samples = 20

def calculate_lift(v1, v2, A):
    return 0.5 * 1.3 * (v1**2 - v2**2) * (A / 10000)

def generate_question1(v1, v2, A):
    return f"In a test experiment on a model aeroplane in a wind tunnel, the flow speeds on the upper and lower surfaces of the wing are {v1} ms-1 and {v2} ms-1. What is the lift on the wing if its area is {A} cm2? (Take the density of air to be 1.3 kgm-3)"

def generate_question2(v1, v2, A):
    return f"In a test experiment on a model aeroplane in a wind tunnel, the flow speeds on the upper and lower surfaces of the wing are {v1} ms-1 and {v2} ms-1. What is the lift on the wing if its area is {A} cm2?"

def generate_input_formula(v1, v2, A):
    return f"0.5 * 1.3 * ({v1}**2 - {v2}**2) * ({A} / 10000)"

def generate_output_explanation(F):
    return f"The lift on the wing is {F} newton."

samples = []

for i in range(no_of_samples):
    sample = {}
    v2 = random.randint(1, 100)
    v1 = random.randint(v2 + 1, v2 + 40)
    A = random.randint(1, 400) * 100
    types = random.randint(0, 1)

    if types:
        question = generate_question1(v1, v2, A)
    else:
        question = generate_question2(v1, v2, A)

    F = calculate_lift(v1, v2, A)
    input_formula = generate_input_formula(v1, v2, A)
    output_explanation = generate_output_explanation(F)

    sample["instruction"] = question
    sample["input"] = input_formula
    sample["output"] = output_explanation

    samples.append(sample)

# Read the existing JSON file
with open("science/MechanicalPropertiesOfLiquids/mpl.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/MechanicalPropertiesOfLiquids/mpl.json", "w") as file:
    json.dump(existing_data, file, indent=4)

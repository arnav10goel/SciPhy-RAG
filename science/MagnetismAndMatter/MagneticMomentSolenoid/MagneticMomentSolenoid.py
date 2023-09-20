import random
import json

no_of_samples = 20

def generate_question1(n, i, A):
    return f"A closely wounded solenoid of {n} turns and an area of cross-section {A} m² carries a current of {i} A. What is its associated magnetic moment?"

def generate_input_formula1(n, i, A):
    return f"n * i * A"

def generate_output_explanation1(n, i, A):
    return f"The magnetic moment (m) of a solenoid is given by the formula m = n * i * A, where 'n' is the number of turns, 'i' is the current, and 'A' is the area of cross-section. Substituting the given values, we have m = {n} * {i} * {A} = {n * i * A}."

samples = []

for i in range(no_of_samples):
    sample = {}
    n = random.randint(1, 50) * 20
    i = random.randint(1, 100)
    A = round(random.randint(1, 200) * 0.0001, 4)

    question = generate_question1(n, i, A)
    input_formula = generate_input_formula1(n, i, A)
    output_explanation = generate_output_explanation1(n, i, A)

    sample["instruction"] = question
    sample["input"] = input_formula
    sample["output"] = output_explanation

    samples.append(sample)

# Read the existing JSON file
with open("science/MagnetismAndMatter/mam.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/MagnetismAndMatter/mam.json", "w") as file:
    json.dump(existing_data, file, indent=4)

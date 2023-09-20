import random
import json

no_of_samples = 20

def cal1(t1, t2):
    return round(t1 / t2, 2)

def generate_question_type1(t1, t2):
    relation = cal1(t1, t2)
    question = f"Two absolute scales A and B have triple points of water defined to be {t1} A and {t2} B. What is the relation between TA and TB?"
    input_formula = "Relation between TA and TB = TA / TB"
    output = f"To find the relation between TA and TB, we divide the temperature on scale A (TA) by the temperature on scale B (TB). Therefore, the relation is given by:\n\n{input_formula}\n\nSubstituting the given values, we find that the relation is approximately {relation}."
    return question, input_formula, output

samples = []

for i in range(no_of_samples):
    t1 = random.randint(-200, 800)
    t2 = random.randint(-200, 800)

    while t2 == 0:
        t2 = random.randint(-200, 800)

    while t1 == 0:
        t1 = random.randint(-200, 800)

    question, input_formula, output = generate_question_type1(t1, t2)

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

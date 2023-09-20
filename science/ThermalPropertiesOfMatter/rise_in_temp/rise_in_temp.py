import random
import json

no_of_samples = 20

def cal1(P, m, p, s, t):
    return round((p * P * t) / (m * s), 1)

def generate_question_type1(P, m, p, s, t):
    temperature = cal1(P, m, p, s, t)
    question = f"A {P} kW drilling machine is used to drill a bore in a small aluminium block of mass {m} kg. How much is the rise in temperature of the block in {t} minutes, assuming {p} percent of power is used up in heating the machine itself or lost to the surroundings? Specific heat of aluminium = 0.91 J g-1 K-1."
    input_formula = "Rise in temperature = (p * P * t) / (m * s)"
    output = f"To calculate the rise in temperature, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the rise in temperature is approximately {temperature} degrees Celsius."
    return question, input_formula, output

samples = []

for i in range(no_of_samples):
    P = random.randint(1, 100)
    m = random.randint(1, 20)
    p = random.randint(10, 60)
    t = random.randint(1, 10)
    t1 = random.randint(1, 2)

    if t1 == 1:
        s = 0.91
        question, input_formula, output = generate_question_type1(P, m, p, s, t)
    elif t1 == 2:
        s = 0.39
        question, input_formula, output = generate_question_type1(P, m, p, s, t)

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

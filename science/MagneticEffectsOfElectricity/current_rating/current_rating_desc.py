import random
import json

no_of_samples = 20

def generate_question1(P, V, I):
    return f"An electric appliance of {P} W power rating is operated in a domestic electric circuit of {V} V that has a current rating of {I} A. Will the appliance be safe for a longer time?"

def generate_question2(P, V):
    return f"An electric appliance of {P} W power is operated in a domestic circuit of {V} V. What is the minimum current rating it should have to avoid overloading?"

def generate_input_formula1(P, V, I):
    return f"P/V - I"

def generate_input_formula2(P, V):
    return f"P/V"

def generate_output_explanation1(P, V, I):
    safe_threshold = 0.01
    result = P/V - I
    explanation = f"It will be safer if P/V - I is less than or equal to {safe_threshold}. Now P/V - I = {P}/{V} - {I} = {result:.3f}."
    if result <= safe_threshold:
        explanation += " So, it will be safe for a longer time."
    else:
        explanation += " So, it will not be safe for a longer time."
    return explanation

def generate_output_explanation2(P, V):
    return f"The minimum current rating required = P/V = {P}/{V} = {P/V:.1f} ampere."

samples = []

for i in range(no_of_samples):
    sample = {}
    V = random.randint(220, 240)
    P = random.randint(24, 100000)
    I = round(random.randint(10, 1000) / 10, 1)

    if random.randint(1, 4) != 3:
        question = generate_question1(P, V, I)
        input_formula = generate_input_formula1(P, V, I)
        output_explanation = generate_output_explanation1(P, V, I)
    else:
        question = generate_question2(P, V)
        input_formula = generate_input_formula2(P, V)
        output_explanation = generate_output_explanation2(P, V)

    sample["instruction"] = question
    sample["input"] = input_formula
    sample["output"] = output_explanation

    samples.append(sample)

# Read the existing JSON file
with open("science/MagneticEffectsOfElectricity/mec.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/MagneticEffectsOfElectricity/mec.json", "w") as file:
    json.dump(existing_data, file, indent=4)

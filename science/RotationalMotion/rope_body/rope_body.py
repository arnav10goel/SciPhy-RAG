import random
import json

no_of_samples = 90
c = [1, 1/2, 2/3, 2/5]

def calculate_angular_acceleration(k, m, r, f):
    return round((f * 100) / (k * m * r), 1)

def calculate_linear_acceleration(k, m, f):
    return round(f / (k * m), 1)

def generate_question_type1(m, r, f, t):
    if t == 0:
        object_type = "hollow cylinder"
        quantity_type = "angular"
        c = 1 
    elif t == 1:
        object_type = "hollow cylinder"
        quantity_type = "linear"
        c = 1 
    elif t == 2:
        object_type = "solid cylinder"
        quantity_type = "angular"
        c = 1/2
    elif t == 3:
        object_type = "solid cylinder"
        quantity_type = "linear"
        c = 1/2
    elif t == 4:
        object_type = "hollow sphere"
        quantity_type = "angular"
        c = 2/3
    elif t == 5:
        object_type = "hollow sphere"
        quantity_type = "linear"
        c = 2/3
    elif t == 6:
        object_type = "solid sphere"
        quantity_type = "angular"
        c = 2/5
    else:
        object_type = "solid sphere"
        quantity_type = "linear"
        c = 2/5

    q = f"A rope of negligible mass is wound round a {object_type} of mass {m} kg and radius {r} cm. What is the {quantity_type} acceleration of the {object_type} if the rope is pulled with a force of {f} N? Assume that there is no slipping."

    if quantity_type == "angular":
        a = str(calculate_angular_acceleration(c, m, r, f)) + " rad/s²"
    else:
        a = str(calculate_linear_acceleration(c, m, f)) + " m/s²"

    input_formula = "Acceleration = Force / (k * mass * radius)"
    formula_explanation = f"Acceleration = {f} N / ({c} * {m} kg * {r} cm)"

    output = f"To calculate the {quantity_type} acceleration of the {object_type}, we use the following formula:\n\n{input_formula}\n\nSubstituting the values:\n\nForce = {f} N\nk = {c}\nMass = {m} kg\nRadius = {r} cm\n\nWe find that the {quantity_type} acceleration of the {object_type} is approximately {a}."

    return q, input_formula, formula_explanation, output

samples = []

for i in range(no_of_samples):
    m = random.randint(1, 100)
    r = random.randint(1, 100)
    f = random.randint(1, 100)
    t = random.randint(0, 7)

    question, input_formula, formula_explanation, answer = generate_question_type1(m, r, f, t)

    output = f"{formula_explanation}\n\n{answer}"

    sample = {
        "instruction": question,
        "input": input_formula,
        "output": output
    }

    samples.append(sample)

# Load existing JSON file
with open("science/RotationalMotion/rom.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/RotationalMotion/rom.json", "w") as file:
    json.dump(existing_data, file, indent=4)

import random
import math
import json

no_of_samples = 20
ang = [0, math.pi/6, math.pi/3, math.pi/2]

def calculate_torque(f, l, r):
    return round(f * l * math.sin(math.radians(r)), 1)

def calculate_force(t, l, r):
    return round(t / (l * math.sin(math.radians(r))), 1)

def generate_question_type1(f, l, r):
    torque = calculate_torque(f, l, r)
    question = f"Calculate the torque produced by a {f} N force acting at the end of a {l} m long wrench at an angle of {r} degrees to the wrench."
    input_formula = "torque = force * length * sin(angle)"
    output = f"To calculate the torque, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the torque is approximately {torque} Nm."
    return question, input_formula, output

def generate_question_type2(t, l, r):
    force = calculate_force(t, l, r)
    question = f"A torque of {t} Nm is produced by a force acting at the end of a {l} m long wrench at an angle of {r} degrees to the wrench. What is the value of the force?"
    input_formula = "force = torque / (length * sin(angle))"
    output = f"To calculate the force, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the force is approximately {force} N."
    return question, input_formula, output

samples = []

for i in range(no_of_samples):
    types = random.randint(1, 2)

    if types == 1:
        f = random.randint(1, 500)
        l = random.randint(1, 500)
        temp = random.randint(0, 3)
        question, input_formula, output = generate_question_type1(f, l, ang[temp])

    else:
        t = random.randint(500, 1000)
        l = random.randint(1, 500)
        temp = random.randint(1, 3)
        question, input_formula, output = generate_question_type2(t, l, ang[temp])

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

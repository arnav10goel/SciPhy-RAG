import random
import json
import math

no_of_samples = 20

pi = math.pi

def generate_question1(b, d, t):
    return f"A short bar magnet placed with its axis at {d} degrees with a uniform external magnetic field of {b} T experiences a torque of magnitude equal to {t} J. What is the magnitude of the magnetic moment of the bar magnet?"

def generate_question2(b, d, m):
    return f"A short bar magnet of magnetic moment {m} is placed with its axis at {d} degrees with a uniform external magnetic field of {b} T. What is the magnitude of the torque experienced by the bar magnet?"

def generate_input_formula1(b, d, t):
    return f"t / (b * sin(d*pi/180))"

def generate_input_formula2(b, d, m):
    return f"m * b * sin(d*pi/180)"

def generate_output_explanation1(b, d, t):
    d = math.sin((d * pi) / 180)
    return f"If 'b' is the magnetic field strength, 't' is the torque due to that magnetic moment, 'd' is the angle between the axis of the magnet and the magnetic field, and 'm' is the magnetic moment, then t = m * b * sin(d). Solving for 'm', we have m = t / (b * sin(d)) = {t} / ({b} * {d:.2f})."

def generate_output_explanation2(b, d, m):
    d = math.sin((d * pi) / 180)
    return f"If 'b' is the magnetic field strength, 't' is the torque due to that magnetic moment, 'd' is the angle between the axis of the magnet and the magnetic field, and 'm' is the magnetic moment, then t = m * b * sin(d) = {m} * {b} * {d:.2f}."

samples = []

for i in range(no_of_samples):
    sample = {}
    b = round(random.randint(1, 100) * 0.01, 2)
    d = random.randint(1, 90)
    t = round(random.randint(1, 200) * 0.001, 3)
    m = round(random.randint(1, 200) * 0.01, 2)

    if random.randint(1, 2) == 1:
        question = generate_question1(b, d, t)
        input_formula = generate_input_formula1(b, d, t)
        output_explanation = generate_output_explanation1(b, d, t)
    else:
        question = generate_question2(b, d, m)
        input_formula = generate_input_formula2(b, d, m)
        output_explanation = generate_output_explanation2(b, d, m)

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

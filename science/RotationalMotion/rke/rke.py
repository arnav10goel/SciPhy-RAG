import random
import json

no_of_samples = 40

def calculate_power(w, t):
    return w * t

def calculate_torque(w, p):
    return round(p / w, 1)

def calculate_angular_speed(t, p):
    return round(p / t, 1)

def generate_question_type1(w, t):
    q = f"To maintain a rotor at a uniform angular speed of {w} rad/s, an engine needs to transmit a torque of {t} Nm. What is the power required by the engine?"
    input_formula = "Power = Angular Speed * Torque"
    formula_explanation = f"Power = {w} rad/s * {t} Nm"
    p = calculate_power(w, t)
    output = f"To calculate the power required by the engine, we use the following formula:\n\n{input_formula}\n\nSubstituting the values:\n\nAngular Speed = {w} rad/s\nTorque = {t} Nm\n\nWe find that the power required by the engine is {p} watts."
    return q, input_formula, formula_explanation, output

def generate_question_type2(w, p):
    q = f"To maintain a rotor at a uniform angular speed of {w} rad/s, an engine requires a power of {p} W. What is the torque transmitted by the engine?"
    input_formula = "Torque = Power / Angular Speed"
    formula_explanation = f"Torque = {p} W / {w} rad/s"
    t = calculate_torque(w, p)
    output = f"To calculate the torque transmitted by the engine, we use the following formula:\n\n{input_formula}\n\nSubstituting the values:\n\nPower = {p} W\nAngular Speed = {w} rad/s\n\nWe find that the torque transmitted by the engine is {t} Nm."
    return q, input_formula, formula_explanation, output

def generate_question_type3(t, p):
    q = f"Torque of {t} Nm is transmitted to an engine at a power of {p} W. What is the angular speed of the rotor?"
    input_formula = "Angular Speed = Power / Torque"
    formula_explanation = f"Angular Speed = {p} W / {t} Nm"
    w = calculate_angular_speed(t, p)
    output = f"To calculate the angular speed of the rotor, we use the following formula:\n\n{input_formula}\n\nSubstituting the values:\n\nPower = {p} W\nTorque = {t} Nm\n\nWe find that the angular speed of the rotor is {w} rad/s."
    return q, input_formula, formula_explanation, output

samples = []

for i in range(no_of_samples):
    w = random.randint(1, 1000)
    t = random.randint(1, 1000)
    p = random.randint(1, 1000)

    types = random.randint(1, 3)

    if types == 1:
        question, input_formula, formula_explanation, answer = generate_question_type1(w, t)
    elif types == 2:
        question, input_formula, formula_explanation, answer = generate_question_type2(w, p)
    elif types == 3:
        question, input_formula, formula_explanation, answer = generate_question_type3(t, p)

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
import random
import json
import math

pi = math.pi

no_of_samples = 30

def calculate_magnetic_force_per_unit_length(i, d, b):
    d = math.sin(math.radians(d))
    return round(b * i * d, 1)

def generate_question_type1(i, d, b):
    q = f"What is the magnitude of the magnetic force per unit length on a wire carrying a current of {i} A and making an angle of {d} degrees with the direction of a uniform magnetic field of {b} tesla?"
    a = f"{calculate_magnetic_force_per_unit_length(i, d, b)} newtons per meter"
    return q, a

def generate_question_type2(i, d, b, l):
    q = f"A {l} cm of wire carrying a current of {i} A is placed inside a solenoid making an angle of {d} degrees with its axis. The magnetic field inside the solenoid is {b} tesla. Find the magnetic force on the wire."
    a = f"{calculate_magnetic_force_per_unit_length(i, d, b) * (l / 100)} newtons"
    return q, a

samples = []

for i in range(no_of_samples):
    types = random.randint(1, 2)
    d = random.randint(1, 180)
    i = random.randint(1, 200)
    b = random.randint(1, 100)
    l = random.randint(1, 50)

    if types == 1:
        question, answer = generate_question_type1(i, d, b)
    else:
        question, answer = generate_question_type2(i, d, b, l)

    input_formula = "Force per unit length = b * i * sin(d)"
    output = f"To calculate the magnitude of the magnetic force, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values:\n- b = {b} tesla\n- i = {i} A\n- d = {d} degrees\n\nAfter evaluating the formula, we find that the magnetic force per unit length is approximately {answer}."

    sample = {
        "instruction": question,
        "input": input_formula,
        "output": output
    }

    samples.append(sample)

# Read the existing JSON file
with open("science/MovingChargesAndMagnetism/mcm.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/MovingChargesAndMagnetism/mcm.json", "w") as file:
    json.dump(existing_data, file, indent=4)
import random
import json
import math

no_of_samples = 50

pi = math.pi
mu = 4 * pi * (10 ** -7)

def calculate_magnetic_field(n, r, i):
    r = r * (10 ** -2)
    return (mu * n * i) / (2 * r)

def generate_question_type1(n, r, i):
    q = f"A circular coil of wire consisting of {n} turns, each of radius {r} cm carries a current of {i} A. What is the magnitude of the magnetic field B at the center of the coil?"
    b = calculate_magnetic_field(n, r, i)
    a = f"{b:.2e} tesla"
    return q, a

def generate_question_type2(n, r, i):
    q = f"A circular coil of wire consisting of {n} turns, each of radius {r} cm placed in a horizontal plane carries a current of {i} A in clockwise direction. What is the magnitude and direction of the magnetic field B at the center of the coil?"
    b = calculate_magnetic_field(n, r, i)
    a = f"{b:.2e} tesla vertically downwards"
    return q, a

def generate_question_type3(n, r, i):
    q = f"A circular coil of wire consisting of {n} turns, each of radius {r} cm placed in a horizontal plane carries a current of {i} A in anticlockwise direction. What is the magnitude and direction of the magnetic field B at the center of the coil?"
    b = calculate_magnetic_field(n, r, i)
    a = f"{b:.2e} tesla vertically upwards"
    return q, a

samples = []

for i in range(no_of_samples):
    n = random.randint(1, 200)
    i = random.randint(1, 20)
    r = random.randint(10, 1000)

    types = random.randint(1, 3)

    if types == 1:
        question, answer = generate_question_type1(n, r, i)
    elif types == 2:
        question, answer = generate_question_type2(n, r, i)
    else:
        question, answer = generate_question_type3(n, r, i)

    input_formula = "B = (mu * n * i) / (2 * r)"
    output = f"To calculate the magnetic field B at the center of the coil, we use the following formula:\n\n{input_formula}\n\nWhere,\n- B = Magnetic field at the center of the coil\n- mu = Permeability of free space (4 * pi * 10^(-7) T*m/A)\n- n = Number of turns in the coil\n- i = Current flowing through the coil\n- r = Radius of the coil\n\nSubstituting the given values into the formula, we find that the magnitude of the magnetic field B is approximately {answer}."

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

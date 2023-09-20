import random
import json
import math

no_of_samples = 20

pi = math.pi
mu = 4 * pi * (10 ** -7)

def calculate_magnetic_field(n, r, i, x):
    r = r * (10 ** -2)
    x = x * (10 ** -2)
    return (mu * n * i * r * r) / (2 * math.sqrt(((r * r) + (x * x)) ** 3))

def generate_question_type1(n, r, i, x):
    q = f"A circular coil of wire consisting of {n} turns, each of radius {r} cm carries a current of {i} A. What is the magnitude of the magnetic field B at a point on the axis which is {x} cm from the center of the coil?"
    b = calculate_magnetic_field(n, r, i, x)
    a = f"{b:.2e} tesla"
    return q, a

samples = []

for i in range(no_of_samples):
    n = random.randint(1, 200)
    i = random.randint(1, 20)
    r = random.randint(10, 100)
    x = random.randint(10, 100)

    types = random.randint(1, 1)

    if types == 1:
        question, answer = generate_question_type1(n, r, i, x)

    input_formula = "B = (mu * n * i * r^2) / (2 * sqrt((r^2 + x^2)^3))"
    output = f"To calculate the magnetic field B at a point on the axis, which is {x} cm from the center of the coil, we use the following formula:\n\n{input_formula}\n\nWhere,\n- B = Magnetic field at the point on the axis\n- mu = Permeability of free space (4 * pi * 10^(-7) T*m/A)\n- n = Number of turns in the coil\n- i = Current flowing through the coil\n- r = Radius of the coil\n- x = Distance from the center of the coil to the point on the axis\n\nSubstituting the given values into the formula, we find that the magnitude of the magnetic field B is approximately {answer}."

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
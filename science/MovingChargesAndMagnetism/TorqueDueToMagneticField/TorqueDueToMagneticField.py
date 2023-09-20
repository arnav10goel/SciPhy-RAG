import random
import json
import math

no_of_samples = 40

pi = math.pi

def calculate_torque(n, i, d, b, A):
    A = A * (10 ** -4)
    d = math.sin((d * pi) / 180)
    return round(n * b * i * d * A, 1)

def generate_question_type1(n, i, d, b, l):
    q = f"A square coil of side {l} cm consists of {n} turns and carries a current of {i} A. The coil is suspended vertically, and the normal to the plane of the coil makes an angle of {d} degrees with the direction of a uniform horizontal magnetic field of magnitude {b} tesla. What is the magnitude of the torque experienced by the coil."
    A = l * l
    torque = calculate_torque(n, i, d, b, A)
    a = f"{torque} newton-m"
    return q, a

def generate_question_type2(n, i, d, b, l):
    q = f"A circular coil of radius {l} cm consists of {n} turns and carries a current of {i} A. The coil is suspended vertically, and the normal to the plane of the coil makes an angle of {d} degrees with the direction of a uniform horizontal magnetic field of magnitude {b} tesla. What is the magnitude of the torque experienced by the coil."
    A = pi * l * l
    torque = calculate_torque(n, i, d, b, A)
    a = f"{torque} newton-m"
    return q, a

samples = []

for i in range(no_of_samples):
    n = random.randint(10, 50)
    i = random.randint(1, 20)
    d = random.randint(1, 90)
    b = random.randint(1, 20)
    l = random.randint(1, 50)

    types = random.randint(1, 2)

    if types == 1:
        question, answer = generate_question_type1(n, i, d, b, l)
    elif types == 2:
        question, answer = generate_question_type2(n, i, d, b, l)

    input_formula = "Torque = n * b * i * A * sin(d)"
    output = f"To calculate the magnitude of the torque experienced by the coil, we use the following formula:\n\n{input_formula}\n\nWhere,\n- n = Number of turns in the coil\n- b = Magnetic field\n- i = Current in the coil\n- A = Area of the coil\n- d = Angle between the normal to the coil and the magnetic field\n\nFor a square coil, the area (A) is equal to the square of the side length (l) of the coil. For a circular coil, the area (A) is equal to pi times the square of the radius (l) of the coil.\n\nSubstituting the given values into the formula and evaluating it, we find that the magnitude of the torque experienced by the coil is approximately {answer}."

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
import random
import json
import math

no_of_samples = 30

pi = math.pi
mu = 4 * pi * (10 ** -7)

def calculate_net_magnetic_field(r1, r2, n1, n2, i1, i2):
    r1 = r1 * (10 ** -2)
    r2 = r2 * (10 ** -2)
    b1 = (mu * n1 * i1) / (2 * r1)
    b2 = (mu * n2 * i2) / (2 * r2)
    if b1 > b2:
        return b1 - b2, "east"
    return b2 - b1, "west"

def generate_question_type1(r1, r2, n1, n2, i1, i2):
    q = f"Two circular coils X and Y of radii {r1} cm and {r2} cm, respectively, lie in the same vertical plane containing the north to south direction. Coil A has {n1} turns and carries a current of {i1} A, Coil B has {n2} turns and carries a current of {i2} A. The sense of current in X is anti-clockwise direction and in Y is clockwise direction. From an observer looking at the coils facing west, give the magnitude and direction of the net magnetic field due to the coils at the center."
    b, direction = calculate_net_magnetic_field(r1, r2, n1, n2, i1, i2)
    a = f"{b:.2e} tesla and towards {direction}"
    return q, a

def generate_question_type2(r1, r2, n1, n2, i1, i2):
    q = f"Two circular coils X and Y of radii {r1} cm and {r2} cm, respectively, lie in the same vertical plane containing the north to south direction. Coil A has {n1} turns and carries a current of {i1} A, Coil B has {n2} turns and carries a current of {i2} A. The sense of current in X is anti-clockwise direction and in Y is clockwise direction. From an observer looking at the coils facing east, give the magnitude and direction of the net magnetic field due to the coils at the center."
    b, direction = calculate_net_magnetic_field(r1, r2, n1, n2, i1, i2)
    a = f"{b:.2e} tesla and towards {direction}"
    return q, a

samples = []

for i in range(no_of_samples):
    r1 = random.randint(10, 40)
    r2 = random.randint(10, 40)
    n1 = random.randint(1, 20)
    n2 = random.randint(1, 20)
    i1 = random.randint(10, 40)
    i2 = random.randint(10, 40)

    types = random.randint(1, 2)

    if types == 1:
        question, answer = generate_question_type1(r1, r2, n1, n2, i1, i2)
    elif types == 2:
        question, answer = generate_question_type2(r1, r2, n1, n2, i1, i2)

    input_formula = "Net magnetic field = |b1 - b2|"
    output = f"To calculate the net magnetic field, we use the following formula:\n\n{input_formula}\n\nWhere,\n- b1 = Magnetic field due to coil X\n- b2 = Magnetic field due to coil Y\n\nWe calculate the magnetic field for each coil using the formula:\n- Magnetic field due to coil X = (mu * n1 * i1) / (2 * r1)\n- Magnetic field due to coil Y = (mu * n2 * i2) / (2 * r2)\n\nSubstituting the given values and evaluating the formula, we find that the magnitude of the net magnetic field is approximately {answer}."

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

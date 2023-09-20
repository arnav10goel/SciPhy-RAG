import random
import json
import math

pi = math.pi
mu = 4 * pi * (10 ** -7)

no_of_samples = 70

def calculate_force(i1, i2, r, l):
    r = r * (10 ** -2)
    l = l * (10 ** -2)
    return (mu * i1 * i2 * l) / (2 * pi * r)

def generate_question_type1(i1, i2, r, l, t):
    if t == 1:
        q = f"Two long and parallel straight wires A and B carrying currents of {i1} A and {i2} A in the same direction are separated by a distance {r} cm. Estimate the force and its nature on the {l} cm section of wire A."
    elif t == 2:
        q = f"Two long and parallel straight wires A and B carrying currents of {i1} A and {i2} A in the same direction are separated by a distance {r} cm. Estimate the force and its nature on the {l} cm section of wire B."
    elif t == 3:
        q = f"Two long and parallel straight wires A and B carrying currents of {i1} A and {i2} A in the same direction are separated by a distance {r} cm. Estimate the force and its nature on the {l} cm section of wire A. (mu = 4 x pi x 10^(-7) TmA^-1)"
    else:
        q = f"Two long and parallel straight wires A and B carrying currents of {i1} A and {i2} A in the same direction are separated by a distance {r} cm. Estimate the force and its nature on the {l} cm section of wire B. (mu = 4 x pi x 10^(-7) TmA^-1)"
    a = "{:.2e}".format(calculate_force(i1, i2, r, l)) + " newtons and attractive"
    return q, a

def generate_question_type2(i1, i2, r, l, t):
    if t == 1:
        q = f"Two long and parallel straight wires A and B carrying currents of {i1} A and {i2} A in the opposite direction are separated by a distance {r} cm. Estimate the force and its nature on the {l} cm section of wire A."
    elif t == 2:
        q = f"Two long and parallel straight wires A and B carrying currents of {i1} A and {i2} A in the opposite direction are separated by a distance {r} cm. Estimate the force and its nature on the {l} cm section of wire B."
    elif t == 3:
        q = f"Two long and parallel straight wires A and B carrying currents of {i1} A and {i2} A in the opposite direction are separated by a distance {r} cm. Estimate the force and its nature on the {l} cm section of wire A. (mu = 4 x pi x 10^(-7) TmA^-1)"
    else:
        q = f"Two long and parallel straight wires A and B carrying currents of {i1} A and {i2} A in the opposite direction are separated by a distance {r} cm. Estimate the force and its nature on the {l} cm section of wire B. (mu = 4 x pi x 10^(-7) TmA^-1)"
    a = "{:.2e}".format(calculate_force(i1, i2, r, l)) + " newtons and repulsive"
    return q, a

samples = []

for i in range(no_of_samples):
    types = random.randint(1, 2)
    r = random.randint(1, 100)
    i1 = random.randint(1, 50)
    i2 = random.randint(1, 50)
    l = random.randint(1, 50)
    t = random.randint(1, 4)

    if types == 1:
        question, answer = generate_question_type1(i1, i2, r, l, t)
    else:
        question, answer = generate_question_type2(i1, i2, r, l, t)

    input_formula = f"Force = (mu * i1 * i2 * l) / (2 * pi * r)"
    output = f"To calculate the force and its nature, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values:\n- mu = 4 * pi * 10^(-7) TmA^-1\n- i1 = {i1} A\n- i2 = {i2} A\n- r = {r} cm\n- l = {l} cm\n\nAfter evaluating the formula, we find that the force on the {l} cm section of wire is approximately {answer}."

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

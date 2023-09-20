import random
import json
import math

no_of_samples = 30

pi = math.pi
mu = 4 * pi * (10 ** -7)

def calculate_magnetic_field(n, r1, r2, i):
    r1 = r1 * (10 ** -2)
    r2 = r2 * (10 ** -2)
    l = (r1 + r2) * math.pi
    return (mu * n * i) / l

def generate_question(n, r1, r2, i):
    q = f"A toroid has a core of inner radius {r1} cm and outer radius {r2} cm, around which {n} turns of a wire are wound. If the current in the wire is {i} A, what is the magnetic field inside the core of the solenoid."
    b = calculate_magnetic_field(n, r1, r2, i)
    a = f"{b:.2e} tesla"
    return q, a

samples = []

for i in range(no_of_samples):
    n = random.randint(100, 300)
    i = random.randint(1, 50)
    r1 = random.randint(50, 150)
    r2 = random.randint(r1 + 1, r1 + 50)

    question, answer = generate_question(n, r1, r2, i)

    input_formula = "Magnetic field = (mu * n * i) / l"
    output = f"To calculate the magnetic field inside the toroid, we use the following formula:\n\n{input_formula}\n\nWhere,\n- n = Number of turns of the wire\n- i = Current in the wire\n- l = Length of the wire\n\nWe calculate the length of the wire using the formula:\n- Length of the wire = (r1 + r2) * pi\n\nSubstituting the given values and evaluating the formula, we find that the magnetic field inside the core of the toroid is approximately {answer}."

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


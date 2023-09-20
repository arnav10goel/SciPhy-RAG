import random
import json
import math

no_of_samples = 30

pi = math.pi
mu = 4 * pi * (10 ** -7)

def calculate_magnetic_field(k, n, l, i):
    l = l * (10 ** -2)
    return (mu * n * i) / l

def generate_question_type1(k, n, l, i):
    q = f"A closely wounded solenoid {l} cm long has {k} layers of windings of {n} turns each. The diameter of the solenoid is d cm. If the current carried is {i} A, estimate the magnitude of the magnetic field inside the solenoid near its center."
    b = calculate_magnetic_field(k, n, l, i)
    a = f"{b:.2e} tesla"
    return q, a

samples = []

for i in range(no_of_samples):
    n = random.randint(1, 10) * 50
    i = random.randint(1, 50)
    k = random.randint(1, 10)
    d = random.randint(1, 100)
    l = random.randint(10, 1000)

    types = random.randint(1, 2)

    
    question, answer = generate_question_type1(k, n, l, i)

    input_formula = "B = (mu * n * i) / l"
    output = f"To estimate the magnitude of the magnetic field inside the solenoid near its center, we use the following formula:\n\n{input_formula}\n\nWhere,\n- B = Magnetic field inside the solenoid near its center\n- mu = Permeability of free space (4 * pi * 10^(-7) T*m/A)\n- n = Number of turns per layer\n- i = Current flowing through the solenoid\n- l = Length of the solenoid\n\nSubstituting the given values into the formula, we find that the magnitude of the magnetic field inside the solenoid near its center is approximately {answer}."

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

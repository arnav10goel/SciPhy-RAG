import random
import json
import math

no_of_samples = 20

m = 9.1 * (10**-31)
e = 1.6 * (10**-19)
pi = math.pi

def calculate_frequency_of_revolution(b, v, d):
    return (b * e) / (2 * pi * m)

def generate_question_type1(b, v, d):
    q = f"In a chamber, a uniform magnetic field of {b} T is maintained. An electron is shot into the field with a speed of {v} m/s, making an angle of {d} degrees with the field. Determine the frequency of the revolution of the electron."
    a = f"{calculate_frequency_of_revolution(b, v, d):.2e} sec^-1"
    return q, a

samples = []

for i in range(no_of_samples):
    b = random.randint(1, 120) * 10**-4
    v = random.randint(1, 120) * 10**6
    d = random.randint(1, 90)

    types = random.randint(1, 1)

    if types == 1:
        question, answer = generate_question_type1(b, v, d)

    input_formula = "Frequency of revolution = (b * e) / (2 * pi * m)"
    output = f"To calculate the frequency of revolution, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values:\n- b = {b} T\n- e = {e} C\n- m = {m} kg\n\nAfter evaluating the formula, we find that the frequency of revolution is approximately {answer}."

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

import random
import json
import math

no_of_samples = 30

pi = math.pi

def generate_question1(b, m):
    return f"A short bar magnet of magnetic moment {m} J/T is placed in a uniform magnetic field of {b} T. If the magnet is free to rotate in the plane of the field, what is the potential energy of the magnet at stable position?"

def generate_question2(b, m):
    return f"A short bar magnet of magnetic moment {m} J/T is placed in a uniform magnetic field of {b} T. If the magnet is free to rotate in the plane of the field, what is the potential energy of the magnet at unstable position?"

def generate_question3(b, m, d):
    return f"A short bar magnet of magnetic moment {m} J/T is placed in a uniform magnetic field of {b} T. If the magnet is free to rotate in the plane of the field, what is the potential energy of the magnet at a position making an angle of {d} degrees with the magnetic field?"

def generate_input_formula1(b, m):
    return f"-m * b"

def generate_input_formula2(b, m):
    return f"m * b"

def generate_input_formula3(b, m, d):
    d = math.cos((d * pi) / 180)
    return f"-m * b * {d:.2f}"

def generate_output_explanation1(b, m):
    return f"The potential energy of the magnet at a stable position can be calculated using the formula -m * b, where 'm' is the magnetic moment of the bar magnet and 'b' is the magnetic field strength. Substituting the given values, we have -({m}) * {b} = {(-m * b):.2e} joule."

def generate_output_explanation2(b, m):
    return f"The potential energy of the magnet at an unstable position can be calculated using the formula m * b, where 'm' is the magnetic moment of the bar magnet and 'b' is the magnetic field strength. Substituting the given values, we have {m} * {b} = {(m * b):.2e} joule."

def generate_output_explanation3(b, m, d):
    d = math.cos((d * pi) / 180)
    return f"The potential energy of the magnet at a position making an angle of {d} degrees with the magnetic field can be calculated using the formula -m * b * cos(d), where 'm' is the magnetic moment of the bar magnet, 'b' is the magnetic field strength, and 'd' is the angle. Substituting the given values, we have -({m}) * {b} * {d:.2f} = {(-m * b * d):.2e} joule."

samples = []

for i in range(no_of_samples):
    sample = {}
    b = round(random.randint(1, 2000) * 0.01, 2)
    m = round(random.randint(1, 2000) * 0.01, 2)
    d = random.randint(1, 179)

    if random.randint(1, 3) == 1:
        question = generate_question1(b, m)
        input_formula = generate_input_formula1(b, m)
        output_explanation = generate_output_explanation1(b, m)
    elif random.randint(1, 3) == 2:
        question = generate_question2(b, m)
        input_formula = generate_input_formula2(b, m)
        output_explanation = generate_output_explanation2(b, m)
    else:
        question = generate_question3(b, m, d)
        input_formula = generate_input_formula3(b, m, d)
        output_explanation = generate_output_explanation3(b, m, d)

    sample["instruction"] = question
    sample["input"] = input_formula
    sample["output"] = output_explanation

    samples.append(sample)

# Read the existing JSON file
with open("science/MagnetismAndMatter/mam.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/MagnetismAndMatter/mam.json", "w") as file:
    json.dump(existing_data, file, indent=4)
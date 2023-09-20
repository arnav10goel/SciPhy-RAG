import random
import json
import math

no_of_samples = 20

pi = math.pi

def generate_question1(b, m, d1, d2):
    return f"A bar magnet of magnetic moment {m} J/T is kept in a uniform magnetic field of {b} T. What is the work done by an external torque to turn the magnet which is aligned at an angle of {d1} degrees with the magnetic field to an angle of {d2} degrees?"

def generate_question2(b, m, d1, d2):
    return f"A solenoid of magnetic moment {m} J/T is kept in a uniform magnetic field of {b} T. What is the work done by an external torque to turn the magnet which is aligned at an angle of {d1} degrees with the magnetic field to an angle of {d2} degrees?"

def generate_input_formula(b, m, d1, d2):
    d1 = math.cos((d1 * pi) / 180)
    d2 = math.cos((d2 * pi) / 180)
    return f"-m * b * (d1 - d2)"

def generate_output_explanation(b, m, d1, d2):
    d1 = math.cos((d1 * pi) / 180)
    d2 = math.cos((d2 * pi) / 180)
    return f"The work done by an external torque to turn the magnet aligned at an angle of {d1} degrees with the magnetic field to an angle of {d2} degrees can be calculated using the formula -m * b * (d1 - d2), where 'm' is the magnetic moment of the magnet, 'b' is the magnetic field strength, 'd1' is the initial angle, and 'd2' is the final angle. Substituting the given values, we have -({m}) * {b} * ({d1:.2f} - {d2:.2f})."

samples = []

for i in range(no_of_samples):
    sample = {}
    b = round(random.randint(1, 100) * 0.01, 2)
    m = round(random.randint(1, 200) * 0.01, 2)
    d1 = random.randint(1, 150)
    d2 = random.randint(d1 + 1, 180)
    if random.randint(1, 2) == 1:
        question = generate_question1(b, m, d1, d2)
        input_formula = generate_input_formula(b, m, d1, d2)
        output_explanation = generate_output_explanation(b, m, d1, d2)
    else:
        question = generate_question2(b, m, d1, d2)
        input_formula = generate_input_formula(b, m, d1, d2)
        output_explanation = generate_output_explanation(b, m, d1, d2)

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
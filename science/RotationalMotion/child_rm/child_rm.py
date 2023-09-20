import random
import json

no_of_samples = 30
def calculate_angular_speed(n1, n2, w):
    return round((n2 * w) / n1, 1)

def calculate_kinetic_energy_ratio(n1, n2):
    return round((n2 ** 3) / (n1 ** 3), 1)

def generate_question_type1(n1, n2, w):
    q = f"A child stands at the centre of a turntable with his arms outstretched. The turntable is rotating with an angular speed of {w} rad/s. How much is the angular speed of the child if he folds his hands back and thereby reduces his moment of inertia to {n1}/{n2} times the initial value?"
    angular_speed = calculate_angular_speed(n1, n2, w)
    a = f"{angular_speed} rad/s"
    return q, a

def generate_question_type2(n1, n2, w):
    q = f"A child stands at the centre of a turntable with his arms outstretched. The turntable is rotating with an angular speed of {w} rad/s. How many times is the kinetic energy of the rotation increased if he folds his hands back and thereby reduces his moment of inertia to {n1}/{n2} times the initial value?"
    kinetic_energy_ratio = calculate_kinetic_energy_ratio(n1, n2)
    a = f"{kinetic_energy_ratio}"
    return q, a

samples = []

for i in range(no_of_samples):
    types = random.randint(1, 2)
    n1 = random.randint(1, 100)
    n2 = random.randint(n1 + 1, n1 + 100)
    w = random.randint(1, 200)

    if types == 1:
        question, angular_speed = generate_question_type1(n1, n2, w)
        output = f"To calculate the angular speed and kinetic energy ratio, we use the following formulas:\n\nAngular Speed = (n2 * w) / n1\nKinetic Energy Ratio = (n2^3) / (n1^3)\n\nWhere,\n- n1 = Initial moment of inertia\n- n2 = Reduced moment of inertia\n- w = Initial angular speed\n\nSubstituting the given values into the formulas, we find that the angular speed of the child is approximately {angular_speed} rad/s."
    else:
        question, kinetic_energy_ratio = generate_question_type2(n1, n2, w)
        output = f"To calculate the angular speed and kinetic energy ratio, we use the following formulas:\n\nAngular Speed = (n2 * w) / n1\nKinetic Energy Ratio = (n2^3) / (n1^3)\n\nWhere,\n- n1 = Initial moment of inertia\n- n2 = Reduced moment of inertia\n- w = Initial angular speed\n\nSubstituting the given values into the formulas, we find that the kinetic energy of the rotation is increased by approximately {kinetic_energy_ratio} times."

    input_formula = "Angular Speed = (n2 * w) / n1\nKinetic Energy Ratio = (n2^3) / (n1^3)"
    

    sample = {
        "instruction": question,
        "input": input_formula,
        "output": output
    }

    samples.append(sample)

# Load existing JSON file
with open("science/RotationalMotion/rom.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/RotationalMotion/rom.json", "w") as file:
    json.dump(existing_data, file, indent=4)

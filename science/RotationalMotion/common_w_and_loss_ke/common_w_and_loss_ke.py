import random
import json

no_of_samples = 30

def calculate_angular_speed(i1, i2, w1, w2):
    return round(((i1 * w1) + (i2 * w2)) / (i1 + i2), 1)

def calculate_loss_in_kinetic_energy(i1, i2, w1, w2):
    w = ((i1 * w1) + (i2 * w2)) / (i1 + i2)
    k = 0.5 * (i1 + i2) * w * w
    k1 = 0.5 * i1 * w1 * w1
    k2 = 0.5 * i2 * w2 * w2
    return round(k1 + k2 - k, 1)

def generate_question_type1(i1, i2, w1, w2):
    q = f"Two discs of moments of inertia {i1} and {i2} about their respective axes, and rotating with angular speed {w1} rad/s and {w2} rad/s are brought into contact face to face with their axes of rotation coincident. What is the angular speed of the two-disc system?"
    angular_speed = calculate_angular_speed(i1, i2, w1, w2)
    a = f"{angular_speed} rad/s"
    return q, a

def generate_question_type2(i1, i2, w1, w2):
    q = f"Two discs of moments of inertia {i1} and {i2} about their respective axes, and rotating with angular speed {w1} rad/s and {w2} rad/s are brought into contact face to face with their axes of rotation coincident. What is the loss in kinetic energy of the two-disc system?"
    loss_in_kinetic_energy = calculate_loss_in_kinetic_energy(i1, i2, w1, w2)
    a = f"{loss_in_kinetic_energy} joules"
    return q, a

samples = []

for i in range(no_of_samples):
    types = random.randint(1, 2)
    i1 = random.randint(1, 100)
    i2 = random.randint(1, 100)
    w1 = random.randint(1, 100)
    w2 = random.randint(1, 100)

    if types == 1:
        question, answer = generate_question_type1(i1, i2, w1, w2)
        output = f"To calculate the angular speed and loss in kinetic energy, we use the following formulas:\n\nAngular Speed = ((i1 * w1) + (i2 * w2)) / (i1 + i2)\nLoss in Kinetic Energy = k1 + k2 - k\n\nWhere,\n- i1 = Moment of inertia of the first disc\n- i2 = Moment of inertia of the second disc\n- w1 = Angular speed of the first disc\n- w2 = Angular speed of the second disc\n\nSubstituting the given values into the formulas, we find that the angular speed of the two-disc system is approximately {answer} rad/s"

    else:
        question, answer = generate_question_type2(i1, i2, w1, w2)
        output = f"To calculate the angular speed and loss in kinetic energy, we use the following formulas:\n\nAngular Speed = ((i1 * w1) + (i2 * w2)) / (i1 + i2)\nLoss in Kinetic Energy = k1 + k2 - k\n\nWhere,\n- i1 = Moment of inertia of the first disc\n- i2 = Moment of inertia of the second disc\n- w1 = Angular speed of the first disc\n- w2 = Angular speed of the second disc\n\nSubstituting the given values into the formulas, we find that the loss in kinetic energy is approximately {answer} joules."


    input_formula = "Angular Speed = ((i1 * w1) + (i2 * w2)) / (i1 + i2)\nLoss in Kinetic Energy = k1 + k2 - k\n\nk1 = 0.5 * i1 * w1^2\nk2 = 0.5 * i2 * w2^2\nk = 0.5 * (i1 + i2) * w^2"

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


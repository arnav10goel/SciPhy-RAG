import random
import math
import json

no_of_samples = 50

def calculate_angular_position(w1, w2, a):
    return round(((w2 ** 2 - w1 ** 2) / (2 * a)), 1)

def calculate_initial_angular_velocity(w2, r, a):
    return round(math.sqrt((w2 ** 2) - (2 * a * r)), 1)

def calculate_final_angular_velocity(w1, r, a):
    return round(math.sqrt((w1 ** 2) + (2 * a * r)), 1)

def calculate_angular_acceleration(w1, w2, r):
    return round((((w2 ** 2) - (w1 ** 2)) / (2 * r)), 1)

def generate_question_type1(w1, w2, a):
    r = calculate_angular_position(w1, w2, a)
    question = f"A wheel starting with an initial angular velocity of {w1} rad/s accelerates with a constant angular acceleration of {a} rad/s² and reaches a velocity of {w2} m/s. What is its angular position?"
    input_formula = "angular_position = ((final_angular_velocity^2 - initial_angular_velocity^2) / (2 * angular_acceleration))"
    output = f"To calculate the angular position, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the angular position is approximately {r} rad."
    return question, input_formula, output

def generate_question_type2(a, r):
    w2 = random.randint(int(2 * a * r), int(2 * a * r) + 100)
    w1 = calculate_initial_angular_velocity(w2, r, a)
    question = f"A wheel, when applied with a constant angular acceleration of {a} rad/s², reaches a velocity of {w2} rad/s when the angular position is {r} rad. What is its initial angular velocity?"
    input_formula = "initial_angular_velocity = sqrt(final_angular_velocity^2 - (2 * angular_acceleration * angular_position))"
    output = f"To calculate the initial angular velocity, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the initial angular velocity is approximately {w1} rad/s."
    return question, input_formula, output

def generate_question_type3(w1, r, a):
    w2 = calculate_final_angular_velocity(w1, r, a)
    question = f"A wheel starting with an initial angular velocity of {w1} rad/s accelerates with a constant angular acceleration of {a} rad/s². If it reaches an angular position of {r} rad, then what is its final velocity?"
    input_formula = "final_angular_velocity = sqrt(initial_angular_velocity^2 + (2 * angular_acceleration * angular_position))"
    output = f"To calculate the final angular velocity, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the final angular velocity is approximately {w2} rad/s."
    return question, input_formula, output

def generate_question_type4(w1, w2, r):
    a = calculate_angular_acceleration(w1, w2, r)
    question = f"A wheel starting with an initial angular velocity of {w1} rad/s accelerates and reaches a final velocity of {w2} rad/s when the angular position is {r} rad. What is its angular acceleration?"
    input_formula = "angular_acceleration = ((final_angular_velocity^2 - initial_angular_velocity^2) / (2 * angular_position))"
    output = f"To calculate the angular acceleration, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the angular acceleration is approximately {a} rad/s²."
    return question, input_formula, output

samples = []

for i in range(no_of_samples):
    types = random.randint(0, 3)

    if types == 0:
        w1 = random.randint(1, 100)
        w2 = random.randint(w1, w1 + 100)
        a = random.randint(1, 100)
        question, input_formula, output = generate_question_type1(w1, w2, a)

    elif types == 1:
        a = random.randint(1, 100)
        r = random.randint(1, 100)
        question, input_formula, output = generate_question_type2(a, r)

    elif types == 2:
        w1 = random.randint(1, 100)
        r = random.randint(1, 100)
        a = random.randint(1, 100)
        question, input_formula, output = generate_question_type3(w1, r, a)

    else:
        w1 = random.randint(1, 100)
        w2 = random.randint(w1, w1 + 100)
        r = random.randint(1, 100)
        question, input_formula, output = generate_question_type4(w1, w2, r)

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


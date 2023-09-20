import random
import math
import json

no_of_samples = 50

def calculate_angular_position(w1, a, t):
    return round((w1 * t) + (0.5 * a * t * t), 1)

def calculate_initial_angular_velocity(r, a, t):
    return round((r - (0.5 * a * t * t)) / t, 1)

def calculate_angular_acceleration(r, w1, t):
    return round((2 * (r - w1 * t)) / (t * t), 1)

def calculate_time(r, w1, a):
    temp = (4 * w1 * w1) + (8 * a * r)
    return round((-(2 * w1) + math.sqrt(temp)) / (2 * a), 1)

def generate_question_type1(w1, a, t):
    r = calculate_angular_position(w1, a, t)
    question = f"A wheel starting with an initial angular velocity of {w1} rad/s is applied with a constant angular acceleration of {a} rad/s². What is the angular position after {t} seconds?"
    input_formula = "angular_position = (initial_angular_velocity * time) + (0.5 * angular_acceleration * time^2)"
    output = f"To calculate the angular position, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the angular position is approximately {r} rad."
    return question, input_formula, output

def generate_question_type2(a, t):
    tp = int(0.5 * a * t * t)
    r = random.randint(tp, tp + 1000)
    w1 = calculate_initial_angular_velocity(r, a, t)
    question = f"A wheel reaches an angular position of {r} rad when applied with a constant angular acceleration of {a} rad/s² for {t} seconds. What is its initial angular velocity?"
    input_formula = "initial_angular_velocity = (angular_position - (0.5 * angular_acceleration * time^2)) / time"
    output = f"To calculate the initial angular velocity, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the initial angular velocity is approximately {w1} rad/s."
    return question, input_formula, output

def generate_question_type3(w1, t):
    tp = w1 * t
    r = random.randint(tp + 10, tp + 1010)
    a = calculate_angular_acceleration(r, w1, t)
    question = f"A wheel starting with an initial angular velocity of {w1} rad/s reaches an angular position of {r} rad after {t} seconds by the application of constant angular acceleration. What is the angular acceleration applied?"
    input_formula = "angular_acceleration = (2 * (angular_position - (initial_angular_velocity * time))) / (time^2)"
    output = f"To calculate the angular acceleration, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the angular acceleration is approximately {a} rad/s²."
    return question, input_formula, output

def generate_question_type4(w1, a):
    r = random.randint(1, 1000)
    t = calculate_time(r, w1, a)
    question = f"A wheel starting with an initial angular velocity of {w1} rad/s is applied with a constant angular acceleration of {a} rad/s². What is the time taken to reach an angular position of {r} rad?"
    input_formula = "time = (-(2 * initial_angular_velocity) + sqrt((4 * initial_angular_velocity^2) + (8 * angular_acceleration * angular_position))) / (2 * angular_acceleration)"
    output = f"To calculate the time, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the time is approximately {t} seconds."
    return question, input_formula, output

samples = []

for i in range(no_of_samples):
    types = random.randint(0, 3)

    if types == 0:
        w1 = random.randint(1, 1000)
        a = random.randint(1, 100)
        t = random.randint(1, 10)
        question, input_formula, output = generate_question_type1(w1, a, t)

    elif types == 1:
        a = random.randint(1, 100)
        t = random.randint(1, 10)
        question, input_formula, output = generate_question_type2(a, t)

    elif types == 2:
        w1 = random.randint(1, 100)
        t = random.randint(1, 10)
        question, input_formula, output = generate_question_type3(w1, t)

    else:
        w1 = random.randint(1, 100)
        a = random.randint(1, 10)
        question, input_formula, output = generate_question_type4(w1, a)

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

import random
import json

no_of_samples = 40

def calculate_angular_acceleration(w1, w2, t):
    return round((w2 - w1) / t, 1)

def calculate_initial_angular_velocity(w, a, t):
    return round(w - (a * t), 1)

def calculate_final_angular_velocity(w1, a, t):
    return round(w1 + (a * t), 1)

def calculate_time(w1, w2, a):
    return round((w2 - w1) / a, 1)

def generate_question_type1(w1, w2, t):
    a = calculate_angular_acceleration(w1, w2, t)
    question = f"At t = 0, a wheel is rotating with an angular velocity of {w1} rad/s at a constant angular acceleration. It attains an angular velocity of {w2} rad/s in t = {t} sec. What is the value of the angular acceleration?"
    input_formula = "angular_acceleration = (final_angular_velocity - initial_angular_velocity) / time"
    output = f"To calculate the angular acceleration, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the angular acceleration is approximately {a} rad/s²."
    return question, input_formula, output

def generate_question_type2(w, a, t):
    w1 = calculate_initial_angular_velocity(w, a, t)
    question = f"At t = 0, a wheel is rotating with an angular velocity of w rad/s at a constant angular acceleration of {a} rad/s². It attains an angular velocity of {w} rad/s in t = {t} sec. What is the value of the initial angular velocity?"
    input_formula = "initial_angular_velocity = final_angular_velocity - (angular_acceleration * time)"
    output = f"To calculate the initial angular velocity, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the initial angular velocity is approximately {w1} rad/s."
    return question, input_formula, output

def generate_question_type3(w1, a, t):
    w2 = calculate_final_angular_velocity(w1, a, t)
    question = f"At t = 0, a wheel is rotating with an angular velocity of {w1} rad/s at a constant angular acceleration of {a} rad/s². It attains an angular velocity of w rad/s in t = {t} sec. What is the value of the final angular velocity?"
    input_formula = "final_angular_velocity = initial_angular_velocity + (angular_acceleration * time)"
    output = f"To calculate the final angular velocity, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the final angular velocity is approximately {w2} rad/s."
    return question, input_formula, output

def generate_question_type4(w1, w2, a):
    t = calculate_time(w1, w2, a)
    question = f"At t = 0, a wheel is rotating with an angular velocity of {w1} rad/s at a constant angular acceleration of {a} rad/s². It attains an angular velocity of {w2} rad/s. What is the value of t in seconds?"
    input_formula = "time = (final_angular_velocity - initial_angular_velocity) / angular_acceleration"
    output = f"To calculate the time, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the time is approximately {t} seconds."
    return question, input_formula, output

samples = []

for i in range(no_of_samples):
    types = random.randint(1, 4)

    if types == 1:
        w1 = random.randint(0, 500)
        w2 = random.randint(w1, w1 + 500)
        t = random.randint(1, 20)
        question, input_formula, output = generate_question_type1(w1, w2, t)

    elif types == 2:
        w = random.randint(0, 1000)
        a = random.randint(0, 40)
        t = random.randint(1, 40)
        question, input_formula, output = generate_question_type2(w, a, t)

    elif types == 3:
        w1 = random.randint(0, 1000)
        a = random.randint(0, 40)
        t = random.randint(1, 40)
        question, input_formula, output = generate_question_type3(w1, a, t)

    else:
        w1 = random.randint(0, 500)
        w2 = random.randint(w1, w1 + 500)
        a = random.randint(1, 20)
        question, input_formula, output = generate_question_type4(w1, w2, a)

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

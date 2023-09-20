import random
import json

no_of_samples = 60

def calculate_distance_from_center(s, r):
    return round(s / r, 1)

def calculate_velocity_at_circumference(w, r):
    return round(w * r, 1)

def calculate_radius_from_velocity(v, w):
    return round(v / w, 1)

def calculate_acceleration_at_circumference(aa, r):
    return round(aa * r, 1)

def calculate_radius_from_acceleration(a, aa):
    return round(a / aa, 1)

def generate_question_type1(s, r):
    distance = calculate_distance_from_center(s, r)
    question = f"A girl sitting on a merry-go-round is moving in a counter-clockwise arc length of {s} m. If the angular displacement is {r} rad, how far is she from the center of the merry-go-round?"
    input_formula = "distance_from_center = arc_length / radius"
    output = f"To calculate the distance from the center, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the distance from the center is approximately {distance} m."
    return question, input_formula, output

def generate_question_type2(r, w):
    velocity = calculate_velocity_at_circumference(w, r)
    question = f"If a wheel of radius {r} m has an angular velocity of {w} rad/s, what is the velocity of a point at the circumference of the wheel?"
    input_formula = "velocity_at_circumference = angular_velocity * radius"
    output = f"To calculate the velocity at the circumference, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the velocity at the circumference is approximately {velocity} m/s."
    return question, input_formula, output

def generate_question_type3(r, aa):
    acceleration = calculate_acceleration_at_circumference(aa, r)
    question = f"If a wheel of radius {r} m has an angular acceleration of {aa} rad/s², what is the acceleration of a point at the circumference of the wheel?"
    input_formula = "acceleration_at_circumference = angular_acceleration * radius"
    output = f"To calculate the acceleration at the circumference, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the acceleration at the circumference is approximately {acceleration} m/s²."
    return question, input_formula, output

def generate_question_type4(v, w):
    radius = calculate_radius_from_velocity(v, w)
    question = f"If a point on the circumference of a wheel rotating with an angular velocity of {w} rad/s has a velocity of {v} m/s, what is the radius of the wheel?"
    input_formula = "radius = velocity / angular_velocity"
    output = f"To calculate the radius, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the radius is approximately {radius} m."
    return question, input_formula, output

def generate_question_type5(a, aa):
    radius = calculate_radius_from_acceleration(a, aa)
    question = f"If a point on the circumference of a wheel rotating with an angular acceleration of {aa} rad/s² has an acceleration of {a} m/s², what is the radius of the wheel?"
    input_formula = "radius = acceleration / angular_acceleration"
    output = f"To calculate the radius, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the radius is approximately {radius} m."
    return question, input_formula, output

samples = []

for i in range(no_of_samples):
    types = random.randint(0, 4)

    if types == 0:
        s = random.randint(1, 1000)
        r = random.randint(1, 1000)
        question, input_formula, output = generate_question_type1(s, r)

    elif types == 1:
        r = random.randint(1, 1000)
        w = random.randint(1, 1000)
        question, input_formula, output = generate_question_type2(r, w)

    elif types == 2:
        r = random.randint(1, 1000)
        aa = random.randint(1, 1000)
        question, input_formula, output = generate_question_type3(r, aa)

    elif types == 3:
        v = random.randint(1, 1000)
        w = random.randint(1, 1000)
        question, input_formula, output = generate_question_type4(v, w)

    else:
        a = random.randint(1, 1000)
        aa = random.randint(1, 1000)
        question, input_formula, output = generate_question_type5(a, aa)

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

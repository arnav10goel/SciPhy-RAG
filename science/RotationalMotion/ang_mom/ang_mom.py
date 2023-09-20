import random
import json

no_of_samples = 80
con = [1 / 2, 2 / 5, 2 / 3, 1 / 3]

def calculate_angular_momentum(c, m, r, w):
    return round(c * m * r * r * w, 1)

def generate_question_type1(m, r, w, t):
    if t == 0:
        q = f"A solid cylinder of mass {m} kg rotates about its axis with angular speed {w} rad/s. The radius of the cylinder is {r} m. What is the magnitude of angular momentum of the cylinder about its axis?"
        a = f"{calculate_angular_momentum(con[0], m, r, w)} kg·m²"
    elif t == 1:
        q = f"A solid sphere of mass {m} kg rotates about its axis with angular speed {w} rad/s. The radius of the sphere is {r} m. What is the magnitude of angular momentum of the sphere about its axis?"
        a = f"{calculate_angular_momentum(con[1], m, r, w)} kg·m²"
    elif t == 2:
        q = f"A hollow sphere of mass {m} kg rotates about its axis with angular speed {w} rad/s. The radius of the sphere is {r} m. What is the magnitude of angular momentum of the sphere about its axis?"
        a = f"{calculate_angular_momentum(con[2], m, r, w)} kg·m²"
    elif t == 3:
        q = f"A rod of mass {m} kg rotates about its end with angular speed {w} rad/s. The length of the rod is {r} m. What is the magnitude of angular momentum of the rod about its end?"
        a = f"{calculate_angular_momentum(con[3], m, r, w)} kg·m²"
    return q, a

samples = []

for i in range(no_of_samples):
    m = random.randint(1, 1000)
    r = random.randint(1, 40)
    w = random.randint(1, 40)
    t = random.randint(0, 3)

    question, answer = generate_question_type1(m, r, w, t)

    input_formula = "Angular Momentum = c * m * r² * w"
    output = f"To calculate the magnitude of the angular momentum, we use the following formula:\n\n{input_formula}\n\nWhere,\n- c = Constant for the object\n- m = Mass of the object\n- r = Radius or length of the object\n- w = Angular speed of the object\n\nThe value of the constant (c) depends on the type of object being considered:\n- For a solid cylinder: c = 1/2\n- For a solid sphere: c = 2/5\n- For a hollow sphere: c = 2/3\n- For a rod: c = 1/3\n\nSubstituting the given values into the formula, we find that the magnitude of the angular momentum is approximately {answer}."

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

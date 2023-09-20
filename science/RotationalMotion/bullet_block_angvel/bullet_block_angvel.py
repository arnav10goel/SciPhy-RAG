import random
import json

no_of_samples = 20

def calculate_angular_speed(m1, m2, v1, l):
    am = (m1 * v1 * l) / (1000 * 2)
    i = (m2 * l * l) / 3
    return round(am / i, 1)

def generate_question_type1(m1, m2, v1, l):
    q = f"A bullet of mass {m1} g and speed {v1} m/s is fired into a door and gets embedded at the center of the door. The door is {l} m wide and weighs {m2} kg. It is hinged at one end and rotates about a vertical axis. Find the angular speed of the door just after the bullet embeds into it."
    a = f"{calculate_angular_speed(m1, m2, v1, l)} rad/s"
    return q, a

samples = []

for i in range(no_of_samples):
    m1 = random.randint(1, 500)
    m2 = random.randint(1, 100)
    l = random.randint(1, 100)
    v1 = random.randint(1000, 1500)

    question, answer = generate_question_type1(m1, m2, v1, l)

    input_formula = "Angular Speed = (m1 * v1 * l) / (1000 * 2 * I)"
    output = f"To calculate the angular speed of the door, we use the following formula:\n\n{input_formula}\n\nWhere,\n- m1 = Mass of the bullet\n- v1 = Speed of the bullet\n- l = Width of the door\n- I = Moment of inertia of the door\n\nThe moment of inertia of the door can be calculated as I = (m2 * l²) / 3, where m2 is the mass of the door.\n\nSubstituting the given values into the formula, we find that the angular speed of the door is approximately {answer}."

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

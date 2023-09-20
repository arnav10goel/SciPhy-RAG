import random
import math
import json

no_of_samples = 30
g = 9.8

def calculation_h(u):
    return round(((u ** 2) / (2 * g)), 1)

def calculation_u(h):
    return round(math.sqrt(2 * g * h), 1)

data = []

def generate_type1():
    u = random.randint(1, 1000000) / 100
    h = calculation_h(u)

    instruction = "A stone is thrown vertically upward with an initial velocity of " + str(u) + " m/s under gravity. What is the maximum height attained by the stone?"
    explanation = f"maximum height (h) = (initial velocity (u)²) / (2 * acceleration (g))\nh = ({u}²) / (2 * {g})\nh = {u ** 2} / {2 * g}\nh = {h}"
    output = {
        "instruction": instruction,
        "input": "initial velocity (u) = " + str(u) + " m/s",
        "output": explanation
    }
    return output

def generate_type2():
    h = random.randint(1, 1000000)
    u = calculation_u(h)

    instruction = "A stone is thrown vertically upward and reaches a maximum height of " + str(h) + " m. What is the initial velocity of the stone?"
    explanation = f"maximum height (h) = (initial velocity (u)²) / (2 * acceleration (g))\n{h} = (u²) / (2 * {g})\n{h} = u² / {2 * g}\n{h} * {2 * g} = u²\n{2 * g * h} = u²\n√{2 * g * h} = u\nu = {u}"
    output = {
        "instruction": instruction,
        "input": "maximum height (h) = " + str(h) + " m",
        "output": explanation
    }
    return output

for i in range(no_of_samples):
    types = random.randint(0, 1)
    if types == 0:
        data.append(generate_type1())
    elif types == 1:
        data.append(generate_type2())

# Read the existing JSON file
with open("science/kinematics/kinematics_data.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinematics/kinematics_data.json", "w") as file:
    json.dump(existing_data, file, indent=4)

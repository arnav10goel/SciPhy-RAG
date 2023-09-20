import random
import math
import json

no_of_samples = 40
g = 9.8

def calculation_h(u, v):
    return round(((v ** 2 - u ** 2) / (2 * g)), 1)

def calculation_u(v, h):
    return round(math.sqrt((v ** 2) - (2 * g * h)), 1)

def calculation_v(u, h):
    return round(math.sqrt((u ** 2) + (2 * g * h)), 1)

data = []

def generate_type1():
    u = random.randint(1, 1000)
    v = random.randint(u, u + 1000)
    h = calculation_h(u, v)

    instruction = "A body is dropped with an initial velocity of " + str(u) + " m/s and reaches the ground with a velocity of " + str(v) + " m/s. From what height was it dropped?"
    
    explanation = f"height (h) = (final velocity (v)² - initial velocity (u)²) / (2 * acceleration (g))\nh = ({v}² - {u}²) / (2 * {g})\nh = ({v ** 2} - {u ** 2}) / {2 * g}\nh = {h}"
    output = {
        "instruction": instruction,
        "input": "initial velocity (u) = " + str(u) + " m/s, final velocity (v) = " + str(v) + " m/s",
        "output": explanation   
    }
    return output

def generate_type2():
    h = random.randint(1, 10000)
    tmp = 2 * g * h
    v = random.randint(int(tmp), int(tmp) + 100)
    u = calculation_u(v, h)

    instruction = "A body is dropped from a height of " + str(h) + " m and reaches the ground with a velocity of " + str(v) + " m/s. With what initial velocity was it dropped?"
    explanation = f"initial velocity (u) = √(final velocity (v)² - 2 * acceleration (g) * height (h))\nu = √({v}² - 2 * {g} * {h})\nu = √({v ** 2} - {tmp})\nu = √{v ** 2 - tmp}\nu = √{u}\nu = {u}"
    output = {
        "instruction": instruction,
        "input": "height (h) = " + str(h) + " m, final velocity (v) = " + str(v) + " m/s",
        "output": explanation
    }
    return output

def generate_type3():
    h = random.randint(1, 10000)
    u = random.randint(0, 100)
    v = calculation_v(u, h)

    instruction = "A body is dropped from a height of " + str(h) + " m with an initial velocity of " + str(u) + " m/s. With what velocity will it strike the ground?"
    explanation = f"final velocity (v) = √(initial velocity (u)² + 2 * acceleration (g) * height (h))\nv = √({u}² + 2 * {g} * {h})\nv = √({u ** 2} + {2 * g * h})\nv = √{u ** 2 + 2 * g * h}\nv = √{v}\nv = {v}"
    output = {
        "instruction": instruction,
        "input": "height (h) = " + str(h) + " m, initial velocity (u) = " + str(u) + " m/s",
        "output": explanation
    }
    return output

for i in range(no_of_samples):
    types = random.randint(0, 2)
    if types == 0:
        data.append(generate_type1())
    elif types == 1:
        data.append(generate_type2())
    elif types == 2:
        data.append(generate_type3())

# Read the existing JSON file
with open("science/kinematics/kinematics_data.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinematics/kinematics_data.json", "w") as file:
    json.dump(existing_data, file, indent=4)

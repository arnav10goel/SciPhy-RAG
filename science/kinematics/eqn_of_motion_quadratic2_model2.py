import random
import math
import json

no_of_samples = 40

def calculation_s(u, a, t):
    return round((u * t) + (0.5 * a * t * t), 1)

def calculation_u(s, a, t):
    return round((s - (0.5 * a * t * t)) / t, 1)

def calculation_t(s, u, a):
    temp = (4 * u * u) + (8 * a * s)
    return round((-(2 * u) + math.sqrt(temp)) / (2 * a), 1)

data = []

def generate_type1():
    a = 9.8
    u = random.randint(1, 5000)
    t = random.randint(1, 200)
    s = calculation_s(u, a, t)

    instruction = "A body is dropped from the top of a building with an initial velocity of " + str(u) + " m/s under gravity, and it reaches the ground after " + str(t) + " s. What is the height of the building?"
    explanation = f"height (s) = initial velocity (u) * time (t) + 0.5 * acceleration (a) * time (t)²\ns = {u} * {t} + 0.5 * {a} * {t}²\ns = {u * t} + {0.5 * a * t ** 2}\ns = {s}"
    output = {
        "instruction": instruction,
        "input": "initial velocity (u) = " + str(u) + " m/s, time (t) = " + str(t) + " s",
        "output": explanation
    }
    return output

def generate_type2():
    a = 9.8
    t = random.randint(1, 200)
    tp = int(0.5 * a * t * t)
    s = random.randint(tp, tp + 5000)
    u = calculation_u(s, a, t)

    instruction = "A body is dropped from the top of a building of height " + str(s) + " m reaches the ground after " + str(t) + " s under gravity. With what initial velocity was it dropped?"
    explanation = f"initial velocity (u) = (height (s) - 0.5 * acceleration (a) * time (t)²) / time (t)\nu = ({s} - 0.5 * {a} * {t}²) / {t}\nu = ({s} - {0.5 * a * t ** 2}) / {t}\nu = ({s - (0.5 * a * t ** 2)}) / {t}\nu = {u}"
    output = {
        "instruction": instruction,
        "input": "height (h) = " + str(s) + " m, time (t) = " + str(t) + " s",
        "output": explanation
    }
    return output

def generate_type3():
    a = 9.8
    u = random.randint(1, 200)
    s = random.randint(u, u + 5000)
    t = calculation_t(s, u, a)

    instruction = "A body is dropped from the top of a building of height " + str(s) + " m with an initial velocity of " + str(u) + " m/s under gravity. After what time does it reach the ground?"
    explanation = f"time (t) = (-(2 * initial velocity (u)) + √((4 * initial velocity (u)²) + (8 * acceleration (a) * height (s)))) / (2 * acceleration (a))\nt = (-(2 * {u}) + √((4 * {u}²) + (8 * {a} * {s}))) / (2 * {a})\nt = (-(2 * {u}) + √({(4 * u * u)} + {(8 * a * s)})) / {(2 * a)}\nt = (-(2 * {u}) + √({(4 * u * u) + (8 * a * s)})) / {(2 * a)}\nt = (-(2 * {u}) + √({(4 * u * u) + (8 * a * s)})) / {(2 * a)}\nt = (-(2 * {u}) + √({(4 * u * u) + (8 * a * s)})) / {(2 * a)}\nt = (-(2 * {u}) + √({(4 * u * u) + (8 * a * s)})) / {(2 * a)}\nt = (-(2 * {u}) + √({(4 * u * u) + (8 * a * s)})) / {(2 * a)}\nt = (-(2 * {u}) + √({(4 * u * u) + (8 * a * s)})) / {(2 * a)}\nt = (-(2 * {u}) + √({(4 * u * u) + (8 * a * s)})) / {(2 * a)}\nt = (-(2 * {u}) + √({(4 * u * u) + (8 * a * s)})) / {(2 * a)}\nt = {t}"
    output = {
        "instruction": instruction,
        "input": "height (h) = " + str(s) + " m, initial velocity (u) = " + str(u) + " m/s",
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

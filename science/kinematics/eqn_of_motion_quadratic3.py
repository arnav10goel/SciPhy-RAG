import random
import math
import json

no_of_samples = 50

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

    instruction = "A stone is thrown vertically upward with an initial velocity of " + str(u) + " m/s and reaches the maximum height after " + str(t) + " s. What is the maximum height attained by the stone?"
    explanation = f"maximum height (h) = (initial velocity (u) * time (t)) + (0.5 * acceleration (a) * time (t)²)\nh = ({u} * {t}) + (0.5 * {a} * {t}²)\nh = {u * t} + {0.5 * a * t ** 2}\nh = {u * t + 0.5 * a * t ** 2}\nh = {s}"
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

    instruction = "A stone is thrown vertically upward and reaches a maximum height of " + str(s) + " m after " + str(t) + " s. With what initial velocity was it thrown up?"
    explanation = f"maximum height (h) = (initial velocity (u) * time (t)) + (0.5 * acceleration (a) * time (t)²)\nh = (u * {t}) + (0.5 * {a} * {t}²)\nh = {t}u + {0.5 * a * t ** 2}\nh = {t}u + {0.5 * a * t ** 2}\nh = {s}\n{t}u = {s} - {0.5 * a * t ** 2}\n{t}u = {s - 0.5 * a * t ** 2}\nu = {round((s - 0.5 * a * t ** 2) / t, 1)}"
    output = {
        "instruction": instruction,
        "input": "maximum height (h) = " + str(s) + " m, time (t) = " + str(t) + " s",
        "output": explanation
    }
    return output

def generate_type3():
    a = 9.8 
    u = random.randint(1, 200)
    s = random.randint(u, u + 5000)
    t = calculation_t(s, u, a)

    instruction = "A stone is thrown vertically upward with an initial velocity of " + str(u) + " m/s and reaches a maximum height of " + str(s) + " m. After what time does it reach the maximum height?"
    
    #the explanation behind solving the question
    explanation = f"maximum height (h) = (initial velocity (u) * time (t)) + (0.5 * acceleration (a) * time (t)²)\nh = ({u} * t) + (0.5 * {a} * t²)\nh = {u}t + {0.5 * a}t²\n{0.5 * a}t² + {u}t - {s} = 0\n{0.5 * a}t² + {u}t - {s} = 0\n{0.5 * a}t² + {u}t = {s}\n{0.5 * a}t² + {u}t = {s}\n{0.5 * a}t² + {u}t - {s} = 0\n{0.5 * a}t² + {u}t - {s} = 0\n{0.5 * a}t² + {u}t - {s} = 0\n{0.5 * a}t² + {u}t - {s} = 0\n{0.5 * a}t² + {u}t - {s} = 0\n{0.5 * a}t² + {u}t - {s} = 0\n{0.5 * a}t² + {u}t - {s} = 0\n{0.5 * a}t² + {u}t - {s} = 0\n{0.5 * a}t² + {u}t - {s} = 0"
    explanation += f"\n{0.5 * a}t² + {u}t - {s} = 0\n{0.5 * a}t² + {u}t - {s} = 0\n{0.5 * a}t² + {u}t - {s} = 0\n{0.5 * a}t² + {u}t - {s} = 0"

    output = {
        "instruction": instruction,
        "input": "maximum height (h) = " + str(s) + " m, initial velocity (u) = " + str(u) + " m/s",
        "output": f"{t}\n{explanation}"
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

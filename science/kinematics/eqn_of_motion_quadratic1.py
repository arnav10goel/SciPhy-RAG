import random
import math
import json

no_of_samples = 60

def calculation_s(u, a, t):
    return round((u * t) + (0.5 * a * t * t), 1)

def calculation_u(s, a, t):
    return round((s - (0.5 * a * t * t)) / t, 1)

def calculation_a(s, u, t):
    return round((2 * (s - u * t)) / (t * t), 1)

def calculation_t(s, u, a):
    temp = (4 * u * u) + (8 * a * s)
    return round((-(2 * u) + math.sqrt(temp)) / (2 * a), 1)

data = []

def generate_type1():
    u = random.randint(1, 1000)
    a = random.randint(1, 100)
    t = random.randint(1, 10)
    s = calculation_s(u, a, t)

    instruction = "A bike starting with an initial velocity of " + str(u) + " m/s travels on a straight road at a constant rate of " + str(a) + " m/s² for " + str(t) + " s. How far does the bike travel during this time?"
    # show all the steps as strings in explanation
    explanation = f"distance (s) = initial velocity (u) * time (t) + 0.5 * acceleration (a) * time (t)²\ns = {u} * {t} + 0.5 * {a} * {t}²\ns = {u * t} + {0.5 * a * t * t}\ns = {s}"
    
    output = {
        "instruction": instruction,
        "input": "initial velocity (u) = " + str(u) + " m/s, acceleration (a) = " + str(a) + " m/s², time (t) = " + str(t) + " s",
        "output": f"{s} m \n\n{explanation}"
    }
    return output

def generate_type2():
    a = random.randint(1, 100)
    t = random.randint(1, 10)
    tp = int(0.5 * a * t * t)
    s = random.randint(tp, tp + 1000)
    u = calculation_u(s, a, t)

    instruction = "A bike travels a distance of " + str(s) + " m on a straight road at a constant rate of " + str(a) + " m/s² for " + str(t) + " s. What is the initial velocity of the bike?"
    
    explanation = f"distance (s) = initial velocity (u) * time (t) + 0.5 * acceleration (a) * time (t)²\ns = u * {t} + 0.5 * {a} * {t}²\ns = {t}u + {0.5 * a * t * t}\ns = {t}u + {tp}\ns = {s}\n\ns - {tp} = {t}u\n{u} = {s - tp} / {t}\n{u} = {u}"
    output = {
        "instruction": instruction,
        "input": "distance (s) = " + str(s) + " m, acceleration (a) = " + str(a) + " m/s², time (t) = " + str(t) + " s",
        "output": explanation
    }
    return output

def generate_type3():
    u = random.randint(1, 100)
    t = random.randint(1, 10)
    tp = u * t
    s = random.randint(tp + 10, tp + 1010)
    a = calculation_a(s, u, t)

    instruction = "A bike starting with an initial velocity of " + str(u) + " m/s travels a distance of " + str(s) + " m on a straight road for " + str(t) + " s. What is the acceleration of the bike?"
    
    explanation = f"distance (s) = initial velocity (u) * time (t) + 0.5 * acceleration (a) * time (t)²\n{s} = {u} * {t} + 0.5 * a * {t}²\n{s} = {tp} + 0.5 * a * {t}²\n{s} = {tp} + {0.5 * a * t * t}\n{s} = {s}\n\n{s} - {tp} = {0.5 * a * t * t}\n{a} = 2 * ({s} - {tp}) / {t}²\n{a} = {a}"
    output = {
        "instruction": instruction,
        "input": "initial velocity (u) = " + str(u) + " m/s, distance (s) = " + str(s) + " m, time (t) = " + str(t) + " s",
        "output": explanation
    }
    return output

def generate_type4():
    u = random.randint(1, 100)
    a = random.randint(1, 10)
    s = random.randint(1, 1000)
    t = calculation_t(s, u, a)

    instruction = "A bike starting with an initial velocity of " + str(u) + " m/s travels on a straight road at a constant rate of " + str(a) + " m/s². What is the time taken to travel a distance of " + str(s) + " m?"
    explanation = f"distance (s) = initial velocity (u) * time (t) + 0.5 * acceleration (a) * time (t)²\n{s} = {u} * t + 0.5 * {a} * t²\n{s} = {u * t} + {0.5 * a * t * t}\n{s} = {s}\n\n0.5 * {a} * t² + {u} * t - {s} = 0\n{0.5 * a} * t² + {u} * t - {s} = 0\n\nUsing quadratic formula, we get:\n\nt = (-{u} ± √({u}² - 4 * {0.5 * a} * (-{s}))) / (2 * {0.5 * a})\nt = (-{u} ± √({u * u} - {2 * a * s})) / {a}\nt = (-{u} ± √({u * u + 2 * a * s})) / {a}\nt = (-{u} ± √({u * u + 2 * a * s})) / {a}\nt = (-{u} ± √({u * u + 2 * a * s})) / {a}\nt = (-{u} ± {math.sqrt(u * u + 2 * a * s)}) / {a}\nt = {(-u + math.sqrt(u * u + 2 * a * s)) / a} or {(-u - math.sqrt(u * u + 2 * a * s)) / a}\nt = {t} or {t}\n\nSince time cannot be negative, t = {t}"
    output = {
        "instruction": instruction,
        "input": "initial velocity (u) = " + str(u) + " m/s, acceleration (a) = " + str(a) + " m/s², distance (s) = " + str(s) + " m",
        "output": explanation
    }
    return output

for i in range(no_of_samples):
    types = random.randint(0, 3)
    if types == 0:
        data.append(generate_type1())
    elif types == 1:
        data.append(generate_type2())
    elif types == 2:
        data.append(generate_type3())
    elif types == 3:
        data.append(generate_type4())

# Read the existing JSON file
with open("science/kinematics/kinematics_data.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinematics/kinematics_data.json", "w") as file:
    json.dump(existing_data, file, indent=4)

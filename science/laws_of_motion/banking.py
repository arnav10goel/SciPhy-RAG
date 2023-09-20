import random
import json
import math
no_of_samples = 40

def type1():
    m = random.randint(1, 200)
    param = random.randint(1, 80)
    g = 10
    v = random.randint(30, 530)
    q = f"An aircraft of mass {m} kg executes a horizontal loop at a speed of {v} m/s with its wings banked at {param} degrees. What is the radius of the loop?"
    formula = "(v^2) / (g * tan((param * pi) / 180))"
    expr = (v ** 2) / (g * math.tan((param * math.pi) / 180))
    explanation = f"To calculate the radius, we use the formula (v^2) / (g * tan((param * pi) / 180)), where v is the speed ({v} m/s), g is the acceleration due to gravity (10 m/s^2), and param is the angle of banking ({param} degrees)."
    return q, round(expr), formula, explanation

def type2():
    m = random.randint(1, 200)
    param = random.randint(1, 80)
    g = 10
    v = random.randint(30, 530)
    q = f"A train runs along an unbanked circular track of radius {param + 400} m at a speed of {v} m/s. The mass of the train is {m} kg. What is the angle of banking required to prevent wearing out of the rail?"
    formula = "((atan((v^2) / ((param + 400) * g))) * 180) / pi"
    expr = ((math.atan((v ** 2) / ((param + 400) * g))) * 180) / math.pi
    explanation = f"To calculate the angle of banking, we use the formula ((atan((v^2) / ((param + 400) * g))) * 180) / pi, where v is the speed ({v} m/s), g is the acceleration due to gravity (10 m/s^2), and param is the radius ({param + 400} m) of the circular track."
    return q, round(expr), formula, explanation

data = []

for i in range(no_of_samples):
    types = random.randint(1, 2)
    if types == 1:
        ques, answer, formula, explanation = type1()
    else:
        ques, answer, formula, explanation = type2()
    data.append({
        "instruction": ques,
        "input": formula,
        "output": f"{answer}\n{explanation}"
    })

# Read the existing JSON file
with open("science/laws_of_motion/nlm.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/laws_of_motion/nlm.json", "w") as file:
    json.dump(existing_data, file, indent=4)
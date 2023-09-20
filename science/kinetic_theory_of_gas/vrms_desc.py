import random
import json
import math

no_of_samples = 40

data = []

def cal1(t1, m):
    r = 8.31
    t1 = t1 + 273
    return math.sqrt((3 * r * t1 * 1000) / m)

def cal2(t1, v):
    r = 8.31
    t1 = t1 + 273
    return (3 * r * t1 * 1000) / (v * v)

def type1():
    t1 = random.randint(100, 1600)
    m = random.randint(1, 400)
    t = random.randint(1, 2)
    if t == 1:
        q = f"Calculate root mean square velocity of a gas molecule having molar mass of {m} g/mol at {t1} degree C."
    else:
        q = f"Calculate root mean square velocity of a gas molecule having molar mass of {m} g/mol at {t1} degree C. (R = 8.31 J/molK)"
    a = cal1(t1, m)
    formula = "math.sqrt((3 * r * t1 * 1000) / m)"
    return q, a, formula

def type2():
    t1 = random.randint(100, 1600)
    v = random.randint(1000, 2000)
    t = random.randint(1, 2)
    if t == 1:
        q = f"If a gas molecule has root mean square velocity of {v} m/s and is at a temperature {t} degree C. What is the molar mass of the gas."
    else:
        q = f"If a gas molecule has root mean square velocity of {v} m/s and is at a temperature {t} degree C. What is the molar mass of the gas. (R = 8.31 J/molK)"
    a = cal2(t1, v)
    formula = "(3 * r * t1 * 1000) / (v * v)"
    return q, a, formula

for i in range(no_of_samples):
    types = random.randint(1, 2)
    if types == 1:
        ques, answer, formula = type1()
    else:
        ques, answer, formula = type2()
    data.append({
        "instruction": ques,
        "input": formula,
        "output": f"{answer} m/s\n The formula used is: {formula}"
    })

# Read the existing JSON file
with open("science/kinetic_theory_of_gas/ktg.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinetic_theory_of_gas/ktg.json", "w") as file:
    json.dump(existing_data, file, indent=4)

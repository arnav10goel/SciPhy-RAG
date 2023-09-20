import random
import json

no_of_samples = 20

data = []

k = 1.38 * (10 ** -23)

def cal1(t1):
    t1 = t1 + 273
    return round(1.5 * k * t1, 1)

def cal2(t1):
    return round(1.5 * k * t1, 1)

def type1():
    t1 = random.randint(1, 100000)
    t = random.randint(1, 2)
    if t == 1:
        q = f"Estimate the average thermal energy of a helium atom at {t1} degree C. (k = 1.38 x 10^-23)"
    else:
        q = f"Estimate the average thermal energy of a helium atom at {t1} degree C."
    a = cal1(t1)
    formula = "energy = 1.5 * k * temperature"
    return q, a, formula

def type2():
    t1 = random.randint(1, 100000)
    t = random.randint(1, 2)
    if t == 1:
        q = f"Estimate the average thermal energy of a helium atom at {t1} degree K. (k = 1.38 x 10^-23)"
    else:
        q = f"Estimate the average thermal energy of a helium atom at {t1} degree K."
    a = cal2(t1)
    formula = "energy = 1.5 * k * temperature"
    return q, a, formula

for i in range(no_of_samples):
    types = random.randint(1, 2)
    if types == 1:
        q, answer, formula = type1()
    else:
        q, answer, formula = type2()
    data.append({
        "instruction": q,
        "input": formula,
        "output": str(answer) + formula[formula.index('='):]
    })

# Read the existing JSON file
with open("science/kinetic_theory_of_gas/ktg.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinetic_theory_of_gas/ktg.json", "w") as file:
    json.dump(existing_data, file, indent=4)

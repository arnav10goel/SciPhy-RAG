import random
import json
import math

no_of_samples = 20

data = []

R = 8.31
n = 6.023 * (10**23)

def cal1(p, t1, r):
    p = p * (10**5)
    t1 = t1 + 273
    r = r * (10**-10)
    nu = (n * p) / (R * t1)
    return round(1 / (math.sqrt(2) * math.pi * nu * (4 * r * r)), 1)

def type1():
    t1 = random.randint(1, 100)
    p = random.randint(1, 100)
    r = random.randint(1, 100)
    q = f"Estimate the mean free path of a gas molecule in a cylinder containing gas at {p} atm and temperature {t1} degree C. Take the radius of a gas molecule to be roughly {r} A."
    a = cal1(p, t1, r)
    formula = "mean_free_path = 1 / (sqrt(2) * pi * nu * (4 * r * r))"
    explanation = f"Here, nu = (n * p) / (R * t1) = ({n} * {p} * 10^5) / ({R} * {t1} + 273) = {round((n * p * (10**5)) / (R * (t1 + 273)), 2)}\nmean_free_path = 1 / (sqrt(2) * pi * {round((n * p * (10**5)) / (R * (t1 + 273)), 2)} * (4 * {r} * 10^-10 * {r} * 10^-10)) = {a}"
    return q, a, formula, explanation

for i in range(no_of_samples):
    ques, answer, formula, ex = type1()
    data.append({
        "instruction": ques,
        "input": formula,
        "output": f"{answer} m\n{ex}"
    })

# Read the existing JSON file
with open("science/kinetic_theory_of_gas/ktg.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinetic_theory_of_gas/ktg.json", "w") as file:
    json.dump(existing_data, file, indent=4)

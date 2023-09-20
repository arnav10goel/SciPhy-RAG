import random
import json

no_of_samples = 20

data = []

k = 1.38 * (10**-23)

def cal1(v, p, t1):
    p = p * (10**5)
    t1 = t1 + 273
    return round((p * v) / (k * t1), 2)

def type1():
    v = random.randint(10, 110)
    t1 = random.randint(1, 100)
    p = random.randint(1, 100)
    q = f"Estimate the total number of air molecules (inclusive of oxygen, nitrogen, water vapor, and other constituents) in a room of capacity {v} m3 at a temperature of {t1} degree C and {p} atm pressure."
    a = cal1(v, p, t1)
    formula = "total_number_of_molecules = (p * v) / (k * t1)"
    explaination = f"Here, p = {p} atm = {p * (10**5)} Pa, v = {v} m3, t1 = {t1} degree C = {t1 + 273} K, k = 1.38 x 10^-23 J/K"
    return q, a, formula, explaination

for i in range(no_of_samples):
    ques, answer, formula, ex = type1()
    data.append({
        "instruction": ques,
        "input": formula,
        "output": f"{answer} molecules\n{ex}"
    })

# Read the existing JSON file
with open("science/kinetic_theory_of_gas/ktg.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinetic_theory_of_gas/ktg.json", "w") as file:
    json.dump(existing_data, file, indent=4)

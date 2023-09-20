import random
import json
import math

no_of_samples = 20

data = []

def cal1(d):
    n = 6.023 * (10**23)
    return (4 * math.pi * d * d * d * 1000 * n) / (3 * 8 * 22.4)

def type1():
    d = random.randint(1, 10000) / 10
    t = random.randint(1, 2)
    if t == 1:
        q = f"Estimate the fraction of molecular volume to the actual volume occupied by a gas at STP. Take the diameter of the gas molecule to be {d} A."
    else:
        q = f"Estimate the fraction of molecular volume to the actual volume occupied by a gas at STP. Take the diameter of the gas molecule to be {d} A and volume occupied by a gas at STP as 22.4 L."
    a = cal1(d)
    formula = "(4 * pi * d * d * d * 1000 * n) / (3 * 8 * 22.4)"
    return q, a, formula

for i in range(no_of_samples):
    ques, answer, formula = type1()
    data.append({
        "instruction": ques,
        "input": formula,
        "output": f"{answer} \n {formula}"
    })

# Read the existing JSON file
with open("science/kinetic_theory_of_gas/ktg.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinetic_theory_of_gas/ktg.json", "w") as file:
    json.dump(existing_data, file, indent=4)

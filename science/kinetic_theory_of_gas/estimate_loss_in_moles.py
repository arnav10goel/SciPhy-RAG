import random
import json

no_of_samples = 20

data = []

R = 8.31

def cal1(v, p1, p2, t1, t2):
    p1 = p1 * 10 ** 5
    p2 = p2 * 10 ** 5
    v = v * 10 ** -3
    t1 = t1 + 273
    t2 = t2 + 273
    n1 = (p1 * v) / (R * t1)
    n2 = (p2 * v) / (R * t2)
    return round(n1 - n2, 1)

def type1():
    v = random.randint(20, 60)
    t1 = random.randint(20, 40)
    t2 = random.randint(t1 + 5, t1 + 25)
    p1 = random.randint(15, 25)
    p2 = random.randint(p1 - 13, p1 - 3)
    t = random.randint(1, 2)
    if t == 1:
        q = f"An oxygen cylinder of volume {v} litre has an initial gauge pressure of {p1} atmosphere and a temperature of {t1} degree C. After some oxygen is withdrawn from the cylinder, the gauge pressure drops to {p2} atmosphere and its temperature drops to {t2} degree C. Estimate the number of moles of oxygen taken out of the cylinder. (R = 8.3 J mol-1 K-1)"
    else:
        q = f"An oxygen cylinder of volume {v} litre has an initial gauge pressure of {p1} atmosphere and a temperature of {t1} degree C. After some oxygen is withdrawn from the cylinder, the gauge pressure drops to {p2} atmosphere and its temperature drops to {t2} degree C. Estimate the number of moles of oxygen taken out of the cylinder."
    a = cal1(v, p1, p2, t1, t2)
    formula = "n = (p1 * V) / (R * T1) - (p2 * V) / (R * T2)"
    explanation = "p1 = initial pressure\np2 = final pressure\nV = volume\nt1 = initial temperature\nt2 = final temperature\nR = gas constant"
    explanation += f"\nn = ({p1} * {v} * 10^5) / ({R} * {t1 + 273}) - ({p2} * {v} * 10^5) / ({R} * {t2 + 273})"
    explanation += f"\nn = {round((p1 * v * 10 ** 5) / (R * (t1 + 273)), 1)} - {round((p2 * v * 10 ** 5) / (R * (t2 + 273)), 1)}"
    explanation += f"\nn = {round((p1 * v * 10 ** 5) / (R * (t1 + 273)) - (p2 * v * 10 ** 5) / (R * (t2 + 273)), 1)}"
    explanation += f"\nn = {a} mol"
    return q, a, formula, explanation

for i in range(no_of_samples):
    ques, answer, formula, explanation = type1()
    data.append({
        "instruction": ques,
        "input": formula,
        "output": f"{answer} mol \n \n{explanation}"
    })

# Read the existing JSON file
with open("science/kinetic_theory_of_gas/ktg.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinetic_theory_of_gas/ktg.json", "w") as file:
    json.dump(existing_data, file, indent=4)

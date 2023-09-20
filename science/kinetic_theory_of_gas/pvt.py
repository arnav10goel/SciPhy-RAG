import random
import json

no_of_samples = 20

data = []
R = 8.314
def cal1(v, h, t1, t2):
    p1 = (10**5) + (1000 * 9.8 * h)
    p2 = (10**5)
    t1 = t1 + 273
    t2 = t2 + 273
    return round((p1 * v * t2) / (t1 * p2), 1), p1, p2

def type1():
    v = random.randint(10, 110)
    t1 = random.randint(5, 25)
    t2 = random.randint(t1 + 10, t1 + 20)
    h = random.randint(10, 310)
    q = f"An air bubble of volume {v} cm3 rises from the bottom of a lake {h} m deep at a temperature of {t1} degree C. To what volume does it grow when it reaches the surface, which is at a temperature of {t2} degree C."
    a, p1, p2 = cal1(v, h, t1, t2)
    formula = "(p1 * v * t2) / (t1 * p2)"
    explanation = "p1 = initial pressure\np2 = final pressure\nV = volume\nt1 = initial temperature\nt2 = final temperature\nR = gas constant"
    explanation += f"\nn = ({p1} * {v} * 10^5) / ({R} * {t1 + 273}) - ({p2} * {v} * 10^5) / ({R} * {t2 + 273})"
    explanation += f"\nn = {round((p1 * v * 10 ** 5) / (R * (t1 + 273)), 1)} - {round((p2 * v * 10 ** 5) / (R * (t2 + 273)), 1)}"
    explanation += f"\nn = {round((p1 * v * 10 ** 5) / (R * (t1 + 273)) - (p2 * v * 10 ** 5) / (R * (t2 + 273)), 1)}"
    explanation += f"\nV = n * R * t2 / p2 = {round((round((p1 * v * 10 ** 5) / (R * (t1 + 273)) - (p2 * v * 10 ** 5) / (R * (t2 + 273)), 1) * R * (t2 + 273)) / (p2 * 10 ** 5), 1)} cm3"
    return q, a, formula, explanation

for i in range(no_of_samples):
    ques, answer, formula, ex = type1()
    data.append({
        "instruction": ques,
        "input": formula,
        "output": f"{answer} cm3\n{ex}"
    })

# Read the existing JSON file
with open("science/kinetic_theory_of_gas/ktg.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinetic_theory_of_gas/ktg.json", "w") as file:
    json.dump(existing_data, file, indent=4)

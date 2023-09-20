import random
import json
import math

no_of_samples = 50

data = []

def cal1(m1, m2, d1):
    return round((d1 * math.sqrt(m1)) / math.sqrt(m2), 1)

def cal2(d1, d2, m1):
    return round((d1 * math.sqrt(m1)) / d2, 1)

def type1():
    d1 = random.randint(10, 200)
    m1 = random.randint(1, 300)
    m2 = random.randint(1, 300)
    q = f"Gas A has a molar mass of {m1} g/mol and gas B has a molar mass of {m2} g/mol. If diffusion rate of gas A is {d1} cm3/sec, what is the diffusion rate of gas B?"
    a = cal1(m1, m2, d1)
    formula = "d2 = (d1 * sqrt(m2)) / sqrt(m1)"
    return q, a, formula

def type2():
    d2 = random.randint(10, 200)
    m1 = random.randint(1, 300)
    m2 = random.randint(1, 300)
    q = f"Gas A has a molar mass of {m1} g/mol and gas B has a molar mass of {m2} g/mol. If diffusion rate of gas B is {d2} cm3/sec, what is the diffusion rate of gas A?"
    a = cal1(m2, m1, d2)
    formula = "d1 = (d2 * sqrt(m1)) / sqrt(m2)"
    return q, a, formula

def type3():
    d1 = random.randint(10, 200)
    d2 = random.randint(10, 200)
    m1 = random.randint(1, 300)
    q = f"Gas A has a diffusion rate of {d1} cm3/sec and gas B has a diffusion rate of {d2} cm3/sec. If molar mass of gas A is {m1} g/mol, what is the molar mass of gas B?"
    a = cal2(d1, d2, m1)
    formula = "m2 = (d1 * sqrt(m1)) / d2"
    return q, a, formula

def type4():
    d1 = random.randint(10, 200)
    d2 = random.randint(10, 200)
    m2 = random.randint(1, 300)
    q = f"Gas A has a diffusion rate of {d1} cm3/sec and gas B has a diffusion rate of {d2} cm3/sec. If molar mass of gas B is {m2} g/mol, what is the molar mass of gas A?"
    a = cal1(d2, d1, m2)
    formula = "m1 = (d2 * sqrt(m2)) / d1"
    return q, a, formula

for i in range(no_of_samples):
    types = random.randint(1, 4)
    if types == 1:
        ques, answer, formula = type1()
    elif types == 2:
        ques, answer, formula = type2()
    elif types == 3:
        ques, answer, formula = type3()
    elif types == 4:
        ques, answer, formula = type4()
    explain = "Graham's law of diffusion states that the rate of diffusion of a gas is inversely proportional to the square root of its molar mass."
    explain += "In other words, the lighter the gas, the faster it will diffuse."
    explain += "The formula for Graham's law of diffusion is d1 / d2 = sqrt(m2) / sqrt(m1)"
    explain += "where d1 and d2 are the diffusion rates of gas A and gas B respectively, and m1 and m2 are the molar masses of gas A and gas B respectively."
    explain += "Rearranging the formula, we get d1 = (d2 * sqrt(m1)) / sqrt(m2) and d2 = (d1 * sqrt(m2)) / sqrt(m1)"
    explain += "In this question, we are given d1, d2 and m2, and we are required to find m1."
    explain += "Substituting the values into the formula, we get d1 = (d2 * sqrt(m2)) / sqrt(m1)"
    explain += "Rearranging the formula, we get m1 = (d2 * sqrt(m2)) / d1"
    data.append({
        "instruction": ques,
        "input": formula,
        "output": f"{answer} g/mol \n \n {explain}"
    })

# Read the existing JSON file
with open("science/kinetic_theory_of_gas/ktg.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinetic_theory_of_gas/ktg.json", "w") as file:
    json.dump(existing_data, file, indent=4)

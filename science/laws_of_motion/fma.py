import random
import json

no_of_samples = 40

def calculation_F(m, a): 
    return m * a

def calculation_a(F, m):
    return round(F / m, 1)

def calculation_m(F, a):
    return round(F / a, 1)

def type1():
    m = random.randint(1, 1000)
    a = random.randint(1, 1000)
    F = calculation_F(m, a)
    q = f"A force is applied on a body of mass {m} kg placed on a smooth surface resulting in acceleration of {a} m/s^2, then what is the force applied?"
    formula = "F = m * a"
    explanation = f"To calculate the force, we use the formula F = m * a, where F is the force, m is the mass ({m} kg), and a is the acceleration ({a} m/s^2)."
    return q, F, formula, explanation

def type2():
    F = random.randint(9000, 10000)
    m = random.randint(1, 1000)
    a = calculation_a(F, m)
    q = f"A {F} N force is applied on a body of mass {m} kg placed on a smooth surface, then what is the resulting acceleration obtained?"
    formula = "a = F / m"
    explanation = f"To calculate the acceleration, we use the formula a = F / m, where a is the acceleration, F is the force ({F} N), and m is the mass ({m} kg)."
    return q, a, formula, explanation

def type3():
    F = random.randint(9000, 10000)
    a = random.randint(1, 1000)
    m = calculation_m(F, a)
    q = f"A {F} N force is applied on a body placed on a smooth surface resulting in acceleration of {a} m/s^2, then what is the mass of the body?"
    formula = "m = F / a"
    explanation = f"To calculate the mass, we use the formula m = F / a, where m is the mass, F is the force ({F} N), and a is the acceleration ({a} m/s^2)."
    return q, m, formula, explanation

data = []

for i in range(no_of_samples):
    types = random.randint(0, 2)
    if types == 0:
        ques, answer, formula, explanation = type1()
    elif types == 1:
        ques, answer, formula, explanation = type2()
    else:
        ques, answer, formula, explanation = type3()
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

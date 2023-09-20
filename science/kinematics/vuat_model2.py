import random
import json

no_of_samples = 20

data = []

def calculation_u(a, t):
    return round(a * t, 1)

def calculation_t(u, a):
    return round(u / a, 1)

def type1():
    u = random.randint(0, 1000000)
    a = 9.8
    t = calculation_t(u, a)
    q = f"A stone is thrown vertically upward with a velocity of {u} m/s. What is the time taken by it to reach the maximum height?"
    answer = f"The time taken by the stone to reach the maximum height is {t} s."
    formula = "time = initial_velocity / acceleration"
    return q, answer, formula

def type2():
    a = 9.8
    t = random.randint(0, 1000000)
    u = calculation_u(a, t)
    q = f"A stone is thrown vertically upward and reaches a maximum height after {t} s. With what initial velocity was it thrown up?"
    answer = f"The stone was thrown upward with an initial velocity of {u} m/s."
    formula = "initial_velocity = acceleration * time"
    return q, answer, formula

for i in range(no_of_samples):
    types = random.randint(1, 2)
    if types == 1:
        q, answer, formula = type1()
    elif types == 2:
        q, answer, formula = type2()
    data.append({
        "instruction": q,
        "input": formula,
        "output": answer
    })

# Read the existing JSON file
with open("science/kinematics/kinematics_data.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinematics/kinematics_data.json", "w") as file:
    json.dump(existing_data, file, indent=4)

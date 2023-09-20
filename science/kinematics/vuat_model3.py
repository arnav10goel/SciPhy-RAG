import random
import json

no_of_samples = 20

data = []

def calculation_v(u, a, t):
    return round(u + (a * t), 1)

def calculation_u(v, a, t):
    return round(v - (a * t), 1)

def calculation_t(u, v, a):
    return round((v - u) / a, 1)

def type1():
    u = random.randint(0, 4000)
    a = 9.8
    t = random.randint(1, 300)
    v = calculation_v(u, a, t)
    q = f"A body is dropped from a tower with an initial velocity of {u} m/s and reaches the ground after {t} s. With what velocity does it reach the ground?"
    answer = f"The body reaches the ground with a velocity of {v} m/s."
    formula = "velocity = initial_velocity + (acceleration * time)"
    return q, answer, formula

def type2():
    a = 9.8
    t = random.randint(1, 300)
    v = random.randint(int(a * t), int(a * t) + 4000)
    u = calculation_u(v, a, t)
    q = f"A body is dropped from a tower and reaches the ground with a velocity of {v} m/s after {t} s. What is its initial velocity?"
    answer = f"The initial velocity of the body is {u} m/s."
    formula = "initial_velocity = velocity - (acceleration * time)"
    return q, answer, formula

def type3():
    u = random.randint(0, 1000)
    v = random.randint(u, u + 1000)
    a = 9.8
    t = calculation_t(u, v, a)
    q = f"A body is dropped from a tower with an initial velocity of {u} m/s and reaches the ground with a velocity of {v} m/s under gravity. What is the time taken by the body to reach the ground?"
    answer = f"The time taken by the body to reach the ground is {t} s."
    formula = "time = (velocity - initial_velocity) / acceleration"
    return q, answer, formula

for i in range(no_of_samples):
    types = random.randint(1, 3)
    if types == 1:
        q, answer, formula = type1()
    elif types == 2:
        q, answer, formula = type2()
    elif types == 3:
        q, answer, formula = type3()
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
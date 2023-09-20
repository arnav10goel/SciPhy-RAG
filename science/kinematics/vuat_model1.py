import random
import json

no_of_samples = 50

data = []

def calculation_v(u, a, t):
    return round(u + (a * t), 1)

def calculation_u(v, a, t):
    return round(v - (a * t), 1)

def calculation_a(u, v, t):
    return round((v - u) / t, 1)

def calculation_t(u, v, a):
    return round((v - u) / a, 1)

def type1():
    u = random.randint(0, 1000)
    a = random.randint(0, 40)
    t = random.randint(1, 40)
    v = calculation_v(u, a, t)
    q = f"If a car has an initial velocity of {u} m/s and has a constant acceleration of {a} m/s² for {t} s, then what is the final velocity of the car?"
    answer = f"The final velocity of the car is {v} m/s."
    formula = f"final_velocity = initial_velocity + (acceleration * time)"
    return q, answer, formula

def type2():
    a = random.randint(0, 40)
    t = random.randint(1, 40)
    v = random.randint(a * t, (a * t) + 1000)
    u = calculation_u(v, a, t)
    q = f"If a car attains a velocity of {v} m/s by applying a constant acceleration of {a} m/s² for {t} s, then what is the initial velocity of the car?"
    answer = f"The initial velocity of the car is {u} m/s."
    formula = f"initial_velocity = final_velocity - (acceleration * time)"
    return q, answer, formula

def type3():
    u = random.randint(0, 500)
    v = random.randint(u, u + 500)
    t = random.randint(1, 20)
    a = calculation_a(u, v, t)
    q = f"If a car has an initial velocity of {u} m/s and attains a velocity of {v} m/s in {t} s, then what is the acceleration of the car?"
    answer = f"The acceleration of the car is {a} m/s²."
    formula = f"acceleration = (final_velocity - initial_velocity) / time"
    return q, answer, formula

def type4():
    u = random.randint(0, 500)
    v = random.randint(u, u + 500)
    a = random.randint(1, 20)
    t = calculation_t(u, v, a)
    q = f"If a car has an initial velocity of {u} m/s and has a constant acceleration of {a} m/s², then what is the time taken by the car to attain a velocity of {v} m/s?"
    answer = f"The time taken by the car to attain a velocity of {v} m/s is {t} s."
    formula = f"time = (final_velocity - initial_velocity) / acceleration"
    return q, answer, formula

for i in range(no_of_samples):
    types = random.randint(1, 4)
    if types == 1:
        q, answer, formula = type1()
    elif types == 2:
        q, answer, formula = type2()
    elif types == 3:
        q, answer, formula = type3()
    elif types == 4:
        q, answer, formula = type4()
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

import random
import math
import json

no_of_samples = 30
g = 9.8

data = []

def type1():
    v = random.randint(1, 20000)
    theta = random.randint(0, 90)
    q = "An object is projected with an initial velocity of " + str(v) + " m/s at an angle " + str(theta) + " from the ground, what is the horizontal range of the object?"
    range = ((v ** 2) * math.sin(2 * theta * (math.pi / 180))) / g
    a = round(range, 1)
    input_param = "v = " + str(v) + " m/s, theta = " + str(theta) + " degrees"
    return q, a, input_param

def type2():
    h = random.randint(1, 20000)
    theta = random.randint(1, 90)
    q = "An object is projected at an angle " + str(theta) + " from the ground, if the horizontal range of the object is " + str(h) + " m, what is the initial velocity of it?"
    v = math.sqrt((h * g) / (math.sin(2 * theta * (math.pi / 180))))
    a = round(v, 1)
    input_param = "h = " + str(h) + " m, theta = " + str(theta) + " degrees"
    return q, a, input_param

def type3():
    v = random.randint(450, 850)
    h = random.randint(1, 20000)
    q = "An object is projected with an initial velocity of " + str(v) + " m/s, if the horizontal range of the object is " + str(h) + " m, what is the angle of projection?"
    theta = math.asin(g * h / (v ** 2)) * (180 / math.pi)
    a = [round(theta / 2), round((180 - theta) / 2)]
    input_param = "v = " + str(v) + " m/s, h = " + str(h) + " m"
    return q, a, input_param

for i in range(no_of_samples):
    types = random.randint(1, 3)
    if types == 1:
        ques, answer, input_param = type1()
    elif types == 2:
        ques, answer, input_param = type2()
    elif types == 3:
        ques, answer, input_param = type3()
    data.append({
        "instruction": ques,
        "input": input_param,
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

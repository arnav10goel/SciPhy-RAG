import random
import math
import json

no_of_samples = 30

data = []

g = 9.8

def type1():
    v = random.randint(1, 20000)
    theta = random.randint(0, 90)
    instruction = "An object is projected with an initial velocity of " + str(v) + " m/s at an angle " + str(theta) + " from the ground. What is the maximum height reached by it?"
    max_height = ((v * math.sin(theta * (math.pi / 180))) ** 2) / (2 * g)
    output = str(round(max_height / 1000, 1)) + " km"
    return instruction, output

def type2():
    h = random.randint(1, 20000)
    theta = random.randint(1, 90)
    instruction = "An object is projected at an angle " + str(theta) + " from the ground. If the maximum height reached by it is " + str(h) + " m, what is its initial velocity?"
    v = math.sqrt((2 * h * g) / (math.sin(theta * (math.pi / 180)) ** 2))
    output = str(round(v, 1)) + " m/s"
    return instruction, output

def type3():
    v = random.randint(500, 900)
    h = random.randint(1, 10000)
    instruction = "An object is projected with an initial velocity of " + str(v) + " m/s. If the maximum height reached by it is " + str(h) + " m, what is the angle of projection?"
    theta = math.asin(math.sqrt(2 * g * h / (v ** 2))) * (180 / math.pi)
    output = str(round(theta)) + " degrees w.r.t. to the ground"
    return instruction, output

for i in range(no_of_samples):
    types = random.randint(1, 3)
    if types == 1:
        instruction, answer = type1()
    elif types == 2:
        instruction, answer = type2()
    elif types == 3:
        instruction, answer = type3()
    
    data.append({
        "instruction": instruction,
        "input": "",
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

import random
import json

no_of_samples = 10

data = []

def type1():
    v1 = random.randint(1, 2000)
    v2 = random.randint(1, 2000)
    q = "A jet airplane travelling at the speed of " + str(v1) + " m/s ejects its combustion products at the speed of " + str(v2) + " m/s relative to the jet plane. What is the speed of the combustion products with respect to an observer on the ground?"
    a = v1 - v2
    input_param = "v1 = " + str(v1) + " m/s, v2 = " + str(v2) + " m/s"
    return q, a, input_param

def type2():
    v1 = random.randint(1, 2000)
    v2 = random.randint(1, 2000)
    q = "A jet airplane travelling at the speed of " + str(v1) + " m/s ejects its combustion products. If the speed of the combustion products with respect to an observer on the ground is " + str(v2) + " m/s, then what is the speed of the combustion products with respect to the plane?"
    a = v1 - v2
    input_param = "v1 = " + str(v1) + " m/s, v2 = " + str(v2) + " m/s"
    return q, a, input_param

def type3():
    v1 = random.randint(1, 2000)
    v2 = random.randint(1, 2000)
    q = "A jet airplane ejects its combustion products at the speed of " + str(v1) + " m/s with respect to the jet plane. If the speed of the combustion products with respect to an observer on the ground is " + str(v2) + " m/s, then what is the speed of the plane?"
    a = v1 + v2
    input_param = "v1 = " + str(v1) + " m/s, v2 = " + str(v2) + " m/s"
    return q, a, input_param

def type4():
    v1 = random.randint(50, 250)
    v2 = random.randint(300, 500)
    v3 = random.randint(1000, 1200)
    q = "A police van moving on a highway with a speed of " + str(v1) + " m/s fires a bullet at a thief's car speeding away in the same direction with a speed of " + str(v2) + " m/s. If the muzzle speed of the bullet is " + str(v3) + " m/s, with what speed does the bullet hit the thief's car?"
    a = "The speed of the bullet is " + str(v1 + v3) + " m/s, and the relative speed of the bullet with respect to the thief's car is " + str(v1 + v3 - v2) + " m/s"
    input_param = "v1 = " + str(v1) + " m/s, v2 = " + str(v2) + " m/s, v3 = " + str(v3) + " m/s"
    return q, a, input_param

for i in range(no_of_samples):
    types = random.randint(1, 5)
    if types == 1:
        ques, answer, input_param = type1()
    elif types == 2:
        ques, answer, input_param = type2()
    elif types == 3:
        ques, answer, input_param = type3()
    elif types == 4 or types == 5:
        ques, answer, input_param = type4()
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

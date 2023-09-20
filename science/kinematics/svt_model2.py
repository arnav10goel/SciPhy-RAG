import random
import json

no_of_samples = 40

data = []

s_to_r = 2 * 3.14

def calculation_r(v, t): 
    return round((v * t) / s_to_r, 1)

def calculation_v(r, t):
    return round((s_to_r * r) / t, 1)

def calculation_t(r, v):
    return round((s_to_r * r ) / v, 1)

def type1():
    v = random.randint(1, 1000)
    t = random.randint(1, 1000)
    r = calculation_r(v, t)
    q = "If an artificial satellite moving with a speed of " + str(v) + " m/s in a circular orbit takes " + str(t) + " s to complete a rotation, then what is the radius of its orbit?"
    answer = "The radius of the orbit is " + str(r) + " m."
    input_param = "v = " + str(v) + " m/s, t = " + str(t) + " s"
    return q, answer, input_param

def type2():
    r = random.randint(1100, 2100)
    t = random.randint(1, 1000)
    v = calculation_v(r, t)
    q = "If an artificial satellite is moving in a circular orbit of radius " + str(r) + " m, then calculate its speed if it takes " + str(t) + " s to complete a rotation?"
    answer = "The speed of the satellite is " + str(v) + " m/s."
    input_param = "r = " + str(r) + " m, t = " + str(t) + " s"
    return q, answer, input_param

def type3():
    r = random.randint(1100, 2100)
    v = random.randint(1, 1000)
    t = calculation_t(r, v)
    q = "If an artificial satellite moving with a speed of " + str(v) + " m/s in a circular orbit of radius " + str(r) + " m, calculate the time taken by it to complete a rotation?"
    answer = "The time taken to complete a rotation is " + str(t) + " s."
    input_param = "r = " + str(r) + " m, v = " + str(v) + " m/s"
    return q, answer, input_param

for i in range(no_of_samples):
    types = random.randint(0, 2)
    if types == 0:
        ques, answer, input_param = type1()
    elif types == 1:
        ques, answer, input_param = type2()
    elif types == 2:
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
import random
import json

no_of_samples = 20

data = []

def calculation_s(v, t): 
    return round(v * t, 1)

def calculation_v(s, t):
    return round(s / t, 1)

def calculation_t(s, v):
    return round(s / v, 1)

def type1():
    v = random.randint(1, 1000)
    t = random.randint(1, 1000)
    s = calculation_s(v, t)
    q = "What distance will a car travelling with a constant velocity of " + str(v) + " m/s for time " + str(t) + " s will travel?"
    answer = "The car will travel a distance of " + str(s) + " m."
    input_param = "v = " + str(v) + " m/s, t = " + str(t) + " s"
    return q, answer, input_param

def type2():
    s = random.randint(8000, 10000)
    t = random.randint(1, 1000)
    v = calculation_v(s, t)
    q = "A Car travelling with constant velocity has travelled a distance of " + str(s) + " m in " + str(t) + " s, then what is the velocity of the car?"
    answer = "The velocity of the car is " + str(v) + " m/s."
    input_param = "s = " + str(s) + " m, t = " + str(t) + " s"
    return q, answer, input_param

def type3():
    s = random.randint(8000, 10000)
    v = random.randint(1, 1000)
    t = calculation_t(s, v)
    q = "How much time will a car travelling with a constant velocity of " + str(v) + " m/s take to travel a distance of " + str(s) + " m?"
    answer = "The car will take " + str(t) + " s to travel the distance."
    input_param = "s = " + str(s) + " m, v = " + str(v) + " m/s"
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

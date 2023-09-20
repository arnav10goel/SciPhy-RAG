import random
import json

no_of_samples = 20
speed_of_light = 300000000

data = []

def calculation_s(t): 
    return round((speed_of_light * t) / 1000, 1)

def calculation_t(s):
    return round(s / speed_of_light, 5)

def type1():
    t = random.randint(1, 1000000) / 1000000
    s = calculation_s(t)
    q = "A signal from a spaceship reached the ground station in " + str(round(t * 1000, 1)) + " ms, then what was the distance of the spaceship from the ground station? (Signal travels with the speed of light)"
    answer = "The distance of the spaceship from the ground station is " + str(s) + " km."
    input_param = "t = " + str(round(t * 1000, 1)) + " ms"
    return q, answer, input_param

def type2():
    s = random.randint(int(speed_of_light / 10000), int(speed_of_light))
    t = calculation_t(s)
    q = "Distance of a spaceship from the ground station is " + str(round(s / 1000, 1)) + " km, then in what time will a signal from the ground station reach the spaceship? (Signal travels with the speed of light)"
    answer = "The time taken for the signal to reach the spaceship is " + str(round(t * 1000, 1)) + " ms."
    input_param = "s = " + str(round(s / 1000, 1)) + " km"
    return q, answer, input_param

for i in range(no_of_samples):
    types = random.randint(0, 1)
    if types == 0:
        ques, answer, input_param = type1()
    elif types == 1:
        ques, answer, input_param = type2()
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

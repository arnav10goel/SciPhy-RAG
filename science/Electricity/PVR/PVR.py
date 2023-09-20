import random
import math
import json

samples = []
no_of_samples = 30

def calculation_P(V, R):
    return round((V * V) / R, 1)

def calculation_V(P, R):
    return round(math.sqrt(P * R), 1)

def calculation_R(P, V):
    return round((V * V) / P, 1)

def type1():
    R = random.randint(1, 1000)
    V = random.randint(10, 19)
    t = random.randint(1, 1000)
    P = calculation_P(V, R)
    q = f"An Electric bulb of resistance {R} ohm draws current from the service mains of potential difference {V} V in {t} s. Calculate the rate at which heat is developed in the bulb?"
    input_formula = "power = (V * V) / R"
    explanation = f"The rate at which heat is developed in the bulb can be calculated using the formula: power = (V * V) / R, where V is the potential difference and R is the resistance."
    output = f"{P} watt\n\n{explanation}"
    return q, input_formula, output

def type2():
    P = random.randint(1, 100)
    R = random.randint(1, 100)
    t = random.randint(1, 2000)
    V = calculation_V(P, R)
    q = f"An Electric bulb of resistance {R} ohm produces heat at {P} W for {t} s. Calculate the potential difference maintained at service mains?"
    input_formula = "V = sqrt(P * R)"
    explanation = f"The potential difference maintained at service mains can be calculated using the formula: V = sqrt(P * R), where P is the power and R is the resistance."
    output = f"{V} volt\n\n{explanation}"
    return q, input_formula, output

def type3():
    P = random.randint(1, 1000)
    V = random.randint(10, 110)
    t = random.randint(1, 100)
    R = calculation_R(P, V)
    q = f"An Electric bulb draws current from the service mains of potential difference {V} V and produces heat at {P} W for {t} s. Calculate the resistance of the bulb?"
    input_formula = "R = (V * V) / P"
    explanation = f"The resistance of the bulb can be calculated using the formula: R = (V * V) / P, where V is the potential difference and P is the power."
    output = f"{R} ohm\n\n{explanation}"
    return q, input_formula, output

for i in range(no_of_samples):
    types = random.randint(0, 3)
    if types == 0:
        ques, input_formula, answer = type1()
    elif types == 1 or types == 3:
        ques, input_formula, answer = type2()
    elif types == 2:
        ques, input_formula, answer = type3()
    sample = {
        'instruction': ques,
        'input': input_formula,
        'output': answer,
    }
    samples.append(sample)

# Load existing JSON file
with open("science/Electricity/elec.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/Electricity/elec.json", "w") as file:
    json.dump(existing_data, file, indent=4)

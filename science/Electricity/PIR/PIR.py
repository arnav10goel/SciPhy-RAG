import random
import json
import math

samples = []
no_of_samples = 20

def calculation_P(I, R): 
    return I * I * R

def calculation_I(P, R):
    return round(math.sqrt(P / R), 1)

def calculation_R(P, I):
    return round(P / (I * I), 1)

def type1():
    R = random.randint(1, 100)
    I = random.randint(1, 10)
    t = random.randint(1, 10000)
    P = calculation_P(I, R)
    q = f"An Electric heater of resistance {R} ohm draws {I} A current from the service mains in {t} s. Calculate the rate at which heat is developed in the heater?"
    input_formula = "Rate of Heat Development = I^2 * R"
    explanation = "The rate at which heat is developed in the heater can be calculated using the formula: Rate of Heat Development = I^2 * R, where I is the current and R is the resistance."
    output = str(P) + " watt\n\n" + explanation
    return q, input_formula, output

def type2():
    P = random.randint(50, 149)
    R = random.randint(1, 100)
    t = random.randint(1, 2000)
    I = calculation_I(P, R)
    q = f"An Electric heater of resistance {R} ohm produces heat at {P} W for {t} s. Calculate the current drawn from the service mains?"
    input_formula = "Current Drawn = sqrt(P / R)"
    explanation = "The current drawn from the service mains can be calculated using the formula: Current Drawn = sqrt(P / R), where P is the power and R is the resistance."
    output = str(I) + " ampere\n\n" + explanation
    return q, input_formula, output

def type3():
    P = random.randint(10, 1010)
    I = random.randint(1, 10)
    t = random.randint(1, 1000)
    R = calculation_R(P, I)
    q = f"An Electric heater draws {I} A current from the service mains produces heat at {P} W for {t} s. Calculate the resistance of the heater?"
    input_formula = "Resistance = P / (I^2)"
    explanation = "The resistance of the heater can be calculated using the formula: Resistance = P / (I^2), where P is the power and I is the current."
    output = str(R) + " ohm\n\n" + explanation
    return q, input_formula, output

for i in range(no_of_samples):
    types = random.randint(0, 3)
    if types == 0:
        ques, input_formula, output = type1()
    if types == 1 or types == 3:
        ques, input_formula, output = type2()
    if types == 2:
        ques, input_formula, output = type3()
    sample = {
        'instruction': ques,
        'input': input_formula,
        'output': output,
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

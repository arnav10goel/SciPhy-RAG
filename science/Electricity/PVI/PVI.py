import random
import json

samples = []
no_of_samples = 20

def calculation_P(V, I):
    return V * I

def calculation_I(P, V):
    return round(P / V, 1)

def calculation_V(P, I):
    return round(P / I, 1)

def type1():
    V = random.randint(1, 1000)
    I = random.randint(1, 1000)
    P = calculation_P(V, I)
    q = f"{I} A of current flows through a circuit with a battery of potential difference {V} V. Calculate the rate of heat generated?"
    input_formula = "power = V * I"
    explanation = f"The rate of heat generated can be calculated using the formula: power = V * I, where V is the potential difference and I is the current."
    output = f"{P} watt\n\n{explanation}"
    return q, input_formula, output

def type2():
    P = random.randint(100, 1100)
    I = random.randint(1, 1000)
    V = calculation_V(P, I)
    q = f"{I} A of current flows through a circuit. If the rate of heat generated is {P} W, calculate the potential difference of the battery?"
    input_formula = "V = P / I"
    explanation = f"The potential difference of the battery can be calculated using the formula: V = P / I, where P is the rate of heat generated and I is the current."
    output = f"{V} volt\n\n{explanation}"
    return q, input_formula, output

def type3():
    P = random.randint(100, 1100)
    V = random.randint(1, 1000)
    I = calculation_I(P, V)
    q = f"In a circuit with a battery of potential difference {V} V, if the rate of heat generated is {P} W, calculate the current in the circuit?"
    input_formula = "I = P / V"
    explanation = f"The current in the circuit can be calculated using the formula: I = P / V, where P is the rate of heat generated and V is the potential difference."
    output = f"{I} ampere\n\n{explanation}"
    return q, input_formula, output

for i in range(no_of_samples):
    types = random.randint(0, 2)
    if types == 0:
        ques, input_formula, answer = type1()
    elif types == 1:
        ques, input_formula, answer = type2()
    else:
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

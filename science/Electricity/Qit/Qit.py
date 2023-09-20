import random
import json

samples = []
no_of_samples = 30

def calculation_Q(I, t): 
    return I * t

def calculation_I(Q, t):
    return round(Q / t, 1)

def calculation_t(Q, I):
    return round(Q / I, 1)

def type1():
    t = random.randint(1, 1000)
    I = random.randint(1, 1000)
    Q = calculation_Q(I, t)
    Q = "{:.2e}".format(Q)
    q = f"If current flowing through a conductor is {I} A, then what is the charge flown through the conductor in {t} s?"
    input_formula = "Q = I * t"
    explanation = "The charge flown through the conductor can be calculated using the formula: Q = I * t, where I is the current and t is the time."
    output = f"{Q} coulomb\n\n{explanation}"
    return q, input_formula, output

def type2():
    Q = random.randint(100, 1100)
    I = random.randint(1, 1000)
    t = calculation_t(Q, I)
    t = round(t, 1)
    q = f"If the current flowing through a conductor is {I} A, then what is the time taken for {Q} C charge to flow through the conductor?"
    input_formula = "t = Q / I"
    explanation = "The time taken for the charge to flow through the conductor can be calculated using the formula: t = Q / I, where Q is the charge and I is the current."
    output = f"{t} s\n\n{explanation}"
    return q, input_formula, output

def type3():
    Q = random.randint(100, 1100)
    t = random.randint(1, 1000)
    I = calculation_I(Q, t)
    I = round(I, 1)
    q = f"If {Q} coulomb of charge flows through any section of a conductor in {t} s, what is the value of current?"
    input_formula = "I = Q / t"
    explanation = "The value of the current can be calculated using the formula: I = Q / t, where Q is the charge and t is the time."
    output = f"{I} ampere\n\n{explanation}"
    return q, input_formula, output

for i in range(no_of_samples):
    types = random.randint(0, 2)
    if types == 0:
        ques, input_formula, answer = type1()
    elif types == 1:
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

# Save the updated JSON data
with open("science/Electricity/elec.json", "w") as file:
    json.dump(existing_data, file, indent=4)

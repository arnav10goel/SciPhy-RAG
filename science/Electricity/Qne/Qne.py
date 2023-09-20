import random
import json

samples = []
no_of_samples = 20
charge_of_electron = 1.6 * 1e-19

def calculation_n(Q):
    return round(Q / charge_of_electron)

def calculation_Q(n):
    return round(float(n) * charge_of_electron, 1)

def type1():
    Q = random.randint(1, 1000000) * charge_of_electron
    n = calculation_n(Q)
    n = "{:.2e}".format(n)
    q = f"Calculate the number of electrons constituting {Q:.2e} C of charge?"
    input_formula = "n = Q / e"
    explanation = "The number of electrons can be calculated using the formula: n = Q / e, where Q is the charge and e is the charge of an electron."
    output = f"{n} electrons\n\n{explanation}"
    return q, input_formula, output

def type2():
    n = random.randint(int(1e18), int(1e19))
    n = "{:.2e}".format(n)
    Q = calculation_Q(n)
    Q = "{:.2e}".format(Q)
    q = f"Calculate the charge (in C) of {n} electrons?"
    input_formula = "Q = n * e"
    explanation = "The charge of electrons can be calculated using the formula: Q = n * e, where n is the number of electrons and e is the charge of an electron."
    output = f"{Q} coulomb\n\n{explanation}"
    return q, input_formula, output

for i in range(no_of_samples):
    types = random.randint(0, 1)
    if types == 0:
        ques, input_formula, answer = type1()
    elif types == 1:
        ques, input_formula, answer = type2()
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

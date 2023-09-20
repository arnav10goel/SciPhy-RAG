import random
import json

samples = []
no_of_samples = 30
e = 1.6 * 1e-19

def type1():
    I = random.randint(1, 1000)
    t = random.randint(1, 1000)
    n = (I * t) / e
    q = f"A steady current of {I} A flows through a conductor, then calculate the number of electrons through any cross section of the conductor in {t} s?"
    input_formula = "n = (I * t) / e"
    explanation = f"The number of electrons through any cross section of the conductor can be calculated using the formula: n = (I * t) / e, where I is the current, t is the time, and e is the charge of an electron."
    output = f"{n}\n\n{explanation}"
    return q, input_formula, output

def type2():
    n = random.randint(1e19, 1e20)
    t = random.randint(1, 10)
    I = (n * e) / t
    I = round(I, 1)
    q = f"A steady current flows through a conductor, if the number of electrons through any cross section of the conductor in {t} s is {n}, then calculate the value of the current?"
    input_formula = "I = (n * e) / t"
    explanation = f"The value of the current can be calculated using the formula: I = (n * e) / t, where n is the number of electrons, e is the charge of an electron, and t is the time."
    output = f"{I} ampere\n\n{explanation}"
    return q, input_formula, output

def type3():
    n = random.randint(1e19, 1e20)
    I = random.randint(1, 10)
    t = (n * e) / I
    t = round(t, 1)
    q = f"A steady current of {I} A flows through a conductor, then calculate the time taken for {n} electrons to pass through any cross section of the conductor?"
    input_formula = "t = (n * e) / I"
    explanation = f"The time taken for the electrons to pass through any cross section of the conductor can be calculated using the formula: t = (n * e) / I, where n is the number of electrons, e is the charge of an electron, and I is the current."
    output = f"{t} s\n\n{explanation}"
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

# Save updated samples to the JSON file with indentation
with open("science/Electricity/elec.json", "w") as file:
    json.dump(existing_data, file, indent=4)

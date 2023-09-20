import random
import math
import json

samples = []
no_of_samples = 20

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1, 4)
    L = random.randint(1, 200)
    C = random.randint(1, 200)
    Q = random.randint(1, 200)
    E = 0.5 * (Q ** 2) * (1 / C)
    v = 1 / (2 * math.pi * math.sqrt(L * C * (10 ** (-9))))
    question = "An LC circuit contains a {} mH inductor and a {} muF capacitor with an initial charge of {} mC. The resistance of the circuit is negligible. Let the instant the circuit is closed be t = 0. ".format(L, C, Q)
    input_formula = ""
    output = ""

    if types <= 2:
        if types == 1:
            question += "What is the initial energy stored, is it conserved during LC oscillations?"
            input_formula = "Initial Energy = 0.5 * (Charge^2) * (1 / Capacitance)"
            output = "{:.2e} joule, it is conserved during oscillations.".format(E)
        else:
            question += "What is the natural frequency of the circuit."
            input_formula = "Natural Frequency = 1 / (2 * pi * sqrt(Inductance * Capacitance))"
            output = "{:.2e} hertz".format(v)
    else:
        x = random.randint(0, 100)
        arr = ["electrical", "magnetic"]
        question += "At what time(s) energy stored in {} form is {} percent of total energy?".format(arr[types - 3], x)
        if types == 4:
            x = 100 - x
        x = x / 100
        angle = math.acos(2 * x - 1)
        T = (1 / v)
        frac = (1 / (4 * math.pi)) * angle
        input_formula = "Time = n * T, where n is an integer\nT = 1 / (Natural Frequency)"
        output = "{}t, {}t, {}t, ...; where t = {:.2e} s".format(
            round(frac, 2), round(frac + 0.5, 2), round(frac + 1, 2), T
        )

    sample["instruction"] = question
    sample["input"] = input_formula
    sample["output"] = output

    samples.append(sample)

# Load existing JSON data
with open("science/AlternatingCurrent/ac.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/AlternatingCurrent/ac.json", "w") as file:
    json.dump(existing_data, file, indent=4)

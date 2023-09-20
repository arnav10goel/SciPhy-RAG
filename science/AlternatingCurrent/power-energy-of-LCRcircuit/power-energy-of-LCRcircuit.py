import random
import math
import json

samples = []
no_of_samples = 20

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1, 2)
    question = ""
    input_formula = ""
    output = ""

    if types == 1:
        L = random.randint(1, 200)
        C = random.randint(1, 200)
        Q = random.randint(1, 200)
        question = "Suppose the initial charge on the capacitor in an LC circuit with {} muF capacitor and {} mH inductor is {} mC. What is the total energy stored in the circuit initially? What is the total energy at later time?".format(C, L, Q)
        input_formula = "Initial Energy = 0.5 * Q^2 * (1 / C)"
        output = "{:.2e} joule, final value is same as initial value".format(0.5 * Q * Q * (1 / C))
    elif types == 2:
        R = random.randint(1, 200)
        L = random.randint(1, 200)
        C = random.randint(1, 200)
        question = "A series LCR circuit with R = {} ohm, L = {} H and C = {} muF is connected to a variable frequency of 200 V ac supply. When the frequency of the supply equals the natural frequency of the circuit, what is the average power transferred to the circuit in one complete cycle?".format(R, L, C)
        input_formula = "Average Power = (V^2 / R)"
        output = "{} watt".format(round((200 * 200) / R, 1))

    sample["instruction"] = question
    sample["input"] = input_formula
    sample["output"] = output

    samples.append(sample)

# Load existing JSON data
json_file_path = "science/AlternatingCurrent/ac.json"
existing_data = []

try:
    with open(json_file_path, "r") as file:
        existing_data = json.load(file)
except FileNotFoundError:
    pass

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open(json_file_path, "w") as file:
    json.dump(existing_data, file, indent=4)

import random
import math
import json

samples = []
no_of_samples = 20

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1, 2)

    if types == 1:
        L = round(random.randint(20, 80) / 100, 2)
        R = random.randint(50, 250)
        V = random.randint(220, 240)
        f = random.randint(20, 80)
        q = "A coil of inductance {} H and resistance {} ohm is connected to a {} V, {} Hz ac supply. What is the time lag between voltage maximum and current maximum?".format(
            L, R, V, f)
        input_formula = "Time_lag = atan((f * L * 2 * pi) / R) / (2 * pi * f)"
        a = "{:.2e} s".format(math.atan((f * L * 2 * math.pi) / R) / (2 * math.pi * f))
    else:
        C = random.randint(20, 220)
        R = random.randint(10, 50)
        V = random.randint(220, 240)
        f = random.randint(20, 80)
        q = "A {} muF capacitor in series with a {} ohm resistance is connected to a {} V, {} Hz supply. What is the time lag between the current maximum and voltage maximum?".format(
            C, R, V, f)
        input_formula = "Time_lag = atan(1 / (f * C * 10^-6 * 2 * pi * R)) / (2 * pi * f)"
        a = "{:.2e} s".format(math.atan(1 / (f * C * (10 ** (-6)) * 2 * math.pi * R)) / (2 * math.pi * f))

    sample["instruction"] = q
    sample["input"] = input_formula
    sample["output"] = a

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

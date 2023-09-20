import random
import math
import json

samples = []
no_of_samples = 50
pi = math.pi

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1, 4)
    val = random.randint(1, 200)
    V = random.randint(20, 250)
    freq = random.randint(1, 200)

    if types == 1:
        q = "A {} ohm resistor is connected to a {} V, {} Hz ac supply. What is the rms value of current in the circuit?".format(
            val, V, freq)
        input_formula = "I_rms = V / R"
        a = "{:.2e} ampere".format(V / val)
    elif types == 2:
        q = "A {} ohm resistor is connected to a {} V, {} Hz ac supply. What is the net power consumed over a full cycle?".format(
            val, V, freq)
        input_formula = "P_net = (V ** 2) / R"
        a = "{:.2e} watt".format((V * V) / val)
    elif types == 3:
        q = "A {} mH inductor is connected to {} V, {} Hz ac supply. Determine the rms value of current in the circuit?".format(
            val, V, freq)
        input_formula = "X_l = 2 * pi * f * L * 0.001\nI_rms = V / X_l"
        xl = 2 * pi * val * 0.001 * freq
        a = "{:.2e} ampere".format(V / xl)
    elif types == 4:
        q = "A {} microfarad capacitor is connected to a {} V, {} Hz ac supply. Determine the rms value of current in the circuit?".format(
            val, V, freq)
        input_formula = "X_c_inverse = 2 * pi * f * C * 0.000001\nI_rms = V * X_c_inverse"
        xc_inverse = 2 * pi * val * freq * 0.000001
        a = "{:.2e} ampere".format(V * xc_inverse)

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

import random
import math
import json

samples = []
no_of_samples = 20
pi = math.pi

for i in range(no_of_samples):
    sample = {}
    f1 = random.randint(100, 2000)
    f2 = random.randint(100, 400)
    L = random.randint(100, 400)
    question = "A radio can tune over the frequency range of a portion of MW broadcast band: ({} kHz to {} kHz). If its LC circuit has an effective inductance of {} muH, what must be the range of its variable capacitor?".format(f1, f1 + f2, L)
    input_formula = "w1 = 2 * pi * f1\nC1 = 1 / ((w1 ** 2) * L)\nw2 = 2 * pi * (f1 + f2)\nC2 = 1 / ((w2 ** 2) * L)"
    w1 = 2 * pi * f1
    C1 = 1 / ((w1 ** 2) * L)
    w2 = 2 * pi * (f1 + f2)
    C2 = 1 / ((w2 ** 2) * L)
    answer = "{:.2e} farad to {:.2e} farad".format(C2, C1)

    sample["instruction"] = question
    sample["input"] = input_formula
    sample["output"] = answer

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

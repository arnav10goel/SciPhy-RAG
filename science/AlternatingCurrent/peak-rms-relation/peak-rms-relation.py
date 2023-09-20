import random
import math
import json

samples = []
no_of_samples = 20
sqrt2 = math.sqrt(2)

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1, 2)
    val = random.randint(1, 2000000)
    question = ""
    input_formula = ""
    output = ""

    if types == 1:
        question = "The peak voltage of an ac supply is {} mV. What is the rms voltage?".format(val)
        input_formula = "RMS Voltage = Peak Voltage / sqrt(2)"
        output = "{:.3e} volt".format((val * 0.001) / sqrt2)
    elif types == 2:
        question = "The rms value of current in an ac circuit is {} microampere. What is the peak current?".format(val)
        input_formula = "Peak Current = RMS Current * sqrt(2)"
        output = "{:.3e} ampere".format(val * 0.000001 * sqrt2)

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

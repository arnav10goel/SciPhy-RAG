import random
import math
import json

samples = []
no_of_samples = 20

for i in range(no_of_samples):
    sample = {}
    l = random.randint(100, 40000)
    q = "A TV antenna is {} cm tall. How much service area can it cover if the receiving antenna is at ground level?".format(l)
    input_formula = "Service_area = pi * 2 * 6.4 * 10000 * l"
    a = "{:.2e} m2".format(math.pi * 2 * 6.4 * 10000 * l)

    sample["instruction"] = q
    sample["input"] = input_formula
    sample["output"] = a

    samples.append(sample)

# Load existing JSON data
json_file_path = "science/CommunicationSystems/comm.json"
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

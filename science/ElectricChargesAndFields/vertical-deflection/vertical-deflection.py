import random
import math
import json

samples = []

no_of_samples = 20

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1, 2)
    if types == 1:
        m = random.randint(1, 30) * 10
        q1 = random.randint(1, 20)
        v = random.randint(1, 20)
        L = random.randint(1, 30)
        E = random.randint(1, 20)
        q = "A particle of mass {} g and charge -({}) C enters a region between two charged particles initially moving along the x-axis with speed {} m/s. The length of plates is {} cm, and a uniform electric field of {} N/C is applied. Find the vertical deflection?\n".format(
            m, q1, v, L, E
        )
        num = q1 * E * L * L * 0.0001
        den = m * v * v * 0.001
        vertical_deflection = num / den
        a = "{:.2e}".format(vertical_deflection) + " m\n"
        input_str = "Vertical Deflection Formula: vertical_deflection = (q1 * E * L^2 * 0.0001) / (m * v^2 * 0.001)\n"

    else:
        v = random.randint(1, 2000) * 1000
        d = round(random.randint(1, 10) / 10, 2)
        E = random.randint(10, 400) * 10
        q = "An electron is projected between parallel plates separated by {} cm, having a field of {} N/C (up to down), with a speed of {} m/s. In what time will the electron strike the upper plate?\n".format(
            d, E, v
        )
        num = 2 * d * 0.01 * 9.1 * 10 ** (-31) * v * v
        den = 1.6 * 10 ** (-19) * E
        time_taken = math.sqrt(num / den)
        a = "{:.2e}".format(time_taken) + " s\n"
        input_str = "Time Taken Formula: time_taken = sqrt(2 * d * 0.01 * 9.1 * 10^(-31) * v^2 / (1.6 * 10^(-19) * E))\n"

    sample["instruction"] = q
    sample["input"] = input_str
    sample["output"] = a

    samples.append(sample)

# Load existing JSON file
with open("science/ElectricChargesAndFields/ecf.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/ElectricChargesAndFields/ecf.json", "w") as file:
    json.dump(existing_data, file, indent=4)

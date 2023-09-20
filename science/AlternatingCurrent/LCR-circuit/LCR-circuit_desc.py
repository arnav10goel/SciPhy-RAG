import random
import math
import json

samples = []
no_of_samples = 20

for i in range(no_of_samples):
    sample = {}
    L = random.randint(1, 200)
    C = random.randint(1, 200)
    R = random.randint(1, 200)
    question = "A series LCR circuit is connected to a variable frequency 230 V source with L = {} H, C = {} muF, R = {} ohm. ".format(L, C, R)
    types = random.randint(1, 16)
    input_formula = ""
    output = ""

    if types >= 1 and types <= 3:
        question += "Determine the source frequency which drives the circuit in resonance?"
        input_formula = "Source Frequency = 1 / sqrt(L * C)"
        output = "Source Frequency = {:.1f} rad/s".format(1 / math.sqrt(L * C * (10 ** -6)))
    elif types == 4:
        question += "Determine the impedance of the circuit at the resonating frequency?"
        input_formula = "Impedance = sqrt(R^2 + (ωL - 1 / (ωC))^2)"
        output = "Impedance = R = {} ohm".format(R)
    elif types >= 5 and types <= 7:
        question += "Determine the amplitude of current at the resonating frequency?"
        input_formula = "Current Amplitude = V_amplitude / Impedance"
        output = "Current Amplitude = {:.1f} A".format((230 * math.sqrt(2)) / R)
    elif types == 8:
        question += "Determine the RMS potential drop across resistance?"
        input_formula = "RMS Potential Drop across Resistance = Total Potential = 230 V"
        output = "RMS Potential Drop across Resistance = 230 V"
    elif types >= 9 and types <= 12:
        question += "Determine the RMS potential drop across inductance?"
        input_formula = "RMS Potential Drop across Inductance = Current RMS * ω_r * L"
        vl = (230 / R) * (1 / math.sqrt(L * C * (10 ** -6))) * L
        output = "RMS Potential Drop across Inductance = {:.2e} V".format(vl)
    elif types >= 13 and types <= 16:
        question += "Determine the RMS potential drop across capacitance?"
        input_formula = "RMS Potential Drop across Capacitance = Current RMS * 1 / (ω_r * C)"
        vc = (230 / R) * (1 / math.sqrt(L * C * (10 ** -6))) * L
        output = "RMS Potential Drop across Capacitance = {:.2e} V".format(vc)

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

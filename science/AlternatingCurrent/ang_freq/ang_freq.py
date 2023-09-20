import random
import math
import json

# Obtain the resonant angular frequency of a series LCR circuit with L = 2 H, C = 32 muF, R = 10 ohm.
# Obtain the Q-value of a series LCR circuit with L = 2 H, C = 32 muF, R = 10 ohm.
# A charged 30 muF capacitor is connected to 27 mH inductor. What is the angular frequency of free oscillations of the circuit?

samples = []

no_of_samples = 20

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1,3)
    if types == 1 or types == 2:
        L = random.randint(1,200)
        C = random.randint(1,200)
        R = random.randint(1,200)
        arr = ["resonant angular frequency","Q-value"]
        instruction = "Obtain the "+arr[types-1]+" of a series LCR circuit with L = "+str(L)+" H, C = "+str(C)+" muF, R = "+str(R)+" ohm?\n"
        if types == 1:
            output = str(round((1/math.sqrt(L*C*0.000001)),1))+" s-1\n"
        else:
            output = str(round(((1/R)*math.sqrt(L/(C*0.000001))),1)) + "\n"
        input_formula = "Q-value = (1 / R) * sqrt(L / (C * 0.000001))"
    elif types == 3:
        C = random.randint(1,2000)
        L = random.randint(1,2000)
        instruction = "A charged "+str(C)+" muF capacitor is connected to "+str(L)+" mH inductor. What is the angular frequency of free oscillations of the circuit?\n"
        output = str(round(1/math.sqrt(L*C*0.001*0.000001),1)) + " s-1\n"
        input_formula = "Angular frequency = 1 / sqrt(L * C * 0.001 * 0.000001)"
    sample["instruction"] = instruction
    sample["input"] = input_formula
    sample["output"] = output

    samples.append(sample)

# Load existing JSON file
with open("science/AlternatingCurrent/ac.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/AlternatingCurrent/ac.json", "w") as file:
    json.dump(existing_data, file, indent=4)

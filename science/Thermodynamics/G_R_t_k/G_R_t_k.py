import random
import math
import json

# The equilibrium constant for a reaction is n. Calculate the value of ΔG^o, given R = 8.3 J/Kmol and T = t.
# ΔG^o = -RTlnk

no_of_samples = 30

samples = []

R = 8.3

def cal(n, t) :
    ans = -1*R*t*math.log(n)*2.303
    return round(ans,1)

for i in range(no_of_samples):
    sample = {}
    n = random.randint(1,1000)
    t = random.randint(2730,3730)
    t = round(t/10,1)
    type = random.randint(1,2)
    if type == 1:
        ques = "The equilibrium constant for a reaction is " + str(n) + ". Calculate the value of ΔG^o, given R = 8.3 J/Kmol and T = " + str(t) + ".\n"
        input_formula = "ΔG^o = -2.303RTlogK or -RTlnK"
    else :
        ques = "The equilibrium constant for a reaction is " + str(n) + ". Calculate the value of ΔG^o, given T = " + str(t) + ".\n"
        input_formula = "ΔG^o = -2.303RTlogK or -RTlnK"
    answer = str(cal(n, t)) + "\n"
    answer += "To calculate the standard Gibbs free energy change (ΔG^o) for a reaction given the equilibrium constant (K), gas constant (R), and temperature (T), we can use the following equation: ΔG^o = -R * T * ln(K) where ln represents the natural logarithm."
    
    sample["instruction"] = ques
    sample["input"] = input_formula
    sample["output"] = answer

    samples.append(sample)

# Load existing JSON file
with open("science/Thermodynamics/thermo.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/Thermodynamics/thermo.json", "w") as file:
    json.dump(existing_data, file, indent=4) 

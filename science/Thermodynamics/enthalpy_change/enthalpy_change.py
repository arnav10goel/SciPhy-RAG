import random
import json

# Calculate the enthalpy change on freezing of n mol of water at T1 celcius to ice at T2 celcius. A, H = 6.03 KJ/mol at 0 celcius. Cp [H20(l)J = 75.3 J mol-1 K-1; Cp [H20(s)J = 36.8 J mol-1 K-1.

no_of_samples = 30

samples = []

h1 = 75.3
h2 = 36.8
h = 6030

def cal(n, t1, t2) :
    ans = round(h1*t1,1) + round(h2*t2,1) + h
    return round(ans*n,1)

for i in range(no_of_samples):
    sample = {}
    n = random.randint(1,20)
    t1 = random.randint(1,1000)
    t1 = round(t1/10,1)
    t2 = random.randint(-1000,-1)
    t2 = round(t2/10,1)
    types = random.randint(1,2)
    if types == 1 :
        ques = "Calculate the enthalpy change on freezing of " + str(n) + " mol of water at " + str(t1) + " celcius to ice at " + str(t2) + " celcius. Given, H = 6.03 KJ/mol at 0 celcius. Cp [H20(l)J = 75.3 J/molK; Cp [H20(s)J = 36.8 J/molK.\n"
        input_formula = "(ΔH)=(ΔH1)+(ΔH2)"
    else :
        ques = "Calculate the enthalpy change on freezing of " + str(n) + " mol of water at " + str(t1) + " celcius to ice at " + str(t2) + " celcius.\n"
    input_formula = "(ΔH)=(ΔH1)+(ΔH2)"
    answer = str(cal(n, t1, t2)) + "\n"
    answer += "Total enthalpy change involved in the transformation is the sum of the following changes and can be represented using the Hess Law."
    
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


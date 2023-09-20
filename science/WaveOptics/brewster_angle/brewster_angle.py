import random
import math
import json

# What is Brewster angle for a material-1 of refractive index mu1 to material-2 of refractive index mu2 transition.

no_of_samples = 10

samples = []

for i in range(no_of_samples):
    sample = {}
    mu1 = random.randint(101,300)
    mu1 = round(mu1/100,2)
    mu2 = mu1
    while(mu2 == mu1) :
        mu2 = random.randint(101,300)
        mu2 = round(mu2/100,2)
    ques = "What is Brewster angle for a material-1 of refractive index " + str(mu1) + " to material-2 of refractive index " + str(mu2) + " transition.\n"
    input_formula = "tan theta = mu2/mu1"
    answer = "{:.2e}".format(math.atan(mu2/mu1)) + " \n"
    answer += "The Brewster angle (θB) is the angle of incidence at which light with a specific polarization is perfectly transmitted through a boundary between two media with different refractive indices. It can be calculated using the formula: θ = arctan(mu2 / mu1), where mu1 and mu2 are the refractive indices of material-1 and material-2, respectively."
    
    sample["instruction"] = ques
    sample["input"] = input_formula
    sample["output"] = answer

    samples.append(sample)

# Load existing JSON file
with open("science/WaveOptics/wo.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/WaveOptics/wo.json", "w") as file:
    json.dump(existing_data, file, indent=4) 

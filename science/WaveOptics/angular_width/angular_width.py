import random
import math
import json

# In a double-slit experiment the angular width of a fringe is found to be d degrees on a screen placed D m away. The wavelength of light used is l nm. What will be the angular width of the fringe if the entire experimental apparatus is immersed in liquid of refractive index mu.

no_of_samples = 20

samples = []

for i in range(no_of_samples):
    sample = {}
    d = random.randint(1,10)
    d = round(d/10,1)
    D = random.randint(1,10)
    mu = random.randint(101,200)
    mu = round(mu/100,2)
    l = random.randint(1,100)
    ques = "In a double-slit experiment the angular width of a fringe is found to be " + str(d) + " degrees on a screen placed " + str(D) + " m away. The wavelength of light used is " + str(l) + " nm. What will be the angular width of the fringe if the entire experimental apparatus is immersed in liquid of refractive index " + str(mu) + ".\n"
    input_formula = "refractive index = angular width before immersing in water/angular width after immersing in water"
    answer = "{:.2e}".format(d/mu) + " degrees\n"
    answer += "To calculate the angular width of a fringe when the entire experimental apparatus is immersed in a liquid of refractive index (μ), we need to consider the effect of the refractive index on the wavelength of light."
    answer += "we can calculate the angular width of the fringe in the liquid (θ2') using the formula: θ2' = sin^(-1)(λ' / d), where d is the distance to the screen (D) in meters."
    
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
import random
import math
import json

# What is the De-Broglie wavelength associated with a mass of m kg and having a velocity of v m/s.

no_of_samples = 10

samples = []

h = 6.626 * (10**-34)

for i in range(no_of_samples):
    sample = {}
    m = random.randint(1,10000000)
    m = round(m/10000000,7)
    v = random.randint(1,100)
    t = random.randint(1,2)
    if t == 1 :
        ques = "What is the De-Broglie wavelength associated with a mass of " + "{:.4e}".format(m) + " kg and having a velocity of " + str(v) + " m/s.\n"
    else :
        ques = "What is the De-Broglie wavelength associated with a mass of " + "{:.4e}".format(m) + " kg and having a velocity of " + str(v) + " m/s. (h = 6.626 x 10^-34 Js)\n"
    input_formula = "wavelength = Planck's constant/mass*velocity"
    answer = "{:.2e}".format(h/(m*v)) + " \n"
    answer += "The de Broglie wavelength (λ) associated with a particle can be calculated using the de Broglie wavelength equation: λ = h / (m * v), where λ is the wavelength, h is the Planck constant (approximately 6.626 x 10^-34 J·s), m is the mass of the particle, and v is its velocity."
    
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

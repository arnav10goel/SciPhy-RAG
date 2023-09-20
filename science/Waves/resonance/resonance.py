import random
import json

# A metre-long tube open at one end, with a movable piston at the other end, shows resonance with a fixed frequency source (a turning fork of frequency 340 Hz) when the tube length is 25.5 cm or 79.3 cm. Estimate the speed of sound in air at the temperature of the experiment. The edge effect may be neglected.

no_of_samples = 20
# no_of_samples = 10

samples = []

for i in range(no_of_samples):
    sample = {}
    freq = random.randint(100,1100)
    length = random.randint(5,95)
    error = random.randint(-8,8)
    q = "A 3m long tube open at one end, with a movable piston at the other end, shows resonance with a fixed frequency source (a turning fork of frequency "+str(freq)+" Hz) when the tube length is "+str(length)+" cm or "+str(length*3+error)+" cm. Estimate the speed of sound in air.\n"
    input_formula = "wavelength = 4*length of tube, speed of sound = frequency*wavelength"
    a = "{:.2e}".format((freq*4*length)/100)+" ms-1\n"
    a += "Since the given pipe is attached with a piston at one end, it will behave as a pipe with one end closed and the other end open. Such a system produces odd harmonics."
    
    sample["instruction"] = q
    sample["input"] = input_formula
    sample["output"] = a

    samples.append(sample)

# Load existing JSON file
with open("science/Waves/wave.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/Waves/wave.json", "w") as file:
    json.dump(existing_data, file, indent=4) 
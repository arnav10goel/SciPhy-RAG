import random
import math
import json

# A stone dropped from the top of a tower of height 300 m high splashes into the water of a pond near the base of the tower. When is the splash heard at the top given that the speed of sound in air is 340 ms-1 ? (g = 9.8 ms-2 )

no_of_samples = 20
# no_of_samples = 10

samples = []

for i in range(no_of_samples):
    sample = {}
    h = random.randint(20,2000)
    m = random.randint(2,2000)
    if random.randint(0,1):
        q = "A stone of mass "+str(m)+" g dropped from the top of a tower of height "+str(h)+" m high splashes into the water of a pond near the base of the tower. When is the splash heard at the top given that the speed of sound in air is 340 ms-1 ? (g = 9.8 ms-2 )\n"
        input_formula = "Height = Initial Speed + 1/2*g*time^2, Total time = t1+t2"
    else:
        q = "A stone of mass "+str(m)+" g dropped from the top of a tower of height "+str(h)+" m high splashes into the water of a pond near the base of the tower. When is the splash heard at the top given.\n"
    t1 = math.sqrt((2*h)/9.8)
    t2 = h/340
    input_formula = "Height = Initial Speed + 1/2*g*time^2, Total time = t1+t2"
    a = str(round(t1+t2,2))+" s\n"
    a += "Use the equation of motion: Height = Initial Speed + 1/2*g*time^2, to calculate the time of splash heard."
    
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
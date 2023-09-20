import random
import json

samples = []
no_of_samples = 20

def determine_ohmic_conductor(observations):
    is_ohmic = all(observations[i][1] == observations[i][0] * R for i in range(len(observations)))
    return is_ohmic

for i in range(no_of_samples):
    sample = {}
    setOfNumbers = set()
    while len(setOfNumbers) < 6:
        setOfNumbers.add(random.randint(1, 40))
    arr = list(setOfNumbers)
    types = random.randint(0, 11)
    q = "Given observations (tuples of I (in A) and V (in V)): "
    R = random.randint(1, 20)
    observations = []
    for i in range(6):
        I = arr[i]
        V = arr[i] * R
        if types == i:
            noise = random.randint(-5, 5)
            while noise == 0:
                noise = random.randint(-5, 5)
            V += noise
        observation = (I, V)
        observations.append(observation)
        string = "(" + str(I) + ", " + str(V)
        if i != 5:
            string += "), "
        else:
            string += "); "
        q += string
    q += "Determine whether the given conductor is an ohmic conductor or not.\n"
    a = ""
    if determine_ohmic_conductor(observations):
        a = "Yes, it is an ohmic conductor.\n"
    else:
        a = "No, it is not an ohmic conductor.\n"
    
    sample['instruction'] = q
    sample['input'] = ""
    sample['output'] = a
    samples.append(sample)

# Load existing JSON file
with open("science/Electricity/elec.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/Electricity/elec.json", "w") as file:
    json.dump(existing_data, file, indent=4)

import random
import json

# Two sitar strings A and B playing the note ‘Ga’ are slightly out of tune and produce beats of frequency 6Hz. The tension in the string A is slightly reduced and the beat frequency is found to reduce to 3Hz. If the original frequency of A is 324 Hz, what is the frequency of B?

no_of_samples = 30
# no_of_samples = 10

samples = []

arr = ["reduced","increased"]

for i in range(no_of_samples):
    sample = {}
    fund = random.randint(100,1300)
    f1 = random.randint(1,60)
    f2 = random.randint(1,60)
    while f2 == f1:
        f2 = random.randint(1,60)
    types = random.randint(0,1)
    q = "Two sitar strings A and B playing the note ‘Ga’ are slightly out of tune and produce beats of frequency "+str(f1)+" Hz. The tension in the string A is slightly "+arr[types]+" and the beat frequency is found to be "+str(f2)+" Hz. If the original frequency of A is "+str(fund)+" Hz, what is the frequency of B?\n"
    input_formula = "Beat frequency = |f1+-f2|"
    if types == 0:
        if f2 < f1:
            a = str(fund-f1)+" hertz\n"
        else:
            a = str(fund+f1)+" hertz\n"
    else:
        if f2 < f1:
            a = str(fund+f1)+" hertz\n"
        else:
            a = str(fund-f1)+" hertz\n"
    a += "Frequency decreases with a decrease in the tension of a string.\nThis is because frequency is directly proportional to the square root of tension."
    
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
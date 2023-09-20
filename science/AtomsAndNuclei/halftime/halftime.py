import math
import random
import json

# A radioactive isotope has a half-life of T years. How long will it take the activity to reduce to p percent.

no_of_samples = 10

samples = []

for i in range(no_of_samples):
    sample = {}
    T = random.randint(1,1000)
    p = random.randint(10,990)
    p = round(p/10,1)
    ques = "A radioactive isotope has a half-life of " + str(T) + " years. How long will it take the activity to reduce to " + str(p) + " percent.\n"
    input_formula = "Time = Half Life/ln2 * ln(Initial Acitivity/Final Activity)"
    answ = (math.log(100/p)*T)/0.693
    answer = "{:.2e}".format(answ) + "years\n"
    answer += "To calculate the time it takes for the activity of a radioactive isotope to reduce to a certain percentage, we can use the concept of half-life. The half-life (T) is the time it takes for the activity of a radioactive substance to reduce by half. To find the time required to reduce the activity to a certain percentage (p), we can use the formula: t = T * log(0.01) / log(p/100), where t is the time required, T is the half-life, and p is the desired percentage."
    
    sample["instruction"] = ques
    sample["input"] = input_formula
    sample["output"] = answer

    samples.append(sample)

# Load existing JSON file
with open("science/AtomsAndNuclei/aan.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/AtomsAndNuclei/aan.json", "w") as file:
    json.dump(existing_data, file, indent=4) 
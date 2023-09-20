import random
import json

no_of_samples = 20

def cal1(w, n, d):
    return round(w * (1 / (1 + (n / d))), 1)

def cal2(w, n, d):
    return round(w * (1 - (n / d)), 1)

def type1():
    w = random.randint(1, 1000)
    n = random.randint(1, 100)
    d = random.randint(n + 1, n + 100)
    ques = f"A body weighs {w} N on the surface of the Earth. What is the gravitational force on it due to the Earth at a height equal to {n}/{d} the radius of the Earth?"
    input_formula = f"Weight on the Surface (W) = {w} N, Height Ratio (n/d) = {n}/{d}"
    output_explanation = f"The gravitational force on the body at a height equal to {n}/{d} the radius of the Earth is {cal1(w, n, d)} newtons."
    return ques, input_formula, output_explanation

def type2():
    w = random.randint(1, 1000)
    n = random.randint(1, 100)
    d = random.randint(n + 1, n + 100)
    ques = f"Assuming the Earth to be a sphere of uniform mass density, how much would a body weigh {n}/{d} down to the center of the Earth if it weighed {w} N on the surface?"
    input_formula = f"Weight on the Surface (W) = {w} N, Height Ratio (n/d) = {n}/{d}"
    output_explanation = f"The weight of the body {n}/{d} down to the center of the Earth, assuming a uniform mass density, would be {cal2(w, n, d)} newtons."
    return ques, input_formula, output_explanation

samples = []

for i in range(no_of_samples):
    sample = {}
    types = random.randint(0, 1)
    if types == 0:
        ques, input_formula, output_explanation = type1()
    elif types == 1:
        ques, input_formula, output_explanation = type2()

    sample["instruction"] = ques
    sample["input"] = input_formula
    sample["output"] = output_explanation

    samples.append(sample)

# Read the existing JSON file
with open("science/Gravitation/g.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/Gravitation/g.json", "w") as file:
    json.dump(existing_data, file, indent=4)

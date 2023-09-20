import random
import json

no_of_samples = 20

def type1():
    mass = random.randint(1, 2000)
    volume = random.randint(1, 200)
    density_another = random.randint(1, 10)
    ques = f"The volume of {mass} g of a substance is {volume} cm³. If the density of the liquid in which the substance is placed is {density_another} g/cm³, will the substance float or sink?"
    input_formula = f"Density of Substance = {mass / volume} g/cm³, Density of Liquid = {density_another} g/cm³"
    output_explanation = ""
    if mass / volume == density_another:
        output_explanation = "The substance will just sink."
    elif mass / volume > density_another:
        output_explanation = "The substance will sink."
    else:
        output_explanation = "The substance will float."

    return ques, input_formula, output_explanation

samples = []

for i in range(no_of_samples):
    sample = {}
    ques, input_formula, output_explanation = type1()

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

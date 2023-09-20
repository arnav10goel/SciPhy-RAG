import random
import math
import json

no_of_samples = 20

def calculate_pressure_difference(rate, length, radius, density, viscosity):
    V = (rate * (10 ** (-4))) / density
    p = (8 * V * viscosity * length * 100000) / (math.pi * (radius ** 4))
    return p

def generate_question(rate, length, radius, has_properties):
    properties_text = ""
    if has_properties:
        properties_text = f" (Density of glycerine = 1.3 x 10^3 kg/m^3 and viscosity of glycerine = 0.83 Pa s)"
    return f"Glycerine flows steadily through a horizontal tube of length {length} mm and radius {radius} cm. If the amount of glycerine collected per second at one end is {rate} x 10^(-4) kg/s, what is the pressure difference between the two ends of the tube?{properties_text}"

samples = []

for i in range(no_of_samples):
    length = random.randint(100, 2000)
    radius = random.randint(1, 10)
    rate = random.randint(100, 1000)
    has_properties = random.randint(0, 1)

    question = generate_question(rate, length, radius, has_properties)
    pressure_difference = calculate_pressure_difference(rate, length, radius, 1300, 0.83)
    input_formula = "pressure difference = (8 * V * viscosity * length * 100000) / (pi * (radius ** 4))"
    output = f"The pressure difference between the two ends of the tube is {pressure_difference:.2e} pascal."

    sample = {
        "instruction": question,
        "input": input_formula,
        "output": output
    }

    samples.append(sample)

# Read the existing JSON file
with open("science/MechanicalPropertiesOfLiquids/mpl.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/MechanicalPropertiesOfLiquids/mpl.json", "w") as file:
    json.dump(existing_data, file, indent=4)

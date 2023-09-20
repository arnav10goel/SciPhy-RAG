import random
import json

no_of_samples = 10

def generate_question(days, r):
    return f"Assume an unknown planet of orbital period {days} days is rotating around the sun with an orbit of radius {r} * 10^8 m. What is the ratio of the mass of the sun to the mass of the unknown planet?"

def generate_input_formula(days, r):
    return f"Mass Ratio = ((R_earth^3) * (T_planet^2)) / ((R_planet^3) * (T_earth^2)) = ((149.6 * 10^8)^3 * ({days}^2)) / (({r} * 10^8)^3 * (365.25^2))"

def generate_output_explanation(days, r):
    days_earth = 365.25
    rad_earth = 149.6 * (10**8)
    mass_ratio = ((rad_earth**3) * (days**2)) / ((r**3 * (10**24)) * (days_earth**2))
    return f"The ratio of the mass of the sun to the mass of the unknown planet is approximately {mass_ratio:.1f}."

samples = []

for i in range(no_of_samples):
    sample = {}
    days = random.randint(200, 2000)
    r = random.randint(1, 2000)

    question = generate_question(days, r)
    input_formula = generate_input_formula(days, r)
    output_explanation = generate_output_explanation(days, r)

    sample["instruction"] = question
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

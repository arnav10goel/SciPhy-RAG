import random
import json

no_of_samples = 10

def generate_question(m, M, r, h, is_energy=True):
    question_type = "energy" if is_energy else "potential"
    return f"A satellite orbits the earth at a height of {h} km above the surface. How much {question_type} must be expended to rocket the satellite out of the planet's gravitational influence? Mass of the satellite = {m} kg; mass of the planet = {M} kg; radius of the planet = {r} m."

def generate_input_formula(m, M, r, h, is_energy=True):
    g = 6.67 * (10**-11)
    formula_type = "(g * m * M) / (2 * (r + h))" if is_energy else "-(g * m * M) / (r + h)"
    return f"{formula_type}"

def generate_output_explanation(m, M, r, h, is_energy=True):
    g = 6.67 * (10**-11)
    energy = (g * m * M) / (2 * (r + h)) if is_energy else -(g * m * M) / (r + h)
    return f"The {'' if is_energy else 'gravitational '}{'energy' if is_energy else 'potential'} required to rocket the satellite out of the planet's gravitational influence is approximately {energy:.2e} joules."

samples = []

for i in range(no_of_samples):
    sample = {}
    m = 200
    M = 6.0 * (10**24)
    r = 6.4 * (10**6)
    h = random.randint(100, 1100)
    is_energy = random.randint(0, 1)

    question = generate_question(m, M, r, h, is_energy)
    input_formula = generate_input_formula(m, M, r, h, is_energy)
    output_explanation = generate_output_explanation(m, M, r, h, is_energy)

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

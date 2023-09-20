import random
import json

no_of_samples = 10

def generate_question(m, M, h, R, is_energy):
    question_type = "potential energy" if is_energy else "potential"
    return f"A satellite of mass {m} kg orbits around a planet at a height of {h} m from the surface of the planet. What is the gravitational {question_type} on the satellite due to the planet's magnetic field? Mass of the planet = {M} kg and radius of the planet = {R} m."

def generate_input_formula(m, M, h, R, is_energy):
    formula_type = "-M / (h + R)" if is_energy else "-M * m / (h + R)"
    return f"Gravitational {formula_type}"

def generate_output_explanation(m, M, h, R, is_energy):
    g = 6.67 * (10**-11)
    potential = -M / (h + R) if is_energy else -M * m / (h + R)
    return f"The gravitational {'potential energy' if is_energy else 'potential'} on the satellite due to the planet's magnetic field is approximately {potential:.2e} joule{'s' if is_energy else '/kg'}."

samples = []

for i in range(no_of_samples):
    sample = {}
    m = random.randint(400, 600)
    M = random.randint(1, 100) * (10**10)
    h = random.randint(1, 10) * (10**3)
    R = random.randint(1, 10) * (10**6)
    is_energy = random.randint(0, 1)

    question = generate_question(m, M, h, R, is_energy)
    input_formula = generate_input_formula(m, M, h, R, is_energy)
    output_explanation = generate_output_explanation(m, M, h, R, is_energy)

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

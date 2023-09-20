import random
import json
import math

no_of_samples = 10

def calculate_terminal_speed(r, den):
    return (2 / (9 * 1.8 * (10 ** (-5)))) * (r * r * den * 9.8 * (10 ** (-12)))

def calculate_viscous_force(r, vt):
    return 6 * math.pi * (1.8 * (10 ** (-5))) * r * (10 ** (-6)) * vt

def generate_question(r, den, is_viscous_force):
    if is_viscous_force:
        return f"In Mullikan’s oil drop experiment, what is the viscous force on the drop of radius {r} x 10^(-6) m and density {den} kg m-3 at terminal speed?"
    else:
        return f"In Mullikan’s oil drop experiment, what is the terminal speed of an uncharged drop of radius {r} x 10^(-6) m and density {den} kg m-3?"

def generate_input_formula(r, den):
    return f"(2 / (9 * 1.8 * (10 ** -5))) * ({r} ** 2 * {den} * 9.8 * (10 ** -12))"

def generate_output_explanation(result, is_viscous_force):
    if is_viscous_force:
        return f"The viscous force on the drop is {result:.2e} newton."
    else:
        return f"The terminal speed of the drop is {result:.2e} m/s."

samples = []

for i in range(no_of_samples):
    sample = {}
    r = random.randint(1, 2000)
    den = random.randint(1000, 3000)
    is_viscous_force = bool(random.getrandbits(1))

    question = generate_question(r, den, is_viscous_force)
    if is_viscous_force:
        result = calculate_terminal_speed(r, den)
    else:
        result = calculate_viscous_force(r, calculate_terminal_speed(r, den))
    input_formula = generate_input_formula(r, den)
    output_explanation = generate_output_explanation(result, is_viscous_force)

    sample["instruction"] = question
    sample["input"] = input_formula
    sample["output"] = output_explanation

    samples.append(sample)

# Read the existing JSON file
with open("science/MechanicalPropertiesOfLiquids/mpl.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/MechanicalPropertiesOfLiquids/mpl.json", "w") as file:
    json.dump(existing_data, file, indent=4)

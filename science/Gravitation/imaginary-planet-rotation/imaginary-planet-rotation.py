import random
import json

no_of_samples = 10

def generate_question(expr):
    return f"Suppose there existed a planet that went around the Sun {expr} times as fast as the Earth. What would be its orbital size as compared to that of the Earth?"

def generate_input_formula(expr):
    return f"Orbital Size Ratio = (T_p / T_e)^(2/3) = ({expr})^(2/3)"

def generate_output_explanation(expr):
    tp = eval(expr)
    rp = tp ** (2 / 3)
    return f"The orbital size of the planet compared to that of the Earth would be approximately {rp:.1f} times faster than Earth."

samples = []

for i in range(no_of_samples):
    sample = {}
    num = random.randint(1, 3000)
    den = random.randint(100, 3000)
    expr = f"{num}/{den}"

    question = generate_question(expr)
    input_formula = generate_input_formula(expr)
    output_explanation = generate_output_explanation(expr)

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

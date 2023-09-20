import random
import math
import json

no_of_samples = 30

def calculate_max_load(r, stress):
    max_load = (stress * math.pi * (r ** 2)) / 1000000
    return max_load

def calculate_max_tension(d, shearing_stress):
    r = d / 2
    max_tension = shearing_stress * math.pi * r ** 2 * 4 * (10 ** (-6))
    return max_tension

def generate_question_cable(r, stress):
    return f"A steel cable with a radius of {r} mm supports a chairlift at a ski area. If the maximum stress is not to exceed {stress} x 10^(6) Nm-2, what is the maximum load the cable can support?"

def generate_question_rivets(d, shearing_stress):
    return f"Two strips of metal are riveted together at their ends by four rivets, each of diameter {d} mm. What is the maximum tension that can be exerted by the riveted strip if the shearing stress on the rivet is not to exceed {shearing_stress}?"

samples = []

for i in range(no_of_samples):
    types = random.randint(1, 2)

    if types == 1:
        r = random.randint(1, 200)
        stress = random.randint(1, 40000)
        question = generate_question_cable(r, stress)
        max_load = calculate_max_load(r, stress)
        output = f"The maximum load the cable can support is {max_load:.1e} newton."

    else:
        d = random.randint(1, 20)
        shearing_stress = random.randint(100, 200000) * 100
        question = generate_question_rivets(d, shearing_stress)
        max_tension = calculate_max_tension(d, shearing_stress)
        output = f"The maximum tension that can be exerted by the riveted strip is {max_tension:.1e} newton."

    sample = {
        "instruction": question,
        "input": "",
        "output": output
    }

    samples.append(sample)

# Read the existing JSON file
with open("science/MechanicalPropertiesOfSolids/mps.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/MechanicalPropertiesOfSolids/mps.json", "w") as file:
    json.dump(existing_data, file, indent=4)

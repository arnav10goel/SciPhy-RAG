import random
import json
import math

no_of_samples = 10

def calculate_speed_of_ejection(A, num, dia, flow):
    a1 = A * (10 ** (-4))
    v1 = flow / 60
    a2 = math.pi * dia * dia * 0.25 * (10 ** (-6))
    return (a1 * v1) / a2

def generate_question(A, num, dia, flow):
    return f"The cylindrical tube of a spare pump has a cross-section of {A} cm², one end of which has {num} fine holes each of diameter {dia} mm. If the liquid flow inside the tube is {flow} m/min, what is the speed of ejection of the liquid through the holes?"

def generate_input_formula(A, num, dia, flow):
    return f"({A} * (10 ** -4) * ({flow} / 60)) / (math.pi * {dia} ** 2 * 0.25 * (10 ** -6))"

def generate_output_explanation(speed):
    return f"The speed of ejection of the liquid through the holes is {speed:.2e} m/s."

samples = []

for i in range(no_of_samples):
    sample = {}
    A = random.randint(1, 100)
    num = random.randint(1, 200)
    dia = random.randint(1, 10)
    flow = random.randint(1, 10)

    question = generate_question(A, num, dia, flow)
    speed = calculate_speed_of_ejection(A, num, dia, flow)
    input_formula = generate_input_formula(A, num, dia, flow)
    output_explanation = generate_output_explanation(speed)

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

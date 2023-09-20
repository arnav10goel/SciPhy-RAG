import random
import json
import math

no_of_samples = 20

def generate_question(m, R, r):
    return f"Two stars each of one solar mass {m} kg are approaching each other for a head-on collision. When they are at a distance {R} km, their speeds are negligible. What is the speed with which they collide? The radius of each star is {r} km. Assume the stars remain undistorted until they collide."

def generate_input_formula(m, R, r):
    return f"Speed = sqrt((-G*m/R) + (G*m/(2*r))) = sqrt(((-6.67 * 10^-11) * {m}) / ({R * 1000})) + ((6.67 * 10^-11) * {m}) / ({2 * r * 1000}))"

def generate_output_explanation(m, R, r):
    g = 6.67 * (10**-11)
    speed = math.sqrt((-g * m / (R * 1000)) + (g * m / (2 * r * 1000)))
    return f"The speed with which the stars collide is approximately {speed:.2e} m/s."

samples = []

for i in range(no_of_samples):
    sample = {}
    m = random.randint(1, 100) * (10**30)
    R = random.randint(1, 100) * (10**9)
    r = random.randint(1, 100) * (10**4)

    question = generate_question(m, R, r)
    input_formula = generate_input_formula(m, R, r)
    output_explanation = generate_output_explanation(m, R, r)

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

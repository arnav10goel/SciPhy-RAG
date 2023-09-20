import random
import json
import math

no_of_samples = 20

m = 9.1 * (10 ** -31)
e = 1.6 * (10 ** -19)
pi = math.pi

def calculate_radius(b, v, d):
    d = math.sin((d * pi) / 180)
    return (m * v) / (b * e * d)

def generate_question(b, v, d):
    q = f"In a chamber, a uniform magnetic field of {b} T is maintained. An electron is shot into the field with a speed of {v} m/s, making an angle of {d} degrees with the field. Determine the radius of the circular path of the electron."
    radius = calculate_radius(b, v, d)
    a = f"{radius:.2e} m"
    return q, a

samples = []

for i in range(no_of_samples):
    b = random.randint(1, 120) * (10 ** -4)
    v = random.randint(1, 120) * (10 ** 6)
    d = random.randint(1, 90)

    question, answer = generate_question(b, v, d)

    input_formula = "Radius = (m * v) / (b * e * sin(d))"
    output = f"To calculate the radius of the circular path, we use the following formula:\n\n{input_formula}\n\nWhere,\n- m = Mass of the electron\n- v = Speed of the electron\n- b = Magnetic field\n- e = Charge of the electron\n- d = Angle between the velocity vector and the magnetic field vector\n\nWe substitute the given values into the formula and evaluate it to find that the radius of the circular path of the electron is approximately {answer}."

    sample = {
        "instruction": question,
        "input": input_formula,
        "output": output
    }

    samples.append(sample)


# Read the existing JSON file
with open("science/MovingChargesAndMagnetism/mcm.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/MovingChargesAndMagnetism/mcm.json", "w") as file:
    json.dump(existing_data, file, indent=4)

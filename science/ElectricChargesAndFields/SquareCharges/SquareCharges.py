import random
import math
import json

samples = []

no_of_samples = 20

for i in range(no_of_samples):
    sample = {}
    q1 = random.randint(1, 20)
    q2 = random.randint(1, 20)
    q3 = random.randint(1, 20)
    q4 = random.randint(1, 20)
    qc = random.randint(1, 20)
    if random.randint(0, 1):
        q1 = -q1
    if random.randint(0, 1):
        q2 = -q2
    if random.randint(0, 1):
        q3 = -q3
    if random.randint(0, 1):
        q4 = -q4
    if random.randint(0, 1):
        qc = -qc
    d = random.randint(1, 20)
    q = "Four point charges q1 = {} x 10^(-6) C, q2 = {} x 10^(-6) C, q3 = {} x 10^(-6) C, q4 = {} x 10^(-6) C, are located at corners of square ABCD of side {} cm. What is the force on a charge of {} x 10^(-6) C placed at the centre of the square?\n".format(
        q1, q2, q3, q4, d, qc)
    d1 = d / math.sqrt(2)
    if q1 > q3:
        m1 = q1 - q3
    else:
        m1 = q3 - q1
    if q2 > q4:
        m2 = q2 - q4
    else:
        m2 = q4 - q2
    F = math.sqrt(m1 ** 2 + m2 ** 2) * qc * (9 * (10 ** 9)) * (10 ** (-12)) * (1 / (d * d * 0.0001))
    a = "To calculate the force on the charge placed at the center of the square, we use the formula for electric force between two point charges:\n"
    a += "Force (F) = k * |q1 - q3| * |q2 - q4| * q_c / (d^2)\n"
    a += "where k is Coulomb's constant (9 * 10^9 N·m²/C²), q1, q2, q3, q4 are the charges at the corners of the square (in Coulombs), q_c is the charge placed at the center of the square (in Coulombs), and d is the side length of the square (in meters).\n"
    a += "Given q1 = {} x 10^(-6) C, q2 = {} x 10^(-6) C, q3 = {} x 10^(-6) C, q4 = {} x 10^(-6) C, d = {} cm, and q_c = {} x 10^(-6) C:\n".format(q1, q2, q3, q4, d, qc)
    a += "Force (F) = {:.2e} N\n".format(F)

    sample["instruction"] = q
    sample["input"] = "Force (F) = k * |q1 - q3| * |q2 - q4| * q_c / (d^2)"
    sample["output"] = a

    samples.append(sample)

# Load existing JSON file
with open("science/ElectricChargesAndFields/ecf.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/ElectricChargesAndFields/ecf.json", "w") as file:
    json.dump(existing_data, file, indent=4)


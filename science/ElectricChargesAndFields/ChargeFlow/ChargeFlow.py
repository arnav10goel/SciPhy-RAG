import random
import json

samples = []

no_of_samples = 40

def force(q1, q2, d):
    const = 9 * (10 ** 9)
    F = const * q1 * q2 * (1 / d) * (1 / d) * (10 ** (-8))
    return F

for i in range(no_of_samples):
    sample = {}
    qa = random.randint(1, 200)
    qb = random.randint(1, 200)
    if random.randint(0, 1):
        qa = -qa
    if random.randint(0, 1):
        qb = -qb
    d = random.randint(1, 200)
    q = "Two spheres q1 of charge " + str(qa) + " x 10^(-6)C, q2 of charge " + str(qb) + " x 10^(-6)C are placed at a distance " + str(d) + " cm. If an uncharged sphere C first comes in contact with A, then with B and placed at " + str(d) + " cm from both of them, then what is the "
    types = random.randint(1, 15)
    if types < 3:
        q = q + "final charge on A?\n"
        a = "The final charge on sphere A can be calculated by dividing the initial charge qa by 2. Therefore, the final charge on A is " + str(round(qa / 2, 2)) + " coulomb\n"
        input_formula = "Final charge on A = qa / 2"
    elif types < 5:
        q = q + "final charge on B?\n"
        a = "The final charge on sphere B can be calculated by adding half of the initial charge qa and the full charge qb. Therefore, the final charge on B is " + str(round(qa / 4 + qb / 2, 2)) + " coulomb\n"
        input_formula = "Final charge on B = qa / 4 + qb / 2"
    elif types < 7:
        q = q + "final charge on C?\n"
        a = "The final charge on sphere C can be calculated by adding half of the initial charge qa and the full charge qb. Therefore, the final charge on C is " + str(round(qa / 4 + qb / 2, 2)) + " coulomb\n"
        input_formula = "Final charge on C = qa / 4 + qb / 2"
    elif types < 10:
        q = q + "final force between A and B?\n"
        a = "The final force between spheres A and B can be calculated using the formula F = k * qa * qb / d^2, where k is the electrostatic constant, qa and qb are the charges on A and B respectively, and d is the distance between them. Therefore, the final force between A and B is " + "{:.2e}".format(force(qa / 2, qa / 4 + qb / 2, d)) + " newton\n"
        input_formula = "Final force between A and B = k * qa * qb / d^2"
    elif types < 13:
        q = q + "final force between A and C?\n"
        a = "The final force between spheres A and C can be calculated using the formula F = k * qa * qb / d^2, where k is the electrostatic constant, qa and qb are the charges on A and C respectively, and d is the distance between them. Therefore, the final force between A and C is " + "{:.2e}".format(force(qa / 2, qa / 4 + qb / 2, d)) + " newton\n"
        input_formula = "Final force between A and C = k * qa * qb / d^2"
    else:
        q = q + "final force between C and B?\n"
        a = "The final force between spheres C and B can be calculated using the formula F = k * qa * qb / d^2, where k is the electrostatic constant, qa and qb are the charges on C and B respectively, and d is the distance between them. Therefore, the final force between C and B is " + "{:.2e}".format(force(qa / 4 + qb / 2, qa / 4 + qb / 2, d)) + " newton\n"
        input_formula = "Final force between C and B = k * qa * qb / d^2"
    
    sample["instruction"] = q
    sample["input"] = input_formula
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

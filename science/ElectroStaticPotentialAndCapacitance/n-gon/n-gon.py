import random
import json

no_of_samples = 20

def calculate_potential(n, q1, d):
    potential = 9 * (10**9) * n * (q1 * (10**(-6))) * (1 / (d * 0.01))
    return "{:.2e}".format(potential) + " volt"

data = []

for i in range(no_of_samples):
    n = random.randint(3, 20)
    q1 = random.randint(1, 500)
    d = random.randint(1, 500)
    if random.randint(0, 1):
        q1 = -q1

    q = f"A regular {n}-gon with a distance between each vertex and the center as {d} cm has a charge of {q1} micro-Coulombs at each of its vertices. Calculate the potential at the center of the {n}-gon?"
    in_formula = "9 * 10^9 * n * (q1 * 10^(-6)) * (1 / (d * 0.01))"
    in_values = f"n = {n}, q1 = {q1} micro-C, d = {d} cm"
    a = calculate_potential(n, q1, d)
    explanation = f"The potential at the center of the {n}-gon can be calculated using the formula:\n\nV = k * n * q1 / d\n\nwhere k is the electrostatic constant (9 * 10^9 Nm^2/C^2), n is the number of vertices, q1 is the charge at each vertex, and d is the distance between each vertex and the center.\n\nSubstituting the given values, we have:\n\nV = 9 * 10^9 * {n} * ({q1} * 10^(-6)) / ({d} * 0.01) = {a}"
    
    data.append({
        "instruction": q,
        "input": f"Formula: {in_formula}\nValues: {in_values}",
        "output": "Answer: " + a + "\n\nExplanation:\n" + explanation
    })

# Read the existing JSON file
with open("science/ElectroStaticPotentialAndCapacitance/esp.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/ElectroStaticPotentialAndCapacitance/esp.json", "w") as file:
    json.dump(existing_data, file, indent=4)

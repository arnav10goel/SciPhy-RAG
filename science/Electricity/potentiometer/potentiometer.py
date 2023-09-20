import random
import json

samples = []
no_of_samples = 20

for i in range(no_of_samples):
    types = random.randint(1, 7)
    if types <= 2:
        V = random.randint(1, 200)
        b1 = random.randint(1, 200)
        b2 = random.randint(1, 200)
        while b2 == b1:
            b2 = random.randint(1, 200)
        q = f"In a potentiometer arrangement, a cell of emf {V} V gives a balance point at {b1} cm length of the wire. If the cell is replaced by another cell and the balance point shifts to {b2} cm, what is the emf of the second cell?"
        input_formula = None
        explanation = f"The emf of the second cell can be calculated using the formula: emf2 = (emf1 * b2) / b1, where emf1 is the emf of the first cell, b1 is the balance point with the first cell, and b2 is the balance point with the second cell."
        output = f"{(V * b2) / b1} volt\n\n{explanation}"
    elif types <= 4:
        R = random.randint(1, 200)
        b1 = random.randint(1, 200)
        b2 = random.randint(1, 200)
        q = f"A potentiometer circuit is used for comparison of two resistances. The balance point with a standard resistance of {R} ohm is found to be {b1} cm, while that with the unknown resistor X is {b2} cm. Find the value of X?"
        input_formula = None
        explanation = f"The value of X can be calculated using the formula: X = (R * b2) / b1, where R is the standard resistance, b1 is the balance point with the standard resistance, and b2 is the balance point with the unknown resistor."
        output = f"{(R * b2) / b1} ohm\n\n{explanation}"
    else:
        V1 = random.randint(1, 90)
        V = random.randint(1, 20)
        b1 = random.randint(1, 90)
        b2 = random.randint(1, 20)
        R = random.randint(1, 20)
        q = f"A {V + V1} V potentiometer used for the determination of internal resistance of {V1} V cell. The balance point of the cell in the open circuit is {b1 + b2} cm. When a resistor of {R} ohm is used in the external circuit, the balance point shifts to {b1} cm. Find the internal resistance of the cell."
        input_formula = None
        explanation = f"The internal resistance of the cell can be calculated using the formula: internal_resistance = (b2 / b1) * R, where b1 is the balance point in the open circuit, b2 is the balance point with the external resistor, and R is the external resistor."
        output = f"{(b2 / b1) * R} ohm\n\n{explanation}"
    sample = {
        'instruction': q,
        'input': input_formula,
        'output': output,
    }
    samples.append(sample)

# Load existing JSON file
with open("science/Electricity/elec.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/Electricity/elec.json", "w") as file:
    json.dump(existing_data, file, indent=4)
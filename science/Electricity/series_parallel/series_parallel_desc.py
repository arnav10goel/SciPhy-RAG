import random
import json

samples = []
no_of_samples = 40

def calculate_series(R1, R2, R3):
    R_total = R1 + R2 + R3
    return R_total

def calculate_parallel(R1, R2, R3):
    R_total = (R1 * R2 * R3) / (R1 * R2 + R2 * R3 + R3 * R1)
    return round(R_total, 1)

for i in range(no_of_samples):
    R1 = random.randint(1, 200)
    R2 = random.randint(1, 200)
    R3 = random.randint(1, 100)
    types = random.randint(0, 3)
    if types == 0:
        word = "the highest"
        formula = "R_total = R1 + R2 + R3"
        explanation = "To calculate the highest combination of resistances, we add the resistances in series. The total resistance (R_total) is equal to the sum of the individual resistances (R1, R2, and R3)."
        R_total = calculate_series(R1, R2, R3)
        answer = f"The highest combination of resistances can be obtained by connecting them in series. The total resistance is {R1} + {R2} + {R3} = {R_total} ohm."
    else:
        word = "the lowest"
        formula = "R_total = (R1 * R2 * R3) / (R1 * R2 + R2 * R3 + R3 * R1)"
        explanation = "To calculate the lowest combination of resistances, we connect them in parallel. The total resistance (R_total) is given by the formula (R1 * R2 * R3) / (R1 * R2 + R2 * R3 + R3 * R1), where R1, R2, and R3 are the individual resistances."
        R_total = calculate_parallel(R1, R2, R3)
        answer = f"The lowest combination of resistances can be obtained by connecting them in parallel. The total resistance is calculated as ({R1} * {R2} * {R3}) / ({R1} * {R2} + {R2} * {R3} + {R3} * {R1}) = {R_total} ohm."
    ques = f"What is {word} total resistance that can be secured by combinations of three coils of resistance {R1}, {R2}, {R3}?"
    input_formula = formula
    output = f"{answer}\n\n{explanation}"
    sample = {
        'instruction': ques,
        'input': input_formula,
        'output': output
    }
    samples.append(sample)

# Load existing JSON file
with open("science/Electricity/elec.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save the updated JSON data
with open("science/Electricity/elec.json", "w") as file:
    json.dump(existing_data, file, indent=4)

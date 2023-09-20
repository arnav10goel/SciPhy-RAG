import random
import json

samples = []
no_of_samples = 10

def calculate_effective_wattage(P1, V1, V2):
    effective_wattage = round(((V2**2)*P1)/(V1**2), 1)
    return effective_wattage

for i in range(no_of_samples):
    P1 = random.randint(251, 1250)
    V1 = random.randint(1, 50)
    V2 = random.randint(1, 50)
    if V1 != V2:
        q = "The wattage of a bulb is "+str(P1)+" W when it is connected to a "+str(V1)+" V battery. Calculate its effective wattage if it operates on a "+str(V2)+" V battery?"
        input_formula = "Effective Wattage = ((V2^2) * P1) / (V1^2)"
        explanation = "The effective wattage of the bulb can be calculated using the formula: Effective Wattage = ((V2^2) * P1) / (V1^2), where V2 is the voltage of the new battery, P1 is the wattage of the bulb with the initial battery voltage V1."
        output = str(calculate_effective_wattage(P1, V1, V2))
        samples.append({
            "instruction": q,
            "input": input_formula,
            "output": output + "\n\n" + explanation
        })

# Load existing JSON file
with open("science/Electricity/elec.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/Electricity/elec.json", "w") as file:
    json.dump(existing_data, file, indent=4)

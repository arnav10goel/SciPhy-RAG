import random
import json

# Generate new samples
samples = []
no_of_samples = 10

for i in range(no_of_samples):
    V1 = random.randint(220, 240)
    V2 = random.randint(220, 240)
    P1 = random.randint(1, 100)
    P2 = random.randint(1, 100)
    q = f"Two lamps, one rated {P1} W at {V1} V, and the other {P2} W at {V2} V, which has more resistance?"
    if (V1 ** 2) / P1 > (V2 ** 2) / P2:
        answer = "lamp1"
    elif (V1 ** 2) / P1 < (V2 ** 2) / P2:
        answer = "lamp2"
    else:
        continue
    samples.append({"instruction": q, "input": "", "output": answer})

# Load existing JSON file
with open("science/Electricity/elec.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save the updated JSON data
with open("science/Electricity/elec.json", "w") as file:
    json.dump(existing_data, file, indent=4)

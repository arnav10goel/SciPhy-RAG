import random
import math
import json

no_of_samples = 20

data = []

for i in range(no_of_samples):
    v1 = random.randint(1500, 3500)
    v2 = random.randint(1, 2000)

    instruction = "In a harbour, wind is blowing at the speed of " + str(v1) + " m/s and the flag on the mast of a boat anchored in the harbour flutters along the N-E direction. If the boat starts moving at a speed of " + str(v2) + " m/s to the north, what is the direction of the flag on the mast of the boat?"
    sin45 = 1 / math.sqrt(2)
    tan_beta = v2 * sin45 / (v1 - v2 * sin45)
    beta = round(math.atan(tan_beta) * 57.2958, 1)
    if beta >= 45:
        output = str(round(beta - 45)) + " degrees south of east"
    else:
        output = str(round(45 - beta)) + " degrees north of east"

    data.append({
        "instruction": instruction,
        "input": "v1 = " + str(v1) + " m/s, v2 = " + str(v2) + " m/s",
        "output": output
    })

# Read the existing JSON file
with open("science/kinematics/kinematics_data.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinematics/kinematics_data.json", "w") as file:
    json.dump(existing_data, file, indent=4)

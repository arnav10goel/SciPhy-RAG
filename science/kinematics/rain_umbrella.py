import random
import math
import json

no_of_samples = 10

data = []

for i in range(no_of_samples):
    v1 = random.randint(1, 2000)
    v2 = random.randint(1, 2000)
    instruction = "Rain is falling vertically with a speed of " + str(v1) + " cm/s. A woman rides a bicycle with a speed of " + str(v2) + " cm/s in the north to south direction. In which direction should she hold her umbrella?"
    output = str(round(math.atan(v2 / v1) * 57.2958)) + " degrees south of vertical"
    data.append({
        "instruction": instruction,
        "input": "tan(v2 / v1)",
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

import random
import json
import math

no_of_samples = 20

data = []

for i in range(no_of_samples):
    angle = random.randint(1, 89)
    dist = random.randint(200, 500)
    u_2 = (dist * 9.8) / math.sin(math.radians(angle))
    R_opt = round(u_2 / 9.8)
    dist2 = random.randint(R_opt - 150, R_opt + 150)
    instruction = "A bullet fired at an angle of " + str(angle) + " degrees with the horizontal hits the ground " + str(dist) + " m away. By adjusting its angle of projection, can one hope to hit a target " + str(dist2) + " m away?"

    if dist2 > R_opt:
        output = {
            "instruction": instruction,
            "input": "no",
            "output": f"The target is too far away to be hit."
        }
    else:
        output = {
            "instruction": instruction,
            "input": "yes",
            "output": f"The target can be hit."
        }

    data.append(output)

# Read the existing JSON file
with open("science/kinematics/kinematics_data.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinematics/kinematics_data.json", "w") as file:
    json.dump(existing_data, file, indent=4)
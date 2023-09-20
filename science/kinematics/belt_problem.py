import random
import json

no_of_samples = 40

data = []

for i in range(no_of_samples):
    v2 = random.randint(1, 80)
    v1 = random.randint(v2 + 1, v2 + 50)
    distance = random.randint(1, 1000)
    instruction = "On a long horizontally moving belt, a child runs to and fro with a speed of " + str(v1) + " ms-1 (with respect to the belt) between his parents located " + str(distance) + " m apart on the moving belt. The belt moves with a speed of " + str(v2) + " ms-1. For an observer on a stationary platform outside, what is the "

    types = random.randint(1, 4)

    if types == 1:
        instruction = instruction + "speed of the child running in the direction of motion of the belt?"
        output = {
            "instruction": instruction,
            "input": "speed_child = speed_belt + speed_relative",
            "output": f"The speed of the child running in the direction of motion of the belt is {v1 + v2} ms-1."
        }

    elif types == 2:
        instruction = instruction + "speed of the child running opposite to the direction of motion of the belt?"
        output = {
            "instruction": instruction,
            "input": "speed_child = speed_relative - speed_belt",
            "output": f"The speed of the child running opposite to the direction of motion of the belt is {v1 - v2} ms-1."
        }

    elif types == 3 or types == 4:
        instruction = instruction + "time taken by the child to go from one parent to another parent?"
        output = {
            "instruction": instruction,
            "input": "time = distance / speed_relative",
            "output": f"The time taken by the child to go from one parent to another parent is {distance / (v1 - v2)} s."
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

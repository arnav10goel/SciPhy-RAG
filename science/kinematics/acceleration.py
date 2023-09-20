import random
import json

no_of_samples = 20

data = []

for i in range(no_of_samples):
    v = random.randint(33, 433)
    s = random.randint(1, 10000)

    q = "A car moving along a straight highway with a speed of " + str(v) + " ms-1 is brought to a stop within a distance of " + str(s) + " m. What is the acceleration of the car (assumed uniform), and how long does it take for the car to stop?"

    acc = (v ** 2) / s
    a = {
        "instruction": q,
        "input": "a = -v^2 / s, t = v / a",
        "output": f"The acceleration of the car is {round(acc, 1)} ms-2 and it takes {round(v / acc, 1)} seconds to stop."
    }

    data.append(a)

# Read the existing JSON file
with open("science/kinematics/kinematics_data.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinematics/kinematics_data.json", "w") as file:
    json.dump(existing_data, file, indent=4)

import random
import math
import json

no_of_samples = 20

data = []

for i in range(no_of_samples):
    types = random.randint(1, 2)
    if types == 1:
        x = random.randint(1, 1500)
        temp = random.randint(1, 2)
        if temp == 2:
            x = -x
        y = random.randint(-1500, 1500)
        mag = math.sqrt(x ** 2 + y ** 2)
        dir = math.atan(y / x) * (180 / math.pi)
        q = f"What is the magnitude and direction of ({x}) i + ({y}) j?"
        a = f"The magnitude is {round(mag, 1)} and the direction is {round(dir)} degrees with the positive x-axis."
        formula = f"magnitude = sqrt({x}^2 + {y}^2), direction = atan({y}/{x}) * (180 / pi)"
    elif types == 2:
        x1 = random.randint(1, 100)
        y1 = random.randint(1, 100)
        temp = random.randint(1, 2)
        if temp == 2:
            x1 = -x1
        temp = random.randint(1, 2)
        if temp == 2:
            y1 = -y1
        x2 = random.randint(1, 10)
        y2 = random.randint(1, 10)
        temp = random.randint(1, 2)
        if temp == 2:
            x2 = -x2
        temp = random.randint(1, 2)
        if temp == 2:
            y2 = -y2
        comp = (x1 * x2 + y1 * y2) / math.sqrt(x2 ** 2 + y2 ** 2)
        q = f"What are the components of a vector ({x1}) i + ({y1}) j along the direction of ({x2}) i + ({y2}) j?"
        a = f"The component is {round(comp, 1)} units."
        formula = f"component = ({x1} * {x2} + {y1} * {y2}) / sqrt({x2}^2 + {y2}^2)"
    data.append({
        "instruction": q,
        "input": formula,
        "output": a
    })

# Read the existing JSON file
with open("science/kinematics/kinematics_data.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinematics/kinematics_data.json", "w") as file:
    json.dump(existing_data, file, indent=4)

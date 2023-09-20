import random
import json

no_of_samples = 30

def calculate_scale_reading(m, v):
    return round(m * 10 - v, 1)

def calculate_scale_reading_acceleration(m, acc):
    return round(m * (10 + (acc / 100)) / 1000, 1)

def calculate_scale_reading_deceleration(m, acc):
    return round(m * (10 - (acc / 100)) / 1000, 1)

data = []

for i in range(no_of_samples):
    m = random.randint(100, 5000)
    v = random.randint(0, 1000)
    acc = random.randint(0, 1000)
    type = random.randint(1, 4)

    if type == 1 or type == 2:
        if type == 1:
            q = f"An object of mass {m} g stands on a weighing machine in a lift, which is moving upwards with a uniform speed of {v} cm/s."
            formula = "Scale Reading = m * 10 - v"
            explanation = f"To calculate the scale reading, we use the formula Scale Reading = mass * 10 - velocity, where the mass is {m} g and the velocity is {v} cm/s."
            answer = calculate_scale_reading(m, v)
        elif type == 2:
            q = f"An object of mass {m} g stands on a weighing machine in a lift, which is moving downwards with a uniform speed of {v} cm/s."
            formula = "Scale Reading = m * 10 - v"
            explanation = f"To calculate the scale reading, we use the formula Scale Reading = mass * 10 - velocity, where the mass is {m} g and the velocity is {v} cm/s."
            answer = calculate_scale_reading(m, v)
    elif type == 3:
        q = f"An object of mass {m} g stands on a weighing machine in a lift, which is moving downwards with a uniform acceleration of {acc} cm/s^2."
        formula = "Scale Reading = m * (10 - (acc / 100))"
        explanation = f"To calculate the scale reading, we use the formula Scale Reading = mass * (10 - (acceleration / 100)), where the mass is {m} g and the acceleration is {acc} cm/s^2."
        answer = calculate_scale_reading_deceleration(m, acc)
    elif type == 4:
        q = f"An object of mass {m} g stands on a weighing machine in a lift, which is moving upwards with a uniform acceleration of {acc} cm/s^2."
        formula = "Scale Reading = m * (10 + (acc / 100))"
        explanation = f"To calculate the scale reading, we use the formula Scale Reading = mass * (10 + (acceleration / 100)), where the mass is {m} g and the acceleration is {acc} cm/s^2."
        answer = calculate_scale_reading_acceleration(m, acc)

    data.append({
        "instruction": q,
        "input": formula,
        "output": f"{answer}\n{explanation}"
    })

# Read the existing JSON file
with open("science/laws_of_motion/nlm.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/laws_of_motion/nlm.json", "w") as file:
    json.dump(existing_data, file, indent=4)


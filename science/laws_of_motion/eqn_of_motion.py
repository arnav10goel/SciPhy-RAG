import random
import json

no_of_samples = 40

def calculate_position(m, v, F, t):
    if t <= 0:
        s = v * t
    elif t <= 30:
        s = v * t - (F * (t ** 2)) / (2 * m)
    else:
        s30 = v * 30 - (F * (30 ** 2)) / (2 * m)
        v30 = v - ((F * 30) / m)
        s30after = v30 * (t - 30)
        s = s30 + s30after
    return round(s)

data = []

for i in range(no_of_samples):
    m = random.randint(1, 20)
    v = random.randint(1, 20)
    F = random.randint(2, 200)
    t = random.randint(-30, 60)
    instruction = f"A body of mass {m} kg moving initially with a constant speed of {v} m/s to the north is subject to a constant force of {F} N directed towards the south for 30 s. Take the instant the force is applied to be t = 0, the position of the body at that time to be x = 0, and predict its position at t = {t} s."
    formula = ""
    if t <= 0:
        formula = "s = v * t"
        output = round(v * t)
    elif t <= 30:
        formula = "s = v * t - (F * (t^2)) / (2 * m)"
        output = round(v * t - (F * (t ** 2)) / (2 * m))
    else:
        formula = "s = s30 + s30after"
        s30 = v * 30 - (F * (30 ** 2)) / (2 * m)
        v30 = v - ((F * 30) / m)
        s30after = v30 * (t - 30)
        output = round(s30 + s30after)
    output = str(output)
    output += f"\nThe position at time t = {t} s can be calculated using the formula: {formula}."
    input_data = f"m = {m} kg\nv = {v} m/s\nF = {F} N\nt = {t} s"
    
    question = {
        "instruction": instruction,
        "input": input_data + "\n" + formula,
        "output": output
    }
    data.append(question)

# Read the existing JSON file
with open("science/laws_of_motion/nlm.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/laws_of_motion/nlm.json", "w") as file:
    json.dump(existing_data, file, indent=4)

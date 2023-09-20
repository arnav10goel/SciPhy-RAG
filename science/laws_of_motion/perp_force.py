import random
import math
import json

data = []

no_of_samples = 20

for i in range(no_of_samples):
    m = random.randint(1, 200)
    f_x = random.randint(20, 200)
    f_y = random.randint(20, 200)
    q_type = random.randint(1, 3)
    angle = math.atan(f_y / f_x) * (180 / math.pi)
    f_res = math.sqrt(f_x ** 2 + f_y ** 2)
    
    question = {}
    question['instruction'] = ''
    question['input'] = ''
    question['output'] = ''
    
    if q_type == 1:
        question['instruction'] = f"A body of mass {m} kg is acted upon by two perpendicular forces {f_x} N and {f_y} N. Give the magnitude and direction of the acceleration of the body."
        question['input'] = ''
        question['output'] = f"{round(f_res / m, 1)} ms-2, {round(angle)} degrees with {f_x} newton force"
    else:
        if random.randint(0, 1):
            f_x = -f_x
        if random.randint(0, 1):
            f_y = -f_y
        expr = f"({f_x}) i + ({f_y}) j N."
        if q_type == 2:
            question['instruction'] = f"A body of mass {m} kg is acted upon by the force {expr}. Find the acceleration of the body (in vector notation)."
            question['input'] = expr
            question['output'] = f"({round(f_x / m, 1)}) i + ({round(f_y / m, 1)}) j ms-2"
        elif q_type == 3:
            f_res = math.sqrt(f_x ** 2 + f_y ** 2)
            question['instruction'] = f"A body of mass {m} kg is acted upon by the force {expr}. Give the magnitude of acceleration of the body."
            question['input'] = expr
            question['output'] = f"{round(f_res / m, 1)} ms-2"
    
    data.append(question)

# Read the existing JSON file
with open("science/laws_of_motion/nlm.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/laws_of_motion/nlm.json", "w") as file:
    json.dump(existing_data, file, indent=4)
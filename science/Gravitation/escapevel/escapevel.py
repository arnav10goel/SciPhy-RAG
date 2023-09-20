import random
import math
import json
no_of_samples = 20

def cal1(v):
    return round(math.sqrt((v * v) - (11.2 * 11.2)), 1)

def type1():
    v = random.randint(112000, 212000)
    v = round(v / 1000, 3)
    ra = f"{cal1(v)} km/s"
    q = f"The escape speed of a projectile on the Earth\'s surface is 11.2 km/s. A body is projected out with the speed of {v} km/s. What is the speed of the body far away from the Earth?"
    return q, ra

questions = []

for i in range(no_of_samples):
    ques, answer = type1()
    questions.append({
        "instruction": ques,
        "input": f"Projectile Speed : {answer} km/s",
        "output": answer + "\n\nExplanation: " f"The speed of the body far away from the Earth, when projected with a speed of {answer} km/s, can be calculated using the escape speed formula. By substituting the given values, the speed is found to be {answer}."
    })

# Read the existing JSON file
with open("science/Gravitation/g.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(questions)

# Write the updated data to the JSON file with indentation
with open("science/Gravitation/g.json", "w") as file:
    json.dump(existing_data, file, indent=4)

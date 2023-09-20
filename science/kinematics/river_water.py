import random
import json
import math

no_of_samples = 20

data = []

def generate_question():
    v1 = random.randint(1, 200)
    v2 = random.randint(1, 200)
    s = random.randint(1, 100)
    
    q = "A man can swim with a speed of " + str(v1) + " m/s in still water. How long does he take to cross a river " + str(s) + " km wide if the river flows steadily at " + str(v2) + " m/s and he makes his strokes normal to the river current? How far down the river does he go when he reaches the other bank, and what is the angle of deviation of his path from normal?"
    deviation_angle = round(math.atan(v2/v1) * 57.2958)
    time = (s * 1000) / v1
    a = "The time taken is " + str(round(time, 1)) + " seconds. The distance down the river is " + str(s) + " km. The angle of deviation is " + str(deviation_angle) + " degrees."
    input_param = "v1 = " + str(v1) + " m/s, v2 = " + str(v2) + " m/s, s = " + str(s) + " km"
    
    return q, a, input_param

for i in range(no_of_samples):
    ques, answer, input_param = generate_question()
    data.append({
        "instruction": ques,
        "input": input_param,
        "output": answer
    })

# Read the existing JSON file
with open("science/kinematics/kinematics_data.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinematics/kinematics_data.json", "w") as file:
    json.dump(existing_data, file, indent=4)

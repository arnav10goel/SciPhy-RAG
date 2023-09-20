import random
import math
import json

data = []

no_of_samples = 30

g = 10

def generate_type1():
    m = random.randint(50, 100)
    r = random.randint(2, 10)
    mu = round(random.randint(1, 100) / 100, 2)
    rot_speed = random.randint(1, 5)
    
    question = {}
    question['instruction'] = f"A {m} kg man stands in contact against the inner wall of a hollow cylindrical drum of radius {r} m rotating about its vertical axis with {rot_speed} rev/s. The coefficient of friction between the wall and his clothing is {mu}. What is the minimum rotational speed of the cylinder to enable the man to remain stuck to the wall (without falling) when the floor is suddenly removed?"
    question['input'] = f"Minimum rotational speed (ω) = sqrt(g / (μ * r))"
    
    w = math.sqrt(g / (mu * r))
    question['output'] = f"{round(w, 1)} rad/s"
    return question

def generate_type2():
    rot_speed = random.randint(10, 50)
    r1 = random.randint(1, 50)
    r2 = random.randint(r1 + 1, r1 + 49)
    mu = round(random.randint(1, 100) / 100, 2)
    
    question = {}
    question['instruction'] = f"A disc revolves with a speed of {rot_speed} rpm and has a radius of 1 m. Two coins are placed at {r1} cm (coin-1) and {r2} cm (coin-2) away from the center of the record. If the coefficient of friction between the coins and the record is {mu}, which of the coins will revolve with the record?"
    question['input'] = f"Centripetal acceleration (a) = (π / 30) * rot_speed\nOptimal radius (r_opt) = ((μ * g) / (w * w)) * 100"
    
    w = (math.pi / 30) * rot_speed
    r_opt = ((mu * g) / (w * w)) * 100
    
    if r1 < r_opt:
        answer = "coin1 will revolve,"
    else:
        answer = "coin1 will not revolve,"
    if r2 < r_opt:
        answer += "coin2 will revolve"
    else:
        answer += "coin2 will not revolve"
    
    question['output'] = answer
    return question

for i in range(no_of_samples):
    q_type = random.randint(1, 3)
    
    if q_type == 1:
        question = generate_type1()
    else:
        question = generate_type2()
    
    data.append(question)

# Read the existing JSON file
with open("science/laws_of_motion/nlm.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/laws_of_motion/nlm.json", "w") as file:
    json.dump(existing_data, file, indent=4)

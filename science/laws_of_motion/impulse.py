import random
import json
import math

no_of_samples = 30

def calculate_impulse_collision(m, v):
    impulse = (2 * m * v) / 1000
    return round(impulse, 1)

def calculate_impulse_deflection(m, angle, v):
    anglerad = math.radians(angle)
    impulse = (2 * m * v * math.cos(anglerad)) / 1000
    return round(impulse, 1)

data = []

def type1():
    m = random.randint(50, 2000)
    v = random.randint(2, 2000)
    q = f"Two balls each of mass {m} g, moving in opposite directions with speed {v} m/s collide and rebound with the same speed. What is the impulse imparted to each ball due to the other?"
    impulse = calculate_impulse_collision(m, v)
    explanation = f"The impulse imparted to each ball due to the other can be calculated using the formula (2 * mass * velocity) / 1000, where the mass is {m} g and the velocity is {v} m/s. The result is {impulse} kg·m/s, in the direction of the final velocity for both balls."
    return q, impulse, explanation

def type2():
    m = random.randint(50, 300)
    angle = random.randint(1, 180)
    v = random.randint(1, 200)
    q = f"A batsman deflects a ball by an angle of {angle} degrees without changing its initial speed, which is equal to {v} m/s. What is the impulse imparted to the ball? (The mass of the ball is {m} g)"
    impulse = calculate_impulse_deflection(m, angle, v)
    explanation = f"The impulse imparted to the ball can be calculated using the formula (2 * mass * velocity * cos(angle)) / 1000, where the mass is {m} g, the velocity is {v} m/s, and the angle is {angle} degrees. The result is {impulse} kg·m/s, perpendicular to the point of impact on the bat."
    return q, impulse, explanation

for i in range(no_of_samples):
    q_type = random.randint(1, 3)
    if q_type == 1:
        q, impulse, explanation = type1()
    else:
        q, impulse, explanation = type2()
    data.append({
        "instruction": q,
        "input": "Impulse calculation",
        "output": f"{impulse}\n{explanation}"
    })

# Read the existing JSON file
with open("science/laws_of_motion/nlm.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/laws_of_motion/nlm.json", "w") as file:
    json.dump(existing_data, file, indent=4)

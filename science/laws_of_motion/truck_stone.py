import random
import math
import json

no_of_samples = 40

data = []

for i in range(no_of_samples):
    acc = random.randint(1, 20)
    t1 = random.randint(1, 200)
    h = random.randint(1, 30)
    t2 = random.randint(t1, t1 + 30)
    q = f"A truck starts from rest and accelerates uniformly at {acc} ms-2. At t = {t1} s, a stone is dropped by a person standing on the top of the truck ({h} m high from the ground). What are the (a) velocity, and (b) acceleration of the stone at t = {t2} s? (Neglect air resistance.)"

    vx = t1 * acc
    vy = (t2 - t1) * 10
    v = math.sqrt(vx ** 2 + vy ** 2)
    angle = math.atan(vy / vx) * (180 / math.pi)
    a = f"Velocity is {round(v, 1)} ms-1, at an angle of {round(angle)} degrees with horizontal. Acceleration is g (10 ms-2) downwards."

    question_data = {
        "instruction": q,
        "input": q,
        "output": a
    }

    data.append(question_data)

# Read the existing JSON file
with open("science/laws_of_motion/nlm.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/laws_of_motion/nlm.json", "w") as file:
    json.dump(existing_data, file, indent=4)


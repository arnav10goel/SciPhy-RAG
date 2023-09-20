import random
import math
import json

no_of_samples = 60
shapes = ["solid sphere", "hollow sphere", "solid cylinder", "hollow cylinder", "solid disk", "hoop"]
con = [2/5, 2/3, 1/2, 1, 1/2, 1]

def compare_speed(h1, h2, a1, a2, k1, k2):
    v1 = h1 / (k1 + 1)
    v2 = h2 / (k2 + 1)

    if v1 > v2:
        return 1
    elif v1 < v2:
        return 2
    return 0

def compare_time(h1, h2, a1, a2, k1, k2):
    v1 = math.sqrt((k1 + 1) * h1) / math.sin(math.radians(a1))
    v2 = math.sqrt((k2 + 1) * h2) / math.sin(math.radians(a2))

    if v1 < v2:
        return 1
    elif v1 > v2:
        return 2
    return 0

def generate_question_type1(h1, h2, a1, a2, t1, t2):
    v = compare_speed(h1, h2, a1, a2, con[t1], con[t2])

    if v == 1:
        answer = "The first plane has more speed."
    elif v == 2:
        answer = "The second plane has more speed."
    else:
        answer = "Both planes have the same speed."

    question = f"A {shapes[t1]} rolls down two different inclined planes of heights {h1} cm and {h2} cm and with angles of inclination of {a1} and {a2}, on which it reaches the bottom with more speed?"

    input_formula = "speed = height / (k + 1)"
    output = f"To compare the speeds, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that:\n\n{answer}"

    return question, input_formula, output

def generate_question_type2(h, a1, a2, t1, t2):
    v = compare_time(h, h, a1, a2, con[t1], con[t2])

    if v == 1:
        answer = "The first plane takes less time to reach the ground."
    elif v == 2:
        answer = "The second plane takes less time to reach the ground."
    else:
        answer = "Both planes take the same time to reach the ground."

    question = f"A {shapes[t1]} rolls down two different inclined planes of the same height {h} cm but with angles of inclination of {a1} and {a2}, on which it will reach the ground faster?"

    input_formula = "time = sqrt((k + 1) * height) / sin(angle)"
    output = f"To compare the times, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that:\n\n{answer}"

    return question, input_formula, output

def generate_question_type3(h1, h2, a1, a2, t1, t2):
    v = compare_time(h1, h2, a1, a2, con[t1], con[t2])

    if v == 1:
        answer = "The first plane takes less time to reach the ground."
    elif v == 2:
        answer = "The second plane takes less time to reach the ground."
    else:
        answer = "Both planes take the same time to reach the ground."

    question = f"A {shapes[t1]} rolls down two different inclined planes of heights {h1} and {h2} and with angles of inclination of {a1} and {a2}, on which it will reach the ground faster?"

    input_formula = "time = sqrt(height * (k + 1)) / sin(angle)"
    output = f"To compare the times, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that:\n\n{answer}"

    return question, input_formula, output

def generate_question_type4(h1, h2, a1, a2, t1, t2):
    v = compare_speed(h1, h2, a1, a2, con[t1], con[t2])

    if v == 1:
        answer = f"The {shapes[t1]} reaches the bottom with more speed."
    elif v == 2:
        answer = f"The {shapes[t2]} reaches the bottom with more speed."
    else:
        answer = "Both the solid sphere and the hollow sphere reach the bottom with the same speed."

    question = f"A {shapes[t1]} and a {shapes[t2]} roll down two different inclined planes of heights {h1} and {h2} and with angles of inclination of {a1} and {a2}, which one reaches the bottom with more speed?"

    input_formula = "speed = height / (1 + k)"
    output = f"To compare the speeds, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that:\n\n{answer}"

    return question, input_formula, output

def generate_question_type5(h1, h2, a1, a2, t1, t2):
    v = compare_time(h1, h2, a1, a2, con[t1], con[t2])

    if v == 1:
        answer = f"The {shapes[t1]} takes less time to reach the ground."
    elif v == 2:
        answer = f"The {shapes[t2]} takes less time to reach the ground."
    else:
        answer = "Both the solid sphere and the hollow sphere take the same time to reach the ground."

    question = f"A {shapes[t1]} and a {shapes[t2]} roll down two different inclined planes of heights {h1} and {h2} and with angles of inclination of {a1} and {a2}, which will reach the ground faster?"

    input_formula = "time = sqrt(height * (k + 1)) / sin(angle)"
    output = f"To compare the times, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that:\n\n{answer}"

    return question, input_formula, output

samples = []

for i in range(no_of_samples):
    types = random.randint(1, 5)

    if types == 1:
        h1 = random.randint(1, 20)
        h2 = random.randint(1, 20)
        a1 = random.randint(1, 90)
        a2 = random.randint(1, 90)
        t1 = random.randint(0, 5)
        t2 = random.randint(0, 5)

        question, input_formula, output = generate_question_type1(h1, h2, a1, a2, t1, t2)

    elif types == 2:
        h = random.randint(1, 40)
        a1 = random.randint(1, 90)
        a2 = random.randint(1, 90)
        t1 = random.randint(0, 5)
        t2 = random.randint(0, 5)

        question, input_formula, output = generate_question_type2(h, a1, a2, t1, t2)

    elif types == 3:
        h1 = random.randint(1, 20)
        h2 = random.randint(1, 20)
        a1 = random.randint(1, 90)
        a2 = random.randint(1, 90)
        t1 = random.randint(0, 5)
        t2 = random.randint(0, 5)

        question, input_formula, output = generate_question_type3(h1, h2, a1, a2, t1, t2)

    elif types == 4:
        h1 = random.randint(1, 20)
        h2 = random.randint(1, 20)
        a1 = random.randint(1, 90)
        a2 = random.randint(1, 90)
        t1 = random.randint(0, 5)
        t2 = random.randint(0, 5)

        question, input_formula, output = generate_question_type4(h1, h2, a1, a2, t1, t2)

    elif types == 5:
        h1 = random.randint(1, 20)
        h2 = random.randint(1, 20)
        a1 = random.randint(1, 90)
        a2 = random.randint(1, 90)
        t1 = random.randint(0, 5)
        t2 = random.randint(0, 5)

        question, input_formula, output = generate_question_type5(h1, h2, a1, a2, t1, t2)

    sample = {
        "instruction": question,
        "input": input_formula,
        "output": output
    }

    samples.append(sample)

# Load existing JSON file
with open("science/RotationalMotion/rom.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/RotationalMotion/rom.json", "w") as file:
    json.dump(existing_data, file, indent=4)


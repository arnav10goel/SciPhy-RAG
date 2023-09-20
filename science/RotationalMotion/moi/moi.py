import random
import json

no_of_samples = 110
con = [1/2, 1, 2/5, 2/3, 1/2, 1, 1/2, 1/12, 1/3]

def calculate_moment_of_inertia(c, m, r):
    return round(c * m * r * r, 1)

def generate_question_type1():
    m = random.randint(1,10000)
    r = random.randint(1,100)
    l = random.randint(1,100)
    t = random.randint(0,9)
    if t == 0:
        q = f"A solid cylinder of mass {m} kg has a radius of {r} m. What is the moment of inertia with respect to its symmetric axis?"
        input_formula = "Moment of Inertia = (Constant) * mass * radius^2"
        formula_explanation = f"Constant = {con[0]}\nmass = {m} kg\nradius = {r} m"
        moment_of_inertia = calculate_moment_of_inertia(con[0], m, r)
        output = f"The moment of inertia with respect to its symmetric axis is approximately {moment_of_inertia} kgm^2."
    elif t == 1:
        q = f"A hollow cylinder of mass {m} kg has a radius of {r} m. What is the moment of inertia with respect to its symmetric axis?"
        input_formula = "Moment of Inertia = (Constant) * mass * radius^2"
        formula_explanation = f"Constant = {con[1]}\nmass = {m} kg\nradius = {r} m"
        moment_of_inertia = calculate_moment_of_inertia(con[1], m, r)
        output = f"The moment of inertia with respect to its symmetric axis is approximately {moment_of_inertia} kgm^2."
    elif t == 2:
        q = f"A solid sphere of mass {m} kg has a radius of {r} m. What is the moment of inertia with respect to its symmetric axis?"
        input_formula = "Moment of Inertia = (Constant) * mass * radius^2"
        formula_explanation = f"Constant = {con[2]}\nmass = {m} kg\nradius = {r} m"
        moment_of_inertia = calculate_moment_of_inertia(con[2], m, r)
        output = f"The moment of inertia with respect to its symmetric axis is approximately {moment_of_inertia} kgm^2."
    elif t == 3:
        q = f"A hollow sphere of mass {m} kg has a radius of {r} m. What is the moment of inertia with respect to its symmetric axis?"
        input_formula = "Moment of Inertia = (Constant) * mass * radius^2"
        formula_explanation = f"Constant = {con[3]}\nmass = {m} kg\nradius = {r} m"
        moment_of_inertia = calculate_moment_of_inertia(con[3], m, r)
        output = f"The moment of inertia with respect to its symmetric axis is approximately {moment_of_inertia} kgm^2."
    elif t == 4:
        q = f"A solid disc of mass {m} kg has a radius of {r} m. What is the moment of inertia with respect to its symmetric axis?"
        input_formula = "Moment of Inertia = (Constant) * mass * radius^2"
        formula_explanation = f"Constant = {con[4]}\nmass = {m} kg\nradius = {r} m"
        moment_of_inertia = calculate_moment_of_inertia(con[4], m, r)
        output = f"The moment of inertia with respect to its symmetric axis is approximately {moment_of_inertia} kgm^2."
    elif t == 5:
        q = f"A hoop of mass {m} kg has a radius of {r} m. What is the moment of inertia with respect to its symmetric axis?"
        input_formula = "Moment of Inertia = (Constant) * mass * radius^2"
        formula_explanation = f"Constant = {con[5]}\nmass = {m} kg\nradius = {r} m"
        moment_of_inertia = calculate_moment_of_inertia(con[5], m, r)
        output = f"The moment of inertia with respect to its symmetric axis is approximately {moment_of_inertia} kgm^2."
    elif t == 6:
        q = f"A hoop of mass {m} kg has a radius of {r} m. What is the moment of inertia with respect to its diameter?"
        input_formula = "Moment of Inertia = (Constant) * mass * radius^2"
        formula_explanation = f"Constant = {con[6]}\nmass = {m} kg\nradius = {r} m"
        moment_of_inertia = calculate_moment_of_inertia(con[6], m, r)
        output = f"The moment of inertia with respect to its diameter is approximately {moment_of_inertia} kgm^2."
    elif t == 7:
        q = f"A rod of mass {m} kg has a length of {r} m. What is the moment of inertia with respect to its center?"
        input_formula = "Moment of Inertia = (Constant) * mass * length^2"
        formula_explanation = f"Constant = {con[7]}\nmass = {m} kg\nlength = {r} m"
        moment_of_inertia = calculate_moment_of_inertia(con[7], m, r)
        output = f"The moment of inertia with respect to its center is approximately {moment_of_inertia} kgm^2."
    elif t == 8:
        q = f"A rod of mass {m} kg has a length of {r} m. What is the moment of inertia with respect to its end?"
        input_formula = "Moment of Inertia = (Constant) * mass * length^2"
        formula_explanation = f"Constant = {con[8]}\nmass = {m} kg\nlength = {r} m"
        moment_of_inertia = calculate_moment_of_inertia(con[8], m, r)
        output = f"The moment of inertia with respect to its end is approximately {moment_of_inertia} kgm^2."
    elif t == 9:
        q = f"A solid cylinder of mass {m} kg has a radius of {r} m and length of {l} m. What is the moment of inertia with respect to its diameter?"
        input_formula = "Moment of Inertia = (Constant1) * mass * length^2 + (Constant2) * mass * radius^2"
        formula_explanation = f"Constant1 = {con[7]}\nConstant2 = {con[0]}\nmass = {m} kg\nlength = {l} m\nradius = {r} m"
        moment_of_inertia = calculate_moment_of_inertia(con[7], m, l)
        output = f"The moment of inertia with respect to its end is approximately {moment_of_inertia} kgm^2."

    output += "\n\n" + input_formula + "\n\n" + formula_explanation
    return q, input_formula, output

samples = []
for i in range(no_of_samples):
    q, input_formula, output = generate_question_type1()
    samples.append({
        "instruction": q,
        "input": input_formula,
        "output": output
    })

# Load existing JSON file
with open("science/RotationalMotion/rom.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/RotationalMotion/rom.json", "w") as file:
    json.dump(existing_data, file, indent=4)
import random
import json
import math

no_of_samples = 20

def calculate_height_blood_container(p):
    return (p / (1060 * 9.8)) * 1000

def calculate_velocity_blood_flow(r):
    return (2000 * 2.084) / (1.06 * 2 * r)

def calculate_flow_rate(r, vc):
    return math.pi * r * r * vc * (10 ** (-12))

def generate_question1(p, h1):
    return f"During blood transfusion, the needle is inserted in a vein where the gauge pressure is {p} Pa. If the blood container is placed at {h1} mm above the Earth's level so that blood may just enter the vein, is it safe for the patient?"

def generate_question2(r, l):
    return f"What is the largest average velocity of blood flow in an artery of radius {r} micrometer and length {l} mm if flow must remain laminar? What is the corresponding flow rate?"

def generate_input_formula1(p):
    return f"({p} / (1060 * 9.8)) * 1000"

def generate_input_formula2(r):
    return f"(2000 * 2.084) / (1.06 * 2 * {r})"

def generate_input_formula3(r, vc):
    return f"math.pi * {r} * {r} * {vc} * (10 ** (-12))"

def generate_output_explanation1(h, h1):
    if h1 > h:
        return "Yes, the patient is safe."
    else:
        return "No, the patient is not safe."

def generate_output_explanation2(vc, flow_rate):
    return f"The largest average velocity of blood flow is {round(vc, 2)} m/s. The corresponding flow rate is {flow_rate:.2e} m^3/s."

samples = []

for i in range(no_of_samples):
    sample = {}
    types = random.randint(0, 1)

    if types == 0:
        p = random.randint(1000, 11000)
        h1 = random.randint(max(0, round(calculate_height_blood_container(p)) - 200), round(calculate_height_blood_container(p)) + 200)

        question = generate_question1(p, h1)
        h = calculate_height_blood_container(p)
        input_formula = generate_input_formula1(p)
        output_explanation = generate_output_explanation1(h, h1)
    else:
        r = random.randint(1, 2000)
        l = random.randint(1, 2000)

        question = generate_question2(r, l)
        vc = calculate_velocity_blood_flow(r)
        flow_rate = calculate_flow_rate(r, vc)
        input_formula = generate_input_formula2(r)
        output_explanation = generate_output_explanation2(vc, flow_rate)

    sample["instruction"] = question
    sample["input"] = input_formula
    sample["output"] = output_explanation

    samples.append(sample)

# Read the existing JSON file
with open("science/MechanicalPropertiesOfLiquids/mpl.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/MechanicalPropertiesOfLiquids/mpl.json", "w") as file:
    json.dump(existing_data, file, indent=4)

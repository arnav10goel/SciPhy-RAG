import random
import json

no_of_samples = 30

def calculate_excess_pressure_soap(r, st):
    return (4 * st) / r

def calculate_pressure_air_bubble(depth, rel_den, excess):
    return (1.01 * 10**5) + (depth * rel_den * 10) + (excess / 2)

def calculate_force_door(a1, a2, rel_den, h):
    return h * abs(rel_den - 1) * 0.98 * a2

def generate_question1(r, temp, st, depth, rel_den):
    return f"What is the excess pressure inside a bubble of soap solution of radius {r} mm, given that the surface tension of soap solution at the temperature {temp} K is {st} x 10-3 Nm-1? If an air bubble of the same dimension was formed at a depth of {depth} cm inside a container containing the soap solution (of relative density {rel_den}), what would be the pressure inside the bubble?"

def generate_question2(a1, a2, rel_den, h):
    return f"A tank with a square base of area {a1} m2 is divided by a vertical partition in the middle. The bottom of the partition has a small-hinged door of area {a2} cm2. The tank is filled with water in one compartment, and an acid (of relative density {rel_den}) in the other, both to a height of {h} m. Compute the force necessary to keep the door closed."

def generate_input_formula1(r, st):
    return f"(4 * {st}) / {r}"

def generate_input_formula2(depth, rel_den, excess):
    return f"(1.01 * 10**5) + ({depth} * {rel_den} * 10) + ({excess} / 2)"

def generate_input_formula3(a1, a2, rel_den, h):
    return f"{h} * abs({rel_den} - 1) * 0.98 * {a2}"

def generate_output_explanation1(excess, p):
    return f"The excess pressure inside the soap bubble is {round(excess, 1)} Pascal. The pressure inside the air bubble floating up is {p:.2e} Pascal."

def generate_output_explanation2(f):
    return f"The force necessary to keep the door closed is {round(f, 1)} Newton."

samples = []

for i in range(no_of_samples):
    sample = {}
    types = random.randint(0, 1)

    if types:
        r = random.randint(1, 10)
        temp = random.randint(280, 300)
        st = random.randint(1, 200)
        depth = random.randint(1, 10) * 10
        rel_den = 1 + round(random.randint(1, 20) / 10, 1)

        question = generate_question1(r, temp, st, depth, rel_den)
        excess = calculate_excess_pressure_soap(r, st)
        p = calculate_pressure_air_bubble(depth, rel_den, excess)
        input_formula = generate_input_formula1(r, st)
        output_explanation = generate_output_explanation1(excess, p)
    else:
        a1 = random.randint(1, 200)
        a2 = random.randint(1, 200)
        rel_den = round(random.randint(1, 20) / 10, 1)
        h = random.randint(1, 20)

        question = generate_question2(a1, a2, rel_den, h)
        f = calculate_force_door(a1, a2, rel_den, h)
        input_formula = generate_input_formula3(a1, a2, rel_den, h)
        output_explanation = generate_output_explanation2(f)

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

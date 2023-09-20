import random
import json
import math

no_of_samples = 20

pi = math.pi

def generate_question1(angle, r, st, density):
    return f"A liquid has an angle of contact equal to {angle} degrees with soda-lime glass. A narrow tube of radius {r} mm made of this glass is dipped in a trough containing liquid. By what amount does the liquid dip down in the tube relative to the liquid surface outside? Surface tension of liquid is {st} Nm-2. Density of liquid = {density} x 10^3 kgm-3."

def generate_question2(l1, l2, angle, st, den):
    return f"Two narrow bores of diameters {l1} mm and {l2} mm are joined together to form a U-tube open at both ends. If the U-tube contains an unknown liquid, what is the difference in its levels at two ends? Surface tension of liquid is {st} x 10^(-2) Nm-2. Take the angle of contact to be {angle} degrees and density of liquid to be {den} x 10^3 kgm-3."

def generate_input_formula1(angle, r, st, density):
    return f"(2 * st * cos(angle * pi / 180)) / (r * density * 9.8)"

def generate_input_formula2(l1, l2, angle, st, den):
    common = (2 * (st / 100) * math.cos(angle * pi / 180)) / (den * 1000 * 9.8)
    diff = 1000 * ((1 / l1) - (1 / l2))
    return f"abs({common} * {diff})"

def generate_output_explanation1(angle, r, st, density):
    h = (2 * st * math.cos(angle * pi / 180)) / (r * density * 9.8)
    return f"The liquid in the narrow tube dips down by an amount given by (2 * st * cos(angle * pi / 180)) / (r * density * 9.8). Substituting the given values, we have (2 * {st} * cos({angle} * {pi} / 180)) / ({r} * {density} * 10^3 * 9.8) = {h:.2e} m."

def generate_output_explanation2(l1, l2, angle, st, den):
    common = (2 * (st / 100) * math.cos(angle * pi / 180)) / (den * 1000 * 9.8)
    diff = 1000 * ((1 / l1) - (1 / l2))
    h = abs(common * diff)
    return f"The difference in levels of the U-tube is given by abs({common} * {diff}). Substituting the given values, we have abs({common} * {diff}) = {h:.2e} m."

samples = []

for i in range(no_of_samples):
    sample = {}
    angle = random.randint(0, 180)
    r = random.randint(1, 10)
    st = round(random.randint(1, 100) / 100, 2)
    density = random.randint(1, 20)
    l1 = random.randint(1, 20)
    l2 = random.randint(1, 20)
    while l1 == l2:
        l2 = random.randint(1, 20)
        st2 = random.randint(1, 20)
        den = random.randint(1, 20)
    if random.randint(0, 1) == 0:
        question = generate_question1(angle, r, st, density)
        input_formula = generate_input_formula1(angle, r, st, density)
        output_explanation = generate_output_explanation1(angle, r, st, density)
    else:
        question = generate_question2(l1, l2, angle, st2, den)
        input_formula = generate_input_formula2(l1, l2, angle, st2, den)
        output_explanation = generate_output_explanation2(l1, l2, angle, st2, den)

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

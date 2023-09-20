import random
import json
import math

no_of_samples = 30

def calculate_max_pressure(m, area):
    p_pascal = (m * 9.8) / (area * (10 ** -6))
    p_atm = p_pascal / (1.013 * (10 ** 5))
    return p_pascal, p_atm

def calculate_pressure_heel(m, diameter, single_heel):
    area = (math.pi * diameter * diameter * (10 ** -12)) / 4
    if single_heel:
        p = (m * 9.8) / area
        explanation = f"The pressure exerted by the heel on the horizontal floor is calculated using the formula P = (m * 9.8) / A, where m is the mass of the girl ({m} kg) and A is the area of the heel ({area} m^2)."
    else:
        p = (m * 4.9) / area
        explanation = f"The pressure exerted by each heel on the horizontal floor is calculated using the formula P = (m * 4.9) / A, where m is the mass of the girl ({m} kg) and A is the area of each heel ({area} m^2)."
    return p, explanation

def generate_question_lift(m, area, in_pascal):
    unit = "pascal" if in_pascal else "atmosphere"
    return f"A hydraulic automobile lift is designed to lift cars with a maximum mass of {m} kg. The area of cross-section of the piston carrying the load is {area} mm2. What maximum pressure would the piston have to bear? (in {unit})"

def generate_question_heel(m, diameter, single_heel):
    if single_heel:
        return f"A {m} kg girl wearing high heel shoes balances on a single heel. The heel is circular with a diameter {diameter} micrometer. What is the pressure exerted by the heel on the horizontal floor?"
    else:
        return f"A {m} kg girl wearing high heel shoes. The heels are circular with a diameter {diameter} micrometer. What is the pressure exerted by each of the heels on the horizontal floor?"

def generate_input_formula_lift(m, area):
    return f"{m} * 9.8 / ({area} * (10 ** -6))"

def generate_input_formula_heel(m, diameter, single_heel):
    area = (math.pi * diameter * diameter * (10 ** -12)) / 4
    if single_heel:
        return f"{m} * 9.8 / {area}"
    else:
        return f"{m} * 4.9 / {area}"

samples = []

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1, 4)

    if types == 1 or types == 2:
        m = random.randint(1000, 5000)
        area = random.randint(1000, 5000) * 10
        question = generate_question_lift(m, area, types == 1)
        p_pascal, p_atm = calculate_max_pressure(m, area)
        input_formula = generate_input_formula_lift(m, area)
        if types == 1:
            explanation = f"The maximum pressure is calculated using the formula P = (m * 9.8) / A, where m is the maximum mass of the car ({m} kg) and A is the area of the piston ({area} mm^2)."
            output = f"The maximum pressure the piston has to bear is {p_pascal:.2e} pascal. {explanation}"
        else:
            explanation = f"The maximum pressure is calculated using the formula P = (m * 9.8) / A, where m is the maximum mass of the car ({m} kg) and A is the area of the piston ({area} mm^2)."
            output = f"The maximum pressure the piston has to bear is {p_atm:.1f} atmosphere. {explanation}"
    else:
        m = random.randint(40, 110)
        diameter = random.randint(5000, 35000)
        single_heel = random.randint(0, 1)
        question = generate_question_heel(m, diameter, single_heel)
        p, explanation = calculate_pressure_heel(m, diameter, single_heel)
        input_formula = generate_input_formula_heel(m, diameter, single_heel)
        if single_heel:
            output = f"The pressure exerted by the heel on the horizontal floor is {p:.2e} newton. {explanation}"
        else:
            output = f"The pressure exerted by each heel on the horizontal floor is {p:.2e} newton. {explanation}"

    sample["instruction"] = question
    sample["input"] = input_formula
    sample["output"] = output

    samples.append(sample)

# Read the existing JSON file
with open("science/MechanicalPropertiesOfLiquids/mpl.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/MechanicalPropertiesOfLiquids/mpl.json", "w") as file:
    json.dump(existing_data, file, indent=4)

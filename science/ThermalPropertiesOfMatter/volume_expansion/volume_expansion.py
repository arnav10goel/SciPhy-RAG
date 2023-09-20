import random
import json

no_of_samples = 90

def cal1(t1, t2, d1, a):
    return round(d1 * a * (t2 - t1), 2)

def generate_question_type1(t1, t2, d1, a):
    volume_change = cal1(t1, t2, d1, a)
    question = f"The coefficient of volume expansion of glycerine is {a} K^-1. What is the change in its volume {d1} m^3 for a rise in temperature from {t1} degree C to {t2} degree C?"
    input_formula = "Change in volume = d1 * a * (t2 - t1)"
    output = f"To find the change in volume, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the change in volume is approximately {volume_change} m^3."
    return question, input_formula, output

def generate_question_type2(t1, t2, d1, a):
    volume_change = cal1(t1, t2, d1, a)
    question = f"The coefficient of volume expansion of copper is {a} K^-1. What is the change in its volume {d1} m^3 for a rise in temperature from {t1} degree C to {t2} degree C?"
    input_formula = "Change in volume = d1 * a * (t2 - t1)"
    output = f"To find the change in volume, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the change in volume is approximately {volume_change} m^3."
    return question, input_formula, output

def generate_question_type3(t1, t2, d1, a):
    volume_change = cal1(t1, t2, d1, a)
    question = f"The coefficient of volume expansion of brass is {a} K^-1. What is the change in its volume {d1} m^3 for a rise in temperature from {t1} degree C to {t2} degree C?"
    input_formula = "Change in volume = d1 * a * (t2 - t1)"
    output = f"To find the change in volume, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the change in volume is approximately {volume_change} m^3."
    return question, input_formula, output

def generate_question_type4(t1, t2, d1, a):
    volume_change = cal1(t1, t2, d1, a)
    question = f"The coefficient of volume expansion of steel is {a} K^-1. What is the change in its volume {d1} m^3 for a rise in temperature from {t1} degree C to {t2} degree C?"
    input_formula = "Change in volume = d1 * a * (t2 - t1)"
    output = f"To find the change in volume, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the change in volume is approximately {volume_change} m^3."
    return question, input_formula, output

def generate_question_type5(t1, t2, d1, a):
    volume_change = cal1(t1, t2, d1, a)
    question = f"The coefficient of linear expansion of glycerine is {a} K^-1. What is the change in its volume {d1} m^3 for a rise in temperature from {t1} degree C to {t2} degree C?"
    input_formula = "Change in volume = d1 * a * (t2 - t1)"
    output = f"To find the change in volume, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the change in volume is approximately {volume_change} m^3."
    return question, input_formula, output

def generate_question_type6(t1, t2, d1, a):
    volume_change = cal1(t1, t2, d1, a)
    question = f"The coefficient of linear expansion of copper is {a} K^-1. What is the change in its volume {d1} m^3 for a rise in temperature from {t1} degree C to {t2} degree C?"
    input_formula = "Change in volume = d1 * a * (t2 - t1)"
    output = f"To find the change in volume, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the change in volume is approximately {volume_change} m^3."
    return question, input_formula, output

def generate_question_type7(t1, t2, d1, a):
    volume_change = cal1(t1, t2, d1, a)
    question = f"The coefficient of linear expansion of brass is {a} K^-1. What is the change in its volume {d1} m^3 for a rise in temperature from {t1} degree C to {t2} degree C?"
    input_formula = "Change in volume = d1 * a * (t2 - t1)"
    output = f"To find the change in volume, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the change in volume is approximately {volume_change} m^3."
    return question, input_formula, output

def generate_question_type8(t1, t2, d1, a):
    volume_change = cal1(t1, t2, d1, a)
    question = f"The coefficient of linear expansion of steel is {a} K^-1. What is the change in its volume {d1} m^3 for a rise in temperature from {t1} degree C to {t2} degree C?"
    input_formula = "Change in volume = d1 * a * (t2 - t1)"
    output = f"To find the change in volume, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the change in volume is approximately {volume_change} m^3."
    return question, input_formula, output

samples = []

for i in range(no_of_samples):
    types = random.randint(1, 8)
    if types == 1:
        t1 = random.randint(10, 110)
        t2 = random.randint(t1 + 150, t1 + 400)
        d1 = random.randint(10, 110)
        a = 49 * 10**-5
        question, input_formula, output = generate_question_type1(t1, t2, d1, a)
    elif types == 2:
        t1 = random.randint(10, 110)
        t2 = random.randint(t1 + 150, t1 + 400)
        d1 = random.randint(10, 110)
        a = 5.1 * 10**-5
        question, input_formula, output = generate_question_type2(t1, t2, d1, a)
    elif types == 3:
        t1 = random.randint(10, 110)
        t2 = random.randint(t1 + 150, t1 + 400)
        d1 = random.randint(10, 110)
        a = 6 * 10**-5
        question, input_formula, output = generate_question_type3(t1, t2, d1, a)
    elif types == 4:
        t1 = random.randint(10, 110)
        t2 = random.randint(t1 + 150, t1 + 400)
        d1 = random.randint(10, 110)
        a = 3.6 * 10**-5
        question, input_formula, output = generate_question_type4(t1, t2, d1, a)
    elif types == 5:
        t1 = random.randint(10, 110)
        t2 = random.randint(t1 + 150, t1 + 400)
        d1 = random.randint(10, 110)
        a = 49 * 10**-5
        question, input_formula, output = generate_question_type5(t1, t2, d1, a)
    elif types == 6:
        t1 = random.randint(10, 110)
        t2 = random.randint(t1 + 150, t1 + 400)
        d1 = random.randint(10, 110)
        a = 5.1 * 10**-5
        question, input_formula, output = generate_question_type6(t1, t2, d1, a)
    elif types == 7:
        t1 = random.randint(10, 110)
        t2 = random.randint(t1 + 150, t1 + 400)
        d1 = random.randint(10, 110)
        a = 6 * 10**-5
        question, input_formula, output = generate_question_type7(t1, t2, d1, a)
    elif types == 8:
        t1 = random.randint(10, 110)
        t2 = random.randint(t1 + 150, t1 + 400)
        d1 = random.randint(10, 110)
        a = 3.6 * 10**-5
        question, input_formula, output = generate_question_type8(t1, t2, d1, a)

    sample = {
        'instruction': question,
        'input': input_formula,
        'output': output
    }
    samples.append(sample)

# Load existing JSON file
with open("science/ThermalPropertiesOfMatter/tpm.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/ThermalPropertiesOfMatter/tpm.json", "w") as file:
    json.dump(existing_data, file, indent=4)


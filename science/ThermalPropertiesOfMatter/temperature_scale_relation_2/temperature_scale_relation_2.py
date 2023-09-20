import random
import json

no_of_samples = 40

def cal1(t1, t2, t, ta, tb):
    return round((((t2 - t1) * (t - ta)) / (tb - ta)) + t1, 1)

def generate_question_type1(t1, t2, t):
    temperature = cal1(t1, t2, t, 0, 100)
    question = f"On an unknown scale, the temperature of the melting point and boiling point of water is {t1} degrees and {t2} degrees respectively. If the temperature on the Celsius scale is {t} degrees Celsius, what is the temperature shown on that scale?"
    input_formula = "Temperature on the unknown scale = (((t2 - t1) * (t - ta)) / (tb - ta)) + t1"
    output = f"To find the temperature on the unknown scale, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the temperature on the unknown scale is approximately {temperature}."
    return question, input_formula, output

def generate_question_type2(t1, t2, t):
    temperature = cal1(t1, t2, t, 273, 373)
    question = f"On an unknown scale, the temperature of the melting point and boiling point of water is {t1} degrees and {t2} degrees respectively. If the temperature on the Kelvin scale is {t} degrees Kelvin, what is the temperature shown on that scale?"
    input_formula = "Temperature on the unknown scale = (((t2 - t1) * (t - ta)) / (tb - ta)) + t1"
    output = f"To find the temperature on the unknown scale, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the temperature on the unknown scale is approximately {temperature}."
    return question, input_formula, output

def generate_question_type3(t1, t2, t):
    temperature = cal1(t1, t2, t, 32, 212)
    question = f"On an unknown scale, the temperature of the melting point and boiling point of water is {t1} degrees and {t2} degrees respectively. If the temperature on the Fahrenheit scale is {t} degrees Fahrenheit, what is the temperature shown on that scale?"
    input_formula = "Temperature on the unknown scale = (((t2 - t1) * (t - ta)) / (tb - ta)) + t1"
    output = f"To find the temperature on the unknown scale, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the temperature on the unknown scale is approximately {temperature}."
    return question, input_formula, output

samples = []

for i in range(no_of_samples):
    types = random.randint(1, 3)
    if types == 1:
        t1 = random.randint(-100, 300)
        t2 = random.randint(t1 + 100, t1 + 300)
        t = random.randint(10, 160)
        question, input_formula, output = generate_question_type1(t1, t2, t)
    elif types == 2:
        t1 = random.randint(-100, 300)
        t2 = random.randint(t1 + 100, t1 + 300)
        t = random.randint(280, 400)
        question, input_formula, output = generate_question_type2(t1, t2, t)
    elif types == 3:
        t1 = random.randint(-100, 300)
        t2 = random.randint(t1 + 100, t1 + 300)
        t = random.randint(40, 200)
        question, input_formula, output = generate_question_type3(t1, t2, t)

    sample = {
        "instruction": question,
        "input": input_formula,
        "output": output
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

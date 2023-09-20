import random
import math
import json

no_of_samples = 30

def cal1(t1, t2, d1, a):
    d2 = d1 * (math.sqrt(1 + (a * d1 * (t2 - t1))))
    return round(d2 - d1, 3)

def generate_question_type1(t1, t2, d1, a):
    d_change = cal1(t1, t2, d1, a)
    question = f"A hole is drilled in a steel sheet. The diameter of the hole is {d1} cm at {t1} degree C. What is the change in the diameter of the hole when the sheet is heated to {t2} degree C? Coefficient of linear expansion of steel = 1.2 x 10-5K-1."
    input_formula = "Change in diameter = initial diameter * sqrt(1 + (coefficient of linear expansion * initial diameter * (final temperature - initial temperature))) - initial diameter"
    output = f"To calculate the change in diameter, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the change in diameter is approximately {d_change} cm."
    return question, input_formula, output

def generate_question_type2(t1, t2, d1, a):
    d_change = cal1(t1, t2, d1, a)
    question = f"A hole is drilled in a copper sheet. The diameter of the hole is {d1} cm at {t1} degree C. What is the change in the diameter of the hole when the sheet is heated to {t2} degree C? Coefficient of linear expansion of copper = 1.7 x 10-5K-1."
    input_formula = "Change in diameter = initial diameter * sqrt(1 + (coefficient of linear expansion * initial diameter * (final temperature - initial temperature))) - initial diameter"
    output = f"To calculate the change in diameter, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the change in diameter is approximately {d_change} cm."
    return question, input_formula, output

def generate_question_type3(t1, t2, d1, a):
    d_change = cal1(t1, t2, d1, a)
    question = f"A hole is drilled in a brass sheet. The diameter of the hole is {d1} cm at {t1} degree C. What is the change in the diameter of the hole when the sheet is heated to {t2} degree C? Coefficient of linear expansion of brass = 2 x 10-5K-1."
    input_formula = "Change in diameter = initial diameter * sqrt(1 + (coefficient of linear expansion * initial diameter * (final temperature - initial temperature))) - initial diameter"
    output = f"To calculate the change in diameter, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the change in diameter is approximately {d_change} cm."
    return question, input_formula, output

samples = []

for i in range(no_of_samples):
    types = random.randint(1, 3)

    t1 = random.randint(10, 110)
    t2 = random.randint(t1 + 150, t1 + 400)
    d1 = random.randint(10, 110)

    if types == 1:
        a = 1.2 * 10**-5
        question, input_formula, output = generate_question_type1(t1, t2, d1, a)

    elif types == 2:
        a = 1.7 * 10**-5
        question, input_formula, output = generate_question_type2(t1, t2, d1, a)

    elif types == 3:
        a = 2 * 10**-5
        question, input_formula, output = generate_question_type3(t1, t2, d1, a)

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

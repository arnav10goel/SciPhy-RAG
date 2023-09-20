import random
import json

no_of_samples = 30

def cal1(t1, d1, d2, a):
    return round(t1 + ((d2 - d1) / (a * d1)), 1)

def generate_question_type1(t1, d1, d2, a):
    temperature = cal1(t1, d1, d2, a)
    question = f"A large steel wheel is to be fitted onto a shaft of the same material. At {t1} degree C, the outer diameter of the shaft is {d1} cm and the diameter of the central hole in the wheel is {d2} cm. The shaft is cooled using 'dry ice'. At what temperature of the shaft does the wheel slip on the shaft? Assume the coefficient of linear expansion of the steel to be constant over the required temperature range αsteel = 1.20 x 10-5K-1."
    input_formula = "Required temperature = t1 + ((d2 - d1) / (α * d1))"
    output = f"To calculate the required temperature, we use the following formula:\n\n{input_formula}\n\nSubstituting the given values into the formula, we find that the temperature is approximately {temperature} degree C."
    return question, input_formula, output

samples = []

for i in range(no_of_samples):
    types = random.randint(1, 3)

    t1 = random.randint(10, 210)
    d1 = random.randint(10, 210)
    d2 = random.randint(1, 20)
    d2 = round(d2 / 1000, 3)
    d2 = d1 - d2

    if types == 1:
        a = 1.2 * 10**-5
        question, input_formula, output = generate_question_type1(t1, d1, d2, a)
    elif types == 2:
        a = 2 * 10**-5
        question, input_formula, output = generate_question_type1(t1, d1, d2, a)
    elif types == 3:
        a = 1.7 * 10**-5
        question, input_formula, output = generate_question_type1(t1, d1, d2, a)

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

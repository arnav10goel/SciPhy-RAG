import random
import json

samples = []
no_of_samples = 30

def type1():
    T = random.randint(0, 200)
    R1 = random.randint(1, 800)
    R2 = random.randint(1, 50)
    q = f"At temperature ({T} degree C) the resistance of a heating element is {R1} ohm. What is the temperature of the element if the resistance is found to be {R1 + R2} ohm (temp coeff = 1.7 x 10^(-4) degree C-1)?"
    input_formula = "T = ((R2 - R1) / (R1 * temp_coeff)) + T1"
    explanation = "To calculate the temperature of the element, use the formula: T = ((R2 - R1) / (R1 * temp_coeff)) + T1, where R2 is the final resistance, R1 is the initial resistance, temp_coeff is the temperature coefficient, and T1 is the initial temperature."
    a = f"{round((R2 / (R1 * 1.7 * (10 ** -4))) + T, 1)} degree centigrade"
    output = f"{a}\n\n{explanation}"
    return q, input_formula, output

def type2():
    R1 = random.randint(1, 200)
    T1 = random.randint(1, 200)
    R2 = random.randint(1, 20)
    T2 = random.randint(1, 20)
    q = f"A wire made up of unknown material has a resistance {R1} ohm at {T1} degree C, and a resistance of {R1 + R2} ohm at {T1 + T2} degree C. Determine the temperature coefficient of resistivity of that material?"
    input_formula = "temp_coeff = (R2 - R1) / (R1 * T2)"
    explanation = "To determine the temperature coefficient of resistivity, use the formula: temp_coeff = (R2 - R1) / (R1 * T2), where R2 is the final resistance, R1 is the initial resistance, T2 is the temperature change, and temp_coeff is the temperature coefficient."
    a = "{:.2e} degree centigrade-1".format((R2 / (R1 * T2)))
    output = f"{a}\n\n{explanation}"
    return q, input_formula, output

def type3():
    V = random.randint(220, 240)
    I1 = random.randint(1, 2000)
    I2 = random.randint(1, 200)
    R1 = (V / (I1 + I2)) * 1000
    R2 = (V / I1) * 1000
    q = f"A heating element using nichrome connected to a {V} V supply draws an initial current of {I1 + I2} mA which settles after a few seconds to a steady value of {I1} mA. What is the steady temperature of the heating element if room temperature is 27 degree C (temp coeff of nichrome is 1.70 x 10^(-4) degree C-1)?"
    input_formula = "T = ((R2 - R1) / (R1 * temp_coeff)) + T_room"
    explanation = "To calculate the steady temperature of the heating element, use the formula: T = ((R2 - R1) / (R1 * temp_coeff)) + T_room, where R2 is the resistance with steady current, R1 is the resistance with initial current, temp_coeff is the temperature coefficient, and T_room is the room temperature."
    a = f"{round((R2 - R1) / (R1 * (1.7 * (10 ** -4)))) + 27} degree centigrade"
    output = f"{a}\n\n{explanation}"
    return q, input_formula, output

for i in range(no_of_samples):
    types = random.randint(1, 3)
    if types == 1:
        ques, input_formula, answer = type1()
    elif types == 2:
        ques, input_formula, answer = type2()
    else:
        ques, input_formula, answer = type3()
    sample = {
        'instruction': ques,
        'input': input_formula,
        'output': answer,
    }
    samples.append(sample)

# Load existing JSON file
with open("science/Electricity/elec.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save the updated JSON data
with open("science/Electricity/elec.json", "w") as file:
    json.dump(existing_data, file, indent=4)

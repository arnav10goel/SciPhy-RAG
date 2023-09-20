import random
import json

no_of_samples = 10

def calculate_mass(m1, m2, t1, t2, t3):
    ls = m1 * (t3 - t1)
    rs = m2 * (t2 - t3)
    if t3 > 50:
        res = round((rs - ls) / (t3 - 50), 1)
    elif t3 < 50:
        res = round((ls - rs) / (50 - t3), 1)
    else:
        return "can not be determined"
    return res

def calculate_mass_type2(m1, t1, t2):
    ls = m1 * (t1 - t2)
    return round(ls / (50 - t1), 1)

def calculate_mass_type3(m, t, t1):
    rs = m * (t - t1)
    return round(rs / (t1 - 50), 1)

def calculate_balance_position(m, m1, t1):
    return round(((50 * m) + (m1 * t1)) / (m + m1), 1)

def calculate_balance_position_type5(m, m1, m2, t1, t2):
    return round(((50 * m) + (m1 * t1) + (m2 * t2)) / (m + m1 + m2), 1)

def generate_question_type1(m1, m2, t1, t2, t3):
    q = f"A meter stick is balanced on a knife edge at its center. When two coins, each of mass {m1} g and {m2} g respectively, are put at the {t1} mark and {t2} mark respectively, the stick is found to be balanced at {t3} cm. What is the mass of the meter stick?"
    input_formula = "Mass = (Right Side - Left Side) / Distance"
    left_side_formula = f"Left Side = m1 * (t3 - t1) = {m1} * ({t3} - {t1})"
    right_side_formula = f"Right Side = m2 * (t2 - t3) = {m2} * ({t2} - {t3})"
    mass = calculate_mass(m1, m2, t1, t2, t3)
    if mass == "can not be determined":
        output = "The mass of the meter stick cannot be determined from the given information."
    else:
        output = f"The mass of the meter stick is approximately {mass} g."
    output += f"\n{left_side_formula}\n{right_side_formula}"
    return q, input_formula, output

def generate_question_type2(m1, t1, t2):
    q = f"A meter stick is balanced on a knife edge at its center. When a coin of mass {m1} g is put at the {t1} mark, the stick is found to be balanced at {t2} cm. What is the mass of the meter stick?"
    input_formula = "Mass = (Left Side) / Distance"
    left_side_formula = f"Left Side = m1 * (t1 - t2) = {m1} * ({t1} - {t2})"
    mass = calculate_mass_type2(m1, t1, t2)
    output = f"The mass of the meter stick is approximately {mass} g."
    output += f"\n{left_side_formula}"
    return q, input_formula, output

def generate_question_type3(m, t, t1):
    q = f"A meter stick of mass {m} g is balanced on a knife edge at its center. When a coin is put at the {t1} mark, the stick is found to be balanced at {t} cm. What is the mass of the meter stick?"
    input_formula = "Mass = (Right Side) / Distance"
    right_side_formula = f"Right Side = m * (t - t1) = {m} * ({t} - {t1})"
    mass = calculate_mass_type3(m, t, t1)
    output = f"The mass of the meter stick is approximately {mass} g."
    output += f"\n{right_side_formula}"
    return q, input_formula, output

def generate_question_type4(m, t, t1):
    q = f"A meter stick of mass {m} g is balanced on a knife edge at its center. Where will the stick be balanced when a coin of mass {m1} g is put at the {t1} mark?"
    input_formula = "Balance Position = ((50 * m) + (m1 * t1)) / (m + m1)"
    balance_position_formula = f"Balance Position = ((50 * {m}) + ({m1} * {t1})) / ({m} + {m1})"
    balance_position = calculate_balance_position(m, m1, t1)
    output = f"The stick will be balanced at approximately {balance_position} cm."
    output += f"\n{balance_position_formula}"
    return q, input_formula, output

def generate_question_type5(m, m1, m2, t1, t2):
    q = f"A meter stick is balanced on a knife edge at its center. Where will the stick be balanced when two coins, each of mass {m1} g and {m2} g respectively, are put at the {t1} mark and {t2} mark respectively?"
    input_formula = "Balance Position = ((50 * m) + (m1 * t1) + (m2 * t2)) / (m + m1 + m2)"
    balance_position_formula = f"Balance Position = ((50 * {m}) + ({m1} * {t1}) + ({m2} * {t2})) / ({m} + {m1} + {m2})"
    balance_position = calculate_balance_position_type5(m, m1, m2, t1, t2)
    output = f"The stick will be balanced at approximately {balance_position} cm."
    output += f"\n{balance_position_formula}"
    return q, input_formula, output

samples = []

for i in range(no_of_samples):
    types = random.randint(1, 5)
    m = random.randint(1, 100)
    t = random.randint(1, 100)
    m1 = random.randint(1, 100)
    m2 = random.randint(1, 100)
    t1 = random.randint(1, 48)
    t2 = random.randint(52, 100)
    t3 = random.randint(1, 100)

    if types == 1:
        question, i_f, answer = generate_question_type1(m1, m2, t1, t2, t3)
    elif types == 2:
        question, i_f, answer = generate_question_type2(m1, t1, t2)
    elif types == 3:
        question, i_f, answer = generate_question_type3(m, t, t1)
    elif types == 4:
        question, i_f, answer = generate_question_type4(m, t, t1)
    elif types == 5:
        question, i_f, answer = generate_question_type5(m, m1, m2, t1, t2)

    sample = {
        "instruction" : question,
        "input" : i_f,
        "output" : answer
    }

    samples.append(sample)

# Load existing JSON file
with open("science/RotationalMotion/rom.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/RotationalMotion/rom.json", "w") as file:
    json.dump(existing_data, file, indent=4)

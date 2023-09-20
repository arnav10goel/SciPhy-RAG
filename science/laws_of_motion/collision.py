import random
import json

no_of_samples = 70

def calculation_v1(m1, m2, u1, u2, v2): 
    return round(((m1*u1)+(m2*u2)-(m2*v2))/m1, 1)

def calculation_v2(m1, m2, u1, u2, v1): 
    return round(((m1*u1)+(m2*u2)-(m1*v1))/m2, 1)

def calculation_u1(m1, m2, u2, v1, v2): 
    return round(((m1*v1)+(m2*v2)-(m2*u2))/m1, 1)

def calculation_u2(m1, m2, u1, v1, v2): 
    return round(((m1*v1)+(m2*v2)-(m1*u1))/m2, 1)

def calculation_m1(m2, u1, u2, v1, v2):
    return round((m2*(v2-u2))/(u1-v1), 1)

def calculation_m2(m1, u1, u2, v1, v2):
    return round((m1*(v1-u1))/(u2-v2), 1)

def type1():
    m1 = random.randint(1, 15)
    m2 = random.randint(1, 15)
    u1 = random.randint(1, 30)
    u2 = random.randint(1, 30)
    v1 = random.randint(1, 30)
    instruction = f"Two objects of masses {m1} g and {m2} g are moving along the same line and direction with velocities of {u1} m/s and {u2} m/s respectively. They collide and after the collision, the first object moves at a velocity of {v1} m/s. Determine the velocity of the second object."
    input_values = "v2 = ((m1 * u1) + (m2 * u2) - (m1 * v1)) / m2"
    v2 = calculation_v2(m1, m2, u1, u2, v1)
    output_values = f"To find the velocity of the second object (v2), we use the formula:\n\nv2 = ((m1 * u1) + (m2 * u2) - (m1 * v1)) / m2\n\nSubstituting the given values, we have:\n\nv2 = (({m1} * {u1}) + ({m2} * {u2}) - ({m1} * {v1})) / {m2}\n\nSimplifying the expression gives us v2 = {v2} m/s."
    return instruction, input_values, output_values

def type2():
    m1 = random.randint(1, 15)
    m2 = random.randint(1, 15)
    u1 = random.randint(1, 30)
    u2 = random.randint(1, 30)
    v2 = random.randint(1, 30)
    instruction = f"Two objects of masses {m1} g and {m2} g are moving along the same line and direction with velocities of {u1} m/s and {u2} m/s respectively. They collide and after the collision, the second object moves at a velocity of {v2} m/s. Determine the velocity of the first object."
    input_values = "v1 = ((m1 * u1) + (m2 * u2) - (m2 * v2)) / m1"
    v1 = calculation_v1(m1, m2, u1, u2, v2)
    output_values = f"To find the velocity of the first object (v1), we use the formula:\n\nv1 = ((m1 * u1) + (m2 * u2) - (m2 * v2)) / m1\n\nSubstituting the given values, we have:\n\nv1 = (({m1} * {u1}) + ({m2} * {u2}) - ({m2} * {v2})) / {m1}\n\nSimplifying the expression gives us v1 = {v1} m/s."
    return instruction, input_values, output_values

def type3():
    m1 = random.randint(1, 15)
    m2 = random.randint(1, 15)
    u1 = random.randint(1, 30)
    u2 = random.randint(1, 30)
    v1 = random.randint(1, 30)
    v2 = random.randint(1, 30)

    instruction = f"Two objects of masses {m1} g and {m2} g are moving along the same line and direction with velocities of {u1} m/s and {u2} m/s respectively. They collide and after the collision, the first object moves at a velocity of {v1} m/s. Determine the initial velocity of the first object."
    input_values = "u1 = ((m1 * v1) + (m2 * v2) - (m2 * u2)) / m1"
    u1 = calculation_u1(m1, m2, u1, v1, v2)
    output_values = f"To find the initial velocity of the first object (u1), we use the formula:\n\nu1 = ((m1 * v1) + (m2 * v2) - (m2 * u2)) / m1\n\nSubstituting the given values, we have:\n\nu1 = (({m1} * {v1}) + ({m2} * {v2}) - ({m2} * {u2})) / {m1}\n\nSimplifying the expression gives us u1 = {u1} m/s."
    return instruction, input_values, output_values

def type4():
    m1 = random.randint(1, 15)
    m2 = random.randint(1, 15)
    u1 = random.randint(1, 30)
    u2 = random.randint(1, 30)
    v1 = random.randint(1, 30)
    v2 = random.randint(1, 30)
    instruction = f"Two objects of masses {m1} g and {m2} g are moving along the same line and direction with velocities of {u1} m/s and {u2} m/s respectively. They collide and after the collision, the second object moves at a velocity of {v1} m/s. Determine the initial velocity of the second object."
    input_values = "u2 = ((m1 * v1) + (m2 * v2) - (m1 * u1)) / m2"
    u2 = calculation_u2(m1, m2, u1, v1, v2)
    output_values = f"To find the initial velocity of the second object (u2), we use the formula:\n\nu2 = ((m1 * v1) + (m2 * v2) - (m1 * u1)) / m2\n\nSubstituting the given values, we have:\n\nu2 = (({m1} * {v1}) + ({m2} * {v2}) - ({m1} * {u1})) / {m2}\n\nSimplifying the expression gives us u2 = {u2} m/s."
    return instruction, input_values, output_values

def type5():
    u1 = random.randint(1, 30)
    u2 = random.randint(1, 30)
    v1 = random.randint(1, 30)
    v2 = random.randint(1, 30)
    m2 = random.randint(1, 15)
    instruction = f"Two objects collide and their masses are unknown. Their initial velocities are {u1} m/s and {u2} m/s respectively. After the collision, the first object moves at a velocity of {v1} m/s and the second object moves at a velocity of {v2} m/s. Determine the mass of the first object."
    input_values = "m1 = (m2 * (v2 - u2)) / (u1 - v1)"
    m1 = calculation_m1(m2, u1, u2, v1, v2)
    output_values = f"To find the mass of the first object (m1), we use the formula:\n\nm1 = (m2 * (v2 - u2)) / (u1 - v1)\n\nSubstituting the given values, we have:\n\nm1 = ({m2} * ({v2} - {u2})) / ({u1} - {v1})\n\nSimplifying the expression gives us m1 = {m1} g."
    return instruction, input_values, output_values

def type6():
    u1 = random.randint(1, 30)
    u2 = random.randint(1, 30)
    v1 = random.randint(1, 30)
    v2 = random.randint(1, 30)
    m1 = random.randint(1, 15)
    instruction = f"Two objects collide and their masses are unknown. Their initial velocities are {u1} m/s and {u2} m/s respectively. After the collision, the first object moves at a velocity of {v1} m/s and the second object moves at a velocity of {v2} m/s. Determine the mass of the second object."
    input_values = "m2 = (m1 * (v1 - u1)) / (u2 - v2)"
    m2 = calculation_m2(m1, u1, u2, v1, v2)
    output_values = f"To find the mass of the second object (m2), we use the formula:\n\nm2 = (m1 * (v1 - u1)) / (u2 - v2)\n\nSubstituting the given values, we have:\n\nm2 = ({m1} * ({v1} - {u1})) / ({u2} - {v2})\n\nSimplifying the expression gives us m2 = {m2} g."
    return instruction, input_values, output_values

# Generate questions
questions = []
for _ in range(no_of_samples):
    question_type = random.randint(1, 6)
    if question_type == 1:
        instruction, input_values, output_values = type1()
    elif question_type == 2:
        instruction, input_values, output_values = type2()
    elif question_type == 3:
        instruction, input_values, output_values = type3()
    elif question_type == 4:
        instruction, input_values, output_values = type4()
    elif question_type == 5:
        instruction, input_values, output_values = type5()
    elif question_type == 6:
        instruction, input_values, output_values = type6()

    question = {
        "instruction": instruction,
        "input": input_values,
        "output": output_values
    }
    questions.append(question)

# Read the existing JSON file
with open("science/laws_of_motion/nlm.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(questions)

# Write the updated data to the JSON file with indentation
with open("science/laws_of_motion/nlm.json", "w") as file:
    json.dump(existing_data, file, indent=4)


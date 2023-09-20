import random
import json

no_of_samples = 20

def calculate_acceleration(m1, m2, F):
    return F / (m1 + m2)

def generate_question(m1, m2, F, type):
    if type == 1:
        q = f"Two bodies A, B of masses {m1} kg and {m2} kg respectively kept on a smooth, horizontal surface are tied to the ends of a tight string. A horizontal force F = {F} N is applied to A along the direction of the string. What is the acceleration and tension in the string?"
        T = F - m1 * calculate_acceleration(m1, m2, F)
    else:
        q = f"Two bodies A, B of masses {m1} kg and {m2} kg respectively kept on a smooth, horizontal surface are tied to the ends of a tight string. A horizontal force F = {F} N is applied to B along the direction of the string. What is the acceleration and tension in the string?"
        T = F - m2 * calculate_acceleration(m1, m2, F)
    a = f"The acceleration is {round(calculate_acceleration(m1, m2, F), 1)} m/s^2, and the tension is {round(T, 1)} N."
    return q, a

data = []

for i in range(no_of_samples):
    m1 = random.randint(1, 200)
    m2 = random.randint(1, 200)
    F = random.randint(40, 400)
    question_type = random.randint(1, 2)
    question, answer = generate_question(m1, m2, F, question_type)
    data.append({
        "instruction": question,
        "input": "",
        "output": answer
    })
# Read the existing JSON file
with open("science/laws_of_motion/nlm.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/laws_of_motion/nlm.json", "w") as file:
    json.dump(existing_data, file, indent=4)

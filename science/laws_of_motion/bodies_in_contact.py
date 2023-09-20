import random
import json

no_of_samples = 20

def reaction_of_partition(m1, m2, mu, F):
    q = f"Two bodies A and B of masses {m1} kg and {m2} kg are in contact with each other rest on a table against a rigid wall (such that B is attached to the wall). The coefficient of friction between the bodies and the table is {mu}. A force of {F} N is applied horizontally to A. Then what is the reaction of the partition."
    a = f"{F} newton"
    return q, a

def action_reaction_forces(m1, m2, mu, F):
    q = f"Two bodies A and B of masses {m1} kg and {m2} kg are in contact with each other rest on a table against a rigid wall (such that B is attached to the wall). The coefficient of friction between the bodies and the table is {mu}. A force of {F} N is applied horizontally to A. Then what is the value of action-reaction forces between A and B."
    a = f"{F} newton"
    return q, a

def value_of_action_reaction_forces(m1, m2, mu, F):
    q = f"Two bodies A and B of masses {m1} kg and {m2} kg are in contact with each other rest on a table. The coefficient of friction between the bodies and the table is {mu}. A force of {F} N is applied horizontally to A. Then what is the value of action-reaction forces between A and B."
    if F <= mu * m1 * 10:
        a = "0 newton"
    elif F <= mu * (m1 + m2) * 10:
        a = f"{round(F - mu * m1 * 10, 1)} newton"
    else:
        a = f"{round(mu * m2 * 10, 1)} newton"
    return q, a

def value_of_acceleration(m1, m2, mu, F):
    q = f"Two bodies A and B of masses {m1} kg and {m2} kg are in contact with each other rest on a table. The coefficient of friction between the bodies and the table is {mu}. A force of {F} N is applied horizontally to A. Then what is the value of acceleration."
    if F <= mu * (m1 + m2) * 10:
        a = "0 ms^-2"
    else:
        expr = (F - mu * (m1 + m2) * 10) / (m1 + m2)
        a = f"{round(expr, 1)} ms^-2"
    return q, a

data = []

for i in range(no_of_samples):
    m1 = random.randint(1, 20)
    m2 = random.randint(1, 20)
    mu = round(random.randint(0, 100) / 100, 2)
    F = random.randint(1, 270)
    q_type = random.randint(1, 6)
    if q_type == 1:
        q, a = reaction_of_partition(m1, m2, mu, F)
    elif q_type == 2:
        q, a = action_reaction_forces(m1, m2, mu, F)
    elif q_type == 3 or q_type == 4:
        q, a = value_of_action_reaction_forces(m1, m2, mu, F)
    else:
        q, a = value_of_acceleration(m1, m2, mu, F)

    data.append({
        "instruction": q,
        "input": "",
        "output": a
    })

# Read the existing JSON file
with open("science/laws_of_motion/nlm.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/laws_of_motion/nlm.json", "w") as file:
    json.dump(existing_data, file, indent=4)
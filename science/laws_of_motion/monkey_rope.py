import random
import json

no_of_samples = 20

def generate_question():
    m = random.randint(10, 70)
    T = random.randint(50, 1050)
    upacc = random.randint(1, 10)
    downacc = random.randint(1, 10)
    vel = random.randint(1, 10)
    
    q = f"A monkey of mass {m} kg climbs on a rope which can stand a maximum tension of {T} N. In which of the following cases will the rope break: the monkey\n"
    q += f"(a) climbs up with an acceleration of {upacc} ms-2\n"
    q += f"(b) climbs down with an acceleration of {downacc} ms-2\n"
    q += f"(c) climbs up (or) down with a uniform speed of {vel} ms-1\n"
    
    a = ""
    if T < m * (10 + upacc):
        a += "(a) break, "
    else:
        a += "(a) not break, "
    
    if T < m * (10 - downacc):
        a += "(b) break, "
    else:
        a += "(b) not break, "
    
    if T < m * 10:
        a += "(c) break\n"
    else:
        a += "(c) not break\n"
    
    formulas = f"Tension = m * (10 + {upacc})" + "\n" + f"Tension = m * (10 - {downacc})" + "\n" +"Tension = m * 10"
    
    return q, a, formulas

data = []

for i in range(no_of_samples):
    ques, answer, formulas = generate_question()
    data.append({
        "instruction": ques,
        "input": formulas,
        "output": answer.strip()
    })

# Read the existing JSON file
with open("science/laws_of_motion/nlm.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/laws_of_motion/nlm.json", "w") as file:
    json.dump(existing_data, file, indent=4)

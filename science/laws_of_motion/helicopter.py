import random
import json

no_of_samples = 40

def calculate_force_floor(m1, m2, acc):
    return m2 * (10 + acc)

def calculate_force_rotor(m1, m2, acc):
    return (m1 + m2) * (10 + acc)

def calculate_force_helicopter(m1, m2, acc):
    return (m1 + m2) * (10 + acc)

data = []

for i in range(no_of_samples):
    m1 = random.randint(500, 2500)
    m2 = random.randint(200, 400)
    acc = random.randint(1, 20)
    q_type = random.randint(1, 3)
    
    instruction = f"A helicopter of mass {m1} kg rises with a vertical acceleration of {acc} m/s^2. The crew and the passengers weigh {m2} kg. Give the magnitude and direction of"
    formula = ""
    
    if q_type == 1:
        formula = "force on the floor by the crew and passengers"
        answer = calculate_force_floor(m1, m2, acc)
        output = f"{answer} newton, vertically downwards"
    elif q_type == 2:
        formula = "action of the rotor of the helicopter on surrounding air"
        answer = calculate_force_rotor(m1, m2, acc)
        output= f"{answer} newton, vertically downwards"
    else:
        formula = "force on the helicopter due to the surrounding air"
        answer = calculate_force_helicopter(m1, m2, acc)
        output = f"{answer} newton, vertically upwards"
    
    output += f"\n\nThe {formula} can be calculated based on the given mass ({m1} kg), weight of crew and passengers ({m2} kg), and acceleration ({acc} m/s^2)."
    
    question = {
        "instruction": instruction,
        "input": formula,
        "output": output
    }
    
    data.append(question)

# Read the existing JSON file
with open("science/laws_of_motion/nlm.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/laws_of_motion/nlm.json", "w") as file:
    json.dump(existing_data, file, indent=4)

import random
import json

no_of_samples = 20

def calculate_recoil_velocity(m_b, v_b, m_r):
    return round((m_b * v_b) / m_r, 1)

def calculate_rifle_mass(m_b, v_b, v_r):
    return round((m_b * v_b) / v_r, 1)

def calculate_bullet_velocity(m_r, v_r, v_b):
    return round((m_r * v_r) / v_b, 1)

def calculate_bullet_mass(m_r, v_r, v_b):
    return round((m_r * v_r) / v_b, 1)

data = []

for i in range(no_of_samples):
    types = random.randint(0, 3)
    if types == 0:
        m_b = random.randint(1, 100)
        m_r = random.randint(1, 100) * 100
        v_b = random.randint(900, 1000)
        v_r = calculate_recoil_velocity(m_b, v_b, m_r)
        q = f"From a rifle of mass {m_r} g, a bullet of mass {m_b} g is fired with a velocity of {v_b} m/s, then calculate the recoil velocity of the rifle (in m/s)?"
        a = f"{v_r} m/s"
    elif types == 1:
        m_b = random.randint(1, 100)
        v_b = random.randint(900, 1000)
        v_r = round(random.randint(900, 1000) / 100, 2)
        m_r = calculate_rifle_mass(m_b, v_b, v_r)
        q = f"From a rifle, a bullet of mass {m_b} g is fired with a velocity of {v_b} m/s, if the recoil velocity of the rifle is {v_r} m/s, then calculate the mass of the rifle (in grams)?"
        a = f"{m_r} g"
    elif types == 2:
        m_b = random.randint(1, 100)
        m_r = random.randint(1, 100) * 100
        v_r = round(random.randint(900, 1000) / 100, 2)
        v_b = calculate_bullet_velocity(m_r, v_r, m_b)
        q = f"From a rifle of mass {m_r} g, a bullet of mass {m_b} g is fired, if the recoil velocity of the rifle is {v_r} m/s, then calculate the velocity of the bullet (in m/s)?"
        a = f"{v_b} m/s"
    else:
        m_r = random.randint(1, 100) * 100
        v_b = random.randint(900, 1000)
        v_r = round(random.randint(900, 1000) / 100, 2)
        m_b = calculate_bullet_mass(m_r, v_r, v_b)
        q = f"From a rifle of mass {m_r} g, a bullet is fired with a velocity of {v_b} m/s, if the recoil velocity of the rifle is {v_r} m/s, then calculate the mass of the bullet (in grams)?"
        a = f"{m_b} g"
    
    data.append({
        "instruction": q,
        "input": "Calculate recoil velocity, rifle mass, bullet velocity, or bullet mass",
        "output": f"{a}"
    })

# Read the existing JSON file
with open("science/laws_of_motion/nlm.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/laws_of_motion/nlm.json", "w") as file:
    json.dump(existing_data, file, indent=4)
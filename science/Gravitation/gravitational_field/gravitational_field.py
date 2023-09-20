import random
import json

no_of_samples = 100

G = 6.67 * (10 ** -11)

def cal1(m, r, R):
    return 0

def cal2(m, r, R):
    return (-1 * G * m) / (r * r)

def cal3(m, r):
    return (-1 * G * m) / (r * r)

def cal4(m, r, R):
    return (-1 * G * m * r) / (R ** 3)

def generate_question(types, m, r, R):
    if types == 0:
        return f"What is the gravitational field at a point P at a distance of {r} m from the center of the spherical shell of radius {R} m and mass {m} kg?"
    elif types == 1:
        return f"What is the gravitational field at a point P at a distance of {r} m from the center of the uniform solid sphere of radius {R} m and mass {m} kg?"
    elif types == 2:
        return f"What is the gravitational field at a point P on the surface of the spherical shell of radius {R} m and mass {m} kg?"
    elif types == 3:
        return f"What is the gravitational field at a point P at a distance of {R} m from a mass of {m} kg?"
    elif types == 4:
        return f"What is the gravitational field at the centre of the uniform solid sphere of radius {R} m and mass {m} kg?"
    elif types == 5:
        return f"What is the gravitational field at a point P at a distance of {r} m from the center of the uniform solid sphere of radius {R} m and mass {m} kg?"
    elif types == 6:
        return f"What is the gravitational field at a point P on the surface of the uniform solid sphere of radius {R} m and mass {m} kg?"
    elif types == 7:
        return f"What is the gravitational field at a point P on the surface of the uniform solid sphere of radius {R} m and mass {m} kg?"

def generate_input_formula(types, m, r, R):
    if types == 0:
        return "Gravitational Field (g) = 0 N/kg"
    elif types in (1, 5):
        return f"Gravitational Field (g) = {cal2.__name__}({m}, {r}, {R}) N/kg"
    elif types in (2, 3, 4, 6, 7):
        return f"Gravitational Field (g) = {cal3.__name__}({m}, {R}) N/kg"

def generate_output_explanation(types, m, r, R):
    if types in (0, 4):
        return "The gravitational field at the specified point is zero."
    elif types == 1:
        return f"The gravitational field at a point P at a distance of {r} m from the center of the uniform solid sphere of radius {R} m and mass {m} kg is given by the formula g = (-G * m) / (r^2), where G is the gravitational constant, m is the mass, and r is the distance. Plugging in the values, we get g = {cal2(m, r, R):.2e} N/kg."
    elif types == 2:
        return f"The gravitational field at a point P on the surface of the spherical shell of radius {R} m and mass {m} kg is given by the formula g = (-G * m) / (r^2), where G is the gravitational constant, m is the mass, and r is the distance. Plugging in the values, we get g = {cal3(m, R):.2e} N/kg."
    elif types == 3:
        return f"The gravitational field at a point P at a distance of {R} m from a mass of {m} kg is given by the formula g = (-G * m) / (r^2), where G is the gravitational constant, m is the mass, and r is the distance. Plugging in the values, we get g = {cal3(m, R):.2e} N/kg."
    elif types == 5:
        return f"The gravitational field at a point P at a distance of {r} m from the center of the uniform solid sphere of radius {R} m and mass {m} kg is given by the formula g = (-G * m * r) / (R^3), where G is the gravitational constant, m is the mass, r is the distance, and R is the radius. Plugging in the values, we get g = {cal4(m, r, R):.2e} N/kg."
    elif types == 6:
        return f"The gravitational field at a point P on the surface of the uniform solid sphere of radius {R} m and mass {m} kg is given by the formula g = (-G * m) / (r^2), where G is the gravitational constant, m is the mass, and r is the distance. Plugging in the values, we get g = {cal3(m, R):.2e} N/kg."
    elif types == 7:
        return f"The gravitational field at a point P on the surface of the uniform solid sphere of radius {R} m and mass {m} kg is given by the formula g = (-G * m) / (r^2), where G is the gravitational constant, m is the mass, and r is the distance. Plugging in the values, we get g = {cal3(m, R):.2e} N/kg."

samples = []

for i in range(no_of_samples):
    sample = {}
    types = random.randint(0, 7)
    m = random.randint(1, 500)
    r = random.randint(1, 500)
    R = random.randint(r + 1, r + 100)

    question = generate_question(types, m, r, R)
    input_formula = generate_input_formula(types, m, r, R)
    output_explanation = generate_output_explanation(types, m, r, R)

    sample["instruction"] = question
    sample["input"] = input_formula
    sample["output"] = output_explanation

    samples.append(sample)

# Read the existing JSON file
with open("science/Gravitation/g.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/Gravitation/g.json", "w") as file:
    json.dump(existing_data, file, indent=4)

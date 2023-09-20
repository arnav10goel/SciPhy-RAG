import random
import json

no_of_samples = 40

g = 6.67 * (10 ** -11)

def cal1(m1, m2, R):
    p = (-1 * g * m1) / (R * R) + (g * m2) / (R * R)
    if p < 0:
        return -1 * p
    return p

def cal2(m1, m2, R):
    p = (-1 * g * m1) / R - (g * m2) / R
    return p

def type1():
    m1 = random.randint(1, 200)
    m2 = random.randint(1, 200)
    R = random.randint(1, 200)
    t = random.randint(1, 2)
    if t == 1:
        q = f"Two heavy spheres each of mass {m1} kg, {m2} kg respectively are placed {R} m apart on a horizontal table. What is the gravitational field at the mid point of the line joining the centres of the spheres?"
        input_formula = "Gravitational Field (g) = " + "{:.2e}".format(cal1(m1, m2, R / 2)) + " newton/kg"
        output_explanation = f"The gravitational field at the mid point of the line joining the centres of the spheres is given by the formula g = (-1 * G * m1 / (R^2)) + (G * m2 / (R^2)), where G is the gravitational constant, m1 and m2 are the masses of the spheres, and R is the distance between them. Plugging in the values, we get g = " + "{:.2e}".format(cal1(m1, m2, R / 2)) + " N/kg."
    else:
        q = f"Two heavy spheres each of mass {m1} kg, {m2} kg respectively are placed {R} m apart on a horizontal table. What is the gravitational field at the mid point of the line joining the centres of the spheres? G = 6.67 x 10^-11"
        input_formula = "Gravitational Field (g) = " + "{:.2e}".format(cal1(m1, m2, R / 2)) + " newton/kg"
        output_explanation = f"The gravitational field at the mid point of the line joining the centres of the spheres is given by the formula g = (-1 * G * m1 / (R^2)) + (G * m2 / (R^2)), where G is the gravitational constant, m1 and m2 are the masses of the spheres, and R is the distance between them. Plugging in the values, we get g = " + "{:.2e}".format(cal1(m1, m2, R / 2)) + " N/kg."

    return q, input_formula, output_explanation

def type2():
    m1 = random.randint(1, 200)
    m2 = random.randint(1, 200)
    R = random.randint(1, 200)
    t = random.randint(1, 2)
    if t == 1:
        q = f"Two heavy spheres each of mass {m1} kg, {m2} kg respectively are placed {R} m apart on a horizontal table. What is the gravitational potential at the mid point of the line joining the centres of the spheres?"
        input_formula = "Gravitational Potential (V) = " + "{:.2e}".format(cal2(m1, m2, R / 2)) + " joule/kg"
        output_explanation = f"The gravitational potential at the mid point of the line joining the centres of the spheres is given by the formula V = (-1 * G * m1 / R) - (G * m2 / R), where G is the gravitational constant, m1 and m2 are the masses of the spheres, and R is the distance between them. Plugging in the values, we get V = " + "{:.2e}".format(cal2(m1, m2, R / 2)) + " J/kg."
    else:
        q = f"Two heavy spheres each of mass {m1} kg, {m2} kg respectively are placed {R} m apart on a horizontal table. What is the gravitational potential at the mid point of the line joining the centres of the spheres? G = 6.67 x 10^-11"
        input_formula = "Gravitational Potential (V) = " + "{:.2e}".format(cal2(m1, m2, R / 2)) + " joule/kg"
        output_explanation = f"The gravitational potential at the mid point of the line joining the centres of the spheres is given by the formula V = (-1 * G * m1 / R) - (G * m2 / R), where G is the gravitational constant, m1 and m2 are the masses of the spheres, and R is the distance between them. Plugging in the values, we get V = " + "{:.2e}".format(cal2(m1, m2, R / 2)) + " J/kg."

    return q, input_formula, output_explanation

samples = []

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1, 2)
    if types == 1:
        ques, input_formula, output_explanation = type1()
    else:
        ques, input_formula, output_explanation = type2()

    sample["instruction"] = ques
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

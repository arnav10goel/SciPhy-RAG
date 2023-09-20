import random
import math
import json

no_of_samples = 40

def calculate_vertical_deflection(s, m, Y):
    deflection = (m * 9.8) / (Y * (10 ** 9) * (s * (10 ** (-2))))
    return deflection * (10 ** 9)

def calculate_strain(l, b, F):
    A = l * b * (10 ** (-6))
    strain = F / (A * (42 * (10 ** 9)))
    return strain * (10 ** 6)

def generate_question_cube(s, m, Y):
    input_formula = f"deflection = (mass * 9.8) / (Y * 10^9 * (edge_length * 10^-2))"
    return f"The edge of a cube is {s} cm long. One face of the cube is firmly fixed to a vertical wall. A mass of {m} kg is then attached to the opposite face of the cube. The shear modulus of the material of the cube is {Y} GPa. What is the vertical deflection of this face?", input_formula

def generate_question_copper(l, b, F):
    input_formula = f"strain = force / (A * (shear_modulus * 10^9))"
    return f"A piece of copper having a rectangular cross-section of {l} mm x {b} mm is pulled in tension with {F} N force, producing only elastic deformation. Calculate the resulting strain? Shear modulus of elasticity of copper is 42 x 10^9 N/m^2.", input_formula

samples = []

for i in range(no_of_samples):
    types = random.randint(1, 2)

    if types == 1:
        s = random.randint(1, 200)
        m = random.randint(20, 200)
        Y = random.randint(1, 200)
        question, input_formula = generate_question_cube(s, m, Y)
        deflection = calculate_vertical_deflection(s, m, Y)
        explanation = f"To calculate the vertical deflection, we use the formula:\n\n"
        explanation += f"deflection = (mass * 9.8) / (Y * 10^9 * (edge_length * 10^-2))\n"
        explanation += f"   = ({m} kg * 9.8) / ({Y} * 10^9 GPa * ({s} cm * 10^-2 m/cm))\n"
        explanation += f"   = {deflection:.1f} nm."
        output = explanation

    else:
        l = random.randint(1, 100)
        b = random.randint(1, 100)
        F = random.randint(1, 800) * 100
        question, input_formula = generate_question_copper(l, b, F)
        strain = calculate_strain(l, b, F)
        explanation = f"To calculate the resulting strain, we use the formula:\n\n"
        explanation += f"strain = force / (A * (shear_modulus * 10^9))\n"
        explanation += f"   = {F} N / ({l} mm * {b} mm * 10^-6 m^2 * (42 * 10^9 N/m^2))\n"
        explanation += f"   = {strain:.1f} x 10^(-6)."
        output = explanation

    sample = {
        "instruction": question,
        "input": input_formula,
        "output": output
    }

    samples.append(sample)

# Read the existing JSON file
with open("science/MechanicalPropertiesOfSolids/mps.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/MechanicalPropertiesOfSolids/mps.json", "w") as file:
    json.dump(existing_data, file, indent=4)

import random
import json
import math

samples = []

no_of_samples = 40

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1, 5)
    if types == 1:
        E = random.randint(100, 10100)
        d = random.randint(1, 400)
        q = "In a uniform electric field of " + str(E) + " N/C, what is the flux through a square of " + str(
            d) + " cm, whose plane is parallel to the yz-plane?\n"
        a = "To calculate the flux through the square, we use the formula:\n"
        a += "Flux = Electric field * Area\n"
        a += "Given electric field = " + str(E) + " N/C, area = " + str(d * d) + " cm²,\n"
        a += "Flux = {:.2e} N·m²/C\n".format(E * d * d * (10 ** (-4)))
        input_formula = "Flux = Electric field * Area"
    elif types == 2:
        E = random.randint(10, 1010) * 10
        d = random.randint(1, 50)
        angle = random.randint(0, 90)
        q = "In a uniform electric field of " + str(E) + " N/C, what is the flux through a square of " + str(
            d) + " cm, whose plane is at " + str(angle) + " degrees angle with the x-axis?\n"
        a = "To calculate the flux through the square, we use the formula:\n"
        a += "Flux = Electric field * Area * cos(theta)\n"
        a += "Given electric field = " + str(E) + " N/C, area = " + str(d * d) + " cm², theta = " + str(angle) + " degrees,\n"
        a += "Flux = {:.2e} N·m²/C\n".format(E * d * d * (10 ** (-4)) * math.cos(angle * (math.pi / 180)))
        input_formula = "Flux = Electric field * Area * cos(theta)"
    elif types == 3:
        F = random.randint(1000, 2001000)
        q = "A black box has a net outward flux of " + str(F) + " N·m²/C through its surface. What is the net charge inside the box?\n"
        a = "To determine the net charge inside the box, we use the formula:\n"
        a += "Net charge = Flux * epsilon_0\n"
        a += "Given flux = " + str(F) + " N·m²/C,\n"
        a += "Net charge = {:.2e} C\n".format(8.854 * (10 ** (-12)) * F)
        input_formula = "Net charge = Flux * epsilon_0"
    elif types == 4:
        q1 = random.randint(100, 10100) * (10 ** (-9))
        d = random.randint(1, 400)
        q = "A point charge of " + str(q1) + " C is at a distance of " + str(
            d / 2) + " cm directly above the center of the square of side " + str(
            d) + " cm. What is the flux through the square?\n"
        a = "To calculate the flux through the square, we use the formula:\n"
        a += "Flux = (Q / (6 * epsilon_0)) * A\n"
        a += "Given charge Q = " + str(q1) + " C, area A = " + str(d * d) + " cm²,\n"
        a += "Flux = {:.2e} N·m²/C\n".format((1000 * q1) / (6 * 8.854))
        input_formula = "Flux = (Q / (6 * epsilon_0)) * A"
    else:
        q1 = random.randint(100, 10100) * (10 ** (-9))
        d = random.randint(1, 400)
        q = "A point charge of " + str(q1) + " C is at the center of a cubic Gaussian surface with an edge length of " + str(
            d) + " cm. What is the net flux through the surface?\n"
        a = "To calculate the net flux through the surface, we use the formula:\n"
        a += "Net flux = (Q / epsilon_0)\n"
        a += "Given charge Q = " + str(q1) + " C,\n"
        a += "Net flux = {:.2e} N·m²/C\n".format((1000 * q1) / (8.854))
        input_formula = "Net flux = (Q / epsilon_0)"

    sample["instruction"] = q
    sample["input"] = input_formula
    sample["output"] = a

    samples.append(sample)

# Load existing JSON file
with open("science/ElectricChargesAndFields/ecf.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/ElectricChargesAndFields/ecf.json", "w") as file:
    json.dump(existing_data, file, indent=4)

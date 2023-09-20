import random
import json
import math

samples = []
no_of_samples = 40
pi = math.pi

def calculate_capacitance(r, s):
    ep = 8.85 * (10**(-12))
    C = (ep * pi * r * r * 0.01) / s
    return C

def calculate_rate_of_charge(I, C):
    return I / (C * 1000)

def calculate_displacement_current(I):
    return round(I / 1000, 3)

def calculate_rms_current(I):
    return I

def calculate_magnetic_field_amplitude(d, r, I):
    mu0 = 2 * (10**(-7))
    I0 = math.sqrt(2) * I
    B = (mu0 * d * I0) / (r * r * 0.01)
    return B

for i in range(no_of_samples):
    types = random.randint(1, 13)
    sample = {}

    if types <= 7:
        r = random.randint(1, 200)
        s = random.randint(1, 200)
        I = random.randint(1, 200)
        C = calculate_capacitance(r, s)
        q = f"A capacitor made of two circular plates of radius {r} cm, and separated by {s} cm. The capacitor is being charged by an external source. The charging current is constant and equal to {I} mA. "

        if types <= 3:
            q += "Calculate the capacitance between the plates?"
            input_formula = f"r = {r} cm, s = {s} cm"
            output_formula = f"{C:.2e} farad"
            explanation = "The capacitance of a capacitor can be calculated using the formula: C = (επr²) / s, where ε is the permittivity of free space, r is the radius of the plates, and s is the separation between the plates."
        elif types <= 6:
            q += "Calculate the rate of charge of potential difference between the plates?"
            input_formula = f"I = {I} mA, C = {C:.2e} farad"
            output_formula = f"{calculate_rate_of_charge(I, C):.2e} volt/s"
            explanation = "The rate of change of potential difference between the plates can be calculated using the formula: dV/dt = I / C, where I is the charging current and C is the capacitance."
        else:
            q += "Obtain the displacement current across the plates?"
            input_formula = f"I = {I} mA"
            output_formula = f"{calculate_displacement_current(I)} ampere"
            explanation = "The displacement current across the plates can be calculated by converting the charging current to amperes."

    else:
        r = random.randint(10, 200)
        c = random.randint(1, 200)
        f = random.randint(1, 200) * 10
        I = 230 * f * c * (10**(-12))
        q = f"A parallel plate capacitor made of circular plates of radius r = {r} cm has a capacitance C = {c} pF. The capacitor is connected to a 230 V ac supply with an angular frequency of {f} rad/s. "

        if types <= 10:
            q += "What is the rms value of the conduction current?"
            input_formula = f"I = {I:.2e} ampere"
            output_formula = f"{calculate_rms_current(I):.2e} ampere"
            explanation = "The rms value of the conduction current can be calculated by taking the square root of the average of the square of the current."
        else:
            d = random.randint(1, 10)
            q += f"Determine the amplitude of B at a point {d} cm from the axis between the plates?"
            input_formula = f"d = {d} cm, r = {r} cm, I = {I:.2e} ampere"
            output_formula = f"{calculate_magnetic_field_amplitude(d, r, I):.2e} tesla"
            explanation = "The amplitude of the magnetic field at a point between the plates can be calculated using the formula: B = (μ₀dI₀) / (r²), where μ₀ is the permeability of free space, d is the distance from the axis, I₀ is the rms current, and r is the radius of the plates."

    sample['instruction'] = q
    sample['input'] = input_formula
    sample['output'] = f"{output_formula}\n\n{explanation}"
    samples.append(sample)

# Load existing JSON file
with open("science/ElectroMagneticWaves/emw.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save the updated JSON data
with open("science/ElectroMagneticWaves/emw.json", "w") as file:
    json.dump(existing_data, file, indent=4)

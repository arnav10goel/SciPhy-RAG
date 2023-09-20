import random
import json
import math

samples = []
no_of_samples = 60
pi = math.pi

def determine_B0(E0):
    return E0 / (3 * (10**8))

def determine_angular_frequency(v):
    return 2 * pi * (10**6) * v

def determine_k(v):
    w = 2 * pi * (10**6) * v
    return w / (3 * (10**8))

def determine_wavelength(v):
    return 300 / v

def expression_for_E(E0, k, w):
    return f"{E0}sin[{k:.2e}x-{w:.2e}t]"

def expression_for_B(B0, k, w):
    return f"{B0:.2e}sin[{k:.2e}x-{w:.2e}t]"

for i in range(no_of_samples):
    types = random.randint(1, 22)
    E0 = random.randint(1, 2000)
    v = random.randint(1, 2000)
    sample = {}

    q = f"Suppose that the electric field amplitude of an electromagnetic wave is E0 = {E0} N/C and that its frequency is v = {v} MHz. "

    if types <= 2:
        q += "Determine B0?"
        input_formula = f"E0 = {E0} N/C"
        output_formula = f"{determine_B0(E0):.2e} tesla"
        explanation = "The magnetic field amplitude can be determined by dividing the electric field amplitude by the speed of light."
    elif types <= 4:
        q += "Determine angular frequency?"
        input_formula = f"v = {v} MHz"
        output_formula = f"{determine_angular_frequency(v):.2e} rad/s"
        explanation = "The angular frequency can be calculated by multiplying the frequency by 2π."
    elif types <= 7:
        q += "Determine k?"
        input_formula = f"v = {v} MHz"
        output_formula = f"{determine_k(v):.2e} rad/m"
        explanation = "The wave number (k) can be determined by dividing the angular frequency by the speed of light."
    elif types <= 10:
        q += "Determine wavelength?"
        input_formula = f"v = {v} MHz"
        output_formula = f"{determine_wavelength(v):.2f} m"
        explanation = "The wavelength can be calculated by dividing the speed of light by the frequency."
    elif types <= 15:
        q += "Find an expression for E?"
        w = determine_angular_frequency(v)
        k = determine_k(v)
        input_formula = f"E0 = {E0} N/C, k = {k:.2e} rad/m, w = {w:.2e} rad/s"
        output_formula = expression_for_E(E0, k, w)
        explanation = "The expression for the electric field (E) of an electromagnetic wave can be written as E = E0sin(kx - wt)."
    else:
        q += "Find an expression for B?"
        w = determine_angular_frequency(v)
        k = determine_k(v)
        B0 = determine_B0(E0)
        input_formula = f"B0 = {B0:.2e} tesla, k = {k:.2e} rad/m, w = {w:.2e} rad/s"
        output_formula = expression_for_B(B0, k, w)
        explanation = "The expression for the magnetic field (B) of an electromagnetic wave can be written as B = B0sin(kx - wt)."

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

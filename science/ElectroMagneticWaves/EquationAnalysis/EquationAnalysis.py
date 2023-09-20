import random
import json
import math

samples = []
no_of_samples = 50
pi = math.pi

def determine_wavelength(k):
    return (2 * pi) / k

def determine_frequency(w):
    return w / (2 * pi)

def determine_magnetic_field_amplitude(E0):
    return E0 / (3 * (10**8))

def expression_for_magnetic_field(B0, k, w):
    return f"{B0:.2e}cos[{k}y + {w}t]"

for i in range(no_of_samples):
    types = random.randint(1, 10)
    E0 = random.randint(1, 2000)
    k = random.randint(1, 2000)
    w = round((3 * (10**8)) / k)
    sample = {}

    q = f"Suppose that the electric field part of an electromagnetic wave in vacuum is E = {E0}cos[{k}y + {w}t]. "

    if types <= 2:
        q += "What is the wavelength?"
        input_formula = f"k = {k}"
        output_formula = f"{determine_wavelength(k):.2e} m"
        explanation = "The wavelength can be calculated by dividing 2π by the wave number (k)."
    elif types <= 4:
        q += "What is the frequency?"
        input_formula = f"w = {w}"
        output_formula = f"{determine_frequency(w):.2e} rad/s"
        explanation = "The frequency can be determined by dividing the angular frequency by 2π."
    elif types <= 6:
        q += "What is the amplitude of the magnetic field part of the wave?"
        input_formula = f"E0 = {E0} N/C"
        output_formula = f"{determine_magnetic_field_amplitude(E0):.2e} tesla"
        explanation = "The magnetic field amplitude can be calculated by dividing the electric field amplitude by the speed of light."
    elif types <= 10:
        q += "Write an expression for the magnetic field part of the wave?"
        B0 = determine_magnetic_field_amplitude(E0)
        input_formula = f"B0 = {B0:.2e} tesla, k = {k}, w = {w}"
        output_formula = expression_for_magnetic_field(B0, k, w)
        explanation = "The expression for the magnetic field part of the wave can be written as B = B0cos[ky + wt]."

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

import random
import json

samples = []
no_of_samples = 20

def determine_wavelength(f):
    return 3 * (10**8) / f

def determine_wavelength_band(f1, f2):
    lambda1 = 3 * (10**5) / f1
    lambda2 = 3 * (10**5) / (f1 + f2)
    return f"{round(lambda2, 2)} m to {round(lambda1, 2)} m"

for i in range(no_of_samples):
    types = random.randint(1, 2)
    sample = {}

    if types == 1:
        f = random.randint(1, 2000000) * 100
        q = f"A plane electromagnetic wave travels in vacuum along the z-direction. If the frequency of the wave is {f} Hz, what is its wavelength?"
        input_formula = f"f = {f} Hz"
        output_formula = f"{determine_wavelength(f):.2e} m"
        explanation = "The wavelength of the wave can be calculated by dividing the speed of light by the frequency."
    else:
        f1 = random.randint(1, 2000)
        f2 = random.randint(f1 + 1, f1 + 2000)
        q = f"A radio can tune in to any station in the {f1} kHz to {f1 + f2} kHz band. What is the corresponding wavelength band?"
        input_formula = f"f1 = {f1} kHz, f2 = {f2} kHz"
        output_formula = determine_wavelength_band(f1, f2)
        explanation = "The corresponding wavelength band can be calculated by dividing the speed of light by the frequency range."

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

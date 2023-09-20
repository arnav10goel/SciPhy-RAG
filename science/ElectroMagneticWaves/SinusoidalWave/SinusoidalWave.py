import random
import json

samples = []
no_of_samples = 30

def determine_wavelength(f):
    return 3 / f

def determine_magnetic_field_amplitude(A):
    return A / (3 * (10**8))

for i in range(no_of_samples):
    types = random.randint(1, 2)
    f = random.randint(1, 2000)
    A = random.randint(1, 2000)
    sample = {}

    q = f"In a plane electromagnetic wave, the electric field oscillates sinusoidally at a frequency of {f} x 10^8 Hz and amplitude {A} V/m. "

    if types == 1:
        q += "What is the wavelength of the wave?"
        input_formula = f"f = {f} x 10^8 Hz"
        output_formula = f"{determine_wavelength(f):.2e} m"
        explanation = "The wavelength can be calculated by dividing 3 by the frequency."
    elif types == 2:
        q += "What is the amplitude of the oscillating magnetic field?"
        input_formula = f"A = {A} V/m"
        output_formula = f"{determine_magnetic_field_amplitude(A):.2e} tesla"
        explanation = "The amplitude of the oscillating magnetic field can be calculated by dividing the electric field amplitude by the speed of light."

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

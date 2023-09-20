import random
import json

samples = []
no_of_samples = 20

def calculate_flux_change(i1, i2, t, m):
    return round((m * (i1 - i2)) / t, 2)

for i in range(no_of_samples):
    t = random.randint(1, 100)
    t = round(t * 0.1, 1)
    i2 = random.randint(1, 30)
    i1 = random.randint(i2 + 1, i2 + 20)
    m = random.randint(1, 100)
    m = round(m * 0.1, 1)
    q = "A pair of adjacent coils has a mutual inductance of " + str(m) + " H. If the current in one coil changes from " + str(i1) + " A to " + str(i2) + " A in " + str(t) + " sec, what is the change of flux linkage with the other coil?\n"
    a = str(calculate_flux_change(i1, i2, t, m)) + " weber\n"

    sample = {
        'instruction': q,
        'input': "Change in Flux Linkage = (Mutual Inductance * (Current 1 - Current 2)) / Time",
        'output': a + "\n\nThe change of flux linkage with the other coil can be calculated using the formula Change in Flux Linkage = (Mutual Inductance * (Current 1 - Current 2)) / Time, where Mutual Inductance is the mutual inductance of the coils, Current 1 and Current 2 are the initial and final currents respectively, and Time is the time taken for the change in current to occur."
    }
    samples.append(sample)

# Load existing JSON file
with open("science/ElectroMagneticInduction/emi.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save the updated JSON data
with open("science/ElectroMagneticInduction/emi.json", "w") as file:
    json.dump(existing_data, file, indent=4)

import random
import json

samples = []
no_of_samples = 20

for i in range(no_of_samples):
    I1 = random.randint(1, 200)
    I2 = random.randint(1, 20)
    t = round(random.randint(1, 20) / 100, 2)
    V = random.randint(100, 300)
    q = "Current in a circuit falls from " + str(I1 + I2) + " A to " + str(I2) + " A in " + str(t) + " s. If an average emf of " + str(V) + " V induced, give an estimate of the self-inductance of the circuit.\n"
    a = "{:.2e} henry\n".format((V * t) / I1)

    sample = {
        'instruction': q,
        'input': "Self-Inductance = (Average EMF * Time) / (Initial Current - Final Current)",
        'output': a + "\n\nThe self-inductance of the circuit can be estimated using the formula Self-Inductance = (Average EMF * Time) / (Initial Current - Final Current), where Average EMF is the average induced electromotive force, Time is the time taken for the current to change, Initial Current is the initial current in the circuit, and Final Current is the final current in the circuit."
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

import random
import json

samples = []

no_of_samples = 20

for i in range(no_of_samples):
    sample = {}
    rate = random.randint(1, 2000) * 100
    dipole_moment = random.randint(1, 2000)
    q = "If in a space electric field is along z-axis, increases uniformly along +ve z-direction, at the rate of {} NC⁻¹ per meter. What are the values of force and torque experienced by a system having a total dipole moment of {} x 10⁻⁹ Cm in the negative z-direction?\n".format(rate, dipole_moment)
    a = "To calculate the force and torque experienced by the system, we need to consider the interaction between the electric field and the dipole moment:\n"
    a += "Force = Electric field * Dipole moment\n"
    a += "Torque = 0\n"  # Since the electric field is along the z-axis and the dipole moment is in the negative z-direction, there is no torque.
    a += "Given electric field rate = {} NC⁻¹/m, dipole moment = {} x 10⁻⁹ Cm:\n".format(rate, dipole_moment)
    a += "Force = {:.2e} N\n".format(rate * dipole_moment * (10 ** (-9)))

    sample["instruction"] = q
    sample["input"] = "Force = Electric field * Dipole moment"
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

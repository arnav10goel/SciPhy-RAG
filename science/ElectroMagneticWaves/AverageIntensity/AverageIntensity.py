import random
import math
import json

samples = []
no_of_samples = 20
pi = math.pi

for i in range(no_of_samples):
    per = random.randint(1, 99)
    P = random.randint(1, 400)
    d = random.randint(1, 200)
    q = "About " + str(per) + " percent of the power of a " + str(P) + " W light bulb is converted to visible radiation. What is the average intensity of the visible radiation at a distance of " + str(d) + " m from the bulb?\n"
    P1 = (per / P) * 100
    I = P1 / (4 * pi * d * d)
    a = "{:.2e} watt/m2\n".format(I)

    sample = {
        'instruction': q,
        'input': "Average Intensity = (Percentage Power / Total Power) / (4 * pi * distance^2)",
        'output': a + "\n\nThe average intensity of the visible radiation at a distance 'd' from the bulb can be calculated using the formula Average Intensity = (Percentage Power / Total Power) / (4 * pi * distance^2), where Percentage Power is the percentage of power converted to visible radiation, Total Power is the total power of the light bulb, and 'd' is the distance from the bulb."
    }
    samples.append(sample)

# Load existing JSON file
with open("science/ElectroMagneticWaves/emw.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save the updated JSON data
with open("science/ElectroMagneticWaves/emw.json", "w") as file:
    json.dump(existing_data, file, indent=4)

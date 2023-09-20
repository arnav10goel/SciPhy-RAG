import random
import json

samples = []
no_of_samples = 20

def calculate_emf(B, l, w):
    emf = (B * l * w * w) / 2
    return "{:.2e}".format(emf)

for i in range(no_of_samples):
    B = random.randint(1, 200)
    l = random.randint(10, 210)
    w = random.randint(1, 200)
    q = "A " + str(l) + " cm long metallic rod is rotated with an angular frequency of " + str(w) + " rad s-1 about an axis normal to the rod passing through one of its ends. The other end of the rod is in contact with a circular metallic ring. A uniform magnetic field of " + str(B) + " T parallel to the axis exists everywhere. Find the EMF developed between the center and the ring.\n"
    a = "{:.2e} volt\n".format(float(calculate_emf(B, l, w)))  # Use 's' format code

    sample = {
        'instruction': q,
        'input': "EMF = (B * l * w^2) / 2",
        'output': a + "\n\nThe electromotive force (EMF) can be calculated using the formula EMF = (B * l * w^2) / 2, where B is the magnetic field magnitude, l is the length of the metallic rod, and w is the angular frequency of rotation in radians per second."
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

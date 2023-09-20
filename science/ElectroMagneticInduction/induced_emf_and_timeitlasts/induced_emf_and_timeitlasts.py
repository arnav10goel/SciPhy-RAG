import random
import math
import json

samples = []
no_of_samples = 20

pi = math.pi
mu = 4 * pi * (10 ** -7)

def calculate_emf(b, l, v):
    v = v * (10 ** -2)
    l = l * (10 ** -2)
    emf = b * l * v
    time_last = l / v
    return "{:.2e}".format(emf), "{:.2e}".format(time_last)

def type1():
    b = random.randint(1, 200)
    b = round(b * 0.1, 1)
    v = random.randint(1, 100)
    l1 = random.randint(1, 30)
    l2 = random.randint(1, 30)
    while l2 == l1:
        l2 = random.randint(1, 30)
    q = "A rectangular wire loop of sides " + str(l1) + " cm and " + str(l2) + " cm with a small cut is moving out of a region of uniform magnetic field of magnitude " + str(b) + " T directed normal to the loop. What is the emf developed across the cut if the velocity of the loop is " + str(v) + " cm/s in a direction normal to the two different sides of the loop? For how long does the induced voltage last in each case?\n"
    a1, a2 = calculate_emf(b, l1, v)
    a = a1 + " volt for " + a2 + " s if the velocity is perpendicular to the " + str(l1) + " cm side, "
    a1, a2 = calculate_emf(b, l2, v)
    a += a1 + " volt for " + a2 + " s if the velocity is perpendicular to the " + str(l2) + " cm side\n"
    return q, a

for i in range(no_of_samples):
    ques, answer = type1()
    sample = {
        'instruction': ques,
        'input': "EMF = B * l * v",
        'output': answer + "\n\nThe electromotive force (EMF) can be calculated using the formula EMF = B * l * v, where B is the magnetic field magnitude, l is the side length of the rectangular wire loop, and v is the velocity of the loop after conversion from cm/s to m/s."
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

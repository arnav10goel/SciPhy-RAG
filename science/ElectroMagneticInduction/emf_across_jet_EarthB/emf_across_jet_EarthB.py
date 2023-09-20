import random
import math
import json

samples = []
no_of_samples = 20

pi = math.pi
bH = 5 * (10**-5)

def calculate_voltage_difference(v, l, d):
    b = bH * math.sin((pi * d) / 180)
    v = (v * 5) / 18
    voltage_diff = (b * l * v) / 2
    return "{:.2e}".format(voltage_diff)

def type1():
    v = random.randint(1000, 2000)
    l = random.randint(10, 80)
    d = random.randint(1, 90)
    q = "A jet plane is traveling towards the west at a speed of " + str(v) + " km/h. What is the voltage difference developed between the ends of the wing, having a span of " + str(l) + " m, if the Earth's magnetic field at the location has a magnitude of 5 x 10^(-4) T and the dip angle is " + str(d) + " degrees?\n"
    a = calculate_voltage_difference(v, l, d) + " volt\n"
    return q, a

for i in range(no_of_samples):
    ques, answer = type1()
    sample = {
        'instruction': ques,
        'input': "V = (B * l * v) / 2",
        'output': answer + "\n\nThe voltage difference (V) can be calculated using the formula V = (B * l * v) / 2, where B is the Earth's magnetic field magnitude, l is the span of the wing, and v is the speed of the jet plane after conversion from km/h to m/s."
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

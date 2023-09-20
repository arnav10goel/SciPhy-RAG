import random
import json

# A SONAR system fixed in a submarine operates at a frequency 40.0 kHz. An enemy submarine moves towards the SONAR with a speed of 360 km h-1. What is the frequency of sound reflected by the submarine? Take the speed of sound in water to be 1450 ms-1.

no_of_samples = 20  
# no_of_samples = 10

samples = []

for i in range(no_of_samples):
    sample = {}
    f = random.randint(1000,9000)*10
    v = random.randint(100,900)
    q = "A SONAR system fixed in a submarine operates at a frequency "+str(f)+" Hz. An enemy submarine moves towards the SONAR with a speed of "+str(v)+" kmph. What is the frequency of sound reflected by the submarine? Take the speed of sound in water to be 1450 ms-1.\n"
    v1 = v*(5/18)
    nu1 = ((1450+v1)/(1450-v1))*f
    input_formula = "Apparent frequency = [(Speed of sound in air + Speed of enemy submarine)/Speed of sound in air]*Original Frequency"
    a = "{:.2e}".format(nu1) + " hertz\n"
    a += "To calculate the frequency of sound reflected by the submarine in the SONAR system, we need to consider the Doppler effect due to the relative motion between the submarines. The Doppler effect accounts for the change in frequency observed when the source of sound and the observer are in relative motion."
    a += "The formula to calculate the frequency observed by the submarine is: f' = f * (v_sound / (v_sound - v_sub)), where f' is the observed frequency, f is the emitted frequency, v_sound is the speed of sound in water, and v_sub is the velocity of the submarine."

    sample["instruction"] = q
    sample["input"] = input_formula
    sample["output"] = a

    samples.append(sample)

# Load existing JSON file
with open("science/Waves/wave.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/Waves/wave.json", "w") as file:
    json.dump(existing_data, file, indent=4) 
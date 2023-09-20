import random
import math
import json

# A bat is flitting about in a cave, navigating via ultrasonic beeps. Assume that the sound emission frequency of the bat is 40 kHz. During one fast swoop directly toward a flat wall surface, the bat is moving at 0.03 times the speed of sound in air. What frequency does the bat hear reflected off the wall ?

no_of_samples = 20
# no_of_samples = 10

samples = []

for i in range(no_of_samples):
    sample = {}
    freq = random.randint(1000,6000)*10
    ratio = round(random.randint(200,2000)/10000,4)
    q = "A bat is flitting about in a cave, navigating via ultrasonic beeps. Assume that the sound emission frequency of the bat is "+str(freq)+" Hz. During one fast swoop directly toward a flat wall surface, the bat is moving at "+str(ratio)+" times the speed of sound in air. "
    types = random.randint(1,2)
    if types == 1:
        q = q + "What is the apparent frequency of the sound striking the wall?\n"
        app_freq = (1/(1-ratio))*freq
        input_formula = "apparent frequency = (speed of air/speed of air - speed of bat)*given frequency"
    else:
        q = q + "What frequency does the bat hear reflected off the wall?\n"
        app_freq = ((1+ratio)/(1-ratio))*freq
    input_formula = "apparent frequency = [{(speed of air + speed of bat)}/speed of air]*apparent frequency of sound striking the wall"
    a = "{:.2e}".format(app_freq) + " hertz\n"
    a += "The concept of Doppler's effect has been applied to calculate apparent frequencies."

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

    
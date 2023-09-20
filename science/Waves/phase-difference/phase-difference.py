import random
import json

# For the travelling harmonic wave
# y(x, t) = 2.0 cos 2π (10t – 0.0080x + 0.35)
# where x and y are in cm and t in s. Calculate the phase difference between oscillatory motion of two points separated by a distance of
# (a) 4 m (b) 0.5 m
# (c) λ/2 (d) 3λ/4.

no_of_samples = 30
# no_of_samples = 10

samples = []

for i in range(no_of_samples):
    sample = {}
    amp = random.randint(1,50)
    w = random.randint(1,50)
    k = round(random.randint(1,50)/1000,3)
    types = random.randint(1,2)
    q = "For the travelling harmonic wave y(x, t) = "+str(amp)+" cos 2π ("+str(w)+"t – "+str(k)+"x + 0.35) where x and y are in cm and t in s. Calculate the phase difference between oscillatory motion of two points separated by a distance of "
    lamda = 1/k
    input_formula = "Phase difference = (2pi/wavelength)* Path difference"
    if types == 1:
        dist = random.randint(1,20)
        q = q + str(dist)+" m?\n"
        phase_diff = (2*dist*100)/(lamda)
    else:
        num = random.randint(1,6)
        den = random.randint(1,6)
        while num == den:
            den = random.randint(1,6)
        q = q +str(num)+"λ/"+str(den)+" ?\n"
        phase_diff = (2*num)/den
    a = str(round(phase_diff,1))+" π rad\n"
    a += "To calculate the phase difference between two points in a traveling harmonic wave, we need to compare the phase angles of the wave at those points."
    a += "In the given wave equation, the phase angle is represented by the term inside the cosine function, i.e., 2π(wt - kx + 0.35), where w represents the angular frequency and k represents the wave number."
    a += "Let's assume the two points are at x1 and x2, separated by a distance Δx = x2 - x1. The phase difference between the oscillatory motion of these two points can be calculated using the equation: Phase difference = 2π(kΔx)"

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
import random
import json

# The transverse displacement of a string (clamped at its two ends) is given by y(x, t) = 0.06 sin 2π /3 x cos (120π t)
# where x, y are in m and t in s. The length of the string is 1.5 m and its mass is 3 x 10-2 kg. Answer the following:
# (i) Does the function represent a travelling or a stationary wave?
# (ii) Interpret the wave as a superimposition of two waves travelling in opposite directions. What are the wavelength, frequency and speed of propagation of each wave?
# (iii) Determine the tension in the string.

no_of_samples = 20
# no_of_samples = 10

samples = []

for i in range(no_of_samples):
    sample = {}
    A = round(random.randint(1,30)/100,2)
    num = random.randint(1,9)
    den = random.randint(2,9)
    while den == num:
        den = random.randint(2,9)
    w = random.randint(10,30)*5
    l = random.randint(1,10)
    mass = round(random.randint(1,10)/100,1)
    q = "The transverse displacement of a string is given by y(x, t) = "+str(A)+" sin "+str(num)+"π /"+str(den)+" x cos ("+str(w)+"π t) where x, y are in m and t in s. The length of the string is "+str(l)+" m and its mass is "+str(mass)+" kg,"
    types = random.randint(1,22)
    if types == 1:
        q = q + "does this function represent a travelling or a stationary wave?\n"
        a = "stationary\n"
        a += "It is a stationary wave due to the absence of phase difference."
    elif types < 17:
        q = q + "interpret this wave as a superimposition of two waves travelling in opposite direction, give "
        if types < 7:
            q = q + " wavelength of each wave?\n"
            lamda = num/(2*den)
            input_formula = "Wavelength = 2*pi/Wave number(k)"
            a = str(round(lamda,2))+" m\n"
        elif types < 12:
            q = q + " frequency of each wave?\n"
            freq = w/2
            input_formula = "frequency = w/2*pi"
            a = str(round(freq,1)) +" hertz\n"
        else:
            q = q + " magnitude of speed of propagation of each wave?\n"
            lamda = num/(2*den)
            speed = (lamda*w)/2
            input_formula = "speed = frequency*wavelength"
            a = str(round(speed,1)) +" ms-1\n"
    else:
        q = q + " what is the tension in the string?\n"
        mu = mass/l
        lamda = num/(2*den)
        speed = (lamda*w)/2
        T = mu*speed*speed
        input_formula = "Tension = speed^2*mass/length"
        a = str(round(T))+" newton\n"    
    
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
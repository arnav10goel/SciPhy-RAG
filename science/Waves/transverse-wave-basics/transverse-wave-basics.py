import random
import math
import json

# A transverse harmonic wave on a string is described by y(x, t) = 3.0 sin (36 t + 0.018 x + π/4) where x and y are in cm and t in s. The positive direction of x is from left to right.
# (a) Is this a travelling wave or a stationary wave? If it is travelling, what are the speed and direction of its propagation ?
# (b) What are its amplitude and frequency?
# (c) What is the initial phase at the origin?
# (d) What is the least distance between two successive crests in the wave?


no_of_samples = 60
# no_of_samples = 40

samples = []

for i in range(no_of_samples):
    sample = {}
    amp = random.randint(1,50)
    w = random.randint(1,100)
    k = round(random.randint(1,200)/1000,3)
    div = random.randint(2,10)
    q = "A transverse harmonic wave on a string is described by y(x, t) = "+str(amp)+" sin ("+str(w)+" t + "+str(k)+" x + π/"+str(div)+") where x and y are in cm and t in s. The positive direction of x is from left to right, "
    types = random.randint(1,5)
    if types == 1:
        q = q + "is this a travelling wave or a stationary wave? If it is travelling, what are the speed and direction of its propagation ?\n"
        input_formula = "speed = frequency*wavelength"
        a = "it is a travelling wave, it is travelling in -ve x direction with "+"{:.2e}".format(w/k)+" ms-1\n"
        a += """For a traveling wave, the speed of propagation (v) can be determined by the ratio between the angular frequency (ω) and the wave number (k): v = ω / k. In this case, the angular frequency is "+str(w)+" and the wave number is "+str(k)+". We can calculate the speed of propagation using these values: v = "+str(w)+" / "+str(k)"""
    elif types == 2:
        q = q + "then what is value of amplitude?\n"
        a = str(round(amp/100,2))+" m\n"
        a += "The amplitude represents the maximum displacement of the wave from its equilibrium position. In this case, the amplitude is "+str(amp)+" units, indicating that the wave oscillates between a maximum positive displacement of "+str(amp)+" units and a maximum negative displacement of "+str(amp)+" units from the equilibrium position."""
    elif types == 3:
        q = q + "then what is the value of frequency?\n"
        input_formula = "frequency = speed/wavelength"
        a = str(round(w/(2*math.pi),1)) + " hertz\n"
        a += """The relationship between angular frequency (ω) and frequency (f) is given by the equation: ω = 2πf. Therefore, the frequency (f) can be calculated as: f = ω / (2π). In this case, the angular frequency (ω) is "+str(w)+" radians/s. Substituting this value into the equation, we can calculate the frequency (f): f = "+str(w)+" / (2π). The calculated value of the frequency will give us the number of complete oscillations of the wave per unit time."""
    elif types == 4:
        q = q + "then what is the initial phase at the origin?\n"
        a = "π/"+str(div)+"\n"
        a += """To determine the initial phase, we look at the phase term in the equation, which is "+str(k)+"x + π/"+str(div)+". At the origin (x=0), the phase term becomes "+str("π/"+str(div))+". Hence, the initial phase at the origin is "+str("π/"+str(div))+" radians or "+str("180/"+str(div))+" degrees."""
    else:
        q = q +"then what is the least distance between two successive crests/troughs in the wave?\n"
        input_formula = "distance = 2*pi/k"
        a = str(round((2*math.pi)/k,1))+" m\n"
        a += """The distance between two successive crests or troughs in a wave is known as the wavelength (λ). In the given wave equation, y(x, t) = "+str(amp)+" sin ("+str(w)+" t + "+str(k)+" x + π/"+str(div)+"), the wave number (k) is involved in the phase term. The wave number is related to the wavelength by the equation: k = 2π / λ"""  
    
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
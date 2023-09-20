import random
import math
import json

# Monochromatic light of wavelength of l nm is incident on aa surface of refractive index mu. What is the wavelength, speed and frequenct of reflected light.
# Monochromatic light of wavelength of l nm is incident on aa surface of refractive index mu. What is the wavelength, speed and frequenct of refracted light.

no_of_samples = 30

samples = []

c = 3 * (10**8)

for i in range(no_of_samples):
    sample = {}
    l = random.randint(1,10000)
    mu = random.randint(101,200)
    mu = round(mu/100,2)
    mu = round(l/10,1)
    t = random.randint(1,2)
    if t == 1 :
        ques = "Monochromatic light of wavelength of " + str(l) + " nm is incident on aa surface of refractive index " + str(mu) + ". What is the wavelength, speed and frequenct of reflected light.\n"
        l = l * (10**-9)
        input_formula = "frequency = c/wavelength"
        answ1 = str(l/(10**-9)) + " nm "
        answ3 = "{:.2e}".format((c/l)) + " hz "
        answ2 = "{:.2e}".format(c) + " m/s " 
        answer = answ1 + ", " + answ2 + "and " + answ3 + "\n"
        answer += "The ray will reflect back in the same medium as that of incident ray. Hence, the wavelength, speed, and frequency of the reflected ray will be the same as that of the incident ray."
    else :
        ques = "Monochromatic light of wavelength of " + str(l) + " nm is incident on aa surface of refractive index " + str(mu) + ". What is the wavelength, speed and frequenct of refracted light.\n"
        v = c/mu
        l = l * (10**-9)
        input_formula = "speed of light in water = c/refractive index, wavelength = speed of light in water/frequency"
        answ3 = "{:.2e}".format((c/l)) + " hz "
        answ2 = "{:.2e}".format(v) + " m/s " 
        answ1 = "{:.2e}".format(((v*l)/(c*(10**-9)))) + " nm "
        answer = answ1 + ", " + answ2 + "and " + answ3 + "\n"
        answer += "Frequency of light does not depend on the property of the medium in which it is travelling. Hence, the frequency of the refracted ray in water will be equal to the frequency of the incident or reflected light in air."
    
    sample["instruction"] = ques
    sample["input"] = input_formula
    sample["output"] = answer

    samples.append(sample)

# Load existing JSON file
with open("science/WaveOptics/wo.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/WaveOptics/wo.json", "w") as file:
    json.dump(existing_data, file, indent=4) 
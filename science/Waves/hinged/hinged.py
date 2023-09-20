import random
import json

# A steel rod 100 cm long is clamped at its middle. The fundamental frequency of longitudinal vibrations of the rod is given to be 2.53 k Hz. What is the speed of sound in steel?
# A pipe 20 cm long is closed at one end. Which harmonic mode of the pipe is resonantly excited by a 430 Hz source? Will the same source be in resonance with the pipe if both ends are open? (speed of sound in air is 340 ms-1).

no_of_samples = 30
# no_of_samples = 10

samples = []

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1,3)
    if types == 1:
        l = random.randint(10,2000)
        freq = random.randint(1000,3000)
        an = (2*l*freq)/100
        q = "A steel rod "+str(l)+" cm long is hinged at its middle. The fundamental frequency of longitudinal vibrations of the rod is given to be "+str(freq)+" Hz. What is the speed of sound in steel?\n"
        input_formula = "speed of sound in steel = frequency*wavelength"
        a = "{:.1e}".format(an) + " ms-1\n"
        a += "The distance between two successive nodes is wavelength/2."
    else:
        l = random.randint(10,200)
        f = random.randint(100,600)
        speed = random.randint(320,360)
        q = "A pipe "+str(l)+" cm long is closed at one end. Which harmonic mode of the pipe is resonantly excited by a "+str(f)+" Hz source? Will the same source be in resonance with the pipe if both ends are open? (speed of sound in air is "+str(speed)+" ms-1).\n"
        temp = (4*f*(l/100))/speed
        temp = (temp+1)/2
        input_formula = "fundamental frequency = speed of sound in air/4*length of pipe"
        if abs(temp-round(temp))<0.01:
            a = "resonance in first case with "+str(round(temp))+", "
        else:
            a = "no resonance in first case, "
        temp = (2*f*(l/100))/speed
        if abs(temp-round(temp))<0.01:
            a = a +"resonance in second case with "+str(round(temp))+"\n"
        else:
            a = a +"no resonance in second case\n"
        a += "Resonance condition occurs when the frequency of external sources matches the natural frequency of the system."
    
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
    
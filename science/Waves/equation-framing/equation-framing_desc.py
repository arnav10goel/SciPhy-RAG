import random
import math
import json

# A end of string of mu = 8.0 x 10-3 kgm-1 is connected to tuning fork of nu = 256 Hz. The other end passes over a pulley and is tied to a mass of 90 kg. The pulley end is such that reflected waves at this end have negligible amplitude. At t = 0, the fork end of the string x = 0 has y = 0 and is moving along +ve y axis. The amplitude of the wave is 5.0 cm. Write down y as function of x and t that describes the wave on the string.

no_of_samples = 30
# no_of_samples = 10

samples = []

for i in range(no_of_samples):
    sample = {}
    freq = random.randint(100,500)
    mu = round(random.randint(1,30)/1000,3)
    amp = random.randint(1,40)
    m = random.randint(10,20)*5
    q = "A end of string of mu = "+str(mu)+" kgm-1 is connected to tuning fork of nu = "+str(freq)+" Hz. The other end passes over a pulley and is tied to a mass of "+str(m)+" kg. The pulley end is such that reflected waves at this end have negligible amplitude. At t = 0, the fork end of the string x = 0 has y = 0 and is moving along +ve y axis. The amplitude of the wave is "+str(amp)+" cm. Write down y as function of x,t that describes the wave on the string.\n"
    v = math.sqrt((m*9.8)/mu)
    w = 2*math.pi*v
    lamda = v/freq
    k = (2*math.pi)/lamda
    des = "to form wave equation, we have to find amplitude, frequency, velocity of wave. "
    des += ("given, amplitude = "+str(amp)+" cm = "+str(round(amp/100,2))+" m ")
    des += (",frequency = " +str(freq)+" hz ")
    des += (",v = sqrt(t/mu) = sqrt(" + str(round(m*9.8,1))+"/"+str(mu)+") = "+str(round(v,1))+" ")
    des += (",w = 2*pi*v = 2*3.14*"+str(round(v,1))+" = "+str(round(w,1))+" ")
    des += (",wavelength = v/freq = "+str(round(v,1))+"/"+str(freq)+" ")
    des += (",k = 2*pi/wavelength = " + " 2*pi*"+str(freq)+"/"+str(round(v,1))+" = "+str(round(k,1))+" ")
    des += (",the equation of the wave is, v(x,t) = a sin(wt-kx)"+", ")
    input_formula = "wavelength = speed/frequency"
    a = str(round(amp/100,2))+" sin("+"{:.1e}".format(w)+"t - "+"{:.1e}".format(k)+"x)"+"\n"
    a += des
    
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
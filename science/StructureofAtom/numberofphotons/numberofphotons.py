import random
import json

# What is the number of photons of light with wavelength w pm which provide e Joule of energy ?

no_of_samples = 20

samples = []

h = 6.6 * (10**-34)
c = 3 * (10**8)

def cal1(e,w) :
   return e*w*(10**-12)/(h*c)

def type1() :
    w = random.randint(100,1000000)
    e = random.randint(1,100)
    q = "What is the number of photons of light with wavelength " + str(w) + " pm which provide " + str(e) + " Joule of energy ? \n"
    input_formula = "Number of photons = Energy*wavelength/h*c"
    n = "{:.2e}".format(cal1(e,w)) + "\n"
    n += "To find the number of photons of light with a given wavelength and energy, we can use the equation: Number of photons = Energy / Energy of each photon"
    n += "To calculate the energy of each photon, we can use the formula: Energy of each photon = h * c / λ, where h is the Planck constant (approximately 6.626 x 10^-34 J·s), c is the speed of light (approximately 3 x 10^8 m/s), and λ is the wavelength of light in meters."
    return q,input_formula,n

def type2() :
    w = random.randint(100,1000000)
    e = random.randint(1,100)
    q = "What is the number of photons of light with wavelength " + str(w) + " pm which provide " + str(e) + " Joule of energy ? (h = 6.6 * 10^-34 Js, c = 3 * 10^8 m/s)\n"
    input_formula = "Number of photons = Energy*wavelength/6.6*10^-34 * 3*10^8"
    n = "{:.2e}".format(cal1(e,w)) + "\n"
    n += "To find the number of photons of light with a given wavelength and energy, we can use the equation: Number of photons = Energy / Energy of each photon"
    n += "To calculate the energy of each photon, we can use the formula: Energy of each photon = h * c / λ, where h is the Planck constant (approximately 6.626 x 10^-34 J·s), c is the speed of light (approximately 3 x 10^8 m/s), and λ is the wavelength of light in meters."
    return q,input_formula,n

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1,2)
    if types == 1 :
        ques,input_formula,answer = type1()
    elif types == 2 :
        ques,input_formula,answer = type2()
    
    sample["instruction"] = ques
    sample["input"] = input_formula
    sample["output"] = answer

    samples.append(sample)

# Load existing JSON file
with open("science/StructureofAtom/soa.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/StructureofAtom/soa.json", "w") as file:
    json.dump(existing_data, file, indent=4) 


import random
import json

# The mass of a particle is m × 10-31 kg. If its velocity is v m/s, calculate its wavelength.
# A particle has a velocity of v m/s and wavelength w A. Find its mass.
# The mass of a particle is 9.1 × 10-31 kg. If its wavelength is w A, calculate its velocity.

no_of_samples = 50
h = 6.6 * (10**-34)

samples = []

def cal1(m, v) :
   return round(h/m*v,2)

def cal2(v, w) :
    return round(h/v*w,2)

def cal3(m, w) :
    return round(h/m*w,2)

def type1() :
    v = random.randint(1,10000)
    m = random.randint(1,1000)
    m = m * 10**-31
    q = "The mass of a particle is " + str(m) + " kg. If its velocity is " + str(v) + " m/s, calculate its wavelength.\n"
    input_formula = "Wavelength = h/mass*velocity"
    w = str(cal1(m, v)) + "m\n"
    w += "The momentum (p) of a particle is given by the product of its mass (m) and velocity (v), according to the formula P=M*V"
    w += "The wavelength (λ) of a particle can be calculated using the de Broglie wavelength equation, which relates the wavelength of a particle to its momentum."
    return q,input_formula,w

def type2() :
    w = random.randint(1,10000)
    v = random.randint(1,10000)
    w = w * 10**-10
    q = "A particle has a velocity of " + str(v) + " m/s and wavelength " + str(w) + " A. Find its mass.\n"
    input_formula = "Mass = h/wavelength*velocity"
    m = str(cal2(v, w)) + "kg\n"
    m += "To find the mass of the particle, we can use the de Broglie wavelength equation: λ = h / (m * v) where λ is the wavelength, h is the Planck constant (approximately 6.626 x 10^-34 J·s), m is the mass of the particle, and v is its velocity."
    return q,input_formula,m

def type3() :
    w = random.randint(1,10000)
    m = random.randint(1,1000)
    m = m * 10**-31
    w = w * 10**-10
    q = "The mass of a particle is " + str(m) + " kg. If its wavelength is " + str(w) + " A, calculate its velocity.\n"
    input_formula = "Velocity = h/wavelength*mass"
    v = str(cal3(m, w)) + "m/s\n"
    v += "To find the velocity of the particle, we can use the de Broglie wavelength equation: λ = h / (m * v) where λ is the wavelength, h is the Planck constant (approximately 6.626 x 10^-34 J·s), m is the mass of the particle, and v is its velocity."
    return q,input_formula,v

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1,3)
    if types == 1 :
        ques,input_formula,answer = type1()
    elif types == 2 :
        ques,input_formula,answer = type2()
    elif types == 3 :
        ques,input_formula,answer = type3()
    
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

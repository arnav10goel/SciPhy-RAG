import random
import json

# Calculate the energy of each of the photons which correspond to light of frequency v Hz.
# Calculate the energy of each of the photons which correspond to light of frequency v Hz. (h = 6.6 * 10^-34 Js)
# Calculate the energy of each of the photons which have wavelength of w nm.
# Calculate the energy of each of the photons which have wavelength of w nm. (h = 6.6 * 10^-34 Js, c = 3 * 10^8 m/s)

no_of_samples = 50

samples = []

h = 6.6 * (10**-34)
c = 3 * (10**8)

def cal1(w) :
   return h*w

def cal2(w) :
    return (h*c)*(10**9)/w

def type1() :
    v = random.randint(1,1000000)
    q = "Calculate the energy of each of the photons which correspond to light of frequency " + str(v) + " Hz.\n"
    input_formula = "Energy = h*frequency"
    e = "{:.2e}".format(cal1(v)) + "joules\n"
    e += "To calculate the energy of a photon, you can use the formula: E = h * f, where E is the energy of the photon, h is the Planck constant (approximately 6.626 x 10^-34 J·s), and f is the frequency of the light."
    return q,input_formula,e

def type2() :
    w = random.randint(1,1000000)
    q = "Calculate the energy of each of the photons which have wavelength of " + str(w) + " nm.\n"
    input_formula = "Energy = h*c/wavelength"
    e = "{:.2e}".format(cal2(w)) + "joules\n"
    e += "To calculate the energy of a photon, you can use the formula: E = h * c/lambda, where E is the energy of the photon, h is the Planck constant (approximately 6.626 x 10^-34 J·s), c is the speed of light and lambda is the wavelength of the light."
    return q,input_formula,e

def type3() :
    v = random.randint(1,1000000)
    q = "Calculate the energy of each of the photons which correspond to light of frequency " + str(v) + " Hz. (h = 6.6 * 10^-34 Js)\n"
    input_formula = "E = 6.6*10^-34 * frequency"
    e = "{:.2e}".format(cal1(v)) + "joules\n"
    e += "To calculate the energy of a photon, you can use the formula: E = h * f, where E is the energy of the photon, h is the Planck constant (approximately 6.626 x 10^-34 J·s), and f is the frequency of the light."
    return q,input_formula,e

def type4() :
    w = random.randint(1,1000000)
    q = "Calculate the energy of each of the photons which have wavelength of " + str(w) + " nm. (h = 6.6 * 10^-34 Js, c = 3 * 10^8 m/s)\n"
    input_formula = "E = 6.6*10^-34 * c/wavelength"
    e = "{:.2e}".format(cal2(w)) + "joules\n"
    e += "To calculate the energy of a photon, you can use the formula: E = h * c/lambda, where E is the energy of the photon, h is the Planck constant (approximately 6.626 x 10^-34 J·s), c is the speed of light and lambda is the wavelength of the light."
    return q,input_formula,e

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1,4)
    if types == 1 :
        ques,input_formula,answer = type1()
    elif types == 2 :
        ques,input_formula,answer = type2()
    elif types == 3 :
        ques,input_formula,answer = type3()
    elif types == 4 :
        ques,input_formula,answer = type4()
    
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

import random
import math
import json

# A photon of energy e1 eV strikes on metal surface ; the work function of the metal being e2 eV. Calculate the kinetic energy of the emission and the velocity of the photoelectron. (Given 1 eV = 1.6020 × 10-19 J).

no_of_samples = 20

samples = []

m = 9.1 * 10**-31
k = 1.6 * 10**-19

def cal1(e1,e2) :
   return e1 - e2

def cal2(ke) :
    return math.sqrt((2 * ke * k)/m)

for i in range(no_of_samples):
    sample = {}
    e2 = random.randint(1,1200)
    e1 = random.randint(e2+1,e2+1200)
    ques = "A photon of energy " + str(e1) + " eV strikes on metal surface ; the work function of the metal being " + str(e2) + " eV. Calculate the kinetic energy of the emission and the velocity of the photoelectron. (Given 1 eV = 1.6020 × 10-19 J).\n"
    ke = cal1(e1,e2)
    input_formula = "Kinetic Energy = Energy of Photon - Work Function of Metal"
    a = "kinetic energy of ejected photoelectron = energy of photon - workfunction = " + str(e1) + " - " + str(e2) + " = " + str(ke) 
    answer = a + " joules and if m is mass of ejected electron then velocity of ejected photo electron = sq.root((ke x 2)/m) = sq.root((" + str(ke) + " x 2)/" + str(m) + ") = " + "{:.2e}".format(cal2(ke)) + " m/s\n"
    answer += "To calculate the kinetic energy of the emitted photoelectron and its velocity, we need to apply the principle of conservation of energy. The energy of the incident photon is used to overcome the work function of the metal and provide kinetic energy to the emitted electron."
    answer += "v = sqrt((2 * Kinetic energy) / m), Substituting the calculated kinetic energy and the electron mass into the equation will give us the velocity of the photoelectron."

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
import random
import json

# What is the energy associated with a mass of m g ?

c = 3 * (10**8)

no_of_samples = 10

samples = []

for i in range(no_of_samples):
    sample = {}
    m = random.randint(1,10000)
    m = round(m/10,1)
    t = random.randint(1,2)
    if t == 1 :
        ques = "What is the energy associated with a mass of " + str(m) + " g ?\n"
        input_formula = "Energy = Mass*c^2"
    else :
        ques = "What is the energy associated with a mass of " + str(m) + " g ? (c = 3 x 10^8 m/s)\n"
        input_formula = "Energy = Mass*(3*10^8)^2"
    m = m * (10**-3)
    answ = "{:.2e}".format(m*c*c)
    answer = answ + "joule\n"
    answer += "To calculate the energy associated with a mass, we need to specify the type of energy we are referring to. There are various forms of energy, such as kinetic energy, potential energy, thermal energy, etc. If we assume you are referring to the energy associated with the mass in terms of its rest energy, we can use Einstein's mass-energy equivalence principle, given by the equation: E = m * c^2"
    
    sample["instruction"] = ques
    sample["input"] = input_formula
    sample["output"] = answer

    samples.append(sample)

# Load existing JSON file
with open("science/AtomsAndNuclei/aan.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/AtomsAndNuclei/aan.json", "w") as file:
    json.dump(existing_data, file, indent=4) 

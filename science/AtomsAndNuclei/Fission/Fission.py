import random
import json

# The average energy released per fission for 239Pu94 is 180 MeV. How much energy per fission is released if all the atoms in m g of pure 239Pu94 undergo fission.

no_of_samples = 10

samples = []

N = 6.023 * (10**23)

for i in range(no_of_samples):
    sample = {}
    m = random.randint(1,20000)
    m = round(m/10,1)
    ques = "The average energy released per fission for 239Pu94 is 180 MeV. How much energy per fission is released if all the atoms in " + str(m) + " g of pure 239Pu94 undergo fission.\n"
    input_formula = "Energy per fission = Average energy * 6.023*10^23*1000/239"
    answ = (N*m*180*1.6*(10**-13))/239
    answer = "{:.2e}".format(answ) + "joule\n"
    answer += "To calculate the total energy released when all the atoms in " + str(m) + " g of pure 239Pu94 undergo fission, we need to consider the number of atoms present and the average energy released per fission. First, we need to convert the mass from grams to kilograms: m = m / 1000 kg. Next, we need to calculate the number of atoms using Avogadro's number (6.022 x 10^23 atoms/mol) and the molar mass of 239Pu94 (239 g/mol): Number of atoms = (m / 239 g/mol) * (6.022 x 10^23 atoms/mol)"
    answer += "Finally, we can calculate the total energy released by multiplying the number of atoms by the average energy released per fission: Total energy released = Number of atoms * Average energy released per fission. However, the average energy released per fission is given in mega-electron volts (MeV), so we need to convert it to joules (J): 1 MeV = 1.602 x 10^-13 J. Substituting the values and converting the units, we can calculate the total energy released: Total energy released = (m / 239 g/mol) * (6.022 x 10^23 atoms/mol) * (180 MeV) * (1.602 x 10^-13 J/MeV)"
    
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
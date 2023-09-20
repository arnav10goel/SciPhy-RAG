import random
import json

samples = []

no_of_samples = 20

for i in range(no_of_samples):
    sample = {}
    types = random.randint(0,1)
    if types:
        V = round(random.randint(100,40000)/100,2)
        percent = random.randint(1,100)
        q = "A carrier wave of peak voltage "+str(V)+" V is used to transmit a message signal. What should be the peak voltage of the modulating signal in order to have a modulation index of "+str(percent)+" percent?\n"
        a = "To calculate the peak voltage of the modulating signal, we use the formula V_sig = mod-index * V_car, where the modulation index is given as a percentage. Therefore, V_sig = "+str(round(percent/100,2))+" * "+str(V)+" = "
        a += "{:.2e} V\n".format((percent/100)*V)
        input_formula = "V_sig = mod-index * V_car"
    else:
        A_min = round(random.randint(0,2000)/100,2)
        A_max = round(A_min + random.randint(1,2000)/100,2)
        q = "For an amplitude modulated wave, the maximum amplitude is found to be "+str(A_max)+" V while the minimum amplitude is found to be "+str(A_min)+" V. Determine the modulation index.\n"
        a = "To determine the modulation index of an amplitude modulated wave, we use the formula modulation index = (a_max - a_min) / (a_max + a_min). Given the maximum amplitude (a_max) = "+str(A_max)+" V and the minimum amplitude (a_min) = "+str(A_min)+" V, the modulation index is equal to "+str(round((A_max-A_min)/(A_max+A_min),2)) + "\n"
        input_formula = "Modulation index = (a_max - a_min) / (a_max + a_min)"
    sample["instruction"] = q
    sample["input"] = input_formula
    sample["output"] = a

    samples.append(sample)

# Load existing JSON file
with open("science/CommunicationSystems/comm.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/CommunicationSystems/comm.json", "w") as file:
    json.dump(existing_data, file, indent=4)

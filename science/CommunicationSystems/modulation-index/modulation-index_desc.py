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
        a = "We know that the modulation index is the ratio of the voltage of the modulating signal to the voltage of the carrier. Therefore, the modulation index (in decimal) = V_sig / V_car, and V_sig = mod-index * V_car = "+str(round(percent/100,2))+" * "+str(V)+" = "
        a += "{:.2e} V\n".format((percent/100)*V)
        input_formula = "V_sig = mod-index * V_car"
    else:
        A_min = round(random.randint(0,2000)/100,2)
        A_max = round(A_min + random.randint(1,2000)/100,2)
        q = "For an amplitude modulated wave, the maximum amplitude is found to be "+str(A_max)+" V while the minimum amplitude is found to be "+str(A_min)+" V. Determine the modulation index.\n"
        a = "We know that the modulation index of an amplitude modulated wave is the ratio of the difference between a_max and a_min to the sum of a_max and a_min. The difference of a_max, a_min is equal to "+str(A_max)+" - "+str(A_min)+" = "+str(round(A_max-A_min,2))+", and the sum of a_max, a_min is equal to "+str(A_max)+" + "+str(A_min)+" = "+str(round(A_max+A_min,2))+". Hence, the modulation index is equal to "+str(round(A_max-A_min,2))+" / "+str(round(A_max+A_min,2))+" = " 
        a += str(round((A_max-A_min)/(A_max+A_min),2)) + "\n"
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

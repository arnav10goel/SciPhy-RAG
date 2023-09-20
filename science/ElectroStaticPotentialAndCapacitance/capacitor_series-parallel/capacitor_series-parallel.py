import random
import json

samples = []

no_of_samples = 40

for i in range(no_of_samples):
    sample = {}
    n = random.randint(1,20)
    c = random.randint(1,500)
    v = random.randint(1,500)
    if random.randint(0,1):
        if random.randint(0,1):
            q = str(n)+" capacitors each of capacitance "+str(c)+ "pF are connected in series. What is the total capacitance of the combination when the system is connected to a "+str(v) +" V supply?\n"
            i_f = "1 / C_total = 1 / C1 + 1 / C2 + 1 / C3 + ... + 1 / Cn\n"
            a = "{:.2e}".format(c/n) + " pico-farad\n"
            a += "\nExplanation: 1 / C_total = 1 / " + str(c) + " + 1 / " + str(c) + " + 1 / " + str(c) + " + ... + 1 / " + str(c) + "\n"
        else:
            q = str(n)+" capacitors each of capacitance "+str(c)+ "pF are connected in series. What is the potential difference across each capacitor if the combination is connected to a "+str(v) +" V supply?\n"
            i_f = "V_total = V1 + V2 + V3 + ... + Vn\n"
            a = "{:.2e}".format(v/n) + " volt\n"
            a += "\nExplanation: V_total = " + str(v) + " / " + str(n) + " = " + "{:.2e}".format(v/n) + " volt\n"
    else:
        if random.randint(0,1):
            q = str(n)+" capacitors each of capacitance "+str(c)+ "pF are connected in parallel. What is the total capacitance of the combination when the system is connected to a "+str(v) +" V supply?\n"
            i_f = "C_total = C1 + C2 + C3 + ... + Cn\n"
            a = "{:.2e}".format(c*n) + " pico-farad\n"
            a += "\nExplanation: C_total = " + str(c) + " + " + str(c) + " + " + str(c) + " + ... + " + str(c) + " = " + "{:.2e}".format(c*n) + " pico-farad\n"
        else:
            q = str(n)+" capacitors each of capacitance "+str(c)+ "pF are connected in parallel. What is the charge on each capacitor if the combination is connected to a "+str(v) +" V supply?\n"
            i_f = "Q_capacitor = C_total * v\n"
            a = "{:.2e}".format(c*v) + " pico-coulomb\n"
            a += "\nExplanation: Q_capacitor = " + str(c) + " * " + str(v) + " = " + "{:.2e}".format(c*v) + " pico-coulomb\n"
    sample['instruction'] = q
    sample['input'] = i_f
    sample['output'] = a
    samples.append(sample)

# Load existing JSON file
with open("science/ElectroStaticPotentialAndCapacitance/esp.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save the updated JSON data
with open("science/ElectroStaticPotentialAndCapacitance/esp.json", "w") as file:
    json.dump(existing_data, file, indent=4)
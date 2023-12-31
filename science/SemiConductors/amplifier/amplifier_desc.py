import random
import json

# For a CE-transistor amplifier, the audio signal voltage across the collected resistance of 2 ohm is 2 V. Suppose the current amplification factor of the transistor is 100, find the input signal voltage and base current, if the base resistance is 1 ohm.
# Two amplifiers are connected one after the other in series(cascaded). The first amplifier has a voltage gain of 10 and the second has the voltage gain of 20. If the input signal is 0.01 volt, calculate the output ac signal.

samples = []
no_of_samples = 20
# no_of_samples = 15

def type1():
    R1 = random.randint(200,400)*10
    V1 = random.randint(1,40)
    amp = random.randint(1,20)*10
    R2 = random.randint(100,200)*10
    Vi = (V1*R2)/(amp*R1)
    if types == 0:
        q = "For a CE-transistor amplifier, the audio signal voltage across the collected resistance of "+str(R1)+" ohm is "+str(V1)+" V. Suppose the current amplification factor of the transistor is "+str(amp)+", find the input signal voltage if the base resistance is "+str(R2)+" ohm?\n"
        input_formula = "output voltage/input voltage = current amplification factor*output resistance/input resistance"
        a = "voltage without amplification is "+str(V1)+"/"+str(amp)+" = "+str(round(V1/amp,2))+", to get voltage per unit resistance, we need to divide it by "+str(R1)+", to get to original voltage, we need to multiply per unit resistance voltage with base resistance "+str(R2)+" doing all that we get, "+"{:.2e} volt\n".format(Vi)
    else:
        q = "For a transistor as a switch in saturation state, the audio signal voltage across the collected resistance of "+str(R1)+" ohm is "+str(V1)+" V. Suppose the current amplification factor of the transistor is "+str(amp)+", find the base current if the base resistance is "+str(R2)+" ohm?\n"
        input_formula = "output voltage/input voltage = current amplification factor*output resistance/input resistance"
        a = "voltage without amplification is "+str(V1)+"/"+str(amp)+" = "+str(round(V1/amp,2))+", to get voltage per unit resistance, we need to divide it by "+str(R1)+", the resultant voltage per unit resistance is current and it's value is "+"{:.2e} ampere\n".format(Vi/R2)
    return q,input_formula, a

def type2():
    amp1 = random.randint(2,200)
    amp2 = random.randint(2,200)
    V = round(random.randint(2,200)/1000,3)
    q = "Two amplifiers are connected one after the other in series(cascaded). The first amplifier has a voltage gain of "+str(amp1)+" and the second has the voltage gain of "+str(amp2)+". If the input signal is "+str(V)+" volt, calculate the output ac signal.\n"
    input_formula = "V2 = V1*amp1*amp2"
    a = "If the amplifiers are connected in series, the resultant amplification would be product of amplification factors of each of the amplifer, hence resultant output signal is "+str(amp1)+"*"+str(amp2)+"*"+str(V)+" = {:.2e} volt\n".format(amp1*amp2*V)
    return q, input_formula, a

for i in range(no_of_samples):
    sample = {}
    types = random.randint(0,2)
    if types!=2:
        q,input_formula, a = type1()
    else:
        q, input_formula, a = type2()
    sample["instruction"] = q
    sample["input"] = input_formula
    sample["output"] = a

    samples.append(sample)

# Load existing JSON file
with open("SemiConductors\semi.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("SemiConductors\semi.json", "w") as file:
    json.dump(existing_data, file, indent=4)   



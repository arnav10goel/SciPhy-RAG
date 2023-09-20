import random
import math
import json

# In a p-n junction diode, the current I can be expressed as I = I0*exp((e*V/2*k_b*T)-1), k_b = 8.6 * 10^(-5) eV/K. If for given diode I0 = 5 x 10^(-12) A and T = 300

no_of_samples = 30
e = 1.6 * (10**(-19))
k_b2 = 1.376 * (10**(-23))

samples = []

for i in range(no_of_samples):
    sample = {}
    I0 = random.randint(1000,3000)
    T = random.randint(280,300)
    types = random.randint(1,3)
    q = "In a p-n junction diode, the current I can be expressed as I = I0*exp((e*V/2*k_b*T)-1), k_b = 8.6 * 10^(-5) eV/K. If for given diode I0 = "+str(I0)+" x 10^(-15) A and T = "+str(T)+" K, "
    if types == 1:
        V = round(random.randint(100,300)/1000,3)
        q = q + "what will be the forward current at a forward voltage of "+str(V)+" V?\n"
        input_formula = "I=Io*exp((e*V/2*Kb*T)-1)"
        a = (I0*(10**(-15)))*math.exp((e*V)/(k_b2*T)-1)
        a = "{:.2e} ampere\n".format(a)
        a += "We use the value of V given to us with the values of Kb and T to find forward current."
    elif types == 2:
        V1 = round(random.randint(1,20)/10,1)
        V2 = round(random.randint(1,20)/10,1)
        q = q + "what will be the increase in the current if the voltage across the diode is increased from "+str(V1)+" V to "+str(round(V1+V2,1))+" V?\n"
        input_formula = "I=Io*exp((e*V/2*Kb*T)-1)"
        I1 = (I0*(10**(-15)))*math.exp((e*V1)/(k_b2*T)-1)
        I2 = (I0*(10**(-15)))*math.exp((e*(V1+V2))/(k_b2*T)-1)
        a = "{:.2e} ampere\n".format(I2-I1)
        a += "The resultant forward voltage is V1+V2, input the value while caluclating I2 and use I2-I1 to calculate increase in the current."
    elif types == 3:
        V1 = round(random.randint(1,20)/10,1)
        V2 = round(random.randint(1,20)/10,1)
        q = q + "what will be dynamic resistance if the voltage across the diode is increased from "+str(V1)+" V to "+str(round(V1+V2,1))+" V?\n"
        input_formula = "I=Io*exp((e*V/2*Kb*T)-1), R = V2/I2-I1"
        I1 = (I0*(10**(-15)))*math.exp((e*V1)/(k_b2*T)-1)
        I2 = (I0*(10**(-15)))*math.exp((e*(V1+V2))/(k_b2*T)-1)
        a = "{:.2e} ohm\n".format((V2)/(I2-I1))
        a += "Calculate the resistance by dividing the increased voltage and the increase in current"        
 
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

import random
import math
import json

# A refrigerator is to maintain eatables kept inside at t1 degree C, if room temperature is t2 degree C. Calculate the coefficient of performance.

no_of_samples = 30

samples = []

r = 8.31

def cal1(t1,t2) :
    t1 = t1 + 273
    t2 = t2 + 273   
    return round(t1/(t2-t1),1) 

def cal2(t1,t2) :  
    return round(t1/(t2-t1),1) 

def type1() :
    t = random.randint(1,2)
    if t == 1 :
        t2 = -200
        t1 = random.randint(-100,20)
        while(t2 <= t1) :
            t2 = random.randint(10,100)
        q = "A refrigerator is to maintain eatables kept inside at " + str(t1) + " degree C, if room temperature is " + str(t2) + " degree C. Calculate the coefficient of performance.\n"
        input_formula = "Coefficient of performance = T2/T1-T2"
        a = str(cal1(t1,t2)) + "\n"
        a += "This formula is only applicable if the refrigerator is based on the Carnot Cycle."
    else :
        t2 = -200
        t1 = random.randint(-172,293)
        while(t2 <= t1) :
            t2 = random.randint(283,373)
        q = "A refrigerator is to maintain eatables kept inside at " + str(t1) + " K, if room temperature is " + str(t2) + " K. Calculate the coefficient of performance.\n"
        input_formula = "Coefficient of performance = T2/T1-T2"
        a = str(cal2(t1,t2)) + "\n"
        a += "This formula is only applicable if the refrigerator is based on the Carnot Cycle."
    return q,input_formula,a

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1,1)
    if types == 1 :
        ques,input_formula,answer = type1()
   
    sample["instruction"] = ques
    sample["input"] = input_formula
    sample["output"] = answer

    samples.append(sample)

# Load existing JSON file
with open("science/Thermodynamics/thermo.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/Thermodynamics/thermo.json", "w") as file:
    json.dump(existing_data, file, indent=4) 
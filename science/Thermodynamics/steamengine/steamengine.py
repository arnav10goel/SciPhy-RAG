import random
import json

# A steam engine delivers w J of work per minute and services h J of heat per minute from its boiler. What is the efficiency of the engine? 
# A steam engine delivers w J of work per minute and services h J of heat per minute from its boiler. How much heat is wasted per minute?

no_of_samples = 30

samples = []

r = 8.31

def cal1(w,h) :
    return round((w*100)/h,1) 

def cal2(w,h) : 
    return h-w

def type1() :
    w = random.randint(1,1000)
    h = random.randint(w+1,w+1000)
    q = "A steam engine delivers " + str(w) + " J of work per minute and services " + str(h) + " J of heat per minute from its boiler. What is the efficiency of the engine?\n"
    input_formula = "Efficiency = Work per minute/Heat per minute from its boiler"
    a = str(cal1(w,h)) + "\n"
    a += "The efficiency of an engine can be calculated using the formula: Efficiency = (Work output / Heat input) * 100"
    return q,input_formula,a

def type2() :
    w = random.randint(1,1000)
    h = random.randint(w+1,w+1000)
    q = "A steam engine delivers " + str(w) + " J of work per minute and services " + str(h) + " J of heat per minute from its boiler. How much heat is wasted per minute?\n"
    input_formula = "Efficiency = Work per minute/Heat per minute from its boiler, Heat Wasted = Heat per minute - (Efficiency/100)*Heat per minute"
    a = str(cal2(w,h)) + " joules\n"
    a += "The efficiency of an engine can be calculated using the formula: Efficiency = (Work output / Heat input) * 100"
    return q,input_formula,a

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1,2)
    if types == 1 :
        ques,input_formula,answer = type1()
    else :
        ques,input_formula,answer = type2()
    
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

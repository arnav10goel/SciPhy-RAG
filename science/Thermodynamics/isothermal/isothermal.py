import random
import json

# If a monoatomic gas of n moles at p1 atm and volume v1 lit is isothermally changed to volume v2 lit, then what will be the pressure.
# If a diatomic gas of n moles at p1 atm and volume v1 lit is isothermally changed to volume v2 lit, then what will be the pressure.
# If a monoatomic gas of n moles at p1 atm and volume v1 lit is isothermally changed to pressure p1 atm, then what will be its volume.
# If a diatomic gas of n moles at p1 atm and volume v1 lit is isothermally changed to pressure p1 atm, then what will be its volume.

no_of_samples = 50

samples = []

r = 8.31

def cal1(g,v1,v2,p1) :
    return round((p1*(v1**g))/(v2**g),1)

def cal2(g,p1,p2,v1) : 
    return round(((p1*(v1**g))/p2)**(1/g),1) 

def type1() :
    n = random.randint(1,10)
    p1 = random.randint(10,200)
    v1 = random.randint(10,200)
    v2 = random.randint(10,200)
    q = "If a monoatomic gas of " + str(n) + " moles at " + str(p1) + " atm and volume " + str(v1) + " lit is isothermally changed to volume " + str(v2) + " lit, then what will be the pressure.\n"
    input_formula = "P1*V1 = P2*V2"
    a = str(cal1(1,v1,v2,p1)) + "atm\n"
    a += "To determine the final pressure of a monoatomic gas after an isothermal expansion, we can use Boyle's Law, which states that for an ideal gas at constant temperature: P1 * V1 = P2 * V2, where P1 and V1 are the initial pressure and volume, and P2 and V2 are the final pressure and volume."
    return q,input_formula,a

def type2() :
    n = random.randint(1,10)
    p1 = random.randint(10,200)
    v1 = random.randint(10,200)
    v2 = random.randint(10,200)
    q = "If a diatomic gas of " + str(n) + " moles at " + str(p1) + " atm and volume " + str(v1) + " lit is isothermally changed to volume " + str(v2) + " lit, then what will be the pressure.\n"
    input_formula = "P1*V1 = P2*V2"
    a = str(cal1(1,v1,v2,p1)) + "atm\n"
    a += "To determine the final pressure of a diatomic gas after an isothermal expansion, we can use Boyle's Law, which states that for an ideal gas at constant temperature: P1 * V1 = P2 * V2, where P1 and V1 are the initial pressure and volume, and P2 and V2 are the final pressure and volume."
    return q,input_formula,a

def type3() :
    n = random.randint(1,10)
    p1 = random.randint(10,200)
    v1 = random.randint(10,200)
    p2 = random.randint(10,200)
    q = "If a monoatomic gas of " + str(n) + " moles at " + str(p1) + " atm and volume " + str(v1) + " lit is isothermally changed to pressure " + str(p2) + " atm, then what will be its volume.\n"
    input_formula = "P1*V1 = P2*V2"
    a = str(cal2(1,p1,p2,v1)) + "lit\n"
    a += "To determine the final volume of a monoatomic gas after an isothermal expansion, we can use Boyle's Law, which states that for an ideal gas at constant temperature: P1 * V1 = P2 * V2, where P1 and V1 are the initial pressure and volume, and P2 and V2 are the final pressure and volume."
    return q,input_formula,a

def type4() :
    n = random.randint(1,10)
    p1 = random.randint(10,200)
    v1 = random.randint(10,200)
    p2 = random.randint(10,200)
    q = "If a diatomic gas of " + str(n) + " moles at " + str(p1) + " atm and volume " + str(v1) + " lit is isothermally changed to pressure " + str(p2) + " atm, then what will be its volume.\n"
    input_formula = "P1*V1 = P2*V2"
    a = str(cal2(1,p1,p2,v1)) + "lit\n"
    a += "To determine the final volume of a diatomic gas after an isothermal expansion, we can use Boyle's Law, which states that for an ideal gas at constant temperature: P1 * V1 = P2 * V2, where P1 and V1 are the initial pressure and volume, and P2 and V2 are the final pressure and volume."
    return q,input_formula,a

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1,4)
    if types == 1 :
        ques,input_formula,answer = type1()
    elif types == 2 :
        ques,input_formula,answer = type2()
    elif types == 3 :
        ques,input_formula,answer = type3()
    elif types == 4 :
        ques,input_formula,answer = type4()
    
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

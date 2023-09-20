import random
import json

# If a monoatomic gas of n moles at p1 atm and volume v1 lit is adiabatically changed to volume v2 lit, then what will be the pressure.
# If a diatomic gas of n moles at p1 atm and volume v1 lit is adiabatically changed to volume v2 lit, then what will be the pressure.
# If a monoatomic gas of n moles at p1 atm and volume v1 lit is adiabatically changed to pressure p1 atm, then what will be its volume.
# If a diatomic gas of n moles at p1 atm and volume v1 lit is adiabatically changed to pressure p1 atm, then what will be its volume.

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
    q = "If a monoatomic gas of " + str(n) + " moles at " + str(p1) + " atm and volume " + str(v1) + " lit is adiabatically changed to volume " + str(v2) + " lit, then what will be the pressure.\n"
    input_formula = "P1*(V1^1.66)=P2*(V2^1.66)"
    a = str(cal1(1.66,v1,v2,p1)) + "atm\n"
    a += "To calculate the final pressure of the monoatomic gas after an adiabatic expansion, we can use the adiabatic equation: P1 * V1^γ = P2 * V2^γ, where P1 and V1 are the initial pressure and volume, P2 and V2 are the final pressure and volume, and γ is the heat capacity ratio. The heat capacity ratio (γ) for a monoatomic gas is typically 5/3."
    return q,input_formula,a

def type2() :
    n = random.randint(1,10)
    p1 = random.randint(10,200)
    v1 = random.randint(10,200)
    v2 = random.randint(10,200)
    q = "If a diatomic gas of " + str(n) + " moles at " + str(p1) + " atm and volume " + str(v1) + " lit is adiabatically changed to volume " + str(v2) + " lit, then what will be the pressure.\n"
    input_formula = "P1*(V1^1.4)=P2*(V2^1.4)"
    a = str(cal1(1.4,v1,v2,p1)) + "atm\n"
    a += "To calculate the final pressure of the diatomic gas after an adiabatic expansion, we can use the adiabatic equation: P1 * V1^γ = P2 * V2^γ, where P1 and V1 are the initial pressure and volume, P2 and V2 are the final pressure and volume, and γ is the heat capacity ratio. The heat capacity ratio (γ) for a diatomic gas is typically 7/5."
    return q,input_formula,a

def type3() :
    n = random.randint(1,10)
    p1 = random.randint(10,200)
    v1 = random.randint(10,200)
    p2 = random.randint(10,200)
    q = "If a monoatomic gas of " + str(n) + " moles at " + str(p1) + " atm and volume " + str(v1) + " lit is adiabatically changed to pressure " + str(p2) + " atm, then what will be its volume.\n"
    input_formula = "P1*(V1^1.66)=P2*(V2^1.66)"
    a = str(cal2(1.66,p1,p2,v1)) + "lit\n"
    a += "To calculate the final pressure of the monoatomic gas after an adiabatic expansion, we can use the adiabatic equation: P1 * V1^γ = P2 * V2^γ, where P1 and V1 are the initial pressure and volume, P2 and V2 are the final pressure and volume, and γ is the heat capacity ratio. The heat capacity ratio (γ) for a monoatomic gas is typically 5/3."
    return q,input_formula,a

def type4() :
    n = random.randint(1,10)
    p1 = random.randint(10,200)
    v1 = random.randint(10,200)
    p2 = random.randint(10,200)
    q = "If a diatomic gas of " + str(n) + " moles at " + str(p1) + " atm and volume " + str(v1) + " lit is adiabatically changed to pressure " + str(p2) + " atm, then what will be its volume.\n"
    input_formula = "P1*(V1^1.4)=P2*(V2^1.4)"
    a = str(cal2(1.4,p1,p2,v1)) + "lit\n"
    a += "To calculate the final pressure of the diatomic gas after an adiabatic expansion, we can use the adiabatic equation: P1 * V1^γ = P2 * V2^γ, where P1 and V1 are the initial pressure and volume, P2 and V2 are the final pressure and volume, and γ is the heat capacity ratio. The heat capacity ratio (γ) for a diatomic gas is typically 7/5."
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

import random
import math
import json

# If a monoatomic gas of n moles at v1 m3 is isothermally changed to volume v2 m3 at t K, then what is the work done.
# If a monoatomic gas of n moles at p1 pas is isothermally changed to volume p2 pas at t K, then what is the work done.
# If a diatomic gas of n moles at v1 m3 is isothermally changed to volume v2 m3 at t K, then what is the work done.
# If a diatomic gas of n moles at p1 pas is isothermally changed to volume p2 pas at t K, then what is the work done.
# If a gas of n moles at v1 m3 is isothermally changed to volume v2 m3 at t K, then what is the work done.
# If a gas of n moles at p1 pas is isothermally changed to volume p2 pas at t K, then what is the work done.

no_of_samples = 70

samples = []

r = 8.31

def cal1(n, t, v1, v2) :
    return round(-1*n*r*t*math.log(v2/v1),1)

def cal2(n, t, p1, p2) : 
    return round(-1*n*r*t*math.log(p1/p2),1) 

def type1() :
    n = random.randint(1,10)
    v1 = random.randint(10,60)
    v2 = random.randint(10,60)
    t = random.randint(10,60)
    q = "If a monoatomic gas of " + str(n) + " moles at " + str(v1) + " m3 is isothermally changed to volume " + str(v2) + " m3 at " + str(t) + " K, then what is the work done.\n"
    input_formula = "Work Done = n*R*T*ln(V2/V1)"
    a = str(cal1(n,t,v1,v2)) + " joules\n"
    a += "To calculate the work done during an isothermal expansion of a monoatomic gas, we can use the following equation: Work done = n * R * T * ln(V2/V1), where n is the number of moles of the gas, R is the ideal gas constant (approximately 8.314 J/(mol·K)), T is the temperature in Kelvin, V1 is the initial volume, and V2 is the final volume."
    return q,input_formula,a

def type2() :
    n = random.randint(1,10)
    p1 = random.randint(10,60)
    p2 = random.randint(10,60)
    t = random.randint(10,60)
    q = "If a monoatomic gas of " + str(n) + " moles at " + str(p1) + " pas is isothermally changed to pressure " + str(p2) + " pas at " + str(t) + " K, then what is the work done.\n"
    input_formula = "Work Done = n*R*T*ln(P1/P2)"
    a = str(cal2(n,t,p1,p2)) + " joules\n"
    a += "To calculate the work done during an isothermal expansion of a monoatomic gas, we can use the following equation: Work done = n * R * T * ln(P1/P2), where n is the number of moles of the gas, R is the ideal gas constant (approximately 8.314 J/(mol·K)), T is the temperature in Kelvin, P1 is the initial pressure, and P2 is the final pressure."
    return q,input_formula,a

def type3() :
    n = random.randint(1,10)
    v1 = random.randint(10,60)
    v2 = random.randint(10,60)
    t = random.randint(10,60)
    q = "If a diatomic gas of " + str(n) + " moles at " + str(v1) + " m3 is isothermally changed to volume " + str(v2) + " m3 at " + str(t) + " K, then what is the work done.\n"
    input_formula = "Work Done = n*R*T*ln(V2/V1)"
    a = str(cal1(n,t,v1,v2)) + " joules\n"
    a += "To calculate the work done during an isothermal expansion of a diatomic gas, we can use the following equation: Work done = n * R * T * ln(V2/V1), where n is the number of moles of the gas, R is the ideal gas constant (approximately 8.314 J/(mol·K)), T is the temperature in Kelvin, V1 is the initial volume, and V2 is the final volume."
    return q,input_formula,a

def type4() :
    n = random.randint(1,10)
    p1 = random.randint(10,60)
    p2 = random.randint(10,60)
    t = random.randint(10,60)
    q = "If a diatomic gas of " + str(n) + " moles at " + str(p1) + " pas is isothermally changed to pressure " + str(p2) + " pas at " + str(t) + " K, then what is the work done.\n"
    input_formula = "Work Done = n*R*T*ln(P1/P2)"
    a = str(cal2(n,t,p1,p2)) + " joules\n"
    a += "To calculate the work done during an isothermal expansion of a diatomic gas, we can use the following equation: Work done = n * R * T * ln(P1/P2), where n is the number of moles of the gas, R is the ideal gas constant (approximately 8.314 J/(mol·K)), T is the temperature in Kelvin, P1 is the initial pressure, and P2 is the final pressure."
    return q,input_formula,a

def type5() :
    n = random.randint(1,10)
    v1 = random.randint(10,60)
    v2 = random.randint(10,60)
    t = random.randint(10,60)
    q = "If a gas of " + str(n) + " moles at " + str(v1) + " m3 is isothermally changed to volume " + str(v2) + " m3 at " + str(t) + " K, then what is the work done.\n"
    input_formula = "Work Done = n*R*T*ln(V2/V1)"
    a = str(cal1(n,t,v1,v2)) + " joules\n"
    a += "To calculate the work done during an isothermal expansion of a monoatomic gas, we can use the following equation: Work done = n * R * T * ln(V2/V1), where n is the number of moles of the gas, R is the ideal gas constant (approximately 8.314 J/(mol·K)), T is the temperature in Kelvin, V1 is the initial volume, and V2 is the final volume."
    return q,input_formula,a

def type6() :
    n = random.randint(1,10)
    p1 = random.randint(10,60)
    p2 = random.randint(10,60)
    t = random.randint(10,60)
    q = "If a gas of " + str(n) + " moles at " + str(p1) + " pas is isothermally changed to pressure " + str(p2) + " pas at " + str(t) + " K, then what is the work done.\n"
    input_formula = "Work Done = n*R*T*ln(P1/P2)"
    a = str(cal2(n,t,p1,p2)) + " joules\n"
    a += "To calculate the work done during an isothermal expansion of a monoatomic gas, we can use the following equation: Work done = n * R * T * ln(P1/P2), where n is the number of moles of the gas, R is the ideal gas constant (approximately 8.314 J/(mol·K)), T is the temperature in Kelvin, P1 is the initial pressure, and P2 is the final pressure."
    return q,input_formula,a

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1,6)
    if types == 1 :
        ques,input_formula,answer = type1()
    elif types == 2 :
        ques,input_formula,answer = type2()
    elif types == 3 :
        ques,input_formula,answer = type3()
    elif types == 4 :
        ques,input_formula,answer = type4()
    elif types == 5 :
        ques,input_formula,answer = type5()
    elif types == 6 :
        ques,input_formula,answer = type6()
    
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

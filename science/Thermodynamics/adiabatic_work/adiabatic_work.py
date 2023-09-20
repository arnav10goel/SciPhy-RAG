import random
import json

# If a monoatomic gas of n moles at p1 pas, t1 K and volume v1 m3 is adiabatically changed to volume v2 m3, t2 K at pressure p2 pas, then what is the work done.
# If a monoatomic gas of n moles at p1 pas, t1 K and volume v1 m3 is adiabatically changed to volume v2 m3 and t2 K, then what is the work done.
# If a monoatomic gas of n moles at volume v1 m3 and t1 K is adiabatically changed to volume v2 m3, t2 K at pressure p2 pas, then what is the work done.
# If a diatomic gas of n moles at p1 pas and volume v1 m3 is adiabatically changed to volume v2 m3 at pressure p2 pas, then what is the work done.
# If a diatomic gas of n moles at p1 pas and volume v1 m3 is adiabatically changed to volume v2 m3, then what is the work done.
# If a diatomic gas of n moles at volume v1 m3 and t1 K is adiabatically changed to volume v2 m3, t2 K at pressure p2 pas, then what is the work done.

no_of_samples = 60

samples = []

r = 8.31

def cal1(g,p1,p2,v1,v2) :
    return round(((p2*v2)-(p1*v1))/(1-g),1)

def cal3(g,p2,v1,v2) : 
    return round(((p2*v2)((v2**(1-g))-(v1**(1-g))))/(1-g),1)

def cal2(g,p1,v1,v2) :
    return round(((p1*v1)((v2**(1-g))-(v1**(1-g))))/(1-g),1)


def type1() :
    n = random.randint(1,10)
    p1 = random.randint(10,50)
    p2 = random.randint(10,50)
    v1 = random.randint(10,50)
    v2 = random.randint(10,50)
    t1 = random.randint(10,50)
    t2 = random.randint(10,50)
    q = "If a monoatomic gas of " + str(n) + " moles at " + str(p1) + " pas, " + str(t1) + " K and volume " + str(v1) + " m3 is adiabatically changed to volume " + str(v2) + " m3, " + str(t2) + " K at pressure " + str(p2) + " pas, then what is the work done.\n"
    input_formula = "Work = (P1*V1-P2*V2)/1.66-1"
    a = str(cal1(1.66,p1,p2,v1,v2)) + " joules\n"
    a += "To calculate the work done during the adiabatic expansion of a monoatomic gas, we can use the following formula: (P1*V1-P2*V2)/1.66-1 where P1 and V1 are the initial pressure and volume and P2 and V2 are the final pressure and volume."
    return q,input_formula,a

def type2() :
    n = random.randint(1,10)
    p1 = random.randint(10,50)
    v1 = random.randint(10,50)
    v2 = random.randint(10,50)
    t1 = random.randint(10,50)
    t2 = random.randint(10,50)
    q = "If a monoatomic gas of " + str(n) + " moles at " + str(p1) + " pas, " + str(t1) + " K and volume " + str(v1) + " m3 is adiabatically changed to volume " + str(v2) + " m3, and " + str(t2) + " K, then what is the work done.\n"
    input_formula = "Work = {n*R*(T2-T1)}/1.66-1"
    a = str(cal2(1.66,p1,v1,v2)) + " joules\n"
    a += "To calculate the work done during the adiabatic expansion of a monoatomic gas, we can use the following formula: {n*R*(T2-T1)}/1.66-1 where T1 is initial temperature and T2 is final temperature."
    return q,input_formula,a

def type3() :
    n = random.randint(1,10)
    p2 = random.randint(10,50)
    v1 = random.randint(10,50)
    v2 = random.randint(10,50)
    t1 = random.randint(10,50)
    t2 = random.randint(10,50)
    q = "If a monoatomic gas of " + str(n) + " moles at " + str(t1) + " K and volume " + str(v1) + " m3 is adiabatically changed to volume " + str(v2) + " m3, " + str(t2) + " K at pressure " + str(p2) + " pas, then what is the work done.\n"
    input_formula = "Work = (P1*V1-P2*V2)/1.66-1"
    a = str(cal3(1.66,p2,v1,v2)) + " joules\n"
    a += "To calculate the work done during the adiabatic expansion of a monoatomic gas, we can use the following formula: (P1*V1-P2*V2)/1.66-1 where P1 and V1 are the initial pressure and volume and P2 and V2 are the final pressure and volume."
    return q,input_formula,a

def type4() :
    n = random.randint(1,10)
    p1 = random.randint(10,50)
    p2 = random.randint(10,50)
    v1 = random.randint(10,50)
    v2 = random.randint(10,50)
    t1 = random.randint(10,50)
    t2 = random.randint(10,50)
    q = "If a diatomic gas of " + str(n) + " moles at " + str(p1) + " pas, " + str(t1) + " K and volume " + str(v1) + " m3 is adiabatically changed to volume " + str(v2) + " m3, " + str(t2) + " K at pressure " + str(p2) + " pas, then what is the work done.\n"
    input_formula = "Work = (P1*V1-P2*V2)/1.4-1"
    a = str(cal1(1.4,p1,p2,v1,v2)) + " joules\n"
    a += "To calculate the work done during the adiabatic expansion of a diatomic gas, we can use the following formula: (P1*V1-P2*V2)/1.4-1 where P1 and V1 are the initial pressure and volume and P2 and V2 are the final pressure and volume."
    return q,input_formula,a

def type5() :
    n = random.randint(1,10)
    p1 = random.randint(10,50)
    v1 = random.randint(10,50)
    v2 = random.randint(10,50)
    t1 = random.randint(10,50)
    t2 = random.randint(10,50)
    q = "If a diatomic gas of " + str(n) + " moles at " + str(p1) + " pas, " + str(t1) + " K and volume " + str(v1) + " m3 is adiabatically changed to volume " + str(v2) + " m3, and " + str(t2) + " K, then what is the work done.\n"
    input_formula = "Work = (P1*V1-P2*V2)/1.4-1"
    a = str(cal2(1.4,p1,v1,v2)) + " joules\n"
    a += "To calculate the work done during the adiabatic expansion of a diatomic gas, we can use the following formula: {n*R*(T2-T1)}/1.4-1 where T1 is initial temperature and T2 is final temperature."
    return q,input_formula,a

def type6() :
    n = random.randint(1,10)
    p2 = random.randint(10,50)
    v1 = random.randint(10,50)
    v2 = random.randint(10,50)
    t1 = random.randint(10,50)
    t2 = random.randint(10,50)
    q = "If a diatomic gas of " + str(n) + " moles at " + str(t1) + " K and volume " + str(v1) + " m3 is adiabatically changed to volume " + str(v2) + " m3, " + str(t2) + " K at pressure " + str(p2) + " pas, then what is the work done.\n"
    input_formula = "Work = (P1*V1-P2*V2)/1.4-1"
    a = str(cal3(1.4,p2,v1,v2)) + " joules\n"
    a += "To calculate the work done during the adiabatic expansion of a diatomic gas, we can use the following formula: (P1*V1-P2*V2)/1.4-1 where P1 and V1 are the initial pressure and volume and P2 and V2 are the final pressure and volume."
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

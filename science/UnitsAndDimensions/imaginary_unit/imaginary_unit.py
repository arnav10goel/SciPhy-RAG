import random
import json

# Suppose we employ a system of units in which the unit of mass equals a kg, the unit of length equals b m, the unit of time is c, then value of d joule in new system.
# Suppose we employ a system of units in which the unit of mass equals a kg, the unit of length equals b m, the unit of time is c, then value of d newton in new system.
# Suppose we employ a system of units in which the unit of mass equals a kg, the unit of length equals b m, the unit of time is c, then value of d pascal in new system.
# Suppose we employ a system of units in which the unit of mass equals a kg, the unit of length equals b m, the unit of time is c s, if the value of x joule is equal to d units in new system, find x?"
# Suppose we employ a system of units in which the unit of mass equals a kg, the unit of length equals b m, the unit of time is c s, if the value of x newton is equal to d units in new system, find x?"
# Suppose we employ a system of units in which the unit of mass equals a kg, the unit of length equals b m, the unit of time is c s, if the value of x pascal is equal to d units in new system, find x?"

no_of_samples = 70

samples = []

def type1():
    a = random.randint(10,100)
    b = random.randint(10,100)
    c = random.randint(50,100)
    d = random.randint(1,10)
    q = "Suppose we employ a system of units in which the unit of mass equals "+str(a)+" kg, the unit of length equals "+str(b)+" m, the unit of time is "+str(c)+" s, if the value of x joule is equal to "+str(d)+" units in new system, find x?\n"
    input_formula = "x J = (m kg) * (l m^2) / (t^2 s^2)"
    a = str(round(d*(a)*(b**2)*(c**(-2)),2)) + "\n"
    a += "To find the value of x joules in the given system of units, we need to consider the relationships between the units of mass (kg), length (m), time (s), and energy (Joule). In the new system of units, we have: 1 unit of mass = "+str(a)+" kg, 1 unit of length = "+str(b)+" m, 1 unit of time = "+str(c)+" s. To find the value of x joules, we need to determine the conversion factors between the new system and the standard SI units. The energy (Joule) can be expressed as: x J = (m kg) * (l m^2) / (t^2 s^2). Substituting the given values into this equation, we have: x J = (m * "+str(a)+" kg) * (l * "+str(b)+" m^2) / (t^2 * "+str(c)+" s^2). Simplifying this expression will give us the value of x in joules."
    return q,input_formula,a

def type2():
    a = random.randint(50,110)
    b = random.randint(10,70)
    c = random.randint(10,110)
    d = random.randint(1,10)
    q = "Suppose we employ a system of units in which the unit of mass equals "+str(a)+" kg, the unit of length equals "+str(b)+" m, the unit of time is "+str(c)+" s, if the value of x newton is equal to "+str(d)+" units in new system, find x?\n"
    input_formula = "x N = (m kg) * (l m) / (t^2 s^2)"
    a = str(round(d*(a)*(b)*(c**(-2)),2)) + "\n"
    a += "To find the value of x newtons in the given system of units, we need to consider the relationships between the units of mass (kg), length (m), time (s), and force (Newton). In the new system of units, we have: 1 unit of mass = "+str(a)+" kg, 1 unit of length = "+str(b)+" m, 1 unit of time = "+str(c)+" s. To find the value of x newtons, we need to determine the conversion factors between the new system and the standard SI units. The force (Newton) can be expressed as: x N = (m kg) * (l m) / (t^2 s^2). Substituting the given values into this equation, we have: x N = (m * "+str(a)+" kg) * (l * "+str(b)+" m) / (t^2 * "+str(c)+" s^2). Simplifying this expression will give us the value of x in newtons."
    return q,input_formula,a

def type3():
    a = random.randint(10,50)
    b = random.randint(1,20)
    c = random.randint(10,50)
    d = random.randint(1000,1100)
    q = "Suppose we employ a system of units in which the unit of mass equals "+str(a)+" kg, the unit of length equals "+str(b)+" m, the unit of time is "+str(c)+" s, if the value of x pascal is equal to "+str(d)+" units in new system, find x\n"
    input_formula = "x Pa = (Force N) / (Area m²) = [(m kg) * (l m) / (t² s²)] / [(l m)²]"
    a = str(round(d*(a)*(b**(-1))*(c**(-2)),2)) +"\n"
    a += "To find the value of x pascals in the given system of units, we need to consider the relationships between the units of mass (kg), length (m), time (s), and pressure (Pascal). In the new system of units, we have: 1 unit of mass = "+str(a)+" kg, 1 unit of length = "+str(b)+" m, 1 unit of time = "+str(c)+" s. To find the value of x pascals, we need to determine the conversion factors between the new system and the standard SI units. The pressure (Pascal) can be expressed as: x Pa = (Force N) / (Area m²) = [(m kg) * (l m) / (t² s²)] / [(l m)²] = (m * "+str(a)+" kg) / (t² * "+str(c)+" s²). Substituting the given values into this equation, we have: x Pa = (m * "+str(a)+" kg) / (t² * "+str(c)+" s²). Simplifying this expression will give us the value of x in pascals."
    return q,input_formula,a

def type4():
    a = random.randint(10,50)
    b = random.randint(30,80)
    c = random.randint(50,100)
    d = random.randint(30,80)
    q = "Suppose we employ a system of units in which the unit of mass equals "+str(a)+" kg, the unit of length equals "+str(b)+" m, the unit of time is "+str(c)+" s, then value of "+str(d)+" joules in new system\n"
    input_formula = ""+str(d)+" J = (m kg) * (l m^2) / (t^2 s^2)"
    a = str(round(d*(a**(-1))*(b**(-2))*(c**(2)),2)) + "\n"
    a += "To find the value of "+str(d)+" joules in the given system of units, we need to consider the relationships between the units of mass (kg), length (m), time (s), and energy (Joule). In the new system of units, we have: 1 unit of mass = "+str(a)+" kg, 1 unit of length = "+str(b)+" m, 1 unit of time = "+str(c)+" s. To find the value of "+str(d)+" joules, we need to determine the conversion factors between the new system and the standard SI units. The energy (Joule) can be expressed as: "+str(d)+" J = (m kg) * (l m^2) / (t^2 s^2). Substituting the given values into this equation, we have:"+str(d)+" J = (m * "+str(a)+" kg) * (l * "+str(b)+" m^2) / (t^2 * "+str(c)+" s^2). Simplifying this expression will give us the value of "+str(d)+" joules in the new system of units."
    return q,input_formula,a

def type5():
    a = random.randint(10,80)
    b = random.randint(10,80)
    c = random.randint(10,110)
    d = random.randint(10,20)
    q = "Suppose we employ a system of units in which the unit of mass equals "+str(a)+" kg, the unit of length equals "+str(b)+" m, the unit of time is "+str(c)+" s, then value of "+str(d)+" newton in new system\n"
    input_formula = ""+str(d)+" N = (m kg) * (l m) / (t^2 s^2)"
    a = str(round(d*(a**(-1))*(b**(-1))*(c**(2)),2)) + "\n"
    a += "To find the value of "+str(d)+" newtons in the given system of units, we need to consider the relationships between the units of mass (kg), length (m), time (s), and force (Newton). In the new system of units, we have: 1 unit of mass = "+str(a)+" kg, 1 unit of length = "+str(b)+" m, 1 unit of time = "+str(c)+" s. To find the value of "+str(d)+" newtons, we need to determine the conversion factors between the new system and the standard SI units. The force (Newton) can be expressed as: "+str(d)+" N = (m kg) * (l m) / (t^2 s^2). Substituting the given values into this equation, we have: "+str(d)+" N = (m * "+str(a)+" kg) * (l * "+str(b)+" m) / (t^2 * "+str(c)+" s^2). Simplifying this expression will give us the value of "+str(d)+" newtons in the new system of units."
    return q,input_formula,a

def type6():
    a = random.randint(100,200)
    b = random.randint(1,100)
    c = random.randint(1,50)
    d = random.randint(1,10)
    q = "Suppose we employ a system of units in which the unit of mass equals "+str(a)+" kg, the unit of length equals "+str(b)+" m, the unit of time is "+str(c)+" s, then value of "+str(d)+" pascal in new system\n"
    input_formula = ""+str(d)+" Pa = (Force N) / (Area m²) = [(m kg) * (l m) / (t² s²)] / [(l m)²]"
    a = str(round(d*(a**(-1))*(b**(1))*(c**(2)),2)) +"\n"
    a += "To find the value of "+str(d)+" pascals in the given system of units, we need to consider the relationships between the units of mass (kg), length (m), time (s), and pressure (Pascal). In the new system of units, we have: 1 unit of mass = "+str(a)+" kg, 1 unit of length = "+str(b)+" m, 1 unit of time = "+str(c)+" s. To find the value of "+str(d)+" pascals, we need to determine the conversion factors between the new system and the standard SI units. The pressure (Pascal) can be expressed as: "+str(d)+" Pa = (Force N) / (Area m²) = [(m kg) * (l m) / (t² s²)] / [(l m)²] = (m * "+str(a)+" kg) / (t² * "+str(c)+" s²). Substituting the given values into this equation, we have: "+str(d)+" Pa = (m * "+str(a)+" kg) / (t² * "+str(c)+" s²). Simplifying this expression will give us the value of "+str(d)+" pascals in the new system of units."
    return q,input_formula,a

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1,6)
    if types == 1:
        ques,input_formula,answer = type1()
    elif types == 2:
        ques,input_formula,answer = type2()
    elif types == 3:
        ques,input_formula,answer = type3()
    elif types == 4:
        ques,input_formula,answer = type4()
    elif types == 5:
        ques,input_formula,answer = type5()
    elif types == 6:
        ques,input_formula,answer = type6()
    
    sample["instruction"] = ques
    sample["input"] = input_formula
    sample["output"] = answer

    samples.append(sample)

# Load existing JSON file
with open("science/UnitsAndDimensions/uad.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/UnitsAndDimensions/uad.json", "w") as file:
    json.dump(existing_data, file, indent=4) 
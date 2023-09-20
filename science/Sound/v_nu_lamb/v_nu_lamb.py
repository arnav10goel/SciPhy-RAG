import random
import json

# Calculate the wavelength of a sound wave whose frequency is f hz and speed is v m/s in a given medium. 
# Calculate the frequency of a sound wave whose wavelength is lamb m and speed is v m/s in a given medium. 
# Calculate the speed of a sound wave whose frequency is f hz and wavelength is lamb m in a given medium. 

no_of_samples = 40
# no_of_samples = 30

samples = []

def calculation_lamb(f, v): 
    return v // f

def calculation_f(lamb, v):
    return v // lamb

def calculation_v(f , lamb):
    return f*lamb

def type1():
    f = random.randint(1,1000)
    v = (random.randint(1,1000))*f
    lamb = str(calculation_lamb(f,v)) + " m\n"
    q = "Calculate the wavelength of a sound wave whose frequency is "+str(f)+" hz and speed is "+str(v)+" m/s in a given medium ?\n"
    lamb += "To calculate the wavelength of a sound wave, we can use the formula: Wavelength = Speed / Frequency. In this case, the speed of the sound wave is "+str(v)+" m/s and the frequency is "+str(f)+" Hz. Substituting these values into the formula, we can calculate the wavelength: Wavelength = "+str(v)+" m/s / "+str(f)+" HzTo calculate the wavelength of a sound wave, we can use the formula: Wavelength = Speed / Frequency. In this case, the speed of the sound wave is "+str(v)+" m/s and the frequency is "+str(f)+" Hz. Substituting these values into the formula, we can calculate the wavelength: Wavelength = "+str(v)+" m/s / "+str(f)+" Hz"
    return q,lamb

def type2():
    lamb = random.randint(1,1000)
    v = (random.randint(1,1000))*lamb
    f = str(calculation_f(lamb,v)) + " hz\n"
    q = "Calculate the frequency of a sound wave whose wavelength is "+str(lamb)+" m and speed is "+str(v)+" m/s in a given medium ?\n"
    f += "To calculate the frequency of a sound wave, we can use the formula: Frequency = Speed / Wavelength. In this case, the speed of the sound wave is "+str(v)+" m/s and the wavelength is "+str(lamb)+" m. Substituting these values into the formula, we can calculate the frequency: Frequency = "+str(v)+" m/s / "+str(lamb)+" m"
    return q,f

def type3():
    f = random.randint(1,2000)
    lamb = random.randint(1,1000)
    v = str(calculation_v(f,lamb)) + " m/s\n"
    q = "Calculate the speed of a sound wave whose frequency is "+str(f)+" hz and wavelength is "+str(lamb)+" m in a given medium ?\n"
    v += "To calculate the speed of a sound wave, we can use the formula: Speed = Frequency × Wavelength. In this case, the frequency of the sound wave is "+str(f)+" Hz and the wavelength is "+str(lamb)+" m. Substituting these values into the formula, we can calculate the speed: Speed = "+str(f)+" Hz × "+str(lamb)+" m"
    return q,v

for i in range(no_of_samples):
    sample = {} 
    types = random.randint(0,3)
    if types == 0:
        ques,answer = type1()
    if types == 1:
        ques,answer = type2()
    if types == 2 or types == 3:
        ques,answer = type3()
    
    input_formula = "Wavelength = Speed / Frequency"

    sample["instruction"] = ques
    sample["input"] = input_formula
    sample["output"] = answer

    samples.append(sample)

# Load existing JSON file
with open("science/Sound/sound.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/Sound/sound.json", "w") as file:
    json.dump(existing_data, file, indent=4) 
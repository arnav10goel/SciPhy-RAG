import random
import json

# Estimate the distance for which ray optics is good approximation for an aperture of d mm and wavelength l nm.
# Two towers on top of two hills are d km apart. The line joining them passes l m above a hill halfway between the towers. What is the longest wavelength of radio waves, which can be sent between the two towers without appreciable diffraction effects. 

no_of_samples = 20

samples = []

def type1() :
    d = random.randint(1,20)
    l = random.randint(1,1000)
    q = "Estimate the distance for which ray optics is good approximation for an aperture of " + str(d) + " mm and wavelength " + str(l) + " nm.\n"
    l = l *(10**-9)
    input_formula = "Fresnel Distance = Aperture^2/Wavelength of light"
    a = "{:.2e}".format((d*d)/l) + " m\n"
    a += "The criterion for ray optics to be a good approximation is when the size of the aperture is much larger than the wavelength of light. This condition ensures that the wave nature of light can be neglected, and light can be treated as a ray."
    a += "To estimate the distance for which ray optics is a good approximation, we can use the following formula: Distance ≈ 2 * (aperture size)^2 / (wavelength)"
    return q,input_formula,a 

def type2() :
    d = random.randint(1,100)
    l = random.randint(1,200)
    q = "Two towers on top of two hills are " + str(d) + " km apart. The line joining them passes " + str(l) + " m above a hill halfway between the towers. What is the longest wavelength of radio waves, which can be sent between the two towers without appreciable diffraction effects.\n"
    d = d * (10**3)
    input_formula = "Fresnel Distance*Aperture = Wavelength of light^2"
    a = "{:.2e}".format((l*l)/d) + " m\n"
    a += "To determine the longest wavelength of radio waves that can be sent between the two towers without appreciable diffraction effects, we can use the Fresnel diffraction criterion. The Fresnel diffraction criterion states that when the distance (d) between the two towers is much larger than the square of the wavelength (λ), diffraction effects can be neglected."
    a += "In this case, we want to find the maximum wavelength, so we can rearrange the formula to solve for λ: λ ≈ sqrt(d * l)"
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
with open("science/WaveOptics/wo.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/WaveOptics/wo.json", "w") as file:
    json.dump(existing_data, file, indent=4) 

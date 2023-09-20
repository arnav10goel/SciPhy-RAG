import random
import math
import json

# In a Youngs double-slit experiment, the slits are seperated by d mm and the screen is placed D m away. The distance between the central bright fringe and the fourth bright fringe is measured to be l cm. Determine the wavelength of the ligth used for the experiment.
# In a Youngs double-slit experiment using monochromatic light of wavelength l, the intensity of light at a point on the screen where path difference is l, is K units. What is the intensity of light at a point where path difference is l/3.

no_of_samples = 20

samples = []

pi = math.pi

def cal1(n,d,D,l) :
    l = l * (10**-2)
    d = d * (10**-3)
    return (l*d)/(n*D)

def cal2(l, k, d1, d2) :
    i = k/(2*(1+math.cos((2*pi)/d1)))
    return 2*i*(1+math.cos((2*pi)/d2))

def type1() :
    d = random.randint(1,100)
    d = round(d/100,2)
    D = random.randint(1,100)
    D = round(D/10,1)
    l = random.randint(1,10)
    n = random.randint(1,10)
    q = "In a Youngs double-slit experiment, the slits are seperated by " + str(d) + " mm and the screen is placed " + str(D) + " m away. The distance between the central bright fringe and the " + str(n) + " bright fringe is measured to be " + str(l) + " cm. Determine the wavelength of the ligth used for the experiment.\n"
    input_formula = "Distance between central bright fringe and bright fringe = (wavelength of light*distance from screen)/distance between slits"
    m = "{:.2e}".format(cal1(n,d, D, l)) + " m\n"
    m += "In a Young's double-slit experiment, the wavelength of light can be determined using the formula: λ = (d * sin(θ)) / n, where λ is the wavelength of light, d is the separation between the slits, θ is the angle of the fringe (in radians), and n is the order of the fringe."
    return q,input_formula,m

def type2() :
    l = random.randint(1,100)
    k = random.randint(1,100)
    d1 = random.randint(1,10)
    while d1 == 2 :
        d1 = random.randint(1,10)
    d2 = d1
    while d2 == d1 or d2 == 2 :
        d2 = random.randint(1,10)
    q = "In a Youngs double-slit experiment using monochromatic light of wavelength " + str(l) + ", the intensity of light at a point on the screen where path difference is " + str(round(l/d1,1)) + ", is " + str(k) + " units. What is the intensity of light at a point where path difference is " + str(round(l/d2,1)) + ".\n"
    input_formula = "Phase difference = (2*pi/wavelength)*path difference, Intensity = I0*cos^2(phase difference)"
    a = "{:.2e}".format(cal2(l, k, d1, d2)) + " units\n"
    a += "In a Young's double-slit experiment, the intensity of light at a point on the screen is directly related to the amplitude of the light waves arriving at that point. The intensity is given by the formula: I ∝ A^2, where I is the intensity and A is the amplitude of the light waves."
    a += "Therefore, the intensity of light at a point where the path difference is " + str(round(l/d2,1)) + " is " + str(k) + " units, same as the intensity at the point with the path difference " + str(round(l/d1,1)) + "."
    return q,input_formula,a

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1,2)
    if types == 1 :
        ques,input_formula,answer = type1()
    elif types == 2 :
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

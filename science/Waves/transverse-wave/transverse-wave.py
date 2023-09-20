import random
import math
import json

# A string of mass 2.50 kg is under a tension of 200 N. The length of the stretched string is 20.0 m. If the transverse jerk is struck at one end of the string, how long does the disturbance take to reach the other end?
# A steel wire has a length of 12.0 m and a mass of 2.10 kg. What should be the tension in the wire so that speed of a transverse wave on the wire equals the speed of sound in dry air at 2 0°C = 340 ms-1.
# A wire stretched between two rigid supports vibrates in its fundamental mode with a frequency of 45 Hz. The mass of the wire is 3.5 x 10-2 kg and its linear mass density is 4.0 x 10-2 kg m-3. What is (a) the speed of a transverse wave on the string, and (b) the tension in the string?

no_of_samples = 40
# no_of_samples = 30

samples = []

def type1():
    m = random.randint(1,100)
    l = random.randint(1,100)
    t = random.randint(1,800)
    q = "A string of mass "+str(m)+" kg is under a tension of "+str(t)+" N. The length of the stretched string is "+str(l)+" m. If the transverse jerk is struck at one end of the string, how long does the disturbance take to reach the other end?\n"
    v = math.sqrt(t*l/m)
    time = l/v
    input_formula = "Speed^2 = Tension*length/mass"
    a = "{:.2e}".format(time) + " s\n"
    a += "To determine the time it takes for a disturbance to travel from one end of a string to the other, we can use the wave speed equation for transverse waves on a string. The wave speed (v) on a string is given by: v = sqrt(T / μ), where T is the tension in the string and μ is the linear mass density of the string, which is given by the mass per unit length (μ = m / l)."
    return q,input_formula,a

def type2():
    l = random.randint(1,400)
    m = random.randint(1,400)
    temp = random.randint(15,35)
    q = "A steel wire has a length of "+str(l)+" m and a mass of "+str(m)+" kg. What should be the tension in the wire so that speed of a transverse wave on the wire equals the speed of sound in dry air at "+str(temp)+" degree C = 340 ms-1.\n"
    T = (340*340)*(m/l)
    input_formula = "Speed^2 = Tension*length/mass"
    a = "{:.2e}".format(T) + " newton\n"
    a += "To determine the time it takes for a disturbance to travel from one end of a string to the other, we can use the wave speed equation for transverse waves on a string. The wave speed (v) on a string is given by: v = sqrt(T / μ), where T is the tension in the string and μ is the linear mass density of the string, which is given by the mass per unit length (μ = m / l)."
    return q,input_formula,a

def type3(types):
    f = random.randint(1,200)
    m = round(random.randint(1,200)/1000,3)
    mu = round(random.randint(1,200)/1000,3)
    q = "A wire stretched between two rigid supports vibrates in its fundamental mode with a frequency of "+str(f)+" Hz. The mass of the wire is "+str(m)+" kg and its linear mass density is "+str(mu)+" kg m-3. What is "
    l = m/mu
    lamda = 2*l
    speed = f*lamda
    if types == 3:
        q = q + "the speed of a transverse wave on the string?\n"
        input_formula = "Speed^2 = Tension*length/mass"
        a = "{:.2e}".format(speed) + " ms-1\n"
    else:
        q = q + "the tension in the string?\n"
        input_formula = "Speed^2 = Tension*length/mass"
        a = "{:.2e}".format(speed*speed*mu) + " newton\n"
    a += """To find the length of the wire, we can use the formula for the fundamental frequency of a vibrating wire:
f = (1/2L) * sqrt(T / μ)

Where f is the frequency, L is the length of the wire, T is the tension in the wire, and μ is the linear mass density.

We can rearrange the formula to solve for L:

L = (1/2) * sqrt(T / (f^2 * μ))

Given that the frequency f is "+str(f)+" Hz, the mass m is "+str(m)+" kg, and the linear mass density μ is "+str(mu)+" kg/m³, we need to determine the tension T in the wire.

The tension T can be calculated using the formula:

T = μ * g * L

Where g is the acceleration due to gravity.

Substituting the known values into the formula, we can calculate the tension T.

Once we have the tension T, we can substitute it and the other known values into the formula for L to find the length of the wire in its fundamental mode.

L = (1/2) * sqrt(T / (f^2 * μ))

Calculating this expression will give us the length of the wire."""    
    return q,input_formula,a
        
    
for i in range(no_of_samples):
    sample = {}
    types = random.randint(1,4)
    if types == 1:
        q,input_formula,a = type1()
    elif types == 2:
        q,input_formula,a = type2()
    else:
        q,input_formula,a = type3(types)
    
    sample["instruction"] = q
    sample["input"] = input_formula
    sample["output"] = a

    samples.append(sample)

# Load existing JSON file
with open("science/Waves/wave.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/Waves/wave.json", "w") as file:
    json.dump(existing_data, file, indent=4) 
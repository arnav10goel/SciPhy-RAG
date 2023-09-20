import random
import json

# A sonar device on a submarine sends out a signal and receives an echo t s later. Find the speed of sound in that material if the distance of the object from the submarine is s m ?
# A sonar device on a submarine sends out a signal. Find the time after which echo is received if speed of sound in that material is v m/s and distance of the object from the submarine is s m ?
# A sonar device on a submarine sends out a signal and receives an echo t s later. Find the distance of the object from the submarine if speed of sound in that material is v m/s ?

no_of_samples = 30
# no_of_samples = 30

samples = []

def calculation_s(v, t): 
    return round(v * (t/2), 1)

def calculation_v(s, t):
    return round((2*s) / t, 1)

def calculation_t(s, v):
    return round((2*s) / v, 1)

def type1():
    v = random.randint(1,1000)
    t = random.randint(1,1000)
    s = str(calculation_s(v,t)) + " m\n"
    q = "A sonar device on a submarine sends out a signal and receives an echo "+str(t)+" s later. Find the distance of the object from the submarine if speed of sound in that material is "+str(v)+" m/s ?\n"
    s += "To find the distance of the object from the submarine, we can use the equation: Distance = Speed * Time. In this case, the speed of sound in the material is "+str(v)+" m/s and the time it takes for the echo to return is "+str(t)+" seconds. Substituting these values into the equation, we can calculate the distance of the object from the submarine: Distance = "+str(v)+" m/s * "+str(t)+" s. Calculating this expression will give us the distance of the object from the submarine."
    return q,s

def type2():
    s = random.randint(4000,5000)
    t = random.randint(1,1000)
    v = str(calculation_v(s,t)) + " m/s\n"
    q = "A sonar device on a submarine sends out a signal and receives an echo "+str(t)+" s later. Find the speed of sound in that material if the distance of the object from the submarine is "+str(s)+" m ?\n"
    v += "To find the speed of sound in the material, we can use the equation: Speed = Distance / Time. In this case, the distance of the object from the submarine is "+str(s)+" meters and the time it takes for the echo to return is "+str(t)+" seconds. Substituting these values into the equation, we can calculate the speed of sound in the material: Speed = "+str(s)+" m / "+str(t)+" s. Calculating this expression will give us the speed of sound in the material."
    return q,v

def type3():
    s = random.randint(4000,5000)
    v = random.randint(1,1000)
    t = str(calculation_t(s,v)) + " s\n"
    q = "A sonar device on a submarine sends out a signal. Find the time after which echo is received if speed of sound in that material is "+str(v)+" m/s and distance of the object from the submarine is "+str(s)+" m ?\n"
    t += "To find the time it takes for the echo to be received, we can use the equation: Time = Distance / Speed. In this case, the speed of sound in the material is "+str(v)+" m/s and the distance of the object from the submarine is "+str(s)+" meters. Substituting these values into the equation, we can calculate the time it takes for the echo to be received: Time = "+str(s)+" m / "+str(v)+" m/s. Calculating this expression will give us the time it takes for the echo to be received by the sonar device on the submarine."
    return q,t

for i in range(no_of_samples):
    sample = {}
    types = random.randint(0,2)
    if types == 0:
        ques,answer = type1()
    if types == 1:
        ques,answer = type2()
    if types == 2:
        ques,answer = type3()
    
    input_formula = "Distance = Speed * Time"
    
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
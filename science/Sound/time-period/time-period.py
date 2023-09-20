import random
import json

# The frequency of sound is f Hz.How many times does it vibrate in t seconds?
# A person is listening to a tone of f Hz sitting at a distance of s m from the source
# of the sound. What is the time interval between successive compressions from the source? 

no_of_samples = 30
# no_of_samples = 20

samples = []

def calculation_vib(f, t): 
    return f * t

def calculation_t(f):
    return round(1000000/f,1)

def type1():
    f = random.randint(1,1000)
    t = random.randint(1,2000)
    num = str(calculation_vib(f,t)) + " \n"
    q = "The frequency of sound is "+str(f)+" Hz.How many times does it vibrate in "+str(t)+" seconds?\n"
    input_formula = "Number of vibrations = frequency*time"
    num += "To calculate the number of vibrations (cycles) of a sound wave in a given time, we can use the formula: Number of vibrations = frequency × time. In this case, the frequency of the sound wave is "+str(f)+" Hz and the time is "+str(t)+" seconds. Substituting these values into the formula, we can calculate the number of vibrations: Number of vibrations = "+str(f)+" Hz × "+str(t)+" s"
    return q,input_formula,num

def type2():
    f = random.randint(1,1000000)
    s = random.randint(1,200)
    t = str(calculation_t(f)) + " microseconds\n"
    q = "A person is listening to a tone of "+str(f)+" Hz sitting at a distance of "+str(s)+" m from the source of the sound. What is the time interval between successive compressions from the source?\n"
    input_formula = "Time interval = Distance / Speed"
    t += "To calculate the time interval between successive compressions from the source, we need to consider the speed of sound in the medium. The speed of sound in air at room temperature is approximately 343 meters per second. The time interval between successive compressions (or any two consecutive points with maximum compression) can be calculated using the formula: Time interval = Distance / Speed. In this case, the distance from the source of the sound is "+str(s)+" meters and the speed of sound is approximately 343 m/s. Substituting these values into the formula, we can calculate the time interval between successive compressions: Time interval = "+str(s)+" m / 343 m/s. Calculating this expression will give us the time interval between successive compressions from the source."
    return q,input_formula,t

for i in range(no_of_samples):
    sample = {}
    types = random.randint(0,1)
    if types == 0:
        ques,input_formula,answer = type1()
    if types == 1:
        ques,input_formula,answer = type2()
    
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

import random
import json

# Find the ratio of time taken by the sound wave to travel a distance of x m in material-1 and material-2 (speed of sound in material-1 is v1 m/s, in material-2 is v2 m/s) ? 

no_of_samples = 20
# no_of_samples = 10

samples = []

for i in range(no_of_samples):
    sample = {}
    x = random.randint(1,10)
    v1 = random.randint(1,2000)
    v2 = random.randint(8000,10000)
    ques = "Find the ratio of time taken by the sound wave to travel a distance of "+str(x)+" m in material-1 and material-2 (speed of sound in material-1 is "+str(v1)+" m/s, in material-2 is "+str(v2)+" m/s) ?\n"
    input_formula = "Speed = Distance/Time"
    answer = str(round(v2/v1,1)) + "\n" 
    answer += "To find the ratio of the time taken by the sound wave to travel a distance of "+str(x)+" m in material-1 and material-2, we can use the equation: Ratio of time = time in material-1 / time in material-2. The time taken by the sound wave to travel a distance in material-1 can be calculated using the equation: time in material-1 = distance / speed in material-1. Similarly, the time taken by the sound wave to travel the same distance in material-2 can be calculated using: time in material-2 = distance / speed in material-2. Substituting the given values into the equations, we have: time in material-1 = "+str(x)+" m / "+str(v1)+" m/, time in material-2 = "+str(x)+" m / "+str(v2)+" m/s. Therefore, the ratio of the time taken by the sound wave to travel a distance of "+str(x)+" m in material-1 and material-2 is: Ratio of time = ("+str(x)+" m / "+str(v1)+" m/s) / ("+str(x)+" m / "+str(v2)+" m/s)= "+str(v2/v1)
    
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
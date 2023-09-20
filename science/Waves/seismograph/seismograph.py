import random
import json

# Earthquakes generate sound waves inside the earth. Unlike a gas, the earth can experience both transverse (S) and longitudinal (P) sound waves. Typically the speed of S wave is about 4.0 km s-1 . A seismograph records P and S waves from an earthquake. The first P wave arrives 4 min before the first S wave. Assuming the waves travel in straight line, at what distance does the earthquake occur?

no_of_samples = 20
# no_of_samples = 10

samples = []

for i in range(no_of_samples):
    sample = {}
    speed_s = random.randint(100,700)*10
    diff_speed_v = random.randint(20,90)*10
    time = random.randint(20,220)*2
    q = "Earthquakes generate sound waves inside the earth, assuming the speed of transverse(S) wave is "+str(speed_s)+" ms-1, speed of longitudinal(P) wave is "+str(speed_s+diff_speed_v)+" ms-1, if the first P wave arrives "+str(time)+" s before the first S wave to seismograph, at what distance does the earthquake occur?\n"
    input_formula = "Vs*Ts=Vp*Tp, L = Vp*Tp"
    a = "{:.2e}".format((time*speed_s*(speed_s+diff_speed_v))/(diff_speed_v*1000))+" km\n"
    a += "To determine the distance to the earthquake epicenter, we can use the difference in arrival times between the P wave and S wave at the seismograph."
    a += "Using the formula for distance (d) based on wave speed and time: d = (P wave speed - S wave speed) * t"

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
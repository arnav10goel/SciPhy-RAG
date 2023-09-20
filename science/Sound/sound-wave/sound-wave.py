import random
import json

# A sound produces c crests and c troughs in t seconds. When the second crest is produced, 
# the first is s m away from the source, then calculate  

no_of_samples = 30

samples = []

for i in range(no_of_samples):
    sample = {}
    c = random.randint(1,2000)
    t = random.randint(1,100)
    s = random.randint(1,2000)
    ques = "A sound produces "+str(c)+" crests and "+str(c)+" troughs in "+str(t)+" seconds. When the first trough is produced, the first crest is "+str(s)+" m away from the source, then calculate "
    types = random.randint(0,3)
    if types == 0:
        ques += "the wavelength ?\n"
        answer = str(2*s) + " m\n"
    if types == 1:
        ques += "the frequency ?\n"
        answer = str(round(c/t,1)) + " hz\n"
    if types == 2:
        ques += "the wave speed ?\n"
        answer = str(round((2*s)/t,1)) + " m/s\n"
    if types == 3:
        ques += "the time period ?\n"
        answer = str(round((t*1000)/c,1)) + " ms\n"
    input_formula = "Wavelength = Speed*Time Period, "
    answer += "To calculate the speed of sound, we need to determine the distance traveled by a crest or trough in the given time interval. In "+str(t)+" seconds, "+str(c)+" crests and "+str(c)+" troughs are produced. This means that one complete cycle of the wave (a crest and a trough) occurs "+str(c)+" times in "+str(t)+" seconds. Therefore, the time taken for one complete cycle (T) can be calculated as: T = "+str(t)+" s / "+str(c)+" cycles. The distance traveled by one complete cycle (wavelength, λ) is given by the formula: λ = speed * T, where speed is the speed of sound. Since the first crest is "+str(s)+" m away from the source, the distance traveled by a complete cycle (λ) can be expressed as: λ = "+str(s)+" m + "+str(s)+" m = 2 * "+str(s)+" m. Substituting the value of λ and T into the equation, we can calculate the speed of sound: speed = λ / T = (2 * "+str(s)+" m) / ("+str(t)+" s / "+str(c)+" cycles). Calculating this expression will give us the speed of sound."

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

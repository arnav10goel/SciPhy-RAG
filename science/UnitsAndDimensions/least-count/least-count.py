import random
import json

# Which of the following is the most precise device for measuring length:

no_of_samples = 20

samples = []

for i in range(no_of_samples):
    sample = {}
    div_ver = random.randint(1,4000)
    pitch = random.randint(1,10)
    div_guage = random.randint(100,10000)
    ques = "Which of the following is the most precise device for measuring length: (a) a vernier callipers with "+str(div_ver)+" divisions on the sliding scale, (b) a screw guage of pitch "+str(pitch)+" mm and "+str(div_guage)+" divisions on the circular scale, (c) an optical instrument that can measure length to within a wavelength of light?\n"
    answer = ""
    ans_prob = [1/(div_ver*1000),pitch/(1000*div_guage),6*(10**(-7))]
    temp = ans_prob.index(min(ans_prob))
    # print(ans_prob,temp)
    if temp == 0:
        answer = '(a)\n'
    elif temp == 1:
        answer = '(b)\n'
    elif temp == 2:
        answer = '(c)\n'
    answer += "To determine the most precise device for measuring length among the options given, we need to consider the number of divisions or increments on each device and the accuracy of the measurements they can provide, (a) Vernier Callipers: A vernier callipers typically consists of a main scale and a sliding scale with a vernier scale. The vernier scale allows for more precise measurements by providing additional divisions that correspond to a fraction of the main scale division. The precision of the vernier callipers depends on the number of divisions on the sliding scale. (b) Screw Gauge: A screw gauge measures small lengths based on the rotation of a screw with a known pitch. The pitch represents the distance moved per revolution of the screw. The precision of the screw gauge depends on the number of divisions on the circular scale. (c) Optical Instrument: An optical instrument that can measure length to within a wavelength of light has the potential for extremely high precision. The wavelength of light is typically in the order of nanometers, which allows for very accurate measurements. Comparing the options, the optical instrument that can measure length to within a wavelength of light offers the highest precision among the given choices. It can provide measurements with accuracy down to the scale of the wavelength of light."

    sample["instruction"] = ques
    sample["input"] = ""
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
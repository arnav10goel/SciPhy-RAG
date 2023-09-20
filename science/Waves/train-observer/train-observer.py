import random
import json

#  A train, standing at the outer signal of a railway station blows a whistle of frequency 400 Hz in still air.
# - What is the frequency of the whistle for a platform observer when the train 
# (a) approaches the platform with a speed of 10 ms~1. 
# (b) recedes from the platform with a speed of 10 ms-1

# A train, standing in a station-yard, blows a whistle of frequency 400 Hz in still air. The wind starts blowing in the direction from the yard to the station with a speed of 10 ms-1. What are the frequency, wavelength, and speed of sound for an observer standing on the station’s platform? Is the situation exactly identical to the case when the air is still and the observer runs towards the yard at a speed of 10 ms-1? The speed of sound in still air can be taken as 340 ms-1?

no_of_samples = 30
# no_of_samples = 10

samples = []

for i in range(no_of_samples):
    sample = {}
    freq = random.randint(100,900)
    v = random.randint(1,70)
    m = random.randint(40,100)
    types = random.randint(1,5)
    if types < 3:
        arr = ["approaches","recedes from"]
        q = "A train, standing at the outer signal of a railway station blows a whistle of frequency "+str(freq)+" Hz in still air. What is the frequency of the whistle for a platform observer of mass "+str(m)+" kg when the train "+arr[types-1]+" the platform with a speed of "+str(v)+" ms-1\n"
        if types == 1:
            a = str(round((340/(340-v))*freq,1)) + " ms-1\n"
        else:
            a = str(round((340/(340+v))*freq,1)) + " ms-1\n"
            a += "To calculate the frequency of the whistle observed by a platform observer when a train passes by, we need to consider the Doppler effect due to the relative motion between the train and the observer. The Doppler effect accounts for the change in frequency observed when the source of sound and the observer are in relative motion."
    else:
        arr = ["frequency","wavelength","speed of sound"]
        q = "A train, standing in a station-yard, blows a whistle of frequency "+str(freq)+" Hz in still air. The wind starts blowing in the direction from the yard to the station with a speed of "+str(v)+" ms-1. What is the "+arr[types-3]+" for an observer standing on the station’s platform? Compare it with situation when the air is still and the observer of mass "+str(m)+" kg runs towards the yard at a speed of "+str(v)+" ms-1?\n"
        if types == 3:
            bef = str(freq) + " hertz"
            after = str(round(((340+v)/340)*freq,1)) + " hertz"
        elif types == 4:
            bef = str(340+v)+"/"+str(freq) + " m"
            after = str(340)+"/"+str(freq) + " m"
        else:
            bef = str(340+v)+ " ms-1"
            after = "340 ms-1"
        a = "case-1(wind) : "+bef+", case-2(observer) : "+after+"\n"
        a += "To calculate the frequency heard by an observer standing on the station's platform when the wind is blowing, we need to consider the Doppler effect due to the relative motion between the source of sound and the observer. Given that the train blows a whistle of frequency "+str(freq)+" Hz in still air and the wind is blowing in the direction from the yard to the station with a speed of "+str(v)+" m/s, we can determine the observed frequency for the platform observer." 
        a += "The formula to calculate the observed frequency is: f' = f * (v_sound + v_wind) / (v_sound), where f' is the observed frequency, f is the emitted frequency, v_sound is the speed of sound in still air, and v_wind is the velocity of the wind."
    input_formula = "Apparent frequency = (speed of sound in air/speed of sound in air - speed of train)*original frequency"

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
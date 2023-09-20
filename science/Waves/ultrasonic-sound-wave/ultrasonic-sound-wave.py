import random
import json

# A bat emits ultrasonic sound of frequency 1000 kHz in air. If this sound meets a water surface, what is the wavelength of (a) the reflected sound, (b) the transmitted sound? Speed of sound in air = 340 ms-1 and in water = 1486 ms-1.
# A hospital uses an ultrasonic scanner to locate tumours in a tissue. What is the wavelength of sound in a tissue in which the speed of sound is 1.7 km s-1? The operating frequency of the scanner is 4.2 MHz.

no_of_samples = 30
# no_of_samples = 20

samples = []

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1,3)
    if types == 1:
       speed = random.randint(1000,4000)
       freq = random.randint(1000,6000)
       q = "A hospital uses an ultrasonic scanner to locate tumours in a tissue. What is the wavelength of sound in a tissue in which the speed of sound is "+str(speed)+" kms-1? The operating frequency of the scanner is "+str(freq)+" kHz.?\n"
       input_formula = "Wavelength of tissue = speed of sound in wave/operating frequency of scanner"
       a = speed/(freq*1000)
       a = "{:.2e}".format(a) + " m\n"
       a += "To calculate the wavelength of sound in a tissue, we can use the formula: λ = v / f, where λ is the wavelength, v is the speed of sound, and f is the frequency."
    else:
        freq = random.randint(100000,2100000)
        if types == 2:
            q = "A bat emits ultrasonic sound of frequency "+str(freq)+" Hz in air. If this sound meets a water surface, what is the wavelength of the reflected sound? (Speed of sound in air = 340 ms-1 and in water = 1486 ms-1)\n"
            input_formula = "wavelength of refracted sound = speed of sound in air/frequency of the ultrasonic sound"
            a = "{:.2e}".format(340/freq) + " m\n"
            a += "Given that the speed of sound in air is 340 m/s and the speed of sound in water is 1486 m/s, we can substitute these values into the formula to calculate the wavelength. For the sound emitted in air: λ_air = (340 m/s) / "+str(freq)+" Hz, For the sound reflected in water: λ_water = (1486 m/s) / "+str(freq)+" Hz"
        else:
            q = "A bat emits ultrasonic sound of frequency "+str(freq)+" Hz in air. If this sound meets a water surface, what is the wavelength of the transmitted sound? (Speed of sound in air = 340 ms-1 and in water = 1486 ms-1)\n"
            input_formula = "wavelength of transmitted sound = speed of sound in water/frequency of the ultrasonic sound"
            a = "{:.2e}".format(1486/freq) + " m\n"
            a += "Given that the speed of sound in air is 340 m/s and the speed of sound in water is 1486 m/s, we can substitute these values into the formula to calculate the wavelength. For the sound emitted in air: λ_air = (340 m/s) / "+str(freq)+" Hz, For the sound reflected in water: λ_water = (1486 m/s) / "+str(freq)+" Hz"
    
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
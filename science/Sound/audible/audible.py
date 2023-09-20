import random
import json

# A sound wave travels at a speed of v ms-1, if it's wavelength is lambda m, will the sound wave be audible?

no_of_samples = 20

samples = []

for i in range(no_of_samples):
    sample = {}
    lamb = random.randint(1,50)
    v = (round(random.randint(1,400000)/10,1))*lamb
    ques = "A sound wave travels at a speed of "+str(v)+" m/s, if it's wavelength is "+str(lamb)+" m, will the sound wave be audible ? \n"
    input_formula = "frequency = wave speed / wavelength"
    a = "Whether a sound wave is audible or not depends on its frequency, not its wavelength. Audible sound waves have frequencies within the range of human hearing, which is typically between 20 Hz and 20,000 Hz. To determine if a sound wave is audible, we need to calculate its frequency using the wave speed and wavelength. The formula to calculate the frequency of a sound wave is: f = v / λ, where f is the frequency, v is the wave speed, and λ is the wavelength. Substituting the given values into the formula, we can calculate the frequency of the sound wave: f = "+str(v)+" m/s / "+str(lamb)+" m. Now, we can compare the calculated frequency to the audible frequency range (20 Hz to 20,000 Hz) to determine if the sound wave is audible or not."
    if v/lamb > 20 and v/lamb < 20000:
        answer = "audible\n"
        answer += a
    else:
        answer = "not audible\n" 
        answer += a
    
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

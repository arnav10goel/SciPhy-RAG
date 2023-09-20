import random
import json

# A p watt bulb emits monochromatic yellow light of wavelength w pm. Calculate the rate of emission of quanta per second.

no_of_samples = 10

samples = []

h = 6.6 * (10**-34)
c = 3 * (10**8)

def cal1(p,w) :
   return p*w*(10**-12)/(h*c)

for i in range(no_of_samples):
    sample = {}
    p = random.randint(1,100)
    w = random.randint(1,1000000)
    ques = "A " + str(p) + " watt bulb emits monochromatic yellow light of wavelength " + str(w) + " pm. Calculate the rate of emission of quanta per second.\n"
    input_formula = "Rate of emission per quanta = Power*wavelength/h*c"
    answer = "{:.2e}".format(cal1(p,w)) + "per second\n"
    answer += "To calculate the rate of emission of quanta per second, we need to determine the number of photons emitted per second by the light bulb."
    answer += "The energy of each photon can be calculated using the formula: Energy of each photon = h * c / λ, where h is the Planck constant (approximately 6.626 x 10^-34 J·s), c is the speed of light (approximately 3 x 10^8 m/s), and λ is the wavelength of light in meters."
    answer += "Now, we can calculate the rate of emission of quanta per second using the formula: Rate of emission = Power / Energy of each photon, where Power is the power of the light bulb in watts."

    sample["instruction"] = ques
    sample["input"] = input_formula
    sample["output"] = answer

    samples.append(sample)

# Load existing JSON file
with open("science/StructureofAtom/soa.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/StructureofAtom/soa.json", "w") as file:
    json.dump(existing_data, file, indent=4) 
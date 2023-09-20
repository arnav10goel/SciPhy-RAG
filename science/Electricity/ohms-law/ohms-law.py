import random
import json

samples = []
no_of_samples = 20

def type1():
    I = random.randint(1,1000)
    V = random.randint(100,1100)
    R = str(round(V/I,1)) + " ohm"
    q = "If a "+str(V)+" V battery is connected across an unknown resistor, there is "+str(I)+" A in the circuit, find the value of resistance of the resistor?"
    input_formula = "Resistance = Voltage / Current"
    explanation = "The resistance of the unknown resistor can be calculated using Ohm's law formula, where Resistance = Voltage / Current."
    output = R + "\n\n" + explanation
    return q, input_formula, output

def type2():
    I = random.randint(1,1000)
    R = random.randint(1,1000)
    V = str(I*R) + " volt"
    q = "If a resistance of "+str(R)+" ohm is connected across a battery of unknown voltage, there is "+str(I)+" A in the circuit, find the voltage of the battery?"
    input_formula = "Voltage = Current * Resistance"
    explanation = "The voltage of the battery can be determined using Ohm's law formula, where Voltage = Current * Resistance."
    output = V + "\n\n" + explanation
    return q, input_formula, output

def type3():
    V = random.randint(100,1100)
    R = random.randint(1,1000)
    I = str(round(V/R,1)) + " ampere"
    q = "If a "+str(V)+" V battery is connected across a resistance of "+str(R)+" ohm, then find the current in the circuit?"
    input_formula = "Current = Voltage / Resistance"
    explanation = "The current in the circuit can be calculated using Ohm's law formula, where Current = Voltage / Resistance."
    output = I + "\n\n" + explanation
    return q, input_formula, output

for i in range(no_of_samples):
    types = random.randint(0,2)
    if types == 0:
        ques, input_formula, output = type1()
    if types == 1:
        ques, input_formula, output = type2()
    if types == 2:
        ques, input_formula, output = type3()
    samples.append({
        "instruction": ques,
        "input": input_formula,
        "output": output
    })

# Load existing JSON file
with open("science/Electricity/elec.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/Electricity/elec.json", "w") as file:
    json.dump(existing_data, file, indent=4)

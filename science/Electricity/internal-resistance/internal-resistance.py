import random
import json
from num2words import num2words

samples = []
no_of_samples = 40

def maximum_current(emf, resistance):
    explanation = "The maximum current that can be drawn from a battery can be calculated using Ohm's Law: current = emf / resistance. "
    explanation += "Here, emf is the electromotive force or voltage of the battery and resistance is its internal resistance. "
    return round((emf * 1000) / resistance, 1), explanation

def terminal_voltage(V1, r, V, R):
    explanation = "The terminal voltage of a battery during charging can be calculated using the formula: "
    explanation += "terminal voltage = supply voltage - (current * series resistor). "
    explanation += "Here, V1 is the battery emf, r is the internal resistance, V is the supply voltage, and R is the series resistor. "
    V_dash = V - V1
    I = V_dash / (R + r)
    return round(V - I * R, 1), explanation

def current_or_terminal_voltage(n, V, r, R, is_current):
    explanation = "The current drawn or terminal voltage of a series-connected battery setup can be calculated using the formulas: "
    if is_current:
        explanation += "current drawn = (number of batteries * battery emf) / (series resistor + (number of batteries * internal resistance)). "
    else:
        explanation += "terminal voltage = (number of batteries * battery emf * series resistor) / "
        explanation += "(series resistor + (number of batteries * internal resistance)). "
    explanation += "Here, n is the number of batteries, V is the battery emf, r is the internal resistance, and R is the series resistor. "
    I = (n * V) / (R + n * r * 0.001)
    if is_current:
        return "{:.2e} ampere".format(I), explanation
    else:
        return "{:.2e} volt".format(I * R), explanation

def maximum_current_secondary_cell(emf, resistance):
    explanation = "The maximum current that can be drawn from a secondary cell can be calculated using Ohm's Law: "
    explanation += "current = emf / resistance. Here, emf is the electromotive force or voltage of the cell "
    explanation += "and resistance is its internal resistance. "
    return "{:.2e} ampere".format(emf / resistance), explanation

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1, 13)
    
    if types <= 2:
        E = random.randint(1, 2000)
        r = random.randint(1, 2000)
        q = "The storage battery of a car has an emf of {} V, if the internal resistance of the battery is {} milliohm, what is the maximum current that can be drawn from the battery?\n".format(E, r)
        a, explanation = maximum_current(E, r)
        input_formula = "Maximum current = (emf * 1000) / resistance"
        a = str(a) + "\n\nExplanation: " + explanation
    elif types <= 5:
        V1 = random.randint(1, 20)
        r = random.randint(1, 200)
        V = random.randint(20, 200)
        R = random.randint(1, 30)
        q = "A storage battery of emf {} V and internal resistance of {} milliohm is being charged by a {} V DC supply using a series resistor of {} ohm. What is the terminal voltage of the battery during charging?\n".format(V1, r, V, R)
        a, explanation = terminal_voltage(V1, r, V, R)
        input_formula = "Terminal voltage = supply voltage - (current * series resistor)"
        a = str(a) + "\n\nExplanation: " + explanation
    elif types <= 11:
        n = random.randint(2, 20)
        V = random.randint(1, 20)
        r = random.randint(1, 200)
        R = random.randint(5, 200)
        is_current = types <= 8
        q = num2words(n) + " lead-acid type of secondary cells each of emf {} V and internal resistance of {} milliohm are joined in series to provide a supply to a resistor of {} ohm, what is the ".format(V, R, R)
        if is_current:
            q += "current drawn?\n"
        else:
            q += "terminal voltage?\n"
        a, explanation = current_or_terminal_voltage(n, V, r, R, is_current)
        if is_current:
            input_formula = "Current drawn = (n * V) / (R + n * r * 0.001)"
        else:
            input_formula = "Terminal voltage = (n * V * R) / (R + n * r * 0.001)"
        a = str(a) + "\n\nExplanation: " + explanation
    else:
        E = random.randint(1, 400)
        R = random.randint(1000, 11000)
        q = "A secondary cell after long use has an emf of {} V and large internal resistance of {} ohm. What is the maximum current can be drawn from the cell?\n".format(E, R)
        a, explanation = maximum_current_secondary_cell(E, R)
        input_formula = "Maximum current = emf / resistance"
        a = str(a) + "\n\nExplanation: " + explanation
    
    sample["instruction"] = q
    sample["input"] = input_formula
    sample["output"] = a

    samples.append(sample)

# Load existing JSON file
with open("science/Electricity/elec.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/Electricity/elec.json", "w") as file:
    json.dump(existing_data, file, indent=4)

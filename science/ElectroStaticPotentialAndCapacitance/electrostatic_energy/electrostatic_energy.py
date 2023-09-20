import random
import json

k = 9 * (10**9)

no_of_samples = 20

def cal1(c, v):
    return 0.5 * c * v**2 * (10**(-12))

def cal2(c1, c2, v):
    E = 0.5 * c1 * v**2
    c3 = (c1 * c2) / (c1 + c2)
    E1 = 0.5 * c3 * v**2
    return (E - E1) * (10**(-12))

def generate_question_single_capacitor():
    c = random.randint(1, 2000)
    v = random.randint(1, 2000)
    q = f"A {c} pF capacitor is connected to a {v} V battery. How much electrostatic energy is stored in the capacitor?"
    in_formula = f"0.5 * {c} * {v}^2 * 10^(-12)"
    in_values = f"c = {c} pF, v = {v} V"
    a = "{:.2e}".format(cal1(c, v)) + " joule"
    explanation = f"The electrostatic energy stored in the capacitor can be calculated using the formula:\n\nE = 0.5 * C * V^2\n\nwhere C is the capacitance (in Farads) and V is the voltage (in volts).\n\nSubstituting the given values, we have:\n\nE = 0.5 * {c} pF * {v}^2 * 10^(-12) = {a} joule."
    return q, in_formula, in_values, a, explanation

def generate_question_combined_capacitors():
    c1 = random.randint(1, 200)
    c2 = random.randint(1, 200)
    v = random.randint(1, 200)
    q = f"A {c1} pF capacitor is charged by a {v} V supply. It is then disconnected from the supply and is connected to another uncharged {c2} pF capacitor. How much electrostatic energy is lost in this process?"
    E = 0.5 * c1 * v**2
    c3 = (c1 * c2) / (c1 + c2)
    E1 = 0.5 * c3 * v**2
    a = "{:.2e}".format((E - E1) * (10**(-12))) + " joule"
    in_formula = f"({E} - {E1}) * 10^(-12)"
    in_values = f"c1 = {c1} pF, c2 = {c2} pF, v = {v} V"
    explanation = f"The electrostatic energy lost in the process can be calculated by subtracting the final energy from the initial energy:\n\nE_loss = E_initial - E_final\n\nThe initial energy E_initial can be calculated as 0.5 * C1 * V^2, where C1 is the capacitance of the first capacitor and V is the voltage. The final energy E_final can be calculated as 0.5 * C3 * V^2, where C3 is the equivalent capacitance when the two capacitors are combined.\n\nSubstituting the given values, we have:\n\nE_loss = {E} joule - {E1} joule = E_loss = {a} joule."
    return q, in_formula, in_values, a, explanation

data = []

for i in range(no_of_samples):
    types = random.randint(1, 3)
    if types == 1:
        q, in_formula, in_values, a, explanation = generate_question_single_capacitor()
    else:
        q, in_formula, in_values, a, explanation = generate_question_combined_capacitors()

    data.append({
        "instruction": q,
        "input": f"Formula: {in_formula}\nValues: {in_values}",
        "output": "Answer:" + a + "\n\n" + "Explanation: " +  explanation
    })

# Read the existing JSON file
with open("science/ElectroStaticPotentialAndCapacitance/esp.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/ElectroStaticPotentialAndCapacitance/esp.json", "w") as file:
    json.dump(existing_data, file, indent=4)
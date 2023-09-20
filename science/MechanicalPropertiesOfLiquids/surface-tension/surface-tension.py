import random
import json

no_of_samples = 30

def calculate_surface_tension(weight, length):
    return weight / (2 * length)

def calculate_pressure_and_excess(radius, surface_tension, temperature):
    excess_pressure = (2 * surface_tension) / radius
    total_pressure = 1.01 * (10 ** 5) + excess_pressure
    return excess_pressure, total_pressure

def generate_question_surface_tension(weight, length, includes_weight):
    weight_text = f" (which includes the small weight of the slider)" if includes_weight else ""
    return f"A U-shaped wire is dipped in a soap solution, and removed. A thin soap film formed between the wire and a light slider supports a weight of {weight} x 10^(-3) N{weight_text}. The length of the slider is {length} mm. What is the surface tension of the film?"

def generate_question_pressure(radius, surface_tension, temperature):
    return f"What is the pressure inside a drop of liquid of radius {radius} mm at room temperature? Surface tension of liquid at that temperature ({temperature} K) is {surface_tension} x 10^(-3) Nm^(-1). Also give the excess pressure inside the drop."

samples = []

for i in range(no_of_samples):
    sample = {}
    types = random.randint(0, 3)

    if types < 2:
        length = random.randint(1, 2000)
        weight = random.randint(1, 2000)
        includes_weight = types == 1

        question = generate_question_surface_tension(weight, length, includes_weight)
        surface_tension = calculate_surface_tension(weight, length)
        input_formula = f"surface tension = weight / (2 * length)"
        output = f"The surface tension of the film is {surface_tension:.2f} newton/m."

    else:
        radius = random.randint(1, 20)
        surface_tension = random.randint(1, 2000)
        temperature = random.randint(200, 400)

        question = generate_question_pressure(radius, surface_tension, temperature)
        excess_pressure, total_pressure = calculate_pressure_and_excess(radius, surface_tension, temperature)
        input_formula = f"excess pressure = (2 * surface tension) / radius, total pressure = 1.01 * (10 ** 5) + excess pressure"
        output = f"The excess pressure inside the drop is {excess_pressure:.2f} pascal. The total pressure inside the drop is {total_pressure:.2e} pascal."

    sample["instruction"] = question
    sample["input"] = input_formula
    sample["output"] = output

    samples.append(sample)

# Read the existing JSON file
with open("science/MechanicalPropertiesOfLiquids/mpl.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/MechanicalPropertiesOfLiquids/mpl.json", "w") as file:
    json.dump(existing_data, file, indent=4)

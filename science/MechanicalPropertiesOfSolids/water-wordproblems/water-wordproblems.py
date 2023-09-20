import random
import json

no_of_samples = 40

def calculate_density(depth, surface_density):
    del_v_by_v = depth * 45.8 * (10 ** (-8))
    density = surface_density / (1 - del_v_by_v)
    return density

def calculate_pressure_change(percent, volume):
    bulk_modulus = 2.2 * (10 ** 9)
    pressure_change = (bulk_modulus * percent) / 100
    return pressure_change

def calculate_volume_change(pressure, initial_volume):
    volume_change = (pressure * 10 * initial_volume) / (1.6 * (10 ** 11))
    return volume_change

def generate_question_type1(depth, surface_density):
    input_formula = f"density = surface_density / (1 - depth * 45.8 * 10^(-8))"
    return f"What is the density of water at a depth where pressure is {depth} Pa, given that its density at the surface is {surface_density} kg/m^3?", input_formula

def generate_question_type2(percent, volume):
    input_formula = f"pressure_change = (bulk_modulus * percent) / 100"
    return f"How much should the pressure of {volume} ml of water be changed to compress it by {percent}%, assuming a bulk modulus of elasticity of water to be 2.2 x 10^9 N/m^2?", input_formula

def generate_question_type3(pressure, initial_volume):
    input_formula = f"volume_change = (pressure * 10 * initial_volume) / (1.6 * 10^11)"
    return f"The water pressure at the bottom of the trench is about {pressure} x 10^4 Pa. A steel ball of initial volume {initial_volume} dm^3 is dropped into the ocean and falls to the bottom of the trench. What is the change in the volume of the ball when it reaches the bottom?", input_formula

samples = []

for i in range(no_of_samples):
    types = random.randint(1, 5)

    if types == 1 or types == 4:
        depth = random.randint(500, 10000) * 100
        surface_density = random.randint(950, 1050)
        density = calculate_density(depth, surface_density)
        question, input_formula = generate_question_type1(depth, surface_density)
        output = f"The density of water at a depth of {depth} Pa is approximately {density:.1f} kg/m^3. To calculate the density, we use the formula:\n\n{input_formula}"

    elif types == 2:
        percent = round(random.randint(1, 999) / 10, 1)
        volume = random.randint(1, 10000)
        pressure_change = calculate_pressure_change(percent, volume)
        question, input_formula = generate_question_type2(percent, volume)
        output = f"The pressure of {volume} ml of water needs to be changed by {pressure_change:.1e} Pa to compress it by {percent}%. The formula to calculate the pressure change is:\n\n{input_formula}"

    elif types == 3 or types == 5:
        pressure = random.randint(500, 10000)
        initial_volume = random.randint(1, 1000)
        volume_change = calculate_volume_change(pressure, initial_volume)
        question, input_formula = generate_question_type3(pressure, initial_volume)
        output = f"The change in volume of the steel ball when it reaches the bottom of the trench is approximately {volume_change:.1e} m^3. We can calculate the volume change using the formula:\n\n{input_formula}"

    sample = {
        "instruction": question,
        "input": input_formula,
        "output": output
    }

    samples.append(sample)

# Read the existing JSON file
with open("science/MechanicalPropertiesOfSolids/mps.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/MechanicalPropertiesOfSolids/mps.json", "w") as file:
    json.dump(existing_data, file, indent=4)


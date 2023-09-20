import random
import json

no_of_samples = 20
g = 9.8

def calculate_front_wheel_force(m, d, x):
    return round((m * g * (d - x)) / d, 1)

def calculate_back_wheel_force(m, d, x):
    return round((m * g * x) / d, 1)

def generate_question_type1(m, d, x):
    q = f"A car weighs {m} kg. The distance between its front and back axles is {d} m. Its centre of gravity is {x} m behind the front axle. Determine the force exerted by the level ground on each front wheel and each back wheel."
    front_wheel_force = calculate_front_wheel_force(m, d, x)
    back_wheel_force = calculate_back_wheel_force(m, d, x)
    a = f"{front_wheel_force} newtons and {back_wheel_force} newtons"
    return q, front_wheel_force, back_wheel_force, a

samples = []

for i in range(no_of_samples):
    m = random.randint(1000, 2000)
    x = random.randint(1, 100)
    d = random.randint(x + 1, x + 100)

    question, front_wheel_force,  back_wheel_force, a = generate_question_type1(m, d, x)

    input_formula = "Front Wheel Force = (m * g * (d - x)) / d\nBack Wheel Force = (m * g * x) / d"
    output = f"To calculate the force exerted on the front and back wheels, we use the following formulas:\n\nFront Wheel Force = (m * g * (d - x)) / d\nBack Wheel Force = (m * g * x) / d\n\nWhere,\n- m = Mass of the car\n- g = Acceleration due to gravity\n- d = Distance between front and back axles\n- x = Distance of the car's centre of gravity behind the front axle\n\nSubstituting the given values into the formulas, we find that the force exerted on each front wheel is approximately {front_wheel_force} newtons and the force exerted on each back wheel is approximately {back_wheel_force} newtons."

    sample = {
        "instruction": question,
        "input": input_formula,
        "output": output
    }

    samples.append(sample)


# Load existing JSON file
with open("science/RotationalMotion/rom.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/RotationalMotion/rom.json", "w") as file:
    json.dump(existing_data, file, indent=4)

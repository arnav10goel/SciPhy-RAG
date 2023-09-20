import random
import json

no_of_samples = 30

data = []

for i in range(no_of_samples):
    types = random.randint(1, 2)

    if types == 1:
        acceleration = random.randint(1, 10)
        time = random.randint(20, 30)
        length = random.randint(1, 100)
        speed = random.randint(1, 1000)

        instruction = "Two trains A and B of length " + str(length) + " m each are moving on two parallel tracks with a uniform speed of " + str(speed) + " m/s in the same direction, with A ahead of B. The driver of B decides to overtake A and accelerates by " + str(acceleration) + " m/s². If after " + str(time) + " s, the guard of B just brushes past the driver of A, what was the original distance between them?"

        separation_distance = (1 / 2) * acceleration * (time ** 2)
        original_distance = round(separation_distance - 2 * length, 1)
        input_formulae = "separation distance = (1 / 2) * acceleration * (time ** 2)"
        explanation = "The separation distance between the two trains is the distance covered by the guard of B in the time interval of " + str(time) + " s. The guard of B covers this distance in the time interval of " + str(time) + " s with an acceleration of " + str(acceleration) + " m/s². The original distance between the two trains is the separation distance minus the sum of the lengths of the two trains."

        output = {
            "instruction": instruction,
            "input": input_formulae,
            "output": "acceleration of B is " + str(acceleration) + " m/s², time taken by B to cover the separation distance is " + str(time) + " s, length of each train is " + str(length) + " m, speed of each train is " + str(speed) + " m/s" + f"The original distance between the two trains is {original_distance} m." + "\n\n" + input_formulae + "\n\n" + explanation
        }

    else:
        v1 = random.randint(1, 500)
        v2 = random.randint(v1 + 1, v1 + 100)
        distance = random.randint(1, 100)

        instruction = "On a two-lane road, car A is traveling with a speed of " + str(v1) + " m/s. Two cars B and C approach car A in opposite directions with a speed of " + str(v2) + " m/s each. At a certain instant, when the distance AB is equal to AC, both being " + str(distance) + " km, B decides to overtake A before C does. What minimum acceleration of car B is required to avoid an accident?"

        relative_speed_ac = v1 + v2
        relative_speed_ba = v2 - v1
        time = (distance * 1000) / relative_speed_ac
        minimum_acceleration = (2 * (distance * 1000 - relative_speed_ba * time)) / (time ** 2)
        input_formulae = "relative speed of A with respect to C = v1 + v2, relative speed of B with respect to A = v2 - v1, time taken by C to cover distance AC = distance / relative speed of A with respect to C, minimum acceleration required = (2 * (distance - relative speed of B with respect to A * time)) / (time ** 2)"
        explanation = "\n\n" + "The relative speed of A with respect to C is the sum of the speeds of A and C. The relative speed of B with respect to A is the difference between the speeds of B and A. The time taken by C to cover the distance AC is the distance AC divided by the relative speed of A with respect to C. The minimum acceleration required is the acceleration of B required to cover the distance AB in the time interval of time taken by C to cover the distance AC minus the time taken by B to cover the distance AB."

        output = {
            "instruction": instruction,
            "input": input_formulae,
            "output": "relative speed of A with respect to C is " + str(relative_speed_ac) + " m/s, B with respect to A is " + str(relative_speed_ba) + " m/s, time taken by C to cover distance AC is " + str(round(time, 1)) + " s, minimum acceleration required is " + str(round(minimum_acceleration, 1)) + " m/s²" + "\n\n" + input_formulae + "\n\n" + explanation 
        }

    data.append(output)

# Read the existing JSON file
with open("science/kinematics/kinematics_data.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinematics/kinematics_data.json", "w") as file:
    json.dump(existing_data, file, indent=4)

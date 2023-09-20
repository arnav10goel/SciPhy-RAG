import random
import json
import math

no_of_samples = 50

data = []

for i in range(no_of_samples):
    types = random.randint(1, 3)

    if types == 1:
        length = random.randint(1, 200)
        revolutions = random.randint(20, 220)
        time = random.randint(10, 210)

        instruction = "A stone tied to the end of a string " + str(length) + " cm long is whirled in a horizontal circle with a constant speed. If the stone makes " + str(revolutions) + " revolutions in " + str(time) + " s, what is the magnitude and direction of acceleration of the stone?"

        angular_velocity = 2 * math.pi * (revolutions / time)
        acceleration = (angular_velocity ** 2) * (length / 100)
        input_formulae = "a = v²/r, v = 2πr/T"
        explanation = "The stone is moving in a circular path. So, the centripetal acceleration is towards the centre of the circle."

        output = {
            "instruction": instruction,
            "input": input_formulae,
            "output": f"a = {round(acceleration, 1)} ms-2, towards the centre" + " of the circle" + ", v = " + str(round(angular_velocity, 1)) + " rad/s\n {explanation}}"
        }

    elif types == 2:
        radius = random.randint(20, 2000)
        speed = random.randint(33, 2050)

        instruction = "An aircraft executes a horizontal loop of radius " + str(radius) + " m with a steady speed of " + str(speed) + " m/s. Compare its centripetal acceleration with the acceleration due to gravity."

        acceleration = (speed ** 2) / radius
        gravity = 9.8
        # formula = "a = v²/r, g = 9.8 m/s²"
        input_formulae = "a = v²/r, g = 9.8 m/s²"
        explanation = "The centripetal acceleration is towards the centre of the circle. The acceleration due to gravity is towards the centre of the earth. So, the centripetal acceleration is greater than the acceleration due to gravity."

        output = {
            "instruction": instruction,
            "input": input_formulae,
            "output": f"centripetal acceleration is {round(acceleration, 1)} ms-2, ratio is {round(acceleration / gravity, 1)}" + ", g = " + str(gravity) + " ms-2\n {explanation}"
        }

    else:
        radius = random.randint(10, 200)
        speed = random.randint(10, 200)
        braking_rate = random.randint(10, 200)

        instruction = "A cyclist is riding with a speed of " + str(speed) + " m/s. As he approaches a circular turn on the road of radius " + str(radius) + " m, he applies brakes and reduces his speed at a constant rate of " + str(braking_rate) + " m/s² every second. What is the magnitude and direction of the net acceleration of the cyclist on the circular turn?"

        centripetal_acceleration = (speed ** 2) / radius
        beta = math.degrees(math.atan(centripetal_acceleration / braking_rate))
        net_acceleration = math.sqrt(centripetal_acceleration ** 2 + braking_rate ** 2)
        input_formulae = "a = v²/r, a = √(a² + b²), b = v²/r"
        explanation = "The cyclist is moving in a circular path. So, the centripetal acceleration is towards the centre of the circle. The braking force is opposite to the direction of motion. So, the net acceleration is the vector sum of the centripetal acceleration and the braking acceleration."

        output = {
            "instruction": instruction,
            "input": input_formulae,
            "output": f"magnitude is {round(net_acceleration, 1)} ms-2, {round(beta)} degrees from the -ve direction of velocity" + ", a = " + str(round(centripetal_acceleration, 1)) + " ms-2, b = " + str(round(braking_rate, 1)) + " ms-2\n {explanation}"
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

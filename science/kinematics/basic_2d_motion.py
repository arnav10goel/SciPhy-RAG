import random
import math
import json

no_of_samples = 20

data = []

for i in range(no_of_samples):
    u_x = random.randint(1, 10)
    u_y = random.randint(1, 10)
    a_x = random.randint(1, 10)
    a_y = random.randint(1, 10)

    for i in range(4):
        temp = random.randint(1, 2)
        if temp == 2:
            if i == 0:
                u_x = -u_x
            elif i == 1:
                u_y = -u_y
            elif i == 2:
                a_x = -a_x
            elif i == 3:
                a_y = -a_y

    t = random.randint(1, 100)

    q = "A particle starts from origin at t = 0 s with a velocity of (" + str(u_x) + ") i + (" + str(u_y) + ") j ms-1 and moves in x-y plane with a constant acceleration of (" + str(a_x) + ") i + (" + str(a_y) + ") j ms-2, then "

    types = random.randint(1, 6)

    if types == 1 or types == 2 or types == 6:
        q = q + "what is the speed of the particle at t = " + str(t) + " s"
        v_x = u_x + a_x * t
        v_y = u_y + a_y * t
        v_mag = math.sqrt(v_x ** 2 + v_y ** 2)

        if types == 1:
            q = q + " (in vector notation)"
            a = {
                "instruction": q,
                "input": "v = u + a * t",
                "output": f"v = ({round(v_x, 1)}) i + ({round(v_y, 1)}) j ms-1"
            }

        else:
            a = {
                "instruction": q,
                "input": "v = sqrt(vx^2 + vy^2)",
                "output": f"v = {round(v_mag, 1)} ms-1",
            }

    elif types == 3:
        v_x = u_x + a_x * t
        v_y = u_y + a_y * t
        q = q + "what is the time taken to reach the final velocity of " + str(v_x) + " i + " + str(v_y) + " j ms-1"
        a = {
            "instruction": q,
            "input":  "v = u + a * t",
            "output": f"t = {round(t, 1)} s"
        }

    elif types == 4:
        q = q + "what is the x-coordinate after t = " + str(t) + " s"
        s_x = u_x * t + (1 / 2) * a_x * t * t
        a = {
            "instruction": q,
            "input": "s = ut + (1/2) * a * t^2",
            "output": f"x-coordinate = {round(s_x, 1)} m"
        }

    elif types == 5:
        q = q + "what is the y-coordinate after t = " + str(t) + " s"
        s_y = u_y * t + (1 / 2) * a_y * t * t
        a = {
            "instruction": q,
            "input": "s = ut + (1/2) * a * t^2",
            "output": f"y-coordinate = {round(s_y, 1)} m"
           
        }

    data.append(a)

# Read the existing JSON file
with open("science/kinematics/kinematics_data.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinematics/kinematics_data.json", "w") as file:
    json.dump(existing_data, file, indent=4)

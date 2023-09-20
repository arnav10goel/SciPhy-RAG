import random
import math
import json

no_of_samples = 20

data = []

for i in range(no_of_samples):
    q_type = random.randint(1, 2)
    h = random.randint(500, 1000)

    if q_type == 1:
        time = random.randint(1, 200)
        angle = random.randint(0, 179)

        q = "An aircraft is flying at a height of " + str(h) + " m above the ground. If the angle subtended at a ground observation point by the aircraft positions " + str(time) + " s apart is " + str(angle) + " degrees, what is the speed of the aircraft?"

        dist = 2 * h * math.tan((angle * math.pi) / 360)
        a = {
            "instruction": q,
            "input": "speed = (2 * h * tan(angle)) / time",
            "output": f"The speed of the aircraft is {round(dist / time, 1)} ms-1."
            
        }
    else:
        v1 = random.randint(100, 300)
        v2 = random.randint(v1 + 10, v1 + 300)

        q = "A fighter plane flying horizontally at an altitude of " + str(h) + " m with speed " + str(v1) + " ms-1 passes directly overhead an anti-aircraft gun. At what angle from the vertical should the gun be fired for the shell with muzzle speed " + str(v2) + " ms-1 to hit the plane? At what minimum altitude should the pilot fly the plane to avoid being hit? (Take g = 10 ms-2)?"

        angle = math.asin(v1 / v2) * (180 / math.pi)
        h2 = (v2 ** 2 * (1 - (v1 / v2) ** 2)) / 20
        a = {
            "instruction": q,
            "input": "angle = asin(v1 / v2) * (180 / pi), minimum_altitude = (v2^2 * (1 - (v1 / v2)^2)) / (2 * g)",
            "output": f"The angle from the vertical should be {round(angle, 1)} degrees and the minimum altitude should be {round(h2, 1)} m."
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

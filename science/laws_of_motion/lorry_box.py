import random
import json

no_of_samples = 20

def calculate_acceleration_net(acc, mu, g):
    return acc - mu * g

def calculate_time(distance, a_net):
    return round((2 * distance) / a_net, 1)

def calculate_lorry_distance(acc, time):
    return round(0.5 * acc * time**2, 1)

data = []

for i in range(no_of_samples):
    m = random.randint(1, 200)
    mu = round(random.randint(0, 100) / 100, 2)
    acc = random.randint(1, 20)
    distance = random.randint(1, 20)
    q = f"The rear side of a lorry is open and a box of {m} kg mass is placed {distance} m away from the open end. The coefficient of friction between the box and the surface below it is {mu}. On a straight road, the lorry starts from rest and accelerates with {acc} m/s^2. Will the box move? If yes, at what distance from the starting point does the box fall off the lorry?"
    
    a_net = calculate_acceleration_net(acc, mu, 10)  # Assuming g = 10 m/s^2
    if a_net > 0:
        time = calculate_time(distance, a_net)
        lorry_dist = calculate_lorry_distance(acc, time)
        a = f"Yes, the box moves with {round(a_net, 1)} m/s^2 with respect to the lorry. It takes {round(time, 1)} s to fall off the lorry, and the lorry would have moved {round(lorry_dist, 1)} m by the time the box falls off."
    else:
        a = "No, the box will not move."
    
    data.append({
        "instruction": q,
        "input": "Calculate acceleration net, time, and lorry distance",
        "output": f"{a}"
    })

# Read the existing JSON file
with open("science/laws_of_motion/nlm.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/laws_of_motion/nlm.json", "w") as file:
    json.dump(existing_data, file, indent=4)
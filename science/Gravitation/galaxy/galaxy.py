import random
import json
import math

no_of_samples = 10

def cal1(no_of_stars, distance):
    dist_m = distance * 9.46 * (10 ** 15)
    num = 4 * ((math.pi) ** 2) * (dist_m)
    den = 6.67 * (10 ** (-11)) * (2.5 * (10 ** 11) * (1.989 * (10 ** 30)))
    time = math.sqrt((num / den))
    return "{:.3e}".format(time) + " s"

def generate_question(no_of_stars, distance):
    return f"Let us assume that our galaxy consists of {no_of_stars} * 10^9 stars each of one solar mass. How long will a star at a distance of {distance} ly from the galactic centre take to complete one revolution? Take the diameter of the Milky Way to be 10^5 ly."

samples = []

for i in range(no_of_samples):
    no_of_stars = random.randint(1, 300)
    distance = random.randint(30000, 70000)

    question = generate_question(no_of_stars, distance)
    answer = cal1(no_of_stars, distance)

    sample = {
        "instruction": question,
        "input": f"No. of Stars = {no_of_stars} * 10^9, Distance = {distance} ly",
        "output": answer,
    }

    samples.append(sample)

# Read the existing JSON file
with open("science/Gravitation/g.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/Gravitation/g.json", "w") as file:
    json.dump(existing_data, file, indent=4)

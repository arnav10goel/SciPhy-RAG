import random
import json

no_of_samples = 20

data = []

def generate_question():
    disp = random.randint(1, 500)
    time = random.randint(1, 40)
    distance = random.randint(disp + 1, disp + 200)
    
    q = "A passenger arriving in a new town wishes to go from the station to a hotel located " + str(disp) + " km away on a straight road from the station. A dishonest cab man takes him along a circuitous path " + str(distance) + " km long and reaches the hotel in " + str(time) + " min. What is (a) the average speed of the taxi, (b) the magnitude of average velocity? Are the two equal?"
    avg_speed = round((distance * 100) / (time * 6), 1)
    avg_velocity = round((disp * 100) / (time * 6), 1)
    answer = "The average speed of the taxi is " + str(avg_speed) + " m/s. The magnitude of average velocity is " + str(avg_velocity) + " m/s. The two are not equal."
    input_param = "disp = " + str(disp) + " km, distance = " + str(distance) + " km, time = " + str(time) + " min"
    
    return q, answer, input_param

for i in range(no_of_samples):
    ques, answer, input_param = generate_question()
    data.append({
        "instruction": ques,
        "input": input_param,
        "output": answer
    })

# Read the existing JSON file
with open("science/kinematics/kinematics_data.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinematics/kinematics_data.json", "w") as file:
    json.dump(existing_data, file, indent=4)

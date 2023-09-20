import random
import json

no_of_samples = 20

samples = []

for i in range(no_of_samples):
    q1 = random.randint(1, 200)
    q2 = random.randint(1, 200)
    d = random.randint(1, 200)

    if random.randint(0, 1):
        q1 = -q1
    else:
        q2 = -q2

    q = f"Two charges q1 of {q1} x 10^(-8)C and q2 of {q2} x 10^(-8) are located {d} cm apart. At what point(s) on the line joining the two charges is the electric potential zero (take potential at infinity as zero)?"

    r1 = abs((q1 * d) / (q1 - q2))
    absq1 = abs(q1)
    absq2 = abs(q2)

    if absq1 != absq2:
        r2 = abs((q1 * d) / (q1 + q2))

    a = f"{r1:.2e} cm from q1 between q1 and q2"

    if absq1 == absq2:
        a += "\n"
    elif absq1 > absq2:
        a += f", {r2:.2e} cm from q1 to the right of both charges\n"
    else:
        a += f", {r2:.2e} cm from q1 to the left of both charges\n"

    samples.append({
        "question": q,
        "input": f"Charge q1 : {q1} x 10^(-8) C , Charge q2: {q2} x 10^(-8) C, Distance (d) : {d} cm",
        "output": a + "\nExplanation: To find the point(s) on the line where the electric potential is zero, we can use the formula r = (q1 * d) / (q1 - q2), where r is the distance from q1. If the magnitudes of q1 and q2 are not equal, there will be a second point given by r = (q1 * d) / (q1 + q2). Plugging in the values, we get the point(s) as follows: " + a
    })

# Read the existing JSON file
with open("science/ElectroStaticPotentialAndCapacitance/esp.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/ElectroStaticPotentialAndCapacitance/esp.json", "w") as file:
    json.dump(existing_data, file, indent=4)

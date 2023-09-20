import random
import json

no_of_samples = 50

samples = []

for i in range(no_of_samples):
    q1 = random.randint(1, 20)
    q2 = random.randint(1, 20)
    p = random.randint(1, 20)
    q = random.randint(1, 20)
    r1 = random.randint(1, 20)
    r2 = random.randint(1, 20)
    types1 = random.randint(1, 3)
    types2 = random.randint(1, 3)
    types3 = random.randint(1, 3)
    P = ""
    Q = ""
    R = ""
    if types1 == 1:
        P = "(" + str(p) + " cm, 0, 0)"
    elif types1 == 2:
        P = "(0, " + str(p) + " cm, 0)"
    else:
        P = "(0, 0, " + str(p) + " cm)"
    if types2 == 1:
        Q = "(" + str(q) + " cm, 0, 0)"
    elif types2 == 2:
        Q = "(0, " + str(q) + " cm, 0)"
    else:
        Q = "(0, 0, " + str(q) + " cm)"
    if types3 == 1:
        R = "(0, " + str(r1) + " cm, " + str(r2) + " cm)"
    elif types3 == 2:
        R = "(" + str(r1) + " cm, 0, " + str(r2) + " cm)"
    else:
        R = "(" + str(r1) + " cm, " + str(r2) + " cm, 0)"
    qu = "A charge of " + str(q1) + " mC is located at the origin. Calculate the work done in taking a charge " + str(q2) + " nC from a point P" + P + " to a point Q" + Q + ", via a point R" + R + "."
    a = f"{abs(q1 * q2 * 0.009 * (1 / p - 1 / q)):.2e} joule"

    samples.append({
        "instruction": qu,
        "input": f"Charge at Origin (q1) = {q1} mC + Charge at P (q2) {q2} nC + Coordinates of P: {P} + Coordinates of Q : {Q} + Coordinates of R : {R}",
        "output": a + "\nExplanation: The work done in moving a charge between two points is given by the formula W = q1 * q2 * (Vp - Vq), where q1 and q2 are the charges, and Vp and Vq are the potentials at the respective points. The potential difference (Vp - Vq) is calculated as 0.009 * (1 / p - 1 / q). Plugging in the values, we get W = " + a + "."
    })

    
# Read the existing JSON file
with open("science/ElectroStaticPotentialAndCapacitance/esp.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/ElectroStaticPotentialAndCapacitance/esp.json", "w") as file:
    json.dump(existing_data, file, indent=4)

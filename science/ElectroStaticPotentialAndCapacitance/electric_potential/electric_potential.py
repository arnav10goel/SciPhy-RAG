import random
import json

k = 9 * (10 ** 9)

def cal1(m, r, R):
    return (k * m) / R

def cal2(m, r, R):
    return (k * m) / r

def cal3(m, r):
    return (k * m) / r

def type1():
    q = random.randint(-200, 200)
    r = random.randint(1, 500)
    R = random.randint(r + 1, r + 100)
    v = "{:.2e}".format(cal1(q, r, R)) + " joule/coulomb\n"
    Q = "What is the gravitational potential at a point P at a distance of " + str(r) + " m from the center of the spherical shell of radius " + str(R) + " m and having " + "{:.2e}".format(q) + " C charge distributed uniformly on it.\n"
    I = "To calculate the gravitational potential at a point outside a uniformly charged spherical shell, we use the formula:\n\nV = (k * Q) / R\n\nwhere V is the gravitational potential, k is the electrostatic constant (9 * 10^9 Nm^2/C^2), Q is the charge, and R is the distance from the center of the shell."
    return Q, I, v

def type2():
    q = random.randint(-200, 200)
    R = random.randint(1, 500)
    r = random.randint(R + 1, R + 100)
    v = "{:.2e}".format(cal2(q, r, R)) + " joule/coulomb\n"
    Q = "What is the gravitational potential at a point P at a distance of " + str(r) + " m from the center of the spherical shell of radius " + str(R) + " m and having " + "{:.2e}".format(q) + " C charge distributed uniformly on it.\n"
    I = "To calculate the gravitational potential at a point inside a uniformly charged spherical shell, we use the formula:\n\nV = (k * Q) / r\n\nwhere V is the gravitational potential, k is the electrostatic constant (9 * 10^9 Nm^2/C^2), Q is the charge, and r is the distance from the center of the shell."
    return Q, I, v

def type3():
    q = random.randint(-500, 500)
    R = random.randint(1, 1000)
    v = "{:.2e}".format(cal3(q, R)) + " joule/coulomb\n"
    Q = "What is the gravitational potential at a point P on the surface of the spherical shell of radius " + str(R) + " m and having " + "{:.2e}".format(q) + " C charge distributed uniformly on it.\n"
    I = "To calculate the gravitational potential at a point on the surface of a uniformly charged spherical shell, we use the formula:\n\nV = (k * Q) / r\n\nwhere V is the gravitational potential, k is the electrostatic constant (9 * 10^9 Nm^2/C^2), Q is the charge, and r is the distance from the center of the shell."
    return Q, I, v

def type4():
    q = random.randint(-500, 500)
    R = random.randint(1, 1000)
    v = "{:.2e}".format(cal3(q, R)) + " joule/coulomb\n"
    Q = "What is the gravitational potential at a point P at a distance of " + str(R) + " m from a charge of " + "{:.2e}".format(q) + " C.\n"
    I = "To calculate the gravitational potential at a point due to a single charge, we use the formula:\n\nV = (k * Q) / r\n\nwhere V is the gravitational potential, k is the electrostatic constant (9 * 10^9 Nm^2/C^2), Q is the charge, and r is the distance from the charge."
    return Q, I, v

# Open the existing JSON file and read its contents
with open("science/ElectroStaticPotentialAndCapacitance/esp.json", "r") as file:
    data = json.load(file)

# Generate new questions and answers
new_data = []
no_of_samples = 40
for i in range(no_of_samples):
    types = random.randint(0, 3)
    if types == 0:
        ques, instr, answer = type1()
    elif types == 1:
        ques, instr, answer = type2()
    elif types == 2:
        ques, instr, answer = type3()
    elif types == 3:
        ques, instr, answer = type4()

    # Create a dictionary with the question, input, and output
    entry = {
        "instruction": ques,
        "input": instr,
        "output": answer,
    }

    # Add the entry to the new data list
    new_data.append(entry)

# Extend the existing data with the new data
data.extend(new_data)

# Write the updated data to the JSON file with proper indentation
with open("science/ElectroStaticPotentialAndCapacitance/esp.json", "w") as file:
    json.dump(data, file, indent=4)

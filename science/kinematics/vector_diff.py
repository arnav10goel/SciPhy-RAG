import random
from sympy import *
import json 

no_of_samples = 20

data = []

for i in range(no_of_samples):
    x_num = random.randint(1, 20)
    if random.randint(0, 1):
        x_num = -x_num
    y_num = random.randint(1, 20)
    if random.randint(0, 1):
        y_num = -y_num
    z_num = random.randint(1, 20)
    if random.randint(0, 1):
        z_num = -z_num
    x_pow = random.randint(0, 4)
    y_pow = random.randint(0, 4)
    z_pow = random.randint(0, 4)
    select = random.randint(0, 1)
    qtype = "velocity" if select == 0 else "acceleration"
    t = symbols('t')
    x_exp = x_num * (t ** x_pow)
    y_exp = y_num * (t ** y_pow)
    z_exp = z_num * (t ** z_pow)
    q = f"If the position of the particle is given by r = ({x_exp}) i + ({y_exp}) j + ({z_exp}) k m, where t is in seconds, what is the {qtype} of the particle (in vector notation)?"
    x_der = Derivative(x_exp, t).doit()
    y_der = Derivative(y_exp, t).doit()
    z_der = Derivative(z_exp, t).doit()
    if select == 0:
        a = f"The velocity of the particle is ({x_der}) i + ({y_der}) j + ({z_der}) k m/s."
    else:
        x_der2 = Derivative(x_der, t).doit()
        y_der2 = Derivative(y_der, t).doit()
        z_der2 = Derivative(z_der, t).doit()
        a = f"The acceleration of the particle is ({x_der2}) i + ({y_der2}) j + ({z_der2}) k m/s^2."
    data.append({
        "instruction": q,
        "input": "r = xi + yj + zk, v = dr/dt, a = dv/dt",
        "output": a
    })

# Read the existing JSON file
with open("science/kinematics/kinematics_data.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(data)

# Write the updated data to the JSON file with indentation
with open("science/kinematics/kinematics_data.json", "w") as file:
    json.dump(existing_data, file, indent=4)

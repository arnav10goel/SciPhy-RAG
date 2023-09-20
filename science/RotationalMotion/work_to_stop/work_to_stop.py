import random
import json

# A hoop of radius r m weighs m kg. It rolls along a horizontal floor so that its centre of mass has a speed of v m/s. How much work has to be done to stop it?
# A circular disk of radius 2 m weighs 100 kg. It rolls along a horizontal floor so that its centre of mass has a speed of 20 cm/s. How much work has to be done to stop it?
# A hollow sphere of radius 2 m weighs 100 kg. It rolls along a horizontal floor so that its centre of mass has a speed of 20 cm/s. How much work has to be done to stop it?
# A solid sphere of radius 2 m weighs 100 kg. It rolls along a horizontal floor so that its centre of mass has a speed of 20 cm/s. How much work has to be done to stop it?
# A hollow cylinder of radius 2 m weighs 100 kg. It rolls along a horizontal floor so that its centre of mass has a speed of 20 cm/s. How much work has to be done to stop it?
# A solid cylinder of radius 2 m weighs 100 kg. It rolls along a horizontal floor so that its centre of mass has a speed of 20 cm/s. How much work has to be done to stop it?


no_of_samples = 60
con = [1, 1/2, 2/3, 2/5, 1, 1/2]

def cal1(c, m, r, v) :
    return round(0.5*(c+1)*m*v*v,1) 

def type1() :
    m = random.randint(1,100)
    r = random.randint(1,500)
    v = random.randint(1,40)
    t = random.randint(0,5)
    if t == 0 :
        q = "A hoop of radius " + str(r) + " m weighs " + str(m) + " kg. It rolls along a horizontal floor so that its centre of mass has a speed of " + str(v) + " m/s. How much work has to be done to stop it?\n"
        input_formula = f"0.5*({con[0]}+1)*m*v*v"
        a = str(cal1(con[0], m, r, v)) + " joules\n"
    elif t == 1:
        q = "A circular disk of radius " + str(r) + " m weighs " + str(m) + " kg. It rolls along a horizontal floor so that its centre of mass has a speed of " + str(v) + " m/s. How much work has to be done to stop it?\n"
        input_formula = f"0.5*({con[1]}+1)*m*v*v"
        a = str(cal1(con[1], m, r, v)) + " joules\n"
    elif t == 2:
        q = "A hollow sphere of radius " + str(r) + " m weighs " + str(m) + " kg. It rolls along a horizontal floor so that its centre of mass has a speed of " + str(v) + " m/s. How much work has to be done to stop it?\n"
        input_formula = f"0.5*({con[2]}+1)*m*v*v"
        a = str(cal1(con[2], m, r, v)) + " joules\n"
    elif t == 3:
        q = "A solid sphere of radius " + str(r) + " m weighs " + str(m) + " kg. It rolls along a horizontal floor so that its centre of mass has a speed of " + str(v) + " m/s. How much work has to be done to stop it?\n"
        input_formula = f"0.5*({con[3]}+1)*m*v*v"
        a = str(cal1(con[3], m, r, v)) + " joules\n"
    elif t == 4:
        q = "A hollow cylinder of radius " + str(r) + " m weighs " + str(m) + " kg. It rolls along a horizontal floor so that its centre of mass has a speed of " + str(v) + " m/s. How much work has to be done to stop it?\n"
        input_formula = f"0.5*({con[4]}+1)*m*v*v"
        a = str(cal1(con[4], m, r, v)) + " joules\n"
    elif t == 5:
        q = "A solid cylinder of radius " + str(r) + " m weighs " + str(m) + " kg. It rolls along a horizontal floor so that its centre of mass has a speed of " + str(v) + " m/s. How much work has to be done to stop it?\n"
        input_formula = f"0.5*({con[5]}+1)*m*v*v"
        a = str(cal1(con[0], m, r, v)) + " joules\n"
    return q, input_formula, a

samples = []

for i in range(no_of_samples):
    sample = {}
    ques, i_f, answer = type1()
    sample["instruction"] = ques
    sample["input"] = i_f
    sample["output"] = answer

    samples.append(sample)
    

# Load existing JSON file
with open("science/RotationalMotion/rom.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/RotationalMotion/rom.json", "w") as file:
    json.dump(existing_data, file, indent=4)

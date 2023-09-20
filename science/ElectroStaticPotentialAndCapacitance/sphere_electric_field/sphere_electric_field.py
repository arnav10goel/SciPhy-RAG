import random
import json

no_of_samples = 80

k = 9 * (10**9)

def cal2(m, r, R):
    return (k * m) / (r * r)

def cal3(m, r):
    return (k * m) / (r * r)

def cal4(m, r, R):
    return (k * m * r) / (R ** 3)

def type1():
    q = random.randint(-200, 200) * (10 ** -8)
    r = random.randint(1, 500)
    R = random.randint(r + 1, r + 100)
    v = "0 newton/coulomb"
    Q = f"What is the electric field at a point P at a distance of {r} m from the center of the spherical shell of radius {R} m and having {q:.2e} C charge distributed uniformly on it?"
    input_formula = "Electric Field (E) = 0 N/C"
    output_explanation = "For a spherical shell, the electric field inside the shell is zero."
    return Q, input_formula, v, output_explanation

def type2():
    q = random.randint(-200, 200) * (10 ** -8)
    R = random.randint(1, 500)
    r = random.randint(R + 1, R + 100)
    v = f"{cal2(q, r, R):.2e} newton/coulomb"
    Q = f"What is the electric field at a point P at a distance of {r} m from the center of the spherical shell of radius {R} m and having {q:.2e} C charge distributed uniformly on it?"
    input_formula = f"Electric Field (E) = {cal2.__name__}({q:.2e}, {r}, {R}) N/C"
    output_explanation = f"The electric field due to a uniformly charged spherical shell is given by the formula E = k * Q * r / (R^2), where k is the Coulomb's constant, Q is the charge on the shell, r is the distance from the center of the shell, and R is the radius of the shell. Plugging in the values, we get E = {cal2(q, r, R):.2e} N/C."
    return Q, input_formula, v, output_explanation

def type3():
    q = random.randint(-200, 200) * (10 ** -8)
    R = random.randint(1, 1000)
    v = f"{cal3(q, R):.2e} newton/coulomb"
    Q = f"What is the electric field at a point P on the surface of the spherical shell of radius {R} m and having {q:.2e} C charge distributed uniformly on it?"
    input_formula = f"Electric Field (E) = {cal3.__name__}({q:.2e}, {R}) N/C"
    output_explanation = f"The electric field on the surface of a uniformly charged spherical shell is given by the formula E = k * Q / (R^2), where k is the Coulomb's constant, Q is the charge on the shell, and R is the radius of the shell. Plugging in the values, we get E = {cal3(q, R):.2e} N/C."
    return Q, input_formula, v, output_explanation

def type4():
    q = random.randint(-200, 200) * (10 ** -8)
    r = random.randint(1, 500)
    R = random.randint(r + 1, r + 100)
    v = f"{cal4(q, r, R):.2e} newton/coulomb"
    Q = f"What is the electric field at a point P at a distance of {r} m from the center of the uniform solid sphere of radius {R} m and having {q:.2e} C charge distributed uniformly."
    input_formula = f"Electric Field (E) = {cal4.__name__}({q:.2e}, {r}, {R}) N/C"
    output_explanation = f"The electric field inside a uniformly charged solid sphere is given by the formula E = k * Q * r / (R^3), where k is the Coulomb's constant, Q is the charge on the sphere, r is the distance from the center, and R is the radius of the sphere. Plugging in the values, we get E = {cal4(q, r, R):.2e} N/C."
    return Q, input_formula, v, output_explanation

def type5():
    q = random.randint(-200, 200) * (10 ** -8)
    R = random.randint(1, 500)
    r = random.randint(R + 1, R + 100)
    v = f"{cal2(q, r, R):.2e} newton/coulomb"
    Q = f"What is the electric field at a point P at a distance of {r} m from the center of the uniform solid sphere of radius {R} m and having {q:.2e} C charge distributed uniformly."
    input_formula = f"Electric Field (E) = {cal2.__name__}({q:.2e}, {r}, {R}) N/C"
    output_explanation = f"The electric field inside a uniformly charged solid sphere is given by the formula E = k * Q * r / (R^2), where k is the Coulomb's constant, Q is the charge on the sphere, r is the distance from the center, and R is the radius of the sphere. Plugging in the values, we get E = {cal2(q, r, R):.2e} N/C."
    return Q, input_formula, v, output_explanation

def type6():
    q = random.randint(-200, 200) * (10 ** -8)
    R = random.randint(1, 1000)
    v = f"{cal3(q, R):.2e} newton/coulomb"
    Q = f"What is the electric field at a point P on the surface of the uniform solid sphere of radius {R} m and having {q:.2e} C charge distributed uniformly."
    input_formula = f"Electric Field (E) = {cal3.__name__}({q:.2e}, {R}) N/C"
    output_explanation = f"The electric field on the surface of a uniformly charged solid sphere is given by the formula E = k * Q / (R^2), where k is the Coulomb's constant, Q is the charge on the sphere, and R is the radius of the sphere. Plugging in the values, we get E = {cal3(q, R):.2e} N/C."
    return Q, input_formula, v, output_explanation

def type7():
    q = random.randint(-200, 200) * (10 ** -8)
    R = random.randint(1, 1000)
    v = "0 newton/coulomb"
    Q = f"What is the electric field at the centre of the uniform solid sphere of radius {R} m and having {q:.2e} C charge distributed uniformly."
    input_formula = "Electric Field (E) = 0 N/C"
    output_explanation = "For a uniformly charged solid sphere, the electric field at the center is zero."
    return Q, input_formula, v, output_explanation

samples = []

for i in range(no_of_samples):
    sample = {}
    types = random.randint(0, 5)
    if types == 0:
        types2 = random.randint(0, 1)
        if types2 == 0:
            ques, input_formula, ans, output_explanation = type1()
        else:
            ques, input_formula, ans, output_explanation = type7()
    elif types == 1:
        ques, input_formula, ans, output_explanation = type2()
    elif types == 2:
        ques, input_formula, ans, output_explanation = type3()
    elif types == 3:
        ques, input_formula, ans, output_explanation = type4()
    elif types == 4:
        ques, input_formula, ans, output_explanation = type5()
    elif types == 5:
        ques, input_formula, ans, output_explanation = type6()

    sample["instruction"] = ques
    sample["input"] = input_formula
    sample["output"] = ans + "\n" + output_explanation

    samples.append(sample)

# Read the existing JSON file
with open("science/ElectroStaticPotentialAndCapacitance/esp.json", "r") as file:
    existing_data = json.load(file)

# Extend the existing data with the new generated data
existing_data.extend(samples)

# Write the updated data to the JSON file with indentation
with open("science/ElectroStaticPotentialAndCapacitance/esp.json", "w") as file:
    json.dump(existing_data, file, indent=4)
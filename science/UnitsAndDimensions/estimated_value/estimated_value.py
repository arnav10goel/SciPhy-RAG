import random
import json

# The radius of a sphere is measured as (2.1 +/- 0.5) cm calculate its surface area with error limits
# A force of F_val +/- F_error N is applied over an area of A_val +/- A_error m2. Calculate the pressure exerted over the area.
# Find the value of g using simple pendulum, the following observations were made: length of thread l = l_val +/- l_error cm, time period of oscillation T = t_val +/- t_error s, then value of g in error limits is?

no_of_samples = 40

samples = []

def type1():
    r = round(random.randint(410,30000)/10,1)
    error = round(random.randint(1,300)/10,1)
    q = "The radius of a sphere is measured as "+ str(r)+" +/- "+ str(error) +" cm calculate its surface area (in m2) with error limits.\n"
    input_formula = "Surface Area = 4πr²"
    ans_val = round((4*3.14*r*r)/10000,1)
    error = round(2*((ans_val*error)/r),1)
    a = str(ans_val) + "+/-" + str(error) + "\n"
    a += "To calculate the surface area of a sphere with a measured radius, we use the formula: Surface Area = 4πr². In this case, the radius of the sphere is "+ str(r) +" cm, and the error in the measurement is "+ str(error) +" cm. To determine the error in the surface area calculation, we can use error propagation. The formula for calculating the maximum error in a function involving measured quantities is: Max Error = |dA/dx| * Δx, where Max Error is the maximum error, dA/dx is the derivative of the function with respect to the measured quantity (radius in this case), and Δx is the error in the measured quantity. Taking the derivative of the surface area formula with respect to the radius, we have: dA/dr = 8πr. Substituting the given values into the error propagation formula, we can calculate the maximum error in the surface area: Max Error = |8πr| * Δr. Now, we can substitute the given radius and error values to calculate the maximum error in the surface area."
    return q,input_formula,a

def type2():
    F_val = random.randint(20,400)
    F_error = random.randint(1,10)
    A_val = round(random.randint(20,400)/100,2)
    A_error = round(random.randint(1,10)/100,2)
    q = "A force of "+str(F_val)+" +/- "+str(F_error)+" N is applied over an area of "+str(A_val)+" +/- "+str(A_error)+" m2. Calculate the pressure exerted over the area.\n"
    input_formula = "Pressure = Force/Area"
    ans_val = round(F_val / A_val,2)
    ans_error = round(ans_val*(F_error/F_val+A_error/A_val),2)
    a = str(ans_val) + "+/-" + str(ans_error) + "\n"
    a += "To calculate the pressure exerted over an area, we use the formula: Pressure = Force / Area. In this case, the force applied is "+str(F_val)+" N, and the area is "+str(A_val)+" m². The error in the force measurement is "+str(F_error)+" N, and the error in the area measurement is "+str(A_error)+" m². To determine the error in the pressure calculation, we can use error propagation. The formula for calculating the maximum error in a function involving measured quantities is: Max Error = |dP/dx| * Δx, where Max Error is the maximum error, dP/dx is the derivative of the function with respect to the measured quantity (force or area), and Δx is the error in the measured quantity. Taking the derivative of the pressure formula with respect to force and area, we have: dP/dF = 1 / A, dP/dA = -F / A². Substituting the given values into the error propagation formula, we can calculate the maximum error in the pressure: Max Error = |(1 / A_val) * F_error| + |(-F_val / A_val²) * A_error|. Now, we can substitute the given values to calculate the pressure and its maximum error over the given area."
    return q,input_formula,a

def type3():
    l_val = random.randint(20,400)
    l_error = random.randint(1,10)
    t_val = round(random.randint(20,400)/100,2)
    t_error = round(random.randint(1,10)/100,2)
    q = "Find the value of g using simple pendulum, the following observations were made: length of thread l = "+str(l_val)+" +/- "+str(l_error)+" cm, time period of oscillation T = "+str(t_val)+" +/- "+str(t_error)+" s, then value of g in error limits is?\n"
    input_formula = "g = (4π²l) / T²"
    ans_val = round(4*3.14*3.14*(l_val/(t_val*t_val)),2)
    ans_error = round(ans_val*(l_error/l_val+2*(t_error/t_val)),2)
    a = str(ans_val) + "+/-" + str(ans_error) + "\n"
    a += "To find the value of acceleration due to gravity (g) using a simple pendulum, we can use the formula: g = (4π²l) / T², where l is the length of the pendulum and T is the time period of oscillation. In this case, the length of the pendulum is "+str(l_val)+" cm, and the time period of oscillation is "+str(t_val)+" s. The error in the length measurement is "+str(l_error)+" cm, and the error in the time period measurement is "+str(t_error)+" s. To determine the error in the calculated value of g, we can use error propagation. The formula for calculating the maximum error in a function involving measured quantities is: Max Error = |dg/dx| * Δx, where Max Error is the maximum error, dg/dx is the derivative of the function with respect to the measured quantity (length or time period), and Δx is the error in the measured quantity. Taking the derivatives of the g formula with respect to length and time period, we have: dg/dl = (4π²) / T², dg/dT = -(8π²l) / T³. Substituting the given values into the error propagation formula, we can calculate the maximum error in the value of g: Max Error = |(4π² / T_val²) * l_error| + |(-(8π²l_val) / T_val³) * t_error. Now, we can substitute the given values to calculate the value of g and its maximum error within the error limits of length and time period."
    return q,input_formula,a

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1,3)
    if types == 1:
        ques,input_formula,answer = type1()
    elif types == 2:
        ques,input_formula,answer = type2()
    elif types == 3:
        ques,input_formula,answer = type3()

    sample["instruction"] = ques
    sample["input"] = input_formula
    sample["output"] = answer

    samples.append(sample)

# Load existing JSON file
with open("science/UnitsAndDimensions/uad.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/UnitsAndDimensions/uad.json", "w") as file:
    json.dump(existing_data, file, indent=4)     
    

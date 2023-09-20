import random
import json

# If a physical quantity P=(a^1)*(b^2)*(c^3), the percentage errors of measurement in a,b,c are pa,pb,pc respectively. If the calculated value of P is act_p then what is maximum error possible.

no_of_samples = 20
# no_of_samples = 10

samples = []

for i in range(no_of_samples):
    sample = {}
    pow_a = round(random.randint(-6,6)/2,1)
    pow_b = round(random.randint(-6,6)/2,1)
    pow_c = round(random.randint(-6,6)/2,1)
    error_a = random.randint(1,5)
    error_b = random.randint(1,5)
    error_c = random.randint(1,5)
    value = random.randint(1,40)
    expr = '(a^'+str(pow_a)+')*(b^'+str(pow_b)+')*(c^'+str(pow_c)+')'
    ques = "If a physical quantity P="+expr+", the percentage errors of measurement in a,b,c are "+str(error_a)+"%,"+str(error_b)+"%,"+str(error_c)+"% respectively. If the calculated value of P is "+str(value)+" then what is maximum error possible.\n"
    input_formula = "Percentage Error in P = |dP/P| * 100"
    answer = str(round(((abs(pow_a)*error_a+abs(pow_b)*error_b+abs(pow_c)*error_c)*value)/100,2)) + '\n'
    answer += "To find the maximum possible error in the calculated value of P, we can use the concept of percentage error propagation. The formula to calculate the percentage error in a quantity calculated from measured quantities is given by: Percentage Error in P = |dP/P| * 100, where dP is the maximum absolute error in P. Since P = "+expr+", we can differentiate the expression with respect to each measured quantity (a, b, c) to find the maximum absolute error for each term. Then we can substitute the given percentage errors and calculated value of P to find the maximum error. Let's calculate the maximum error using the given information."

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
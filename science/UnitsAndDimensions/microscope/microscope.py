import random
import json

# A student measures the thickness of human hair using a microscope of magnification 100. He makes 20 observations and average width obtained in the field of view of microscope is 3.5 mm. What is the estimate on the thickness of hair?
# A student measures the thickness of human hair by magnifying it using a microscope. He makes 20 observations and average width obtained in the field of view of microscope is 3.5 mm. If the estimate on the thickness of hair is x mm, then what is its magnification?

no_of_samples = 20

samples = []

def type1():
    magnification = random.randint(100,200)
    num_observations = random.randint(1,500)
    avg_val = round(random.randint(100,400) / 100,2)
    ques = "A student measures thickness of human hair using a microscope of magnification "+str(magnification)+". He makes "+str(num_observations)+" observations and average width obtained in the field of view of microscope is "+str(avg_val)+" mm. What is the estimate on the thickness of hair?\n"
    input_formula = "Thickness of hair = Average width in the field of view / Magnification"
    answer = str(round(avg_val/magnification,4)) + " mm\n"
    answer += "To estimate the thickness of a human hair based on the given observations, we can use the following calculation: Thickness of hair = Average width in the field of view / Magnification. In this case, the magnification of the microscope is "+str(magnification)+" and the average width obtained in the field of view is "+str(avg_val)+" mm. Substituting these values into the formula, we have: Thickness of hair = "+str(avg_val)+" mm / "+str(magnification)+". Calculating this expression will give us the estimate of the thickness of the human hair based on the given observations."
    return ques,input_formula,answer

def type2():
    num_observations = random.randint(1,500)
    avg_val = round(random.randint(100,400) / 100,2)
    real_val = round(random.randint(100,200)*avg_val,2)
    ques = "A student measures the thickness of human hair by magnifying it using a microscope. He makes "+str(num_observations)+" observations and average width obtained in the field of view of microscope is "+str(avg_val)+" mm. If the estimate on the thickness of hair is "+str(real_val)+" mm, then what is its magnification?"
    input_formula = "Magnification = Average width in the field of view / Thickness of hair"
    answer = str(avg_val//real_val) + "\n"
    answer += "To find the magnification of the microscope used to measure the thickness of a human hair, we can rearrange the formula: Magnification = Average width in the field of view / Thickness of hair. In this case, the average width obtained in the field of view is "+str(avg_val)+" mm, and the estimate of the thickness of the hair is "+str(real_val)+" mm. Substituting these values into the formula, we have: Magnification = "+str(avg_val)+" mm / "+str(real_val)+" mm. Calculating this expression will give us the magnification of the microscope used to measure the thickness of the human hair based on the given observations and estimate."
    return ques,input_formula,answer

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1,2)
    if types == 1:
        ques,input_formula,answer = type1()
    else:
        ques,input_formula,answer = type2()
    
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
import random
import json

# The far point of a myopic person is x mm in front of the eye. What is the nature and power of the lens required to correct the problem.
# The near point of a hypermetropic person is x mm. What is the nature and power of the lens required to correct the problem(assume normal near point of eye is 25cm).
# A person with a myopic eye cannot see objects beyond x mm distinctly. What should be the type of the corrective lens used to restore proper vision?
# A person with a hypermetropic eye cannot see objects within x mm distinctly. What should be the type of the corrective lens used to restore proper vision?
# A person needs a lens of power – D dioptres for correcting his distant vision. What is the focal length of the lens required for correcting distant vision?
# A person needs a lens of power + D dioptres for correcting his near vision. What is the focal length of the lens required for correcting near vision?


no_of_samples = 60
near_point = 250

samples = []

def calculation_near(far):
    return round(1000/far,2)

def calculation_far(near):
    return round(((near-near_point)*1000)/(near_point*near),2)

def type1():
    far = random.randint(500,100000)
    q = "The far point of a myopic person is "+str(far)+" mm in front of the eye. What is the nature and power of the lens required to correct the problem.\n"
    input_formula = "1/f = 1/v-1/u"
    a = "the remedial lens should make the objects at infinity appear at far point, hence u = infinity, v = far point of defected eye, from P=1/f, 1/f=1/v-1/u, we get P=1/v-1/u, P=1/v-0=1/v, implies P = "+str(calculation_near(far)) + " diatrope, type of lens required is concave.\n"
    return q,input_formula,a

def type2():
    near = random.randint(500,100000)
    q = "The near point of a hypermetropic person is "+str(near)+" mm. What is the nature and power of the lens required to correct the problem(assume normal near point of eye is 25cm).\n"
    input_formula = "1/f=1/v-1/u"
    a = "the remedial lens should make the objects at defected eye's near point appear at normal eye's near point, hence u = 25cm, v = near point of defected eye, from P=1/f, 1/f=1/v-1/u, we get P=1/v-1/u, P=1/v-(1/-0.25)=1/v+1/0.25, implies P = "+str(calculation_far(near))+" diatrope, type of lens required is convex\n"
    return q,input_formula,a

def type11():
    far = random.randint(500,100000)
    q = "A person with a myopic eye cannot see objects beyond "+str(far)+" mm distinctly. What should be the type of the corrective lens used to restore proper vision?\n"
    input_formula = "1/f=1/v-1/u"
    a = "the remedial lens should make the objects at infinity appear at far point, hence u = infinity, v = far point of defected eye, from P=1/f, 1/f=1/v-1/u, we get P=1/v-1/u, P=1/v-0=1/v, implies P = "+str(calculation_near(far)) + " diatrope, type of lens required is concave.\n"
    return q,input_formula,a

def type21():
    near = random.randint(500,100000)
    q = "A person with a hypermetropic eye cannot see objects within "+str(near)+" mm distinctly. What should be the type of the corrective lens used to restore proper vision?\n"
    input_formula = "1/f=1/v-1/u"
    a = "the remedial lens should make the objects at defected eye's near point appear at normal eye's near point, hence u = 25cm, v = near point of defected eye, from P=1/f, 1/f=1/v-1/u, we get P=1/v-1/u, P=1/v-(1/-0.25)=1/v+1/0.25, implies P = "+str(calculation_far(near))+" diatrope, type of lens required is convex\n"
    return q,input_formula,a

def type3():
    D = random.randint(500,100000)
    q = "A person needs a lens of power -"+str(D)+" dioptres for correcting his distant vision. What is the focal length of the lens required for correcting distant vision?\n"
    input_formula = "Power = 1/focal length (f)"
    a = "we know that power(P)=1/f, hence f=1/P, f(in mm)=1000/P, hence f="+str(calculation_near(D)) + " mm\n"
    return q,input_formula,a

def type4():
    D = random.randint(500,100000)
    q = "A person needs a lens of power + "+str(D)+" dioptres for correcting his near vision. What is the focal length of the lens required for correcting near vision?\n"
    input_formula = "Power = 1/focal length (f)"
    a = "we know that power(P)=1/f, hence f=1/P, f(in mm)=1000/P, hence f="+str(calculation_near(D)) + " mm\n"
    return q,input_formula,a

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1,6)
    if types == 1:
        ques, i_f, answer = type1()
    elif types == 2:
        ques, i_f, answer = type2()
    elif types == 3:
        ques,i_f, answer = type3()
    elif types == 4:
        ques, i_f, answer = type4()
    elif types == 5:
        ques, i_f, answer = type11()
    elif types == 6:
        ques, i_f, answer = type21()

    sample["instruction"] = ques
    sample["input"] = i_f
    sample["output"] = answer

    samples.append(sample)
    
# Load existing JSON file
with open("science/HumanEyeAndColorfulWorld/hecw.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open("science/HumanEyeAndColorfulWorld/hecw.json", "w") as file:
    json.dump(existing_data, file, indent=4)  
import random
import json

# A capacitor with air between it's parallel plates has a capacitance of 8 pF. What will be the capacitance if the distance between the plates is reduced by half, and the space between them is filled with a substance of dielectric constant 6?
# A capacitor with air between it's parallel plates, each plate has an area of 6 x 10^(-3) m2 and the distance between the plates is 3 mm. Calculate the capacitance of the capacitor?
# A capacitor with air between it's parallel plates, each plate has an area of 6 x 10^(-3) m2 and the distance between the plates is 3 mm, if this capacitor is connected to a 100 V supply, find charge on each plate of the capacitor?
# A capacitor with air between it's parallel plates, each plate has an area of 6 x 10^(-3) m2 and the distance between the plates is 3 mm, if this capacitor is connected to a 100 V supply and a 3 mm thick mica sheet is inserted between the plates, then what will happen?
# A capacitor with air between it's parallel plates, each plate has an area of 6 x 10^(-3) m2 and the distance between the plates is 3 mm, if this capacitor is connected to a 100 V supply and a 3 mm thick mica sheet is inserted between the plates and then supply is disconnected, then what will happen?

no_of_samples = 60
# no_of_samples = 30
samples = []
for i in range(no_of_samples):
    sample = {}
    types = random.randint(1,5)
    if types == 1:
        c = random.randint(1,2000)
        dist_ratio = random.randint(1,10)
        dielectric = random.randint(1,200)
        q = "A capacitor with air between it's parallel plates has a capacitance of "+str(c)+" pF. What will be the capacitance if the distance between the plates is reduced to 1/"+str(dist_ratio)+", and the space between them is filled with a substance of dielectric constant "+str(dielectric)+"?\n"
        i_f = "C' = K * C * (1 / d)"
        a = "{:.3e}".format(c*dist_ratio*dielectric)+" pico-farad\n"
        a += "\n\n Explanation: When the distance between the plates of a capacitor is reduced to 1/d, and a dielectric substance with a dielectric constant K is inserted between the plates, the new capacitance C' can be calculated by multiplying the original capacitance C by the dielectric constant K and dividing it by the reduced distance 1/d. This formula accounts for the change in capacitance due to the change in distance and the presence of the dielectric material."
    elif types == 2:
        A = round(random.randint(1,2000)/10000,4)
        d = random.randint(1,2000)
        q = "A capacitor with air between it's parallel plates, each plate has an area of "+str(A)+" m2 and the distance between the plates is "+str(d)+" mm. Calculate the capacitance of the capacitor?\n"
        i_f = "C = (ε₀ * A) / d"
        a = "{:.2e}".format((8.854*A)/(d*0.001))+" pico-farad\n"
        a += "\n\n Explanation: To calculate the capacitance C of a capacitor with air between its parallel plates, we use the formula above. In the formula, ε₀ represents the permittivity of free space, A represents the area of each plate, and d represents the distance between the plates. By multiplying the permittivity of free space by the plate area and dividing it by the plate separation, we can determine the capacitance of the capacitor"
    elif types == 3:
        A = round(random.randint(1,2000)/10000,4)
        d = random.randint(1,50)
        V = random.randint(1,800)
        q = "A capacitor with air between it's parallel plates, each plate has an area of "+str(A)+" m2 and the distance between the plates is "+str(d)+" mm, if this capacitor is connected to a "+str(V)+" V supply, find charge on each plate of the capacitor?\n"
        i_f = "Q = C * V"
        a = "{:.2e}".format((8.854*A*V*(10**(-12)))/(d*0.001)) + " coulomb\n"
        a += "\n\nExplanation:To find the charge Q on each plate of a capacitor connected to a voltage supply, we use the formula above. In the formula, Q represents the charge, C represents the capacitance of the capacitor, and V represents the voltage applied across the capacitor. By multiplying the capacitance of the capacitor by the applied voltage, we can determine the charge on each plate."
    elif types == 4:
        A = round(random.randint(1,2000)/10000,4)
        d = random.randint(1,50)
        V = random.randint(1,800)
        q = "A capacitor with air between it's parallel plates, each plate has an area of "+str(A)+" m2 and the distance between the plates is "+str(d)+" mm, if this capacitor is connected to a "+str(V)+" V supply and a "+str(d)+" mm thick mica sheet is inserted between the plates, then what will happen?\n"
        c1 = (8.854*A*6)/(d*0.001)
        q1 = (8.854*A*6*V*(10**(-12)))/(d*0.001)
        i_f= '''
# Formula to calculate the capacitance of a parallel-plate capacitor
capacitance = (8.854 * 10**-12 * epsilon_r * A) / d

# Formula to calculate the electric field between the plates of a capacitor
electric_field = V / d

# Formula to calculate the capacitance of the capacitor with the mica sheet
capacitance_with_mica = (8.854 * 10**-12 * epsilon_r_mica * A) / (2 * d)
'''
        a = "capacitance becomes {:.2e}".format(c1) + " pico-farad, "+"charge becomes {:.2e}".format(q1)+" coulomb\n"
        a += "\n\nExplanation: The capacitance of a parallel-plate capacitor depends on the area of the plates (A) and the distance between them (d). The formula to calculate the capacitance is C = (8.854 * 10**-12 * epsilon_r * A) / d, where epsilon_r is the relative permittivity of the medium between the plates (air in this case). The electric field between the plates of a capacitor is determined by the potential difference (V) applied across the plates and the distance between them (d). The formula to calculate the electric field is E = V / d. When a mica sheet is inserted between the plates, the distance between the plates is effectively reduced to half (2 * d). The capacitance with the mica sheet can be calculated using the same formula as before, but with the relative permittivity of mica (epsilon_r_mica). To summarize, inserting a mica sheet between the plates of the capacitor will decrease the distance between the plates, resulting in an increased capacitance compared to the air-filled capacitor. The electric field between the plates will remain the same, as it depends on the potential difference and the original distance between the plates." 

    elif types == 5:
        A = round(random.randint(1,2000)/10000,4)
        d = random.randint(1,50)
        V = random.randint(1,800)
        q = "A capacitor with air between it's parallel plates, each plate has an area of "+str(A)+" m2 and the distance between the plates is "+str(d)+" mm, if this capacitor is connected to a "+str(V)+" V supply and a "+str(d)+" mm thick mica sheet is inserted between the plates and then supply is disconnected, then what will happen?\n"
        c1 = (8.854*A*6)/(d*0.001)
        q1 = (8.854*A*V*(10**(-12)))/(d*0.001)
        i_f = "C' = εr * C"
        a = "capacitance becomes {:.2e}".format(c1) + " pico-farad, "+"charge remains {:.2e}".format(q1)+" coulomb\n"
        a += "\nWhen a dielectric substance such as a mica sheet is inserted between the plates of a capacitor, the capacitance of the capacitor increases according to the formula above. In the formula, C' represents the new capacitance with the dielectric substance, εr represents the relative permittivity or dielectric constant of the material, and C represents the original capacitance without the dielectric substance. The relative permittivity of the dielectric material represents how much the electric field is intensified within the dielectric compared to free space. \n\nIn the given question, if a capacitor with air between its parallel plates, each plate having an area of A m² and a distance of d mm, is connected to a V V supply and a d mm thick mica sheet is inserted between the plates, the capacitance C' of the capacitor will change according to the formula mentioned above"
    sample['instruction'] = q
    sample['input'] = i_f
    sample['output'] = a
    samples.append(sample)

# Load existing JSON file
with open("science/ElectroStaticPotentialAndCapacitance/esp.json", "r") as file:
    existing_data = json.load(file)

# Append new samples to existing data
existing_data.extend(samples)

# Save the updated JSON data
with open("science/ElectroStaticPotentialAndCapacitance/esp.json", "w") as file:
    json.dump(existing_data, file, indent=4)

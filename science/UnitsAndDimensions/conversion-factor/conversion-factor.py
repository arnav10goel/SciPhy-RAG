import random
import json

# The volume of a cube of side 1 cm is equal to ..... m3.
# The surface area of a solid cylinder of radius 2.0 cm and height 10.0 cm is equal to ……..(mm)2.
# A vehicle moving with a speed of 18 km h-1 covers ………. m in 1 s.
# The relative density of lead is 11.3. Its density is …….. g cm-3 or ………. kg m-3.

no_of_samples = 70

samples = []

def type1():
    volume = round(random.randint(1,2000000)/1000,3)
    q = "What is the side of a cube of volume "+str(volume)+" cm3 (in m).\n"
    input_formula = "Volume = side^3"
    a = str(round((volume**(1/3))*1000000)) + "\n"
    a += "Cube of the side is it's volume."
    return q,input_formula,a

def type2():
    speed = random.randint(1,1000)
    time = random.randint(1,1000)
    q = "An object moving with a speed of "+str(speed)+" kmph covers x m in "+str(time)+" s, then find the value of x?\n"
    input_formula = "Distance = Speed*Time"
    a = str(round(speed*time*(5/18),1)) +"\n"
    a += "Distance = Speed*Time"
    return q,input_formula,a

def type3():
    speed = random.randint(1,1000)
    time = random.randint(1,1000)
    q = "An object moving with a speed of "+str(speed)+" ms-1 covers x km in "+str(time)+" hr, then find the value of x?\n"
    input_formula = "(Speed in km/h)*5/18 = Speed in m/s"
    a = str(round(speed*time*(18/5),1)) +"\n"
    a += "Use the basic conversion and multiple speed in km/5 by 5/18 to get speed in m/s."
    return q,input_formula,a

def type4():
    density = round(random.randint(1,1000000)/100,2)
    q = "The relative density of a substance is "+str(density)+". Its density is x g cm-3 or y kg m-3, then find the value of x,y?\n"
    input_formula = "1 g/cm^3 = 1000 kg/m^3"
    a = "x = " + str(round(density,2))+", y = "+str(round(density*1000,2)) +"\n"
    a += "To convert the relative density of a substance to its density in different units, we can use the following conversions: 1 g/cm³ = 1000 kg/m³. Given that the relative density of the substance is "+str(density)+", we can find the values of x and y as follows: x = density * 1 g/cm³, y = density * 1000 kg/m³. Substituting the value of the relative density into these formulas will give us the density in grams per cubic centimeter (x) and kilograms per cubic meter (y)."
    return q,input_formula,a

def type5():
    radius = random.randint(1,1000)
    height = random.randint(1,1000)
    q = "The surface area of a solid cylinder of radius "+str(radius)+" cm and height "+str(height)+" cm is equal to (in mm2).\n"
    input_formula = "Surface Area = 2πrh + 2πr²"
    a = str(round(628*radius*(height+radius))) + "\n"
    a += "In this case, the radius of the cylinder is "+str(radius)+" cm and the height of the cylinder is "+str(height)+" cm. Substituting these values into the formula, we can calculate the surface area of the solid cylinder: Surface Area = 2π(" + str(radius) + " cm)(" + str(height) + " cm) + 2π(" + str(radius) + " cm)². Calculating this expression will give us the surface area of the solid cylinder in square centimeters (cm²). To convert the surface area to square millimeters (mm²), we multiply the calculated value by 100 (since 1 cm² = 100 mm²): Surface Area (in mm²) = Surface Area (in cm²) * 100. Calculating this expression will give us the surface area of the solid cylinder in square millimeters (mm²)."
    return q,input_formula,a

def type6():
    density = round(random.randint(1000,1010000)/100,2)
    q = "The density of a substance is "+str(density)+" kg m-3, then find relative density?\n"
    input_formula = "Relative Density = Density of Substance / Density of Water"
    a = str(round(density/1000,3)) + "\n"
    a += "The relative density of a substance is calculated by comparing its density to the density of water. The density of water is typically around 1000 kg/m³. To find the relative density, we can divide the density of the substance by the density of water: Relative Density = Density of Substance / Density of Water. Given that the density of the substance is "+str(density)+" kg/m³, we can calculate the relative density as: Relative Density = "+str(density)+" kg/m³ / 1000 kg/m³"
    return q,input_formula,a

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1,9)
    if types == 1 or types == 2 or types == 3:
        ques,input_formula,answer = type1()
    elif types == 4:
        ques,input_formula,answer = type2()
    elif types == 5:
        ques,input_formula,answer = type3()
    elif types == 6:
        ques,input_formula,answer = type4()
    elif types == 7 or types == 9:
        ques,input_formula,answer = type5()
    elif types == 8:
        ques,input_formula,answer = type6()
    
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

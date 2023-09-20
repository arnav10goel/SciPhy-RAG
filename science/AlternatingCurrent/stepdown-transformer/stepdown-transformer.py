import random
import math
import json

samples = []
no_of_samples = 20

for i in range(no_of_samples):
    sample = {}
    types = random.randint(1, 4)

    if types == 1:
        V = random.randint(220, 240)
        turns = random.randint(10, 500)
        scale = random.randint(10, 500)
        q = "A power transformer line feeds input power at {} V to a stepdown transformer with its primary windings having {} turns. What should be the number of turns in the secondary in order to get output at {} V?".format(
            scale * V, turns * scale, V)
        input_formula = "N_secondary = (N_primary * V_primary) / V_secondary"
        a = "{} turns".format(turns)
    else:
        demand = random.randint(50, 100) * 10
        distance = random.randint(10, 30)
        resistance_drop = round(random.randint(10, 90) / 100, 2)
        bigger_voltage = random.randint(300, 500) * 10
        q = "A small town with a demand of {} kW of electric power at 220 V is situated {} km away from an electric plant generating power at 440 V. The resistance of each of the two wires carrying power is {} ohm per km. The town gets power from the line through {} - 220 V step down transformer at a sub-station in the town.".format(
            demand, distance, resistance_drop, bigger_voltage)
        input_formula = ""
        a = ""

        I = (demand * 1000) / bigger_voltage

        if types == 2:
            q += " Estimate the power loss in the form of heat?"
            input_formula += "Power_loss = I^2 * R * 2 * distance"
            power_loss = I * I * resistance_drop * distance * 2
            a = "{:.2e} watt".format(power_loss)
        elif types == 3:
            q += " How much power does the plant supply, assuming there is negligible power loss due to leakage?"
            input_formula += "Total_power_supplied = Power_loss + Demand_power\n" + "Power_loss = I^2 * R * 2 * distance"
            power_loss = I * I * resistance_drop * distance * 2
            a = "{:.2e} watt".format(power_loss + demand * 1000)
        else:
            q += " Characterize the step-up transformer at the plant."
            input_formula += "Voltage_Drop = I * resistance_drop * 2 * distance\n"+"Step_up_transformer_rating = Bigger_voltage - Voltage_drop"
            voltage_drop = I * resistance_drop * 2 * distance
            a = "rating is 440 volt -- {:.2e} volt".format(bigger_voltage + voltage_drop)

    sample["instruction"] = q
    sample["input"] = input_formula
    sample["output"] = a

    samples.append(sample)

# Load existing JSON data
json_file_path = "science/AlternatingCurrent/ac.json"
existing_data = []

try:
    with open(json_file_path, "r") as file:
        existing_data = json.load(file)
except FileNotFoundError:
    pass

# Append new samples to existing data
existing_data.extend(samples)

# Save updated samples to the JSON file with indentation
with open(json_file_path, "w") as file:
    json.dump(existing_data, file, indent=4)

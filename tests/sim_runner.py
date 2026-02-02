import csv
import json
import os 
import random

with open("scenarios/nominal_climb.json", "r") as f:
    scenario = json.load(f)

#grabbing and setting up variables from the json dict
altitude_ft = scenario["initial"]["altitude_ft"]
target_altitude_ft = scenario["initial"]["targets"]["altitude_ft"]
duration_s = scenario["sim"]["duration_s"]
dt_s = scenario["sim"]["dt_s"]
ground_speed_kts = scenario["initial"]["ground_speed_kts"]
scenario_id = scenario["meta"]["id"]
baro_valid = scenario["initial"]["sensors"]["baro"]["valid"]
baro_sigma = scenario["initial"]["sensors"]["baro"]["noise_sigma_ft"]
gps_valid = scenario["initial"]["sensors"]["gps"]["valid"]
gps_sigma = scenario["initial"]["sensors"]["gps"]["noise_sigma_m"]
events = scenario["events"]


time_s = 0.0
gps_sigma_ft = gps_sigma * 3.28084
climb_rate = 500 #ft/min
climb_rate_sec = climb_rate / 60
rows =[]
time_s_check = False



events_sorted = sorted(events, key=lambda e: e["time_s"])
next_event_idx = 0
for e in events_sorted:
    print(e["time_s"], e["type"])

while next_event_idx < len(events_sorted) and events_sorted[next_event_idx]["time_s"] <= time_s

while time_s <= duration_s:
    time_s += dt_s
    altitude_ft += climb_rate_sec * dt_s

    if altitude_ft > target_altitude_ft:
        altitude_ft = target_altitude_ft
    if baro_valid:
        baro_altitude_ft = altitude_ft + random.gauss(0, baro_sigma)
    else: 
        baro_altitude_ft = None 
    if gps_valid:
        gps_altitude_ft = altitude_ft + random.gauss(0, gps_sigma_ft)
    else: 
        gps_altitude_ft = None 

    row_dict = {"time_s": time_s, "true_altitude_ft": altitude_ft, "true_ground_speed": ground_speed_kts, "target_altitude_ft": target_altitude_ft, "baro_valid": baro_valid, "baro_sigma": baro_sigma, "gps_valid": gps_valid, "gps_sigma_ft": gps_sigma_ft, "baro_altitude_ft": baro_altitude_ft, "gps_altitude_ft": gps_altitude_ft}
    rows.append(row_dict)
    













#sending this to logs as a csv file
os.makedirs("logs", exist_ok=True)
fieldnames = ["time_s", "true_altitude_ft", "true_ground_speed", "target_altitude_ft", "baro_valid", "baro_sigma", "gps_valid", "gps_sigma_ft","baro_altitude_ft","gps_altitude_ft"]
output_path = f"logs/{scenario_id}.csv"

with open(output_path, "w", newline="") as f:
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
#write the colom titles 
#writes the rows

print(f"Wrote {len(rows)} to {output_path}")
import json

with open("scenarios/nominal_climb.json", "r") as jf:
    scenario = json.load(jf)

print(type(scenario))
print(scenario["meta"]["id"])
print(scenario["sim"]["duration_s"])
print(scenario["sim"]["dt_s"])
print(scenario["assertions"]["id"])

with open("scenarios/gps_dropout_safe_mode.json") as jf2:
    scenario = json.load(jf2)

print(type(scenario))
print(scenario["meta"]["id"])

with open("scenarios/baro_noise_stability.json") as jf2:
    scenario = json.load(jf2)

print(type(scenario))
print(scenario["meta"]["id"])
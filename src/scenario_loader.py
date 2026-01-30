import json

with open("scenarios/nominal_climb.json", "r") as jf:
    scenario = json.load(jf)

    print(type(scenario))
    print("-----------")
    print(scenario["meta"]["id"])
    print("-----------")
    print(scenario["sim"]["duration_s"])
    print("-----------")
    print(scenario["sim"]["dt_s"])
    print("-----------")
    print(scenario["assertions"][0]["id"])
    print("-----------")

    for i in scenario["events"]:
        print(i)
        print("-----------")
    for i in scenario["assertions"]:
        print(i)
        print("-----------")

with open("scenarios/gps_dropout_safe_mode.json") as jf2:
    scenario2 = json.load(jf2)

    print(type(scenario2))
    print("-----------")
    print(scenario2["meta"]["id"])
    print("-----------")
    print(scenario2["sim"]["duration_s"])
    print("-----------")
    print(scenario2["sim"]["dt_s"])
    print("-----------")
    print(scenario2["assertions"][0]["id"])
    print("-----------")
    for i in scenario2["events"]:
        print(i)
        print("-----------")
    for i in scenario2["assertions"]:
        print(i)
        print("-----------")

with open("scenarios/baro_noise_stability.json") as jf3:
    scenario3 = json.load(jf3)

    print(type(scenario3))
    print("-----------")
    print(scenario3["meta"]["id"])
    print("-----------")
    print(scenario3["sim"]["duration_s"])
    print("-----------")
    print(scenario3["sim"]["dt_s"])
    print("-----------")
    print(scenario3["assertions"][0]["id"])
    print("-----------")
    for i in scenario3["events"]:
        print(i)
        print("-----------")
    for i in scenario3["assertions"]:
        print(i)
        print("-----------")
import json 
from scenario_validator import scenario_validated

def main():
    path = "scenarios/nominal_climb.json"

    with open(path, "r") as file:
        scenario = json.load(file)

    ok, errors = scenario_validated(scenario)

    if ok:
        print("success!")
    if not ok:
        print("yikes!")

        for e in errors:
            print("-", e)
if __name__ == "__main__":
    main()
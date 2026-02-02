def scenario_validated(scenario: dict) -> tuple[bool, list[str]]:
    error = []


#meta checks, one for meta, meta as a dict, name in meta, name is a non empty string, id in meta, id is a non empty string
    if "meta" not in scenario:
        error.append("Meta data missing")
        return False, error
    
    meta = scenario["meta"]
    if not isinstance(meta, dict):
        error.append("Meta isn't a dict")
        return False, error
    if "id" not in meta:
        error.append("id not found in meta")
        return False, error
    if "name" not in meta:
        error.append("name is missing")
        return False, error
    meta_name = meta["name"]
    if not isinstance(meta_name, str) or not meta_name.strip():
        error.append("meta.name is not s string or is empty")
        return False, error

    meta_id = meta["id"]
    if not isinstance(meta_id, str) or not meta_id.strip():
        error.append("meta.id is not s string or is empty")
        return False, error


#sim checks, for sim, for duration in sim, for duration_s positive number status, and for dt_s positive non tiny numbered existance

    if "sim" not in scenario:
        error.append("Sim missing in scenario")
        return False, error
    
    sim = scenario["sim"]
    if "duration_s" not in sim:
        error.append("duration_s is missing")
        return False, error
    
    if "dt_s" not in sim:
        error.append("dt_s is missing")
        return False, error
    
    sim_dur_s = sim["duration_s"]
    if sim_dur_s <= 0 or not isinstance(sim_dur_s, (int, float)):
        error.append("Ethier it isn't an int or is empty or is negative")
        return False, error
    
    sim_dt_s = sim["dt_s"]
    if sim_dt_s <= 0 or not isinstance(sim_dt_s, (int, float)):
        error.append("Ether dt_s is a float or is empty or is negative/too small")
        return False, error
    
#initial checks, checks all involved for existance, and for number or bool validation

    if "initial" not in scenario:
        error.append("initial missing in data")
        return False, error
    
    initial = scenario["initial"]

    if "altitude_ft" not in initial:
        error.append("altitude_ft not found in initial")
        return False, error
    if "ground_speed_kts" not in initial:
        error.append("ground_speed_kts not found in initial")
        return False, error
    if "targets" not in initial:
        error.append("altitude_ft not found in initial")
        return False, error
    if "altitude_ft" not in initial["targets"]:
        error.append("altitude_ft not found in initial[targets]")
        return False, error
    
    if "sensors" not in initial:
        error.append("sensors not found in initial")
        return False, error
    if "baro" not in initial["sensors"]:
        error.append("baro not found in sensors")
        return False, error
    if "gps" not in initial["sensors"]:
        error.append("gps not in sensors")
        return False, error
    if "valid" not in initial["sensors"]["baro"]:
        error.append("valid not found in baro")
        return False, error
    if "valid" not in initial["sensors"]["gps"]:
        error.append("valid not found in gps")
        return False, error


    init_altitude_ft1 = initial["altitude_ft"]
    if not isinstance(init_altitude_ft1, (int, float)):
        error.append("Altitude_ft is not a int")
        return False, error
    init_altitude_ft2 = initial["targets"]["altitude_ft"]
    if not isinstance(init_altitude_ft2, (int, float)):
        error.append("Altitude_ft is not a int")
        return False, error
    init_ground_speed_kts = initial["ground_speed_kts"]
    if not isinstance(init_ground_speed_kts, (int, float)):
        error.append("ground_speed_kts is not a int")
        return False, error
    init_sensors_baro_valid = initial["sensors"]["baro"]["valid"]
    if not isinstance(init_sensors_baro_valid, bool):
        error.append("sensors_baro_valid is not a bool")
        return False, error
    init_sensors_gps_valid = initial["sensors"]["gps"]["valid"]
    if not isinstance(init_sensors_gps_valid, bool):
        error.append("sensors_gps_valid is not a bool")
        return False, error

#checks for events existance, and that its a list

    if "events" not in scenario:
        error.append("events isn't in scenario")
        return False, error
    events = scenario["events"]
    if not isinstance(events, list):
        error.append("events isn't a list")
        return False, error


    if "assertions" not in scenario:
        error.append("Assertions isn't in scenario")
        return False, error
    
    assertions = scenario["assertions"]
    if not isinstance(assertions, list):
        error.append("Assertions isn't a list")
        return False, error
    
    for i in assertions:
        if not isinstance(i, dict):
            error.append("Something wrong with the dict here")
            return False, error
    
    ok, when_errors = validate_assertion_when(assertions, sim_dur_s)
    if not ok:
        error.extend(when_errors)
        return False, error
    
    ok_events, event_errors = validate_events(events, sim_dur_s)
    if not ok_events:
        error.extend(event_errors)
        return False, error
##
    
    is_validated = len(error) == 0
    return is_validated, error





# This is a function that checks the when portion of the assertions
def _is_number(x) -> bool:
    return isinstance(x,(int,float)) and not isinstance(x,bool)

def validate_assertion_when(assertions: list, duration_s: float) -> tuple[bool, list[str]]:
    errors = []

    allowed_assertion_types = {"altitude_within", "mode_equals", "mode_not_equals"}

    for idx, i in enumerate(assertions):
        if not isinstance(i, dict):
            errors.append(f"assertions [{idx}] must be a dict")
            continue
        if "when" not in i:
            errors.append(f"assertions {idx} Missing required field when")
            continue

        if "id" not in i:
            errors.append("id not in assertions")
            continue
        if "type" not in i:
            errors.append("type not in assertions")
            continue
        type_validated = i["type"]
        if not isinstance(type_validated, str) or not type_validated.strip():
            errors.append(f"assertions[{idx}].type is not a string or is empty")
            continue
        if type_validated not in allowed_assertion_types:
            errors.append("type not allowed. go to jail. do not pass go")
            continue
        if "expected" not in i:
            errors.append("expected not in assertions")
            continue
        expected_validated = i["expected"]
        if not isinstance(expected_validated, dict):
            errors.append("expected not in dict format")
            continue
        id_validated = i["id"]
        if not isinstance(id_validated, str) or not id_validated.strip():
            errors.append("assertions id is a not a string or is empty")
            continue


        if type_validated == "altitude_within":
            if "target" not in expected_validated:
                errors.append(f"assertions[{idx}] altitude_within missing expected.target")
            else: 
                if not isinstance(expected_validated["target"], str) or not expected_validated["target"].strip():
                    errors.append(f"assertions[{idx}] expected.target must be a non-empty string")
            
            if "tolerance_ft" not in expected_validated:
                errors.append(f"assertions[{idx}] altitude_within missing expected.tolerance_ft")
            else:
                tol = expected_validated["tolerance_ft"]
                if not isinstance(tol,(int,float)) or isinstance(tol,bool):
                    errors.append(f"assertions[{idx}] expected.tolerance_ft must be a number")
                elif tol <= 0:
                    errors.append("tol must be positive")
        elif type_validated in ("mode_equals", "mode_not_equals"):
            if "value" not in expected_validated:
                errors.append(f"assertions[{idx}] {type_validated} missing expected.value")
            else:
                val = expected_validated["value"]
                if not isinstance(val, str) or not val.strip():
                    errors.append(f"assertions[{idx}] expected.value must be a non-empty string")


        when = i["when"]
        if not isinstance(when, dict):
            errors.append(f"assertions {idx} When isn't a dict")
            continue
        if "time_s" not in when:
            errors.append(f"assertions {idx} time_s missing field")
        else:
            time_valid = when["time_s"]
            if not _is_number(time_valid):
                errors.append("time_s isn't a number")
            elif time_valid < 0 or time_valid > duration_s:
                errors.append(f"assertions[{idx}].when.time_s={time_valid} out of range [0, {duration_s}]")
        
        if "window_s" not in when:
            errors.append(f"assertions {idx} window_s isn't there")
        else:
            when_valid = when["window_s"]
            if not _is_number(when_valid):
                errors.append(f"assertions {idx} when isn't a number")
            elif when_valid < 0:
                errors.append(f"assertopms {idx} when is negative")
            
            if _is_number(when.get("time_s")) and _is_number(when_valid):
                if when["time_s"] + when_valid   > duration_s:
                    errors.append(
                        f"assertions[{idx}] window exceeds sim duration: "
                        f"time_s+window_s={when['time_s'] + when_valid} > {duration_s}"
                        )
    
    
    is_validated = len(errors) == 0

    return is_validated, errors


# This part check the validiy of the items in the dict: events
def validate_events(events: list, duration_s: float) -> tuple[bool, list[str]]:
    errors = []

    allowed_event_types = {"set_target", "inject_fault", "clear_fault"}

    for idx, event in enumerate(events):
        if not isinstance(event, dict):
            errors.append("Event isn't a dict")
            continue
        if "time_s" not in event:
            errors.append("time_s missing from events")
            continue
        if "type" not in event:
            errors.append("type missing from events")
            continue
        time_s_valid = event["time_s"]
        type_valid = event["type"]

        if not isinstance(time_s_valid,(int,float)) or isinstance(time_s_valid, bool):
            errors.append("time_s isn't a numbers or is a bool")
        elif time_s_valid <0 or time_s_valid > duration_s:
            errors.append(f"event[{idx}].time_s={time_s_valid} out of range [0, {duration_s}]")
        if not isinstance(type_valid, str) or not type_valid.strip():
            errors.append("type isn't a string or is empty")
            continue
        if type_valid not in allowed_event_types:
            errors.append(f"event[{idx}].type '{type_valid}' is not supported")
            continue
        if type_valid == "set_target":
            if "target" not in event:
                errors.append(f"event {idx} set_target missing field: target")
            if "value" not in event:
                errors.append(f"event {idx} set_target missing field: value")

        elif type_valid == "inject_fault":
            if "sensor" not in event:
                errors.append(f"event {idx} set_target missing field: sensor")
            if "fault" not in event:
                errors.append(f"event {idx} set_target missing field: fault")
            
            if "fault" in event and event["fault"] == "noise":
                if "value" not in event:
                    errors.append(f"event {idx} set_target missing field: value ")
        
        elif type_valid == "clear_fault":
            if "sensor" not in event:
                errors.append(f"clear_fault missing field: sensor")

    return (len(errors) == 0), errors
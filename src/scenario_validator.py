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
    if initial["targets"]["altitude"] not in initial:
        error.append("target_altitude_ft not found in initial")
        return False, error
    if initial["sensors"]["baro"]["valid"] not in initial:
        error.append("sensors_baro_valid not found in initial")
        return False, error
    if initial["sensors"]["gps"]["valid"] not in initial:
        error.append("sensors_gps_valid not found in initial")
        return False, error
    
    init_altitude_ft = initial["altitude_ft"]
    if not isinstance(init_altitude_ft, (int, float)):
        error.append("Altitude_ft is not a int")
        return False, error
    init_ground_speed_kts = initial["ground_speed_kts"]
    if not isinstance(init_ground_speed_kts, (int, float)):
        error.append("ground_speed_kts is not a int")
        return False, error
    init_target_altitude_ft = initial["target_altitude_ft"]
    if not isinstance(init_target_altitude_ft, (int, float)):
        error.append("target_altitude_ft is not a int")
        return False, error
    init_sensors_baro_valid = initial["sensors_baro_valid"]
    if not isinstance(init_sensors_baro_valid, bool):
        error.append("sensors_baro_valid is not a bool")
        return False, error
    init_sensors_gps_valid = initial["sensors_gps_valid"]
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
#jkfsdjbsdalkjfsdah

    if "assertions" not in scenario:
        error.append("Assertions isn't in scenario")
        return False, error
    
    assertions = scenario["assertions"]
    if not isinstance(assertions, list):
        error.append("Assertions isn't a list")
        return False, error
    
    if "time_s" not in assertions:
        error.append("Time_s ain't there")
        return False, error
    if "type" not in assertions:
        error.append("type isn't in assertions")
        return False, error

    type_valid = assertions["type"]
    if not isinstance(type_valid, str):
        error.append("Type isn't a string")
        return False, error
    time_s_vald = assertions["time_s"]
    if not isinstance(time_s_vald, (int, float)):
        error.append("time_s isn't a number")
        False, error
    id_valid = assertions["id"]
    if not isinstance(id_valid, str) or not id_valid.strip():
        error.append("id is not a string or is empty")
        return False, error
    type_valid2 = assertions["id"]
    if not isinstance(type_valid2, str) or not type_valid2.strip():
        error.append("type is not a string or is empty")
        return False, error

    
    
    is_validated = len(error) == 0

    return is_validated, error
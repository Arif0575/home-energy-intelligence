import json
from functools import lru_cache

# copy config.py.example to config.py and fill in your details
from config import args

from pygoodwe import SingleInverter


@lru_cache() 
def get_single_inverter(args=args):  # pylint: disable=redefined-outer-name,dangerous-default-value
    """test fixture"""
    print("Single Inverter")
    goodwe = SingleInverter(
        system_id=args.get("gw_station_id", ""),
        account=args.get("gw_account", ""),
        password=args.get("gw_password", ""),
    )
    # print("Grabbing data")
    goodwe.getCurrentReadings()
    return goodwe


def test_get_temperature():
    """tests getting the temp"""
    goodwe = get_single_inverter()
    assert goodwe.get_inverter_temperature()

inverter = get_single_inverter()

from datetime import datetime

row = []
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
row.append(timestamp)

CSV_FILE = "goodwe_solar_log.csv"

#print(json.dumps(inverter.data.get("inverter", {}), indent=2))
interesting = [ "out_pac", "battery_power"]
for key in interesting: 
    print(f"{key}:{inverter.data.get("inverter", {}).get(key)}")
    value = ((inverter.data.get("inverter", {}).get(key)))
    row.append(value)
    
    


House_power = ((inverter.data.get("inverter", {}).get("invert_full")))
print(f"House Power: {House_power["pmeter"]}")
grid_power = (House_power["pmeter"])
row.append(grid_power)

print(row)

with open("goodwe_solar_log.csv", "a") as f: f.write(",".join(map(str, row)) + "\n")



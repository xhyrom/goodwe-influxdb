import os
import goodwe

FIELDS: set[str] = {
    "vpv1",
    "ipv1",
    "vpv2",
    "ipv2",
    "ppv",
    "vbattery1",
    "battery_mode",
    "vgrid",
    "igrid",
    "fgrid",
    "pgrid",
    "vgrid2",
    "igrid2",
    "fgrid2",
    "pgrid2",
    "vgrid3",
    "igrid3",
    "fgrid3",
    "pgrid3",
    "load_p1",
    "load_p2",
    "load_p3",
    "temperature",
    "temperature_module",
    "temperature_air",
    "e_day",
    "e_day_exp",
    "e_day_impl",
    "e_load_day",
    "e_load_total",
    "e_total",
    "e_total_exp",
    "e_total_imp",
    "meter_e_total_exp",
    "meter_e_total_imp",
}


async def get_metrics() -> dict[str, str]:
    inverter = await goodwe.connect(str(os.environ.get("GOODWE_IP")))
    runtime_data = await inverter.read_runtime_data()

    data: dict[str, str] = {}

    for sensor in inverter.sensors():
        if sensor.id_ in runtime_data and sensor.id_ in FIELDS:
            data[sensor.id_] = runtime_data[sensor.id_]

    return data

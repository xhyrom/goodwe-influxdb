import asyncio
import goodwe


async def dump():
    ip_address = "192.168.1.10"

    inverter = await goodwe.connect(ip_address)
    runtime_data = await inverter.read_runtime_data()

    for sensor in inverter.sensors():
        if sensor.id_ in runtime_data:
            print(
                f"{sensor.id_:<40} {sensor.name:<35} = {runtime_data[sensor.id_]} {sensor.unit}"
            )


asyncio.run(dump())

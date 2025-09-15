import asyncio
import datetime
import os

import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

from database import store_metrics
from metrics import get_metrics

write_client = influxdb_client.InfluxDBClient(
    url=str(os.environ.get("INFLUXDB_URL")),
    token=os.environ.get("INFLUXDB_TOKEN"),
    org=os.environ.get("INFLUXDB_ORG"),
)
write_api = write_client.write_api(write_options=SYNCHRONOUS)


async def main():
    print("Starting")

    while True:
        time = datetime.datetime.now(datetime.UTC)

        try:
            metrics = await get_metrics()
            print(metrics)

            #store_metrics(write_api, metrics, time)
        except Exception as e:
            print(f"Failed to get metrics: {e}")

        await asyncio.sleep(60)


asyncio.run(main())

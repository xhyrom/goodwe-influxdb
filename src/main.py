import asyncio
import datetime
from time import sleep
import influxdb_client
import os
from influxdb_client.client.write_api import SYNCHRONOUS
from metrics import get_metrics
from database import store_metrics

write_client = influxdb_client.InfluxDBClient(
    url=str(os.environ.get("INFLUXDB_URL")),
    token=os.environ.get("INFLUXDB_TOKEN"),
    org=os.environ.get("INFLUXDB_ORG"),
)
write_api = write_client.write_api(write_options=SYNCHRONOUS)


async def main():
    time = datetime.datetime.now(datetime.UTC)

    metrics = await get_metrics()
    print(metrics)

    store_metrics(write_api, metrics, time)

    sleep(60)


asyncio.run(main())

from datetime import datetime
import os
from influxdb_client import Point, WritePrecision
from influxdb_client.client.write_api import WriteApi


def store_metrics(client: WriteApi, metrics: dict[str, str], time: datetime) -> None:
    point = (
        Point("measurement").tag("type", "photovoltaic").time(time, WritePrecision.NS)
    )

    for key, value in metrics.items():
        point.field(key, value)

    return client.write(
        bucket=str(os.environ.get("INFLUXDB_BUCKET")),
        org=os.environ.get("INFLUXDB_ORG"),
        record=point,
    )

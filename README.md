**Goodwe InfluxDB** is a simple service that scrapes data from the GoodWe inverter and puts them into the database.

### Requirements

goodwe inverter [(ET, EH, BT, BH, ES, EM, BP, DT, MS, D-NS, and XS families should works)](https://github.com/marcelblijleven/goodwe) \
[influxdb](https://www.influxdata.com/) \
[python3](https://www.python.org/)

### Installation

You can install and run the service using [docker compose](./docker-compose.yml). \
Don't forget to update environment variables!

However, if you want to run it outside docker, install packages from [requirements.txt](./requirements.txt) and run <kbd>[src/main.py](./src/main.py)</kbd> with the following environment variables:
`INFLUXDB_TOKEN, INFLUXDB_URL, INFLUXDB_ORG, INFLUXDB_BUCKET, GOODWE_IP`

```bash
$ pip install -r requirements.txt
$ INFLUXDB_TOKEN=hello INFLUXDB_URL=http://localhost:8086 INFLUXDB_ORG=org INFLUXDB_BUCKET=bucket GOODWE_IP=192.168.1.78 python src/main.py
```

You can also run <kbd>[scripts/dump.py](./scripts/dump.py)</kbd> that returns all sensors.

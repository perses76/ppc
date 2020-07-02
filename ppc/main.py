import typing
import os
import mysql.connector  # type: ignore
from . import raw_log
from . import kpi1
from . import kpi2
from . import settings


def run(folder, db_config):
    """Analyze all files in folder and write kpi1 and kpi2 report in Db."""
    reader = raw_log.LogDataReader(folder)
    conn = mysql.connector.connect(**db_config)
    try:
        for calculator, writer in [
            (kpi1.Calculator("5min"), kpi1.DataWriter(conn)),
            (kpi1.Calculator("1H"), kpi1.DataWriter(conn)),
            (kpi2.Calculator("5min"), kpi2.DataWriter(conn)),
            (kpi2.Calculator("1H"), kpi2.DataWriter(conn)),
        ]:
            data = calculator.calculate(reader)
            writer.write(data)
    finally:
        conn.close()


def main():
    """Read app config from environemnt variables and run app."""
    run(settings.INPUT_FOLDER, settings.DB_CONFIG)


if __name__ == "__main__":
    main()

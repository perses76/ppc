import typing
import os
import mysql.connector  # type: ignore
from . import raw_log
from . import kpi1
from . import kpi2


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
    folder = os.environ["folder"]
    db_config = {
        "host": os.environ["host"],
        "database": os.environ["database"],
        "user": os.environ["user"],
        "password": os.environ["password"],
    }
    run(folder, db_config)


if __name__ == "__main__":
    main()

from typing import Iterable
import attr
import pandas as pd  # type: ignore

from . import base
from . import utils


@attr.s(auto_attribs=True)
class Record(base.StatRecord):
    """StatRecord to store in DB."""

    interval_start_timestamp: int
    interval_end_timestamp: int
    service_id: int
    total_bytes: int
    interval: int


class Calculator(base.Calculator):
    """Calculate kpi1."""

    def __init__(self, interval):
        self.interval = interval

    def calculate(self, reader):
        df = utils.convert_raw_rows_to_dataframe(reader.read())
        kpi1_df = df.groupby(
            [
                pd.Grouper(key="start_dt", freq=self.interval),
                "interval_start_timestamp",
                "interval_end_timestamp",
                "service_id",
            ]
        ).agg({"bytes_uplink": "sum", "bytes_downlink": "sum"})
        kpi1_df["total_bytes"] = kpi1_df["bytes_uplink"] + kpi1_df["bytes_downlink"]
        kpi1_df = kpi1_df.sort_values(by=["total_bytes"], ascending=False).iloc[:3, :]
        kpi1_df = kpi1_df.reset_index()
        kpi1_df = kpi1_df.drop(["start_dt", "bytes_uplink", "bytes_downlink"], axis=1)
        return [
            Record(interval=self.interval, **item)
            for item in kpi1_df.to_dict("records")
        ]


class DataWriter(base.DataWriter):
    """Kpi1 to db datawriter."""

    sql_statement = (
        "INSERT INTO kpi1 (interval_start_timestamp, interval_end_timestamp, service_id, total_bytes, `interval`) "
        "VALUES (%s, %s, %s, %s, %s)"
    )

    def __init__(self, conn):
        self.conn = conn

    def write(self, records: Iterable[Record]):  # type: ignore[override]
        cur = self.conn.cursor()
        rows_data = [attr.astuple(r) for r in records]
        try:
            cur.executemany(self.sql_statement, rows_data)
            self.conn.commit()
        finally:
            cur.close()

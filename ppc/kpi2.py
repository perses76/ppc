from typing import Iterable
import attr
import pandas as pd  # type: ignore
from . import base
from . import utils


@attr.s(auto_attribs=True)
class Record(base.StatRecord):
    interval_start_timestamp: int
    interval_end_timestamp: int
    cell_id: int
    number_of_unique_users: int
    interval: int


class Calculator(base.Calculator):
    """Calculate kpi2."""

    def __init__(self, interval):
        self.interval = interval

    def calculate(self, reader):
        """Calculate data for kpi2 report."""
        df = utils.convert_raw_rows_to_dataframe(reader.read())
        kpi2_df = df.groupby(
            [
                pd.Grouper(key="start_dt", freq=self.interval),
                "interval_start_timestamp",
                "interval_end_timestamp",
                "cell_id",
            ]
        ).agg(number_of_unique_users=("msisdn", "nunique"))
        kpi2_df = kpi2_df.sort_values(
            by=["number_of_unique_users", "cell_id"], ascending=False
        ).iloc[:3, :]
        kpi2_df = kpi2_df.reset_index()
        kpi2_df = kpi2_df.drop(["start_dt"], axis=1)
        return [
            Record(interval=self.interval, **item)
            for item in kpi2_df.to_dict("records")
        ]


class DataWriter(base.DataWriter):
    """Kpi2 to db datawriter."""

    sql_statement = (
        "INSERT INTO kpi2 (interval_start_timestamp, interval_end_timestamp, cell_id, number_of_unique_users, `interval`) "
        "VALUES (%s, %s, %s, %s, %s)"
    )

    def __init__(self, conn):
        self.conn = conn

    def write(self, records: Iterable[Record]):  # type: ignore[override]
        """Save kpi2 report in DB."""
        cur = self.conn.cursor()
        rows_data = [attr.astuple(r) for r in records]
        try:
            cur.executemany(self.sql_statement, rows_data)
            self.conn.commit()
        finally:
            cur.close()

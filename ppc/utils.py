from typing import Iterable
import pandas as pd  # type: ignore
from datetime import datetime
import attr
from . import raw_log


def convert_raw_rows_to_dataframe(raw_records: Iterable[raw_log.RawRecord]) -> pd.DataFrame:
    """Convert RawRecords list to pandas DataFrame."""
    records_dict = [attr.asdict(rec) for rec in raw_records]
    df = pd.DataFrame.from_records(records_dict)
    df["start_dt"] = (df["interval_start_timestamp"] / 1000).apply(
        datetime.fromtimestamp
    )
    return df

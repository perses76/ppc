from typing import Iterable
import os
import csv
import attr
from . import base


@attr.s(auto_attribs=True)
class RawRecord(base.LogRecord):
    """Raw record from log file."""

    interval_start_timestamp: int
    interval_end_timestamp: int
    msisdn: int
    bytes_uplink: int
    bytes_downlink: int
    service_id: int
    cell_id: int


class LogDataReader(base.DataReader):
    """Read log data from cvs files in folder."""

    def __init__(self, folder):
        self.folder = folder
        self._records = None

    def read(self) -> Iterable[RawRecord]:  # type: ignore[override]
        """Returns list of raw records."""
        if self._records is None:
            self._records = self._load_records()
        return self._records

    def _load_records(self):
        """Load records from files in folder."""
        all_records = []
        for file_name in os.listdir(self.folder):
            file_path = os.path.join(self.folder, file_name)
            with open(file_path, newline="") as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # skip header
                records = [self.parse_row(row) for row in reader]
                all_records.extend(records)
        return all_records

    def parse_row(self, raw):
        """Parse raw record from CSV file."""
        return RawRecord(*[int(val) for val in raw])

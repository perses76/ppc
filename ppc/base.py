"""Base and absctact classes."""
from typing import Iterable
import attr
import abc


@attr.s(auto_attribs=True)
class StatRecord:
    """Base class for statistic record to store."""
    pass


@attr.s(auto_attribs=True)
class LogRecord:
    """Log record from log file"""

    pass


class DataReader(abc.ABC):
    """Read LogRecords from source."""
    @abc.abstractmethod
    def read(self) -> LogRecord:
        pass


class Calculator(abc.ABC):
    """Calulate statistic."""
    @abc.abstractmethod
    def calculate(self, reader: DataReader) -> Iterable[StatRecord]:
        """Calculate statistics based on input data from reader."""
        pass


class DataWriter(abc.ABC):
    """Write stat data to storage."""

    @abc.abstractmethod
    def write(self, records: Iterable[StatRecord]):
        """Write Statistic to storage."""
        pass

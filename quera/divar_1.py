from __future__ import annotations

from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
from typing import Iterable, Tuple


@dataclass
class EpochRange:
    start: int
    end: int

    def is_inside(self, number: int) -> bool:
        return self.start <= number <= self.end

    def overlap(self, other_range: EpochRange) -> int:
        x = range(self.start, self.end)
        y = range(other_range.start, other_range.end)
        xs = set(x)
        intersection = xs.intersection(y)

        if not intersection:
            return 0
        start = max(self.start, other_range.start)
        end = min(self.end, other_range.end)
        return EpochRange(start, end).length()

    def length(self) -> int:
        return self.end - self.start


class CompanyBase(ABC):
    @abstractproperty
    def registered_meetings(self) -> Iterable[EpochRange]:
        pass

    @abstractmethod
    def register_meeting(self, epoch_range: EpochRange) -> None:
        pass

    @abstractmethod
    def find_metting_time(self, duration: int) -> EpochRange:
        pass


class Company(CompanyBase):
    _COMPANY_START_EPOCH = 0
    _COMPANY_END_EPOCH = 32400000

    def __init__(self) -> None:
        self._registered_meetings = []

    @property
    def registered_meetings(self) -> Iterable[EpochRange]:
        return self._registered_meetings

    def register_meeting(self, epoch_range: EpochRange) -> None:
        self._validate_epoch_range_doesnt_clash_with_registered_meetings(
            epoch_range
        )
        self._registered_meetings.append(epoch_range)

    def find_metting_time(self, duration: int) -> EpochRange:
        sorted_meeting_times = sorted(
            self._registered_meetings, key=lambda r: r.start
        )
        start = Company._COMPANY_START_EPOCH
        for index in range(len(sorted_meeting_times)):
            end = start + duration
            this_range = EpochRange(start, end)
            if not any(
                this_range.overlap(other_range)
                for other_range in sorted_meeting_times[index:]
            ):
                return this_range
            start = sorted_meeting_times[index].end + 1
        end = start + duration
        if end < Company._COMPANY_END_EPOCH:
            return EpochRange(start, end)
        raise ValueError("There is no time available for such meeting.")

    def _validate_epoch_range_doesnt_clash_with_registered_meetings(
        self, epoch_range: EpochRange
    ) -> None:
        for registered_range in self._registered_meetings:
            if registered_range.is_inside(
                epoch_range.start
            ) or registered_range.is_inside(epoch_range.end):
                raise ValueError(
                    "The given range clashes with registered ranges."
                )


def get_inputs() -> Tuple[Iterable[EpochRange], int]:
    number_of_entries = int(input())
    meeting_ranges = []
    for entry_number in range(number_of_entries):
        input_row = list(map(int, input().split()))
        meeting_ranges.append(EpochRange(input_row[1], input_row[2]))
    duration = list(map(int, input().split()))[1]
    return duration, meeting_ranges


def main(duration: int, meeting_ranges: Iterable[EpochRange]) -> EpochRange:
    company = Company()
    for meeting_range in meeting_ranges:
        company.register_meeting(meeting_range)
    return company.find_metting_time(duration)


def print_result(meeting_range: EpochRange) -> None:
    print(meeting_range.start, meeting_range.end)


if __name__ == "__main__":
    print_result(main(*get_inputs()))

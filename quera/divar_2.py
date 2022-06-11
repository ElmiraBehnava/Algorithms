from __future__ import annotations

from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
from typing import AbstractSet, Iterable, Tuple


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
    def employees(self) -> AbstractSet[EmployeeBase]:
        pass

    @abstractmethod
    def register_meeting(self, epoch_range: EpochRange) -> None:
        pass

    @abstractmethod
    def register_employee(self, employee: EmployeeBase) -> None:
        pass

    @abstractmethod
    def find_meeting_time(
        self, duration: int, employee: EmployeeBase
    ) -> EpochRange:
        pass

    @abstractmethod
    def overlap_between_two_employees(
        self, first_employee: EmployeeBase, second_employee: EmployeeBase
    ) -> int:
        pass


class EmployeeBase(ABC):
    @abstractproperty
    def meetings(self) -> Iterable[EpochRange]:
        pass

    @abstractmethod
    def add_meeting(self, meeting_range: EpochRange) -> None:
        pass


class Employee(EmployeeBase):
    def __init__(self) -> None:
        self._meetings = []

    @property
    def meetings(self) -> Iterable[EpochRange]:
        return self._meetings

    def add_meeting(self, meeting_range: EpochRange) -> None:
        self._validate_epoch_range_doesnt_clash_with_registered_meetings(
            meeting_range
        )
        self._meetings.append(meeting_range)

    def _validate_epoch_range_doesnt_clash_with_registered_meetings(
        self, epoch_range: EpochRange
    ) -> None:
        for registered_range in self._meetings:
            if registered_range.is_inside(
                epoch_range.start
            ) or registered_range.is_inside(epoch_range.end):
                raise ValueError(
                    "The given range clashes with registered ranges."
                )


class Company(CompanyBase):
    _COMPANY_START_EPOCH = 0
    _COMPANY_END_EPOCH = 32400000

    def __init__(self) -> None:
        self._employees = set()

    @property
    def employees(self) -> AbstractSet[EmployeeBase]:
        return self._employees

    def register_meeting(
        self, epoch_range: EpochRange, employee: EmployeeBase
    ) -> None:
        employee.add_meeting(epoch_range)

    def register_employee(self, employee: EmployeeBase) -> None:
        self._employees.add(employee)

    def find_meeting_time(
        self, duration: int, employee: EmployeeBase
    ) -> EpochRange:
        sorted_meeting_times = sorted(employee.meetings, key=lambda r: r.start)
        start = Company._COMPANY_START_EPOCH
        for registered_meeting_range in sorted_meeting_times:
            end = start + duration
            if not registered_meeting_range.is_inside(end):
                return EpochRange(start, end)
            start = registered_meeting_range.end + 1
        end = start + duration
        if end < Company._COMPANY_END_EPOCH:
            return EpochRange(start, end)
        raise ValueError("There is no time available for such meeting.")

    def overlap_between_two_employees(
        self, first_employee: EmployeeBase, second_employee: EmployeeBase
    ) -> int:
        result = 0
        for first_meeting, second_meeting in zip(
            first_employee.meetings, second_employee.meetings
        ):
            overlapp = first_meeting.overlap(second_meeting)
            result += overlapp
        return result


def get_inputs() -> Tuple[Iterable[EpochRange], Iterable[EpochRange]]:
    number_of_entries = int(input())
    first_meeting_ranges = []
    for _ in range(number_of_entries):
        input_row = list(map(int, input().split()))
        first_meeting_ranges.append(EpochRange(input_row[1], input_row[2]))

    number_of_entries = int(input())
    second_meeting_ranges = []
    for _ in range(number_of_entries):
        input_row = list(map(int, input().split()))
        second_meeting_ranges.append(EpochRange(input_row[1], input_row[2]))
    return first_meeting_ranges, second_meeting_ranges


def main(
    first_meeting_ranges: Iterable[EpochRange],
    second_meeting_ranges: Iterable[EpochRange],
) -> int:
    company = Company()
    first_employee = Employee()
    for meeting_range in first_meeting_ranges:
        company.register_meeting(meeting_range, first_employee)

    second_employee = Employee()
    for meeting_range in second_meeting_ranges:
        company.register_meeting(meeting_range, second_employee)

    return company.overlap_between_two_employees(
        first_employee, second_employee
    )


def print_result(number: int) -> None:
    print(number)


if __name__ == "__main__":
    print_result(main(*get_inputs()))

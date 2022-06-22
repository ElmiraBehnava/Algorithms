from __future__ import annotations

from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
from typing import Iterable


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


class DeskBase(ABC):
    @abstractmethod
    def reserve_desk_with_given_epoch_range(
        self, username: str, epoch_range: EpochRange
    ):
        pass


class FloorBase(ABC):
    @abstractmethod
    def add_desk_to_floor(self) -> None:
        pass

    @abstractproperty
    def desks(self) -> Iterable[Desk]:
        pass


class Desk(DeskBase):
    def __init__(self, floor_number: int, desk_number: int):
        self._desk_number = desk_number
        self._reserved_times = []
        self.floor_number = floor_number

    def _validate_epoch_range_doesnt_clash_with_registered_reserved_times(
        self, epoch_range: EpochRange
    ) -> None:
        for reserved_time in self._reserved_times:
            if reserved_time.is_inside(
                epoch_range.start
            ) or reserved_time.is_inside(epoch_range.end):
                return "no desk available"

    def reserve_desk_with_given_epoch_range(
        self, username: str, epoch_range: EpochRange
    ) -> None:

        self._validate_epoch_range_doesnt_clash_with_registered_reserved_times(
            epoch_range
        )
        self._reserved_times.append(epoch_range)
        return f"{username}got desk {self._desk_number}-{self.floor_number}"

    def __repr__(self):
        return str(self._desk_number)


class Floor(FloorBase):
    def __init__(self, floor_number: int) -> None:
        self.floor_number = floor_number
        self._desks = []

    def add_desk_to_floor(self, desk: Desk) -> None:
        self._desks.append(desk)

    @property
    def desks(self) -> Iterable[Desk]:
        return self._desks

    def __repr__(self):
        return str(self.floor_number)


def get_inputs():
    floors = []
    number_of_floors = int(input())
    for floor_number in range(number_of_floors):
        floor = Floor(floor_number + 1)
        number_of_desks = int(input())
        for i in range(number_of_desks):
            desk = Desk(floor_number + 1, i + 1)
            floor.add_desk_to_floor(desk)
        floors.append(floor)
    requests = []
    while True:
        user_input = input()
        if user_input == "end":
            break
        user_input = list(user_input.split())
        username = user_input[2]
        start_time = int(user_input[0])
        duration = int(user_input[3])
        end_time = start_time + duration
        requests.append([username, start_time, end_time])
    a = []
    for requests in requests:
        for floor in floors:
            for desk in floor.desks:
                a.append(
                    desk.reserve_desk_with_given_epoch_range(
                        requests[0], EpochRange(requests[1], requests[2])
                    )
                )
                print(floor.desks)
    return a


print(get_inputs())

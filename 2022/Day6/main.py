"""AdventOfCode Day 4"""
from __future__ import annotations
import typing as t
import sys
from api import get_input
from more_itertools import chunked


def part1_2(lines: t.List[str], group: int) -> int:
    """
    :param lines:
    """
    to_check = []
    for idx, char in enumerate(lines[0]):
        if len(to_check) == group:
            to_check.pop(0)
        to_check.append(char)

        if len(set(to_check)) == group:
            return int(idx+1)


def main() -> None:
    """ Entrypoint into the solution.
    """
    with open("input.txt") as f:
        lines = f.read().splitlines()
        print(f"{part1_2(lines, 4)=}")
        print(f"{part1_2(lines, 14)=}")


if __name__ == "__main__":
    get_input.main(6, 2022)
    sys.exit(main())

# Win Result
# part1_2(lines, 4)=1850
# part1_2(lines, 14)=2823

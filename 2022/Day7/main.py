"""AdventOfCode Day 4"""
from __future__ import annotations
import typing as t
import sys
from api import get_input


def part1(lines: t.List[str]) -> None:
    """
    :param lines:
    """
    pass


def main() -> None:
    """ Entrypoint into the solution.
    """
    with open("input.txt") as f:
        lines = f.read().splitlines()
        print(f"{part1(lines)=}")


if __name__ == "__main__":
    get_input.main(7, 2022)
    sys.exit(main())

# Win Result
# part1_2(lines, 4)=1850
# part1_2(lines, 14)=2823

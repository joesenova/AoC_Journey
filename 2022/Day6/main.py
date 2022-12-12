"""AdventOfCode Day 6"""
from __future__ import annotations
import typing as t
import sys
from api import get_input


def part1_2(lines: t.List[str], group: int) -> int:
    """
    :param lines:
    :param group:
    """
    return [int(idx+group) for idx in range(0, len(lines[0])+1)
            if len(set([char for char in lines[0][idx:idx+group]])) == group][0]


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

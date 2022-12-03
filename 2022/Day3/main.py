"""AdventOfCode Day 3"""
from __future__ import annotations
import typing as t
import sys
from api import get_input
import numpy as np


def alpha_ord(line: str) -> t.List[int]:
    """"""
    return [ord(char) - 96 for char in line if char.islower()] + [
        ord(char) - 38 for char in line if char.isupper()]


def part1(lines: t.List[str]) -> int:
    """"""
    sack_tot = []
    for line in lines:
        mid_idx = len(line) // 2
        sack_tot += list(np.intersect1d(alpha_ord(line[mid_idx:]), alpha_ord(line[:mid_idx])))

    return sum(sack_tot)


def part2(lines: t.List[str]) -> int:
    """"""
    line_grp = []
    sack_tot = []
    for idx, line in enumerate(lines):
        line_grp.append(alpha_ord(line))
        if len(line_grp) == 3:
            sack_tot.append([x for x in line_grp[0] if x in line_grp[1] and x in line_grp[2]][0])
            line_grp = []

    return sum(sack_tot)


def main():
    """ Entrypoint into the solution.
    """
    with open("input.txt") as f:
        lines = f.read().splitlines()
        print(f"{part1(lines)=}")
        print(f"{part2(lines)=}")


if __name__ == "__main__":
    get_input.main(3, 2022)
    sys.exit(main())

# Win Result
# part1(lines)=7428
# part2(lines)=2650

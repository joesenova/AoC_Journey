"""AdventOfCode Day 4"""
from __future__ import annotations
import typing as t
import sys
from api import get_input
import numpy as np
from more_itertools import chunked


def expand_range(clean_range: str) -> t.Set[int]:
    rng_list = clean_range.split('-')
    return {a for a in range(int(rng_list[0]), int(rng_list[1])+1)}


def get_sets_from_range(line: str) -> t.Tuple[t.Set[int], t.Set[int]]:
    line = line.split(',')
    return expand_range(line[0]), expand_range(line[1])


def part1(lines: t.List[str]) -> int:
    """"""
    contain_count = 0
    for line in lines:
        set_a, set_b = get_sets_from_range(line)
        if len(set_a) > len(set_b):
            if set_b <= set_a:
                contain_count += 1
        else:
            if set_a <= set_b:
                contain_count += 1

    return contain_count


def part2(lines: t.List[str]) -> int:
    """"""
    part_contain_count = 0
    for line in lines:
        set_a, set_b = get_sets_from_range(line)
        if len(set_a.intersection(set_b)) > 0:
            part_contain_count += 1

    return part_contain_count


def main():
    """ Entrypoint into the solution.
    """
    with open("input.txt") as f:
        lines = f.read().splitlines()
        print(f"{part1(lines)=}")
        print(f"{part2(lines)=}")


if __name__ == "__main__":
    get_input.main(4, 2022)
    sys.exit(main())

# Win Result
# part1(lines)=573
# part2(lines)=867

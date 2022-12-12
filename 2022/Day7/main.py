"""AdventOfCode Day 7"""
from __future__ import annotations
import typing as t
import sys
from collections import defaultdict

from api import get_input


def get_dir_sizes(lines: t.List[str]) -> t.Dict:
    working_dirs = []
    global_dirs = defaultdict(lambda: 0)
    for line in lines:
        line = line.split()
        if line[0].isnumeric():
            size = int(line[0])
            dir_key = ''
            for w_dir in working_dirs:
                dir_key += w_dir
                global_dirs[dir_key] += size

        if line[1] == 'cd':
            if line[2] == '..':
                working_dirs.pop()
            else:
                working_dirs.append(line[2])

    return global_dirs


def part1(lines: t.List[str]) -> int:
    """
    :param lines:
    """

    global_dirs = get_dir_sizes(lines)

    total = [size for size in global_dirs.values() if size <= 100000]
    return sum(total)


def part2(lines: t.List[str]) -> int:
    """
    :param lines:
    """
    global_dirs = get_dir_sizes(lines)
    space_used = global_dirs['/']
    space_free = 70000000 - space_used
    space_needed = 30000000 - space_free

    return min([size for size in global_dirs.values() if size >= space_needed])


def main() -> None:
    """ Entrypoint into the solution.
    """
    with open("input.txt") as f:
        lines = f.read().splitlines()
        print(f"{part1(lines)=}")
        print(f"{part2(lines)=}")


if __name__ == "__main__":
    get_input.main(7, 2022)
    sys.exit(main())

# Win Result
# part1(lines)=1390824
# part2(lines)=7490863

"""AdventOfCode Day 8"""
from __future__ import annotations
import typing as t
import sys

from api import get_input


def calc_vid_tree(line) -> None:
    ref_tree = line[0][0]
    line[0][1] = True
    for tree in line[1:]:
        if tree[0] > ref_tree:
            ref_tree = tree[0]
            tree[1] = True


def calc_vis_trees(grid: t.List[t.List[t.List[int, bool]]]) -> int:
    """
    :param grid:
    """
    total = 0
    for line in grid:
        for tree in line:
            if tree[1]:
                total += 1
    return total


def part1(lines: t.List[str]) -> int:
    """
    :param lines:
    """
    grid = [[[int(a), False] for a in line.strip()] for line in lines]
    grid_y = []
    for x in range(0, len(grid[0])):
        row = []
        for y in range(0, len(grid[0])):
            row.append(grid[y][x])
        grid_y.append(row)

    for line in grid:
        calc_vid_tree(line)
        line.reverse()
        calc_vid_tree(line)

    for line in grid_y:
        calc_vid_tree(line)
        line.reverse()
        calc_vid_tree(line)

    vis_trees = calc_vis_trees(grid)

    return vis_trees


def part2(lines: t.List[str]) -> int:
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
        print(f"{part2(lines)=}")


if __name__ == "__main__":
    get_input.main(8, 2022)
    sys.exit(main())

# Win Result
# part1(lines)=
# part2(lines)=

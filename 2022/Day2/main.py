"""AdventOfCode Day 2"""
from __future__ import annotations
import typing as t
import sys
from api import get_input

CONVERT = {"X": "R", "Y": "P", "Z": "S", "A": "R", "B": "P", "C": "S"}
MAP = {"X": "LOSS", "Y": "DRAW", "Z": "WIN", "RP": "WIN", "RS": "LOSS", "RR": "DRAW", "PR": "LOSS", "PS": "WIN", "PP": "DRAW", "SP": "LOSS", "SR": "WIN", "SS": "DRAW"}
MAP_LOSS = {"A": "S", "B": "R", "C": "P"}
MAP_WIN = {"A": "P", "B": "S", "C": "R"}
SCORE = {"R": 1, "P": 2, "S": 3, "WIN": 6, "DRAW": 3, "LOSS": 0}


def part1(lines: t.List[str]) -> None:
    """ Clac the total score of the game
    :param lines:
    """
    my_score = 0
    for line in lines:
        line = [CONVERT[c] for c in line.split()]
        elf = line[0]
        me = line[1]

        res = MAP[f"{elf}{me}"]
        my_score += SCORE[res]
        my_score += SCORE[me]

    print(f"part1: {my_score=}")


def part2(lines: t.List[str]) -> None:
    """ Clac the total score of the game using the 2nd column as a "cheat sheet"
    :param lines:
    """
    my_score = 0
    for line in lines:
        line = line.split()
        me = line[1]
        elf = line[0]

        res = MAP[me]
        my_score += SCORE[res]

        if res == "DRAW":
            me = CONVERT[elf]
        if res == "LOSS":
            me = MAP_LOSS[elf]
        if res == "WIN":
            me = MAP_WIN[elf]

        my_score += SCORE[me]

    print(f"part2: {my_score=}")


def main():
    """ Entrypoint into the solution.
    """
    with open("input.txt") as f:
        lines = f.read().splitlines()
        part1(lines)
        part2(lines)


if __name__ == "__main__":
    get_input.main(2)
    sys.exit(main())

# Win Result
# part1: my_score = 15691
# part2: my_score = 12989

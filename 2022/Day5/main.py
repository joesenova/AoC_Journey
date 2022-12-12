"""AdventOfCode Day 4"""
from __future__ import annotations
import typing as t
import sys
from api import get_input


def calc_moves_rows(lines: t.List[str]) -> tuple:
    """
    :param lines:
    """
    rows = []
    moves = []
    for idx, line in enumerate(lines):
        if idx <= 9:
            col = []
            for i in range(0, len(line), 4):
                col.append(line[i:i + 3])
            rows.append(col)
        else:
            ln = line.split()
            moves.append([int(ln[1]), int(ln[3]) - 1, int(ln[5]) - 1])

    c_rows = []
    index = 0
    rows.reverse()
    for i in range(1, len(rows)):
        c_col = []
        for idx in range(2, 10):
            to_check = rows[idx][index].strip().lstrip()
            if to_check:
                c_col.append(to_check[1])
        index += 1
        c_rows.append(c_col)

    return moves, c_rows


def get_answer(c_rows: t.List[list]) -> str:
    """

    """
    answer = []
    for row in c_rows:
        answer.append(row[-1])

    return ''.join(answer)


def part1(lines: t.List[str]) -> str:
    """
    :param lines:
    """
    moves, c_rows = calc_moves_rows(lines)
    for move in moves:
        ttl, frm, to = tuple(move)

        for i in range(0, ttl):
            if len(c_rows[frm]) > 0:
                c_rows[to].append(c_rows[frm].pop())

    return get_answer(c_rows)


def part2(lines: t.List[str]) -> str:
    """
    :param lines:
    """
    moves, c_rows = calc_moves_rows(lines)
    for move in moves:
        ttl, frm, to = tuple(move)
        crates = []
        for i in range(0, ttl):
            if len(c_rows[frm]) > 0:
                crates.append(c_rows[frm].pop())

        crates.reverse()
        for crate in crates:
            c_rows[to].append(crate)

    return get_answer(c_rows)


def main() -> None:
    """ Entrypoint into the solution.
    """
    with open("input.txt") as f:
        lines = f.read().splitlines()
        print(f"{part1(lines)=}")
        print(f"{part2(lines)=}")


if __name__ == "__main__":
    get_input.main(5, 2022)
    sys.exit(main())

# Win Result
# part1(moves, c_rows)='JRVNHHCSJ'
# part2(moves, c_rows)='GNFBSBJLH'

"""AdventOfCode Day 9"""
from __future__ import annotations
import typing as t
import sys
from api import get_input


def part1(lines: t.List[str]) -> int:
	""""""
	pass


def part2(lines: t.List[str]) -> int:
	""""""
	pass


def main() -> None:
	""" Entrypoint into the solution.
	"""
	with open("input.txt") as my_file:
		lines = my_file.read().splitlines()

		print(f"{part1(lines)=}")
		print(f"{part2(lines)=}")


if __name__ == "__main__":
	get_input.main(9, 2022)
	sys.exit(main())

# Win Result
# part1(lines)=
# part2(lines)=

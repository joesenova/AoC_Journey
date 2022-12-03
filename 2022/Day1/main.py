"""AdventOfCode Day 1"""
from __future__ import annotations
import typing as t
import sys
from api import get_input


def part1(calories_list: t.List[int]) -> int:
	"""Returns Elf with the most amount of Calories
	:param calories_list: list of calories oer Elf
	"""
	return max(calories_list)


def part2(calories_list: t.List[int]) -> int:
	""" Returns the sum of the top 3 elves that has the most calories
	:param calories_list: list of calories oer Elf
	"""
	calories_list.sort()
	return sum(calories_list[-3:])


def process_calories(calories: t.List[str]) -> t.List[int]:
	""" Processes the input data and return the processed data to be sent off to the solution methods
	:param calories: The list of calories to count/sum for each elf
	:returns t.List[int]: list of calories total, sum of all calories per elf, per elf
	"""
	elf_cal_list: t.List[int] = []
	curr_cals = 0
	for cal in calories:
		if not cal:
			elf_cal_list.append(curr_cals)
			curr_cals = 0
		else:
			curr_cals += int(cal)
	return elf_cal_list


def main() -> None:
	""" Entrypoint into the solution.
	"""
	with open("input.txt") as my_file:
		lines = my_file.read().splitlines()
		cal_list = process_calories(lines)

		print(f"{part1(cal_list)=}")
		print(f"{part2(cal_list)=}")


if __name__ == "__main__":
	get_input.main(1, 2022)
	sys.exit(main())

# Win Result
# part1(cal_list)=74198
# part2(cal_list)=209914

"""AdventOfCode Day 11"""
from __future__ import annotations
import typing as t
import sys
from copy import copy

from api import get_input
from more_itertools import chunked


class Monkeys:
	""""""

	def __init__(self):
		""""""
		self.all_monkeys: t.List[Monkey] = []
		self.monkey: t.Union[Monkey, None] = None

	def set_monkey(self, monkey: Monkey):
		""""""
		self.monkey = monkey

	def calc_worry_with_operator(self, worry):
		""""""
		if self.monkey.operator[0] == 'old':
			val1 = worry
		else:
			val1 = int(self.monkey.operator[0])

		if self.monkey.operator[2] == 'old':
			val2 = worry
		else:
			val2 = int(self.monkey.operator[2])

		if self.monkey.operator[1] == '+':
			return val1 + val2
		elif self.monkey.operator[1] == '*':
			return val1 * val2

	def test_worry(self, worry):
		""""""
		if worry % self.monkey.test == 0:
			return self.monkey.to_true_monkey

		return self.monkey.to_false_monkey

	def inspect(self):
		""""""
		items_copy = copy(self.monkey.items)
		for item in self.monkey.items:
			items_copy.remove(item)
			self.monkey.inspections += 1
			worry = self.calc_worry_with_operator(item) // 3
			to_monkey = self.test_worry(worry)
			self.all_monkeys[to_monkey].items.append(worry)
		self.monkey.items = items_copy


class Monkey(Monkeys):
	""""""
	def __init__(self, lines: t.List[str], idx: int):
		""""""
		super().__init__()
		self.name: str = f'Monkey_{idx+1}'
		self.items: t.List[int] = [int(x) for x in lines[1].split(':')[1].strip().split(',')]
		self.operator: t.List[str] = lines[2].split('=')[1].strip().split(' ')
		self.test: int = int(lines[3].split(' ')[-1])
		self.to_monkey_true: int = int(lines[4].split(' ')[-1])
		self.to_monkey_false: int = int(lines[5].split(' ')[-1])
		self.inspections: int = 0


def part1(monkeys: Monkeys, rounds: int):
	for r in range(rounds):
		for monkey in monkeys.all_monkeys:
			monkeys.set_monkey(monkey)
			monkeys.inspect()

	sorted_monkeys = [monkey.inspections for monkey in monkeys.all_monkeys]
	sorted_monkeys.sort()
	monkey_business = sorted_monkeys[-1] * sorted_monkeys[-2]

	return monkey_business


def main() -> None:
	""" Entrypoint into the solution.
	"""
	with open("input.txt") as my_file:
		lines = my_file.read().splitlines()

		# Add all monkeys to Monkeys Class
		monkeys = Monkeys()
		for idx, data in enumerate(chunked(lines, 7)):
			monkey = Monkey(data, idx)
			monkeys.all_monkeys.append(monkey)

		# Run Part with all monkeys
		print(f"{part1(monkeys, 20)=}")


if __name__ == "__main__":
	get_input.main(11, 2022)
	sys.exit(main())

# Win Result
# part1(monkeys)=113232
# part2(monkeys)=

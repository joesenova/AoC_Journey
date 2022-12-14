"""AdventOfCode Day 9"""
from __future__ import annotations
import typing as t
import sys
from copy import copy

from api import get_input
import matplotlib.pyplot as plt


class Segment:
	def __init__(self, name: str):
		self.name = name
		self.x = 0
		self.y = 0
		self.visited_points: t.List[t.Tuple[int, int]] = []
		self.visited_points_set: t.Set[t.Tuple[int, int]] = set()
		self.prev_co_ord: t.List[int, int] = [0, 0]
		# Start by adding the starting point(x,y = 0,0)
		self.visited_points.append(self.get_co_ord())
		self.visited_points_set.add(self.get_co_ord())

	def get_co_ord(self) -> t.Tuple[int, int]:
		return self.get_x(), self.get_y()

	def get_x(self) -> int:
		return self.x

	def get_y(self) -> int:
		return self.y

	def move(self, direction: str, co_ord: t.List[int, int] = None):
		self.prev_co_ord = self.get_co_ord()
		if direction == 'U':
			self.add('y', 1)
		elif direction == 'D':
			self.sub('y', 1)
		elif direction == 'R':
			self.add('x', 1)
		elif direction == 'L':
			self.sub('x', 1)
		elif direction == 'SLIDE':
			self.x += co_ord[0]
			self.y += co_ord[1]

		self.visited_points.append(self.get_co_ord())
		self.visited_points_set.add(self.get_co_ord())

	def add(self, co_ord: str, distance: int):
		if co_ord == 'x':
			self.x += distance
		else:
			self.y += distance

	def sub(self, co_ord: str, distance: int):
		if co_ord == 'x':
			self.x -= distance
		else:
			self.y -= distance


class Rope:
	def __init__(self, segments: int):
		self.start: Segment = Segment('start')
		self.segments: t.List[Segment] = [Segment(f'seg_{s}') for s in range(0, segments)]

	@staticmethod
	def get_diff(head: Segment, segment: Segment):
		"""
		:param head:
		:param segment:
		"""
		t_x, h_x = segment.get_x(), head.get_x()
		t_y, h_y = segment.get_y(), head.get_y()
		x_diff = h_x - t_x
		y_diff = h_y - t_y

		return x_diff, y_diff

	@staticmethod
	def rules_diag(head: Segment, tail: Segment) -> None:
		""""""
		a = [
			(tail.x - 2, tail.y + 1),
			(tail.x - 2, tail.y + 2),
			(tail.x - 1, tail.y + 2),
		]
		b = [
			(tail.x + 1, tail.y + 2),
			(tail.x + 2, tail.y + 2),
			(tail.x + 2, tail.y + 1),
		]
		c = [
			(tail.x - 2, tail.y - 1),
			(tail.x - 2, tail.y - 2),
			(tail.x - 1, tail.y - 2),
		]
		d = [
			(tail.x + 2, tail.y - 1),
			(tail.x + 2, tail.y - 2),
			(tail.x + 1, tail.y - 2),
		]

		if (head.x, head.y) in a:
			tail.move('SLIDE', [-1, 1])
		elif (head.x, head.y) in b:
			tail.move('SLIDE', [1, 1])
		elif (head.x, head.y) in c:
			tail.move('SLIDE', [-1, -1])
		elif (head.x, head.y) in d:
			tail.move('SLIDE', [1, -1])

	def process_moves(self, moves: t.List[str]):
		""""""
		x = 0
		for move in moves:
			x += 1
			move = [m for m in move.split(' ')]
			direction = move[0]
			distance = int(move[1])
			for i in range(0, distance):
				head = self.segments[0]
				head.move(direction)
				for segment in self.segments[1:]:
					x_diff, y_diff = self.get_diff(head, segment)
					if -1 <= x_diff <= 1 and -1 <= y_diff <= 1:
						head = segment
					else:
						if x_diff == 0 and y_diff > 1:
							segment.move('U')
						elif x_diff == 0 and y_diff < -1:
							segment.move('D')
						elif y_diff == 0 and x_diff > 1:
							segment.move('R')
						elif y_diff == 0 and x_diff < -1:
							segment.move('L')
						else:
							self.rules_diag(head, segment)

						head = segment


def part1(moves: t.List[str]):
	rope = Rope(2)
	rope.process_moves(moves)

	for seg in rope.segments:
		# Tail Plot
		txs = [p[0] for p in seg.visited_points]
		tys = [p[1] for p in seg.visited_points]
		plt.plot(txs, tys)
	# Show Combined Plot
	plt.show()

	return len(rope.segments[-1].visited_points_set)


def part2(moves: t.List[str]):
	rope = Rope(10)
	rope.process_moves(moves)

	for seg in rope.segments:
		# Tail Plot
		txs = [p[0] for p in seg.visited_points]
		tys = [p[1] for p in seg.visited_points]
		plt.plot(txs, tys)
	# Show Combined Plot
	plt.show()

	return len(rope.segments[-1].visited_points_set)


def main() -> None:
	""" Entrypoint into the solution.
	"""
	with open("input.txt") as my_file:
		moves = my_file.read().splitlines()
		print(f'{part1(moves)=}')
		print(f'{part2(moves)=}')


if __name__ == "__main__":
	get_input.main(9, 2022)
	sys.exit(main())

# Win Result
# part1(moves)=5907
# part2(moves)=2303

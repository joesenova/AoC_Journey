"""AdventOfCode Day 12"""
from __future__ import annotations
import typing as t
import sys
from api import get_input
import networkx as nx
import matplotlib.pyplot as plt


DICT = {}
LABELS = {}
GRID = None


def to_str(y, x, GRID) -> str:
	""""""
	DICT[f'{y},{x}'] = y, x
	LABELS[f'{y},{x}'] = f"{y, x}: {GRID[y][x]}"
	return f'{y},{x}'


def part1(G, source, destination):
	""""""
	sp = nx.shortest_path(G, f'{source[1]},{source[0]}',  f'{destination[1]},{destination[0]}')
	ys = [int(co_ord.split(',')[0]) for co_ord in sp]
	xs = [int(co_ord.split(',')[1]) for co_ord in sp]
	plt.plot(xs, ys, linestyle='dashed')
	plt.axis('off')
	plt.show()

	return len(sp)


def part2(G, GRID, destination):
	""""""
	lengths = []
	sources = []
	co_ords = {}
	for y, row in enumerate(GRID):
		for x, _ in enumerate(row):
			if row[x] == 1:
				sources.append((x, y))

	for source in sources:
		try:
			distance = nx.shortest_path_length(G, f'{source[1]},{source[0]}', f'{destination[1]},{destination[0]}')
			lengths.append(distance)
			co_ords[distance] = f'{source[1]},{source[0]}'
		except nx.NetworkXNoPath as e:
			continue

	source = co_ords[min(lengths)]
	sp = nx.shortest_path(G, source,  f'{destination[1]},{destination[0]}')
	ys = [int(co_ord.split(',')[0]) for co_ord in sp]
	xs = [int(co_ord.split(',')[1]) for co_ord in sp]
	plt.plot(xs, ys, linestyle='dashed')
	plt.axis('off')
	plt.show()

	return min(lengths)


def main() -> None:
	""" Entrypoint into the solution.
	"""
	G = nx.DiGraph()

	with open("input.txt") as my_file:
		lines = my_file.read().splitlines()
		GRID = [[ord(l)-96 for l in ln] for ln in lines]
		the_map = GRID
		found_start = False
		found_end = False

		for idx_y, row in enumerate(the_map):
			if -13 in the_map[idx_y]:
				found_start = True
				source = the_map[idx_y].index(-13), idx_y
				the_map[source[1]][source[0]] = ord("a")-96

			if -27 in the_map[idx_y]:
				found_end = True
				destination = the_map[idx_y].index(-27), idx_y
				the_map[destination[1]][destination[0]] = ord("z")-96

			if found_start and found_end:
				break
	for y in range(0, len(GRID)):
		for x in range(0, len(GRID[0])):
			c = GRID[y][x]
			if 0 < x < len(GRID[0]) - 1:
				l = GRID[y][x - 1]
				if c + 1 == l or c >= l:
					c_node = to_str(y, x, GRID)
					n_node = to_str(y, x - 1, GRID)
					G.add_edge(c_node, n_node)
				r = GRID[y][x + 1]
				if c + 1 == r or c >= r:
					c_node = to_str(y, x, GRID)
					n_node = to_str(y, x + 1, GRID)
					G.add_edge(c_node, n_node)
			elif x == 0:
				r = GRID[y][x + 1]
				if c + 1 == r or c >= r:
					c_node = to_str(y, x, GRID)
					n_node = to_str(y, x + 1, GRID)
					G.add_edge(c_node, n_node)
			elif x == len(GRID[0]) - 1:
				l = GRID[y][x - 1]
				if c + 1 == l or c >= l:
					c_node = to_str(y, x, GRID)
					n_node = to_str(y, x - 1, GRID)
					G.add_edge(c_node, n_node)

			if 0 < y < len(GRID) - 1:
				d = GRID[y + 1][x]
				if c + 1 == d or c >= d:
					c_node = to_str(y, x, GRID)
					n_node = to_str(y + 1, x, GRID)
					G.add_edge(c_node, n_node)
				u = GRID[y - 1][x]
				if c + 1 == u or c >= u:
					c_node = to_str(y, x, GRID)
					n_node = to_str(y - 1, x, GRID)
					G.add_edge(c_node, n_node)
			elif y == 0:
				d = GRID[y + 1][x]
				if c + 1 == d or c >= d:
					c_node = to_str(y, x, GRID)
					n_node = to_str(y + 1, x, GRID)
					G.add_edge(c_node, n_node)
			elif y == len(GRID) - 1:
				u = GRID[y - 1][x]
				if c + 1 == u or c >= u:
					c_node = to_str(y, x, GRID)
					n_node = to_str(y - 1, x, GRID)
					G.add_edge(c_node, n_node)

	print(f'{part1(G, source, destination)=}')
	print(f'{part2(G, GRID, destination)=}')

	plt.close()


if __name__ == "__main__":
	get_input.main(12, 2022)
	sys.exit(main())

# Win Result
# part1(lines)=426
# part2(lines)=418

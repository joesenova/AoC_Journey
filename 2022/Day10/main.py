"""AdventOfCode Day 10"""
from __future__ import annotations
import typing as t
import sys
from api import get_input


class Cycle:
    def __init__(self, print_for_gif: bool = False):
        self.X = 1
        self.cycle_count = 0
        self.readings = {20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0}
        self.crt_pixels: t.List[int] = []
        self.crt = [[' ' for _ in range(0, 40)] for _ in range(0, 6)]
        self.crt_pixel_x = 0
        self.crt_pixel_y = 0
        self.print_for_gif: bool = print_for_gif

    def run(self, instruction: str):
        instruction = [ins for ins in instruction.split(' ')]
        if instruction[0] == 'noop':
            self.cycle_count += 1
            self.noop()
        if instruction[0] == 'addx':
            self.cycle_count += 2
            self.addx(instruction)

    def _draw_pixel(self):
        """"""
        if self.crt_pixel_x in [self.X - 1, self.X, self.X + 1]:
            char = '\x1b[6;30;42m' + ' ' + '\x1b[0m'
            if self.print_for_gif:
                char = '#'
            self.crt[self.crt_pixel_y][self.crt_pixel_x] = char

        self.crt_pixel_x += 1
        if self.crt_pixel_x == 40:
            self.crt_pixel_x = 0
            self.crt_pixel_y += 1
            if self.crt_pixel_y == 6:
                self.crt_pixel_y = 0

        if self.print_for_gif:
            with open(f"cycle/{self.cycle_count}.txt", mode="w") as f:
                f.write('\n'.join([''.join(line) for line in self.crt]))

    def noop(self):
        if len(self.readings) > 0:
            self.take_reading()
        self._draw_pixel()

    def addx(self, instruction: t.List[str, str]):
        if len(self.readings) > 0:
            self.take_reading()

        x = self.X
        y = self.X + int(instruction[1])
        self.crt_pixels.append(x)

        self._draw_pixel()
        self._draw_pixel()

        self.X = y

    def take_reading(self):
        for a in self.readings.keys():
            if self.cycle_count >= a and self.readings[a] == 0:
                self.readings[a] = self.X * a


def part1(cycle: Cycle):
    return sum(cycle.readings.values())


def part2(cycle: Cycle):
    drawing = []
    for px_line in cycle.crt:
        drawing.append(''.join(px_line))
    return drawing


def device_startup(lines: t.List[str]):
    """"""
    cycle = Cycle(False)

    for line in lines:
        cycle.run(line)

    print(f"{part1(cycle)=}")
    print("part1(cycle)=")
    print('\n'.join(part2(cycle)))


def main() -> None:
    """ Entrypoint into the solution."""
    with open("input.txt") as my_file:
        lines = my_file.read().splitlines()
        device_startup(lines)


if __name__ == "__main__":
    get_input.main(10, 2022)
    sys.exit(main())

# Win Result
# part1(lines)=17840
# ####  ##  #     ##  #  # #    ###   ##
# #    #  # #    #  # #  # #    #  # #  #
# ###  #  # #    #    #  # #    #  # #
# #    #### #    # ## #  # #    ###  # ##
# #    #  # #    #  # #  # #    #    #  #
# #### #  # ####  ###  ##  #### #     ###
# part2(lines):EALGULPG

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 22:18:33 2015

@author: Alex
"""

# ^ north
# v south
# < east
# > west

# how many houses receive at least one present?


def solve(robo_santa_exists):

    santa_pos_x = 0
    santa_pos_y = 0

    roboSantaPosX = 0
    roboSantaPosY = 0

    input_text = open('input/day03.txt').read()

    visited_set = set()
    visited_set.add((santa_pos_x, santa_pos_y))

    is_santas_turn = True

    for char in input_text:

        if char == "^":
            dX = 0
            dY = 1
        elif char == "v":
            dX = 0
            dY = -1
        elif char == "<":
            dX = -1
            dY = 0
        elif char == ">":
            dX = 1
            dY = 0

        if is_santas_turn:
            santa_pos_x += dX
            santa_pos_y += dY
            if (santa_pos_x, santa_pos_y) not in visited_set:
                visited_set.add((santa_pos_x, santa_pos_y))
            if robo_santa_exists:
                is_santas_turn = False
        else:
            roboSantaPosX += dX
            roboSantaPosY += dY
            if (roboSantaPosX, roboSantaPosY) not in visited_set:
                visited_set.add((roboSantaPosX, roboSantaPosY))

            is_santas_turn = True

    return len(visited_set)


part1 = solve(robo_santa_exists=False)
print("%d houses got at least one present when there is no robo-santa" % part1)

part2 = solve(robo_santa_exists=True)
print("%d houses got at least one present when there is a robo-santa" % part2)

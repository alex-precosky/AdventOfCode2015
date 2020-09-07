# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:34:46 2015

@author: Alex
"""

# Santa starts on floor zero
# (   go up one floor
# )   go down one floor

input_text = open('input/day1input.txt').read()

floor = 0
has_reached_basement = False

for i, char in enumerate(input_text):
    if char == ')':
        floor -= 1
        if floor == -1 and has_reached_basement is False:
            has_reached_basement = True

            # +1 since the first character is position 1
            print(f"Basement entered on character position {i+1}")
    elif char == '(':
        floor += 1

print("Santa ends up on floor %d" % (floor,))

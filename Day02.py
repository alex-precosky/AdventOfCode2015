# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 22:04:40 2015

@author: Alex
"""


def calcArea(l, w, h):
    side1 = l*w
    side2 = w*h
    side3 = h*l

    overall = 2*side1 + 2*side2 + 2*side3

    overall += min((side1, side2, side3))

    return overall


def calcRibbon(l, w, h):
    perimeter1 = 2*l + 2*w
    perimeter2 = 2*l + 2*h
    perimeter3 = 2*w + 2*h

    smallestPerimeter = min((perimeter1, perimeter2, perimeter3))

    # add the bow, equal to the cubic feet volume of the present
    bow = l * w * h

    return smallestPerimeter + bow


inFile = open("input/day02.txt", "r")

totalArea = 0
totalRibbon = 0

for line in inFile.readlines():
    strippedLine = line.strip("\n")
    l, w, h = [int(d) for d in strippedLine.split("x")]

    totalArea += calcArea(l, w, h)
    totalRibbon += calcRibbon(l, w, h)

print("Total area: %d" % (totalArea,))
print("Total ribbon: %d" % (totalRibbon,))

# -*- coding: utf-8 -*-
"""
=========================
| CSAPX Lab 2: Bubbles  |
=========================

A program that creates procedural, recursive turtle drawings based on user arguments.

date: 09/09/2017
author: Kevin Becker
"""


import turtle              # all the turtle
from random import random  # random
from math import pi        # pi


COLORS = 'red', 'dark orange', 'yellow', 'lime green', 'dark turquoise', 'purple', 'deep pink'
FULL_CIRCLE_DEGREES = 360  # the total number of degrees in a circle is 360
TURN_AROUND = 180  # the total number of degrees in a half circle is 180


def main():
    """
    This function prompts the user to specify the arguments and then creates the drawing based on their input.

    :return: None
    """
    initial_bubble_radius = int(input("Desired initial bubble radius (100 or more is suggested): "))
    fanout = int(input("Desired fanout (1 or more; a higher number will take longer): "))
    shrinkage = float(input("Desired shrinkage (between 0 and 1, exclusive): "))
    child_probability = float(input("Desired child probability (between 0 and 1, inclusive): "))
    turtle.speed(0)
    area = draw_bubbles(initial_bubble_radius, fanout, shrinkage, child_probability)
    print('The area of your drawing is', area)
    print('Click anywhere on the screen to exit')
    turtle.exitonclick()


def draw_bubbles(radius: float, fanout: int, shrinkage: float, initial_probability: float, current_probability: float = 1.0, count: int = 0)->float:
    """
    This function recursively creates the bubble drawing.

    :param radius: the radius of the initial bubbles being drawn by the function.
    :param fanout: the number of next-level bubbles to potentially be drawn.
    :param shrinkage: the percentage of the bubbles radius to remain in the next level (ex. 100 @ .6 -> 60).
    :param initial_probability: the initial probability of a child bubble being drawn.
    :param current_probability: the current probability of a child bubble being drawn (ex initial_probability ** count + 1).
    :param count: the current level of bubble being drawn.

    :return: float, the area of the bubbles drawn from the returning circle to the furthest down child.
    """
    if random() > current_probability:
        """ The only way to stop creating children is if the random is greater than the current_probability (it will never be true for 1 """
        return 0.0
    else:
        area = 0
        turtle.pencolor(COLORS[count % len(COLORS)])
        turtle.fillcolor(COLORS[count % len(COLORS)])
        turtle.down()
        turtle.begin_fill()
        turtle.circle(radius, FULL_CIRCLE_DEGREES)
        turtle.up()
        turtle.end_fill()
        for _ in range(0, fanout):
            turtle.circle(radius, FULL_CIRCLE_DEGREES/fanout)
            turtle.right(TURN_AROUND)  # we use TURN_AROUND so that the next coming circle actually is
            # ask if keep the 1-shrinkage, or just leave it as is
            area += draw_bubbles((radius * shrinkage), fanout, shrinkage, initial_probability, (initial_probability ** (count+1)), count+1)
            turtle.right(TURN_AROUND)
        area += pi * (radius ** 2)
    return area


if __name__ == '__main__':
    main()
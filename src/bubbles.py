# -*- coding: utf-8 -*-
"""
=========================
| CSAPX Lab 2: Bubbles  |
=========================

A program that creates procedural, recursive turtle drawings based on user arguments.

date: 09/09/2017
author: Kevin Becker
"""


import turtle              # imports all of the turtle
from random import random  # random
from math import pi        # pi


COLORS = 'red', 'dark orange', 'yellow', 'lime green', 'dark turquoise', 'purple', 'deep pink'
FULL_CIRCLE_DEGREES = 360  # the total number of degrees in a circle is 360
TURN_AROUND = 180  # the total number of degrees in a half circle is 180


def main()->None:
    """
    This function prompts the user to specify the arguments and then creates the drawing based on their input.

    :return: None
    """
    initial_bubble_radius = int(input("Desired initial bubble radius (100 or more is suggested): "))  # gathers the initial bubble radius from user
    fanout = int(input("Desired fanout (1 or more; a higher number will take longer): "))  # gathers the fanout from user
    shrinkage = float(input("Desired shrinkage (between 0 and 1, exclusive): "))  # gathers the shrinkage from user
    child_probability = float(input("Desired child probability (between 0 and 1, inclusive): "))  # gathers the child_probability from the user
    turtle.speed(0)  # this sets the speed of the animation to 0 so it doesn't take eleven years to complete it
    area = draw_bubbles(initial_bubble_radius, fanout, shrinkage, child_probability)  # begins the bubblage
    print('The area of your drawing is', area)  # prints the area of the entire circle
    print('Click anywhere on the screen to exit')  # Tells the user they must exit by clicking on the drawing
    turtle.exitonclick()  # actually makes the previous print truthful


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
    if random() > current_probability:  # base case ending a child bubble tree
        return 0.0
    else:  # all of this is only run if the tree continues down
        area = 0  # set the area to 0 (just so when area += (stuff) is run, python doesn't complain)
        turtle.pencolor(COLORS[count % len(COLORS)])  # sets the pen color to the correct color based on the count
        turtle.fillcolor(COLORS[count % len(COLORS)])  # sets the fill color to the same color
        turtle.down()  # places the pen down (this happens so that the border of the bubbles don't look ugly since it goes around twice)
        turtle.begin_fill()  # begins filling the polygons being created
        turtle.circle(radius, FULL_CIRCLE_DEGREES)  # makes a circle with a radius of the radius parameter
        turtle.up()  # picks the pen up (for the next part, it becomes more obvious why later on)
        turtle.end_fill()  # stops filling
        for _ in range(0, fanout):
            turtle.circle(radius, FULL_CIRCLE_DEGREES/fanout)  # goes around the circle 360/fanout degrees to begin the child stage
            turtle.right(TURN_AROUND)  # we use TURN_AROUND so that the next coming circle actually is oriented correctly
            area += draw_bubbles((radius * shrinkage), fanout, shrinkage, initial_probability, (initial_probability ** (count+1)), count+1)  # makes a child tree
            turtle.right(TURN_AROUND)  # turns right again so it continues on the correct path after this child tree is complete
        area += pi * (radius ** 2)  # adds to the area the area of the current circle
    return area  # returns the area


# does the thing that runs main if no arguments are given (should be run every time since I didn't implement a command line method)
if __name__ == '__main__':
    main()
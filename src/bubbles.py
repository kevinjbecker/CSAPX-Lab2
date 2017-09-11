import turtle
from random import random
from math import pi


def main():
    initial_bubble_radius = 100  # int(input("Desired initial bubble radius (100 or more is suggested): "))
    fanout = 2  # int(input("Desired fanout (1 or more; a higher number will take longer): "))
    shrinkage = .75  # float(input("Desired shrinkage rate (between 0 and 1, exclusive): "))
    child_probability = .25  # float(input("Desired child probability (between 0 and 1, inclusive): "))
    area = draw_bubbles(initial_bubble_radius, fanout, shrinkage, child_probability)
    print('The area of your drawing is', area)
    print('Click anywhere on the screen to exit')
    turtle.exitonclick()


if __name__ == '__main__':
    main()
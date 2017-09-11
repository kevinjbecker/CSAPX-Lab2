import turtle
from random import random
from math import pi


def main():
    initial_bubble_radius = int(input("Desired initial bubble radius (100 or more is suggested): "))
    fanout = int(input("Desired fanout (1 or more; a higher number will take longer): "))
    shrinkage = float(input("Desired shrinkage (between 0 and 1, exclusive): "))
    child_probability = float(input("Desired child probability (between 0 and 1, inclusive): "))
    turtle.speed(0)
    area = draw_bubbles(initial_bubble_radius, fanout, shrinkage, child_probability)
    print('The area of your drawing is', area)
    print('Click anywhere on the screen to exit')
    turtle.exitonclick()


def draw_bubbles(radius: float, fanout: int, shrinkage: float, child_probability: float, current_probability: float = 1.0, count: int = 0)->float:
    colors = 'red', 'dark orange', 'yellow', 'lime green', 'dark turquoise', 'purple', 'deep pink'
    full_circle_degrees = 360  # the total number of degrees in a circle is 360
    half_circle_degrees = 180  # the total number of degrees in a half circle is 180
    random_num = random()
    if int(radius) <= 0 or (random_num > current_probability):
        """ so this only checks current_probability (and not the 
        count as well for the first time because current_probability is default at 1.0 for the first run
        which random could never get to it """
        return 0.0
    else:
        area = 0
        turtle.pencolor(colors[count % len(colors)])
        turtle.fillcolor(colors[count % len(colors)])
        turtle.down()
        turtle.begin_fill()
        turtle.circle(radius, full_circle_degrees)
        turtle.up()
        turtle.end_fill()
        for _ in range(0, fanout):
            turtle.circle(radius, full_circle_degrees/fanout)
            turtle.right(half_circle_degrees)  # we use half_circle_degrees so that the next coming circle actually is
            # ask if keep the 1-shrinkage, or just leave it as is
            area += draw_bubbles((radius * shrinkage), fanout, shrinkage, child_probability, (child_probability ** (count+1)), count+1)
            turtle.right(half_circle_degrees)
        area += pi * (radius ** 2)
    return area


if __name__ == '__main__':
    main()
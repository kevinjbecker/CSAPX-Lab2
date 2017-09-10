import turtle
import random


def main():
    initial_bubble_radius = int(input("Desired initial bubble radius (100 or more is suggested): "))
    fanout = int(input("Desired fanout (1 or more; a higher number will take longer): "))
    shrinkage = float(input("Desired shrinkage rate (between 0 and 1, exclusive): "))
    child_probability = float(input("Desired child probability (between 0 and 1, inclusive): "))
    area = draw_bubbles(initial_bubble_radius, fanout, shrinkage, child_probability)
    print(area)


def draw_bubbles(radius: int, fanout: int, shrinkage: float, child_probability: float, count: int = 0)->float:
    colors = 'chartreuse', 'salmon', 'cyan', 'turquoise', 'lavender', 'tan'
    full_circle_degrees = 360 # the total number of degrees in a circle is 360
    if radius <= 0:
        return 0.0
    else:
        area = 0
        turtle.fillcolor(colors[count])
        turtle.begin_fill()
        turtle.circle(radius, full_circle_degrees + (full_circle_degrees / fanout))
        turtle.end_fill()
        area += draw_bubbles((radius * shrinkage), fanout, shrinkage, child_probability, count+1)


if __name__ == '__main__':
    main()
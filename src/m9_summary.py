"""
An exercise that summarizes what you have learned in this Session.

Authors: David Mutchler, Yiji Zhang, Mark Hays, Derek Whitley, Vibha Alangar,
         Matt Boutell, Dave Fisher, Sriram Mohan, Mohammed Noureddine,
         Amanda Stouder, Curt Clifton, Valerie Galluzzi, their colleagues and
         henry ahmed.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
# done: 2.
#   Define a complete program that:
#     a.  Imports  rosegraphics
#     b.  Defines a   main   function that:
#          - Constructs a TurtleWindow.
#          - Calls the function that YOU define (see next bullet, below) TWICE
#              (with different arguments each time) to TEST your function.
#          - Asks the TurtleWindow to wait for a mouse click, then close.
#     c.  Defines another function that takes three parameters:
#             a SimpleTurtle, a string that represents a color,
#             and an integer for the distance to move (in pixels),
#         and causes the SimpleTurtle to:
#           - Move backward the given distance.
#           - Change its Pen's color to the given color.
#           - Turn left 90 degrees.
#           - Move forward twice the given distance.
#     d.  Calls main.
###############################################################################
import rosegraphics as rg


def main():
    window = rg.TurtleWindow()
    move(rg.SimpleTurtle(), 30, 'red')
    move(rg.SimpleTurtle(), 50, 'green')
    window.close_on_mouse_click()


def move(turtle, distance, color):
    turtle.backward(distance)
    turtle.pen.color = color
    turtle.left(90)
    turtle.forward(2*distance)


main()

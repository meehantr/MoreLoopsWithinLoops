"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Thomas Meehan.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # done: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    original_top_left = rectangle.get_upper_left_corner()
    original_bottom_right = rectangle.get_lower_right_corner()

    top_left = original_top_left.clone()
    bottom_right = original_bottom_right.clone()

    height = rectangle.get_height()
    width = rectangle.get_width()

    for i in range(n):
        for j in range(i + 1):
            rectangle = rg.Rectangle(top_left, bottom_right)
            rectangle.attach_to(window)

            top_left.x = top_left.x + width
            bottom_right.x = bottom_right.x
        top_left.x = original_top_left.clone().x - ((width / 2) * i)
        top_left.y = original_top_left.clone().y - (height * i)
        bottom_right.x = original_bottom_right.clone().x - ((width / 2) * i)
        bottom_right.y = original_bottom_right.clone().y - (height * i)

    window.render()


# ----------------------------------------------------------------------


# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()

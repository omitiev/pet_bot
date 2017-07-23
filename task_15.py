# Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости.
# Каждая окружность задается координатами центра и радиусом.
# r = sqrt( sqr(Xa-Xb) + sqr(Ya-Yb) );

import math
import default

default.start(15)

def is_crossing(radiuses, distance):
    if radiuses <= distance:
        print("The circles with corresponding coordinates and radiuses don't cross")
    else:
        print("The circles with corresponding coordinates and radiuses cross")

circle_coordinates_1 = str(input("Please enter coordinates of center 1-st circle and radius (e.g. 2, 9, 9): "))
circle_coordinates_1_lst = circle_coordinates_1.split(',')
circle_1_x = int(circle_coordinates_1_lst[0])
circle_1_y = int(circle_coordinates_1_lst[1])
radius_1 = int(circle_coordinates_1_lst[2])
circle_coordinates_2 = str(input("Please enter coordinates of center 2-nd circle and radius (e.g. 6, 7, 3): "))
circle_coordinates_2_lst = circle_coordinates_2.split(',')
circle_2_x = int(circle_coordinates_2_lst[0])
circle_2_y = int(circle_coordinates_2_lst[1])
radius_2 = int(circle_coordinates_2_lst[2])
dist_btw_circles = math.sqrt((circle_1_x - circle_2_x)**2 + (circle_1_y - circle_2_y)**2)
r_sum = radius_1 + radius_2

is_crossing(r_sum, dist_btw_circles)

default.end()
import default
from dot import Dot
from circle import Circle


default.start(35)

if __name__ == "__main__":
    dot_coordinates = (input("Please enter X and Y coordinates for the dot (e.g. 2,9): ")).split(',')
    dot = Dot(int(dot_coordinates[0]), int(dot_coordinates[1]))
    dot_coord = Dot.get_coordinates(dot)
    dot.print_info()
    circle_coordinates = (input("Please enter X and Y coordinates for the circle (e.g. 2,9): ")).split(',')
    circle_radius = input("Please enter radius for the circle: ")
    circle = Circle(int(circle_coordinates[0]), int(circle_coordinates[1]), int(circle_radius))
    circle.print_info()
    if Circle.is_dot_in_circle(circle, dot_coord[0], dot_coord[1]):
        print("Inside")
    else:
        print("Outside")


default.end()


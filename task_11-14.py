import math
# Написать функцию, которая будет переводить градусы в радианы.
# Используя эту функцию вывести на экран значения косинусов углов в 60, 45 и 40 градусов.
# print("==========================================================")
# print("task 11")
# print("==========================================================")
#
# def find_rad(x):
#     rad = math.radians(x)
#     return rad
# def find_cos(x):
#     cos = math.cos(x)
#     return cos
# d_sym = '\u00b0'
# print(d_sym)
#
# d_angle_1 = int(input("Enter the value in degree for angle 1: "))
# d_angle_2 = int(input("Enter the value in degree for angle 2: "))
# d_angle_3 = int(input("Enter the value in degree for angle 3: "))
# print("Now we will find the value of cosine for corresponding angles: %d%s , %d%s , %d%s" % (d_angle_1, d_sym, d_angle_2, d_sym, d_angle_3, d_sym))
# cos_angle_1 = find_cos(find_rad(d_angle_1))
# cos_angle_2 = find_cos(find_rad(d_angle_2))
# cos_angle_3 = find_cos(find_rad(d_angle_3))
# print("If I'm right the answers are: \n %.16f for angle 1 \n %.16f for angle 2 \n %.16f for angle 3" % (cos_angle_1,cos_angle_2, cos_angle_3))

# Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа,
# введенного пользователем в консоли, без использования операторов цикла.
# print("==========================================================")
# print("task 12")
# print("==========================================================")
#
# def sum_num(x):
#     sum = int(list(x)[0]) + int(list(x)[1]) + int(list(x)[2])
#     return sum
#
# num = str(input("Enter the number which contain 3 digit: "))
# if len(num) == 3:
#     result = sum_num(num)
#     print("The sum of digits of your number is %d" % result)
# elif len(num) < 3:
#     print("Sorry, your number contain less than 3 digit")
# else:
#     print("Sorry, your number contain more than 3 digit")

# Пользователь вводит длины катетов прямоугольного треугольника.
# Написать функцию, которая вычислит и выведет на экран площадь треугольника и его периметр.
# S=1/2ab
# P=a+b+c

print("==========================================================")
print("task 13")
print("==========================================================")

def square_right_triangle(x , y):
    s = 1/2*x*y
    return s

def perimeter_right_triangle(x, y, z):
    per = x + y + z
    return per

def hypotenuse(x, y):
    hypo = math.sqrt((x ** 2) + (y ** 2))
    return hypo

cat1 = float(input("Enter the value for catheter 1: "))
cat2 = float(input("Enter the value for catheter 2: "))
print("OK. Lets find square and perimeter of your right triangle with catheters %.2f and %.2f" % (cat1, cat2))
square = square_right_triangle(cat1, cat2)
perimeter = perimeter_right_triangle(cat1, cat2, hypotenuse(cat1, cat2))
print("If I'm right the triangle square is %.2f and triangle perimeter is %.2f" % (square, perimeter))


# Написать функцию, которая будет проверять четность некоторого числа.
print("==========================================================")
print("task 14")
print("==========================================================")
import math
# Написать функцию, которая будет переводить градусы в радианы.
# Используя эту функцию вывести на экран значения косинусов углов в 60, 45 и 40 градусов.
print("==========================================================")
print("task 11")
print("==========================================================")

def find_rad(x):
    rad = math.radians(x)
    return rad
def find_cos(x):
    cos = math.cos(x)
    return cos

d_angle_1 = int(input("Enter the value in degree for angle 1: "))
d_angle_2 = int(input("Enter the value in degree for angle 2: "))
d_angle_3 = int(input("Enter the value in degree for angle 3: "))
print("Now we will find the value of cosine for corresponding angles")
r_angle_1 = find_rad(d_angle_1)
cos_angle_1 = find_cos(r_angle_1)
r_angle_2 = find_rad(d_angle_2)
cos_angle_2 = find_cos(r_angle_2)
r_angle_3 = find_rad(d_angle_3)
cos_angle_3 = find_cos(r_angle_3)
print("If I'm right the answers are: \n %.16f for angle 1 \n %.16f for angle 2 \n %.16f for angle 3" % (cos_angle_1,cos_angle_2, cos_angle_3))

# Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа,
# введенного пользователем в консоли, без использования операторов цикла.
print("==========================================================")
print("task 12")
print("==========================================================")




# Пользователь вводит длины катетов прямоугольного треугольника.
# Написать функцию, которая вычислит и выведет на экран площадь треугольника и его периметр.
print("==========================================================")
print("task 13")
print("==========================================================")





# Написать функцию, которая будет проверять четность некоторого числа.
print("==========================================================")
print("task 14")
print("==========================================================")
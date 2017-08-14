# 9. Нормировать одномерный массив случайных чисел.
# Нормирование означает приведение всех значений массива к интервалу [-1;1],
# причем максимальное абсолютное значение элементов после нормирование должно быть равно 1.
# Например, последовательность {-5, 3, 4} после нормирование будет выглядеть {-1, 0.6, 0.8}

import default
import pprint


default.start(9)


def return_max(lst):
    [lst.append(i*(-1)) for i in lst if i < 0]
    return max(lst)


def set_int_value(lst):
    d = {}.fromkeys(lst)
    for elem in lst:
        if elem in d:
            d[elem] = round((elem/return_max(lst)), 4)
    return d


base_lst = default.create_random_lst(10)
print("Base list is: ", base_lst)
print("The interval values for the list are: ")
pprint.pprint(set_int_value(base_lst))


default.end()

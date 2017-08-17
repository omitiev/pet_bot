# 11. В двумерном массиве отсортировать четные столбцы по возрастанию, а нечетные - по убыванию


import default
import random


default.start(11)

def create_random_matrix(lower_bound, upper_bound, rows, columns):
    matrix = [[random.randint(lower_bound,upper_bound) for j in range(rows)]for i in range(columns)]
    return matrix

def sort_matrix(matrix):
    for i in range(len(matrix)):
        if default.is_odd(i):
            matrix[i].sort()
        else:
            matrix[i].sort(reverse= True)
    return matrix


min_value = int(input("Print enter min value for nested list: "))
max_value = int(input("Print enter max value for nested list: "))
mtrx_rows = int(input("Print enter a number of items for internal lists: "))
mtrx_columns = int(input("Print enter a number of items for main list: "))
mtrx = create_random_matrix(min_value, max_value, mtrx_rows, mtrx_columns)
print("Your not sorted nested list is: ", (mtrx))
print("Your sorted nested list is:     ", sort_matrix(mtrx))


default.end()

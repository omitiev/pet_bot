# Написать функцию для поиска разницы сумм всех четных и всех нечетных чисел списка.
# Т.е. от суммы четных чисел вычесть сумму нечетных чисел в списке.

import default
import random


default.start(20)


def diff_btw_the_sums_of_even_and_odd(min_v, max_v, amount):
    total_1 = 0
    total_2 = 0
    for i in range(amount):
        num = random.randint(min_v, max_v)
        if default.is_even(num):
            total_1 += num
        else:
            total_2 += num
    print("""
        The sum of even numbers in a range is %i
        The sum of odd numbers in a range is %i""" % (total_1, total_2))
    diff = total_1 - total_2
    print("The difference between the sums of even and odd is %i" % (diff))

min_value = int(input("Please enter min value for the range:"))
max_value = int(input("Please enter max value for the range:"))
amount = int(input("Please enter amount of selection:"))
if min_value > max_value or amount <= 0:
    print("Something went wrong - check the entered data")
else:
    diff_btw_the_sums_of_even_and_odd(min_value, max_value, amount)


default.end()
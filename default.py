import random

def start(task):
    print('='*70)
    print('Task', task)
    print('='*70)

def end():
    print('=' * 70)
    print('This task was decided by Oleksii Mitiev. Thank you for your attention.')
    print('=' * 70)

def is_even(x):
    return x % 2 == 0

def is_odd(x):
    return x % 2 != 0

def random_list(list1):
    list2 = list(set(list1))
    random.shuffle(list2)
    return list2
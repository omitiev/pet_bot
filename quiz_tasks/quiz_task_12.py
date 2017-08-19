# 12. Для проверки остаточных знаний учеников после летних каникул, учитель младших классов решил начинать каждый урок с того,
# чтобы задавать каждому ученику пример из таблицы умножения, но в классе 15 человек, а примеры среди них не должны повторяться.
# В помощь учителю напишите программу, которая будет выводить на экран 15 случайных примеров из таблицы умножения
# (от 2*2 до 9*9, потому что задания по умножению на 1 и на 10 — слишком просты).
# При этом среди 15 примеров не должно быть повторяющихся (примеры 2*3 и 3*2 и им подобные пары считать повторяющимися)


import default
import random


default.start(12)


def create_list_with_tasks():
    tasks_dict={}
    for i in range(2, 10):
        for j in range(2, 10):
            task = str(i)+'*'+str(j)
            result = i*j
            tasks_dict[task] = result
    return tasks_dict


def select_random_tasks(all, ammount):
    full_list_of_tasks = list(all.keys())
    list_of_tasks = []
    while len(set(list_of_tasks)) < ammount:
        list_of_tasks.append(random.choice(full_list_of_tasks))
    return set(list_of_tasks)


f_tasks = create_list_with_tasks()
rand_tasks = select_random_tasks(f_tasks, 15)
print("Today we should decide next tasks: ", rand_tasks)


default.end()

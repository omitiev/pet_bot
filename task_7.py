# Преобразовать строку с американским форматом даты в европейский. Например, "05.17.2016" преобразуется в "17.05.2016"
'''
print ("==========================================================")
print ("task 7")
print ("==========================================================")

us_date = str(input("Please, enter a date in american way MM.DD.YYYY"))
print ("In US format the date is", us_date)
lst1=us_date.split(".")
eu_date = str(lst1[1])+'.'+str(lst1[0])+'.'+str(lst1[2])
print ("In EU format the date will be", eu_date)
'''

#Написать программу, которая берет две строки и помещает первую строку в середину второй. Результат помещается в середину первой. Длину строки можно получить с помощью функции len().

print ("==========================================================")
print ("task 8")
print ("==========================================================")

str1 = str(input("Please, enter any text"))
str2 = str(input("OK, now enter any other text"))
print ("Thanks! Your texts are: \n1.", str1, "\n2.", str2)
print(len(str2))
#print(new_str)


# print(2+5)
#
# print(11111 * 1111111)
#
# print (40//8)
#
# print (42//8)
#
# #print (42// (4 + 2 * (-2)))
#
# print(2014**14)
#
# print(1.2345e-3)
#
# print(2014.0**14)
#
# print(7/3)
#
# print(7//3)
#
# #https://github.com/snfrolov/Python-course-stepik.org-/blob/master/1.-Operators.-Variables.-Data-types.-Conditions/1.6
#
# print(int(-1.6))
#
# #print(9**19 - int(float(9**19)))

# a = (9**19)
# b = (int(float(9**19)))
# с = (a - b)
# print (с)
# с +=1
# print("Итого:",с)

# Ввод даты и имени
# name = input('Enter your name: ')
# print('Привет,', name)
# date_day = input('Введите дату вашего рождения DD: ')
# date_month = input('Введите месяц вашего рождения прописью: ')
# date_year = input('Введите год вашего рождения YYYYY: ')
# print('Привет,', name, 'вы родились:',date_day,date_month,date_year,'года Все верно?')

# X = int(input())
# Y = int(input())
# print(X*60 + Y)

# X = int(input())
# print(int(X // 60))
# print(int(X % 60))

# x = int(input())
# h = int(input())
# m = int(input())
# print((60*h+m+x) // 60)
# print((60*h+m+x) % 60)

# a = int(input())
# print (a >= 10 and a <=100)
# print (10 <= a < 100)

# x = 5
# y = 10
# print (y > x * x or y >= 2 * x and x < y)

# a = True
# b = False
# print (a and b or not a and not b)

# x = int(input())
# if x % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# Определяем високосный год или нет
x = int(input())
if ((x % 4 == 0) and not (x % 100 == 0)) or (x % 400 == 0):
    print("Високосный")
else:
    print("Обычный")
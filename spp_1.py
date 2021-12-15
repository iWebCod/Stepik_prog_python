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
# name = input('Введите ваше имя: ')
# print('Привет,', name)
# date_day = input('Введите дату вашего рождения (DD): ')
# date_month = input('Введите месяц вашего рождения (MM): ')
# date_year = input('Введите год вашего рождения (YYYYY): ')
# print('Привет,', name + ', ' + 'вы родились:',date_day +'.'+ date_month +'.'+ date_year,'г. Все верно?')

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
# x = int(input())
# if ((x % 4 == 0) and not (x % 100 == 0)) or (x % 400 == 0):
#     print("Високосный")
# else:
#     print("Обычный")

# В Институте биоинформатики между информатиками и биологами устраивается соревнование. Победителям соревнования достанется большой и вкусный пирог. В команде биологов aa человек, а в команде информатиков — bb человек.
# Нужно заранее разрезать пирог таким образом, чтобы можно было раздать кусочки пирога любой команде, выигравшей соревнование, при этом каждому участнику этой команды должно достаться одинаковое число кусочков пирога. И так как не хочется резать пирог на слишком мелкие кусочки, нужно найти минимальное подходящее число.
# Напишите программу, которая помогает найти это число.
# Программа должна считывать размеры команд (два положительных целых числа aa и bb, каждое число вводится на отдельной строке) и выводить наименьшее число dd, которое делится на оба этих числа без остатка.

# a = int(input())
# b = int(input())
# c = a
# while ((a % b) != 0):
#     a += c
# print(a)

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     print(i)
#     if s > 15:
#         continue
#     i = i + 1

# Напишите программу, которая считывает целые числа с консоли по одному числу в строке.
#
# Для каждого введённого числа проверить:
# если число меньше 10, то пропускаем это число;
# если число больше 100, то прекращаем считывать числа;
# в остальных случаях вывести это число обратно на консоль в отдельной строке.
# while True:
#   x = int(input())
#   if x < 10 and x < 100:
#     continue
#   elif x > 100:
#     break
#   print(x)

# import time
# password = '09121421'
#
# pass_int = int(password)
# t1 = time.time()
# for i in range(0, 10 ** len(password)):
#     if i == pass_int:
#         print('Пароль = "{:0{w}}"'.format(i, w=len(password)))
#         break
# print('Время в секундах =', time.time() - t1)
# print('Длина пароля =',len(password),'знаков')

'''Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.

Напишите программу, на вход которой даются четыре числа aa, bb, cc и dd, каждое в своей строке. Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a; b][a;b] на все числа отрезка [c;d][c;d].

Числа aa, bb, cc и dd являются натуральными и не превосходят 10, a \le ba≤b, c \le dc≤d.

Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции. Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и stroka таблицы.'''


# a = int(input())
# # b = int(input())
# # c = int(input())
# # d = int(input())
# # print('\t',end = '')
# # for i in range(c,d+1):
# #     print(str(i)+'\t',end = '')
# # print()
# # for i in range(a,b+1):
# #     print(str(i)+'\t',end = '')
# #     for k in range(c,d+1):
# #         print(str(i * k)+'\t',end = '')
# #     print()

# Напишите программу, которая считывает с клавиатуры два числа a и bb, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b][a;b], которые кратны числу 33.
# В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [-5; 12][−5;12]. Всего чисел, делящихся на 33, на этом отрезке 66: -3, 0, 3, 6, 9, 12−3,0,3,6,9,12. Их среднее арифметическое равно 4.54.5
# На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 33.﻿

# a, b = (int(i) for i in input().split())
# s=0
# k=0
# for j in range(a,b+1):
#     if j%3==0:
#         s+=j
#         k+=1
# print(s/k)

# Подсчет символов в строке
# fam = input()
# print(fam.count('А')) #функция count

# a=input().lower()
# print(((a.count('g')+a.count('c'))/len(a))*100)

# stroka = input()
# dlina = len(stroka)
# i=0
# schetchik=1
# kod = ''
# while i< (dlina - 1):
#     if stroka[i] == stroka[i+1]:
#         schetchik += 1
#     else:
#         kod = kod + stroka[i] + str(schetchik)
#         schetchik=1
#     i+=1
# print(kod + stroka[i] + str(schetchik))

# stroka=[int(i) for i in input().split()]
# if len(stroka)==1:
#     print(stroka[0])
# else:
#     for i in range(len(stroka)-1):
#         stroka2=stroka[i-1]+stroka[i+1]
#         print(str(stroka2),end=" ")
#     posl_element=stroka[0]+stroka[-2]
#     print(posl_element)

# stroka=sorted([int(i) for i in input().split()])
# for i in stroka:
#     if stroka.count(i)>1:
#         print(i,end=" ")
#         for j in range(stroka.count(i)-1):
#             stroka.remove(i)

# arr[col_len-1][row_len]+arr[col_len+1][row_len]+arr[col_len][row_len-1]+arr[col_len][row_len+1]
# col_len=0
# row_len=1
# md=""
# arr=[]
# a0,b0,an,bn=0,0,0,0
# # формируем матрицу
# while row_len>0: # бесконечный цикл
#     md=input().split() # разбиваем строку на элементы для добавления в список
#     if "end" in md:
#         row_len-=1
#         break # если в строке попалось END, закрываем список
#     else:
#         if row_len==1:
#             col_len=len(md)
#         row_len+=1 # счетчик
#         arr.append(md) # добавляем элементы строки в двухмерный список
# # формируем нулевую матрицу
# arr_sum = [[0 for j in range(col_len)] for i in range(row_len)]
# # определяем в матрице элементы из суммы смежных
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if i-1<0: a0=row_len-1
#         else: a0=i-1
#         if j-1<0: b0=col_len-1
#         else: b0=j-1
#         if i+1>row_len-1: an=0
#         else: an=i+1
#         if j+1>col_len-1: bn=0
#         else: bn=j+1
#         arr_sum[i][j]= int(arr[a0][j])+int(arr[an][j])+int(arr[i][b0])+int(arr[i][bn])
# # выводим новую матрицу на экран
# for row in arr_sum:
#     for elem in row:
#         print(elem, end=' ')
#     print()

#Пример функции
# def f(n):
#     return n * 10 + 5
# print(f(f(f(10))))
# while 1:
#     try:
#         first_num = float(input('Напишите первое число: '))
#         answer = input('выберите операцию + - * /')
#         second_num = float(input('Напишите второе число: '))
#     except:
#         print('пожалуйста вводите только числа')
#         continue
#
#     if answer == '+':
#         print(first_num+second_num)
#     elif answer == '-':
#         print(first_num-second_num)
#     elif answer == '*':
#         print(first_num*second_num)
#     elif answer == '/':
#         print(first_num/second_num)
#     else:
#         print('Что то пошло не так! ')
#
#     ext_calc = str(input('Желаете продолжить y/no: '))
#     if ext_calc == 'y':
#         continue
#     else:
#         break
#
#
#

# a = 12
# b = "hello"
# try:
#     c = a+b
#     print(c)
# except:
#     print('Число со строкой нельзя сложить')

# #filter - показывает элементы по какой либо фильтрации,
# # map-показывает элемент по булевской системе
# numbers = [1,2,3,4,5,6]
# a = list(list(lambda x: x%2==0, numbers ))
# print(a)
#
# word = ['apple', 'banana', 'tomato', 'peach', 'pen',
#         'words']
# b = list(map(lambda x: len(x)==5, word ))
# print(b)


# plus = lambda x,y: x+y
#
# print(plus(2,3))

# def plus(a,b):
#     return  a+b
#
# print(plus(2,2))

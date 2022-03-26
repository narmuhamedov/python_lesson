#
# import turtle
#
# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor('black')
# t.pencolor('red')
#
# a = 0
# b = 0
# t.speed(0)
# t.penup()
# t.goto(0, 200)
# t.pendown()
# while (True):
#     t.forward(a)
#     t.right(b)
#     a += 3
#     b += 1
#     if b == 210:
#         break
#     t.hideturtle()
#
# turtle.done()
#



# univer = []
# tehnikum = []
# army = []
# married = []
#
# abiturient = [
#     {'name':'Muhammad Ali','OPT':110,'gender':'male'},
#     {'name': 'Sultan', 'OPT': 120, 'gender': 'male'},
#     {'name': 'Akram', 'OPT': 80, 'gender': 'male'},
#     {'name': 'Aidana', 'OPT': 40, 'gender': 'female'},
#     {'name': 'Emir', 'OPT': 30, 'gender': 'male'},
#     {'name': 'Jasmin', 'OPT': 70, 'gender': 'female'},
#     {'name': 'Aijan', 'OPT': 200, 'gender': 'female'},
#
# ]
#
# def all_abit(lst):
#     for i in lst:
#         for k,v in i.items():
#             print(f'{k}:{v}')
# all_abit(abiturient)
#
# def selection(lst, univer:list, tehnikum:list, army:list,
#               married:list):
#     for i in lst:
#         if i['OPT']>109:
#             univer.append(i)
#         elif i['OPT']<60 and i['gender']=='male':
#             army.append(i)
#         elif i['OPT']<60 and i['gender']=='female':
#             married.append(i)
#         else:
#             tehnikum.append(i)
# selection(abiturient,univer,tehnikum, army, married)
# print(f'В универ-{univer}')
# print(f'В армию-{army}')
# print(f'В техникум-{tehnikum}')
# print(f'Замуж-{married}')
#






# def menu(**kwargs):
#     return kwargs
# monday = menu(breakfast='Яичница', lunch='Бивштекс',
#               dinner='Рис по китайски')
# print(monday)


# def summa(*args):
#     return sum(args)
# print(summa(1,2,3,4,5,6,7,5,5,4,3,3,3))




#Пример с input
# def plus(a,b):
#     print(a+b)
# plus(int(input('Одно число')) , int(input('Второе число')))


#Пример с return
# def plus(a,b,c=2):
#     return a+b+c
# print(plus(1,2,3))


#Аргументы по умолчанию указываются всегда в конце
# def plus(a,b,c=2):
#     print(a+b+c)
# plus(1,2,3)



#Создание функции a,b это параметры
# def plus(a,b):
#     print(a+b)
#
# plus(3,3)
# plus(12,12)

#
# person = ('Aijan', 18, 12.11, 2003, 'Draw', True)
# print(type(person))
# person1 = list(person)
# person1[1] = 19
# print(person1)
# person2 = tuple(person1)
# print(person2)
# print(type(person2))
#

# nominal = (1,3,5,10,20,50,100,200,500,'1k','2k',
#            '5k',1,3,1,1,1,1,1)
# print(nominal.count(1))
# print(nominal.index('5k'))

# persons = ['Ivanov Ivan', 'Asanov Asan', 'Mirbrekov Mirbek', 'Nurlanov Nurlan','Adiletov Adilet']
# programmer = []
# kfc = []
# ufc = []
# club_dancer = []
# drink_vodka = []
#
# persons.append('Man')
# persons.remove('Ivanov Ivan')
# del persons[0]
#
# persons[0]='Aijanova Aijan'
# print(persons)
#
# programmer.append(persons.pop(0))
# print(programmer)
#








# ru = 'белый', 'синий', 'красный'
# gr = 'красный', 'желтый', 'черный'
# ourcolors = []
# while len(ourcolors)!=3:
#     cls = str(input('введите цвет флага: '))
#     ourcolors.append(cls)
#     print(cls)
#     print(ourcolors)
#
# if tuple(ourcolors)==ru:
#     print('This Flag Russia')
# elif tuple(ourcolors)==gr:
#     print('This Flag Germany')
# else:
#     print('This Flag Unknown')





# data_types = ['apples', 'tomato', 123, 321, 12.3, 4.32, True, False]
# data_types2 = ['Hello', 'World', 'Python', 'Django']
# #метод расширения
# data_types.extend(data_types2)
# print(data_types)

#метод перемещения
# data_types2.append(data_types.pop(2))
# print(data_types2)


#метод обновления
# data_types[1] = 'peach'
# print(data_types)
#методы удаления
# data_types.remove(False)
# del data_types[0]
# data_types.clear()

# #Методы добавления списка
# data_types.append('Hello World')
# data_types.insert(1, 'name')
# print(data_types)
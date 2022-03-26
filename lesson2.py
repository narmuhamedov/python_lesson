coca_cola = 3
cola_0_5 = 0
cola_1 = 0
cola_1_5 = 0
cola_2 = 0

while 1:
    coca_cola -= 1
    answer = float(input('Какой литр? 0.5, 1.0, 1.5, 2.0 - '))
    if answer == 0.5:
        cola_0_5+=1
        continue
    elif answer == 1.0:
        cola_1 += 1
        continue
    elif answer == 1.5:
        cola_1_5 += 1
        continue
    elif answer == 2.0:
        cola_2 +=1
    else:
        print(f'Общее кол {coca_cola}\n'
                f'0.5: {cola_0_5}\n'
                f'1.0: {cola_1}\n'
                f'1.5: {cola_1_5}\n'
                f'2.0: {cola_2}')









# while 1:
#     color = str(input('Какой цвет? '))
#     if color == 'Красный':
#         print('STOP')
#
#     elif color == 'Желтый':
#         print('STOP OR GO!')
#
#     elif color == 'Зеленый':
#         print('GO!')
#     else:
#         print('look at situation!')
#         break







#
# day = int(input('День рождения? '))
# month = int(input('Месяц рождения? '))
# if day >= 21 and day<=31 and month==3 or day>=1 and day<=20 and month==4:
#     print('Вы овен ')
# else:
#     print('Вы не овен')

#and or not
# Овен 21 март по 20 апреля

# quest = str(input('Вы болели сегодня? '))
# if quest == 'Да':
#     print('Спи дальше!!!')
# elif quest == 'Нет':
#     print('Иди в школу!!!')
# else:
#     print('Не придуривайся!!!')

# > < >= <= ! ==


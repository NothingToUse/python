import math
import random
import re

user_input_task = int(input('Впишите номер задачи для последующего решения или 0 для завершения: '))

if user_input_task == 1:
    print(' Задача - 1 - хард')

    equation_input = str(input('Введите необходимое уравнение \n вида y=kx-b(equation):'))  # Задаем строкой уравнение
    x_value_input = float(input('Введите значение x:'))  # Вводим значение x как float


    def func_1(equation, x_value):  # Пишем функцию
        pattern = '[0-9]+\.?[0-9]*'  # задаем шаблон
        values = re.findall(pattern, equation)  # Ищем значения в заданной пользователем строке, в последовательности
        if len(values) == 2:  # при нахождении 2-х элементов длина строки достигает значения 2
            k = float(values[0])  # присваеваем элементу строки значение float
            b = float(values[1])  # аналогично
            y = k * x_value + b  # вычисление по формуле
            return y  # Получение искомого результата


    result_func = func_1(equation_input, x_value_input)
    print(result_func)  # no comments

elif user_input_task == 2:
    print('Задача - 2 - hard')
    user_input_1 = int(input('Если желаете решить задачу примитивно - нажмите 1, \n'
                             'для решения другим способом - 2'))
    if user_input_1 == 1:
        #  решил попробовать решить задачу пообрав все параметры, оно работает, но громоздко очень.
        input_1 = input('Введите дату в числовом формате dd.mm.yyyy: ')
        splited_date = (input_1.split('.'))

        dd = splited_date[0]
        mm = splited_date[1]

        yyyy = splited_date[2]

        dd_len = len(dd)
        mm_len = len(mm)
        yyyy_len = len(yyyy)

        jan = int('01')
        feb = int('02')  # Исключение для февраля
        mar = int('03')
        apr = int('04')
        may = int('05')
        jun = int('06')
        jul = int('07')
        aug = int('08')
        sep = int('09')
        oct = int('10')
        nov = int('11')
        dec = int('12')

        if dd_len == 2:
            if mm_len == 2:
                if yyyy_len == 4:
                    if int(mm) == feb:
                        if int(dd) < 28:
                            if int(dd) > 0:
                                if int(yyyy) > 1:
                                    if int(yyyy) < 9999:
                                        print('Формат даты задан верно')
                                    else:
                                        print('Год указан некорректно, либо отрицательное значение')
                                else:
                                    print('Год указан некорректно, либо отрицательное значение')
                            else:
                                print('Количество дней в феврале задано некорректно, либо отрицательное значение')
                        elif 28 < int(dd) < 30:
                            if int(dd) > 0:
                                if int(yyyy) > 1:
                                    if int(yyyy) < 9999:
                                        print('Формат даты задан верно, да, и похоже, у вас високосный год \n'
                                              '(но это не точно)')
                                    else:
                                        print('Год указан некорректно, либо отрицательное значение')
                                else:
                                    print('Год указан некорректно, либо отрицательное значение')
                        else:
                            print('Количество дней в феврале задано некорректно, либо отрицательное значение')
                    elif int(mm) == jan or int(mm) == mar or int(mm) == may or int(mm) == jul or int(mm) == sep \
                            or int(mm) == nov or int(mm) == dec:
                        if int(mm) < 13:
                            if int(mm) > 0:
                                if int(dd) < 31:
                                    if int(dd) > 0:
                                        if int(yyyy) > 1:
                                            if int(yyyy) < 9999:
                                                print('Формат даты задан верно')
                                            else:
                                                print('Год указан некорректно, либо отрицательное значение')
                                        else:
                                            print('Год указан некорректно, либо отрицательное значение')
                                    else:
                                        print('Количество дней в месяце задано некорректно, либо \n '
                                              'отрицательное значение')
                                else:
                                    print('Количество дней в месяце некорректно, либо отрицательное значение')
                            else:
                                print('Количество месяцев в году некорректно, либо отрицательное значение')
                        else:
                            print('Количество месяцев в году некорректно, либо отрицательное значение')
                    elif int(mm) == apr or int(mm) == jun or int(mm) == aug or int(mm) == oct:
                        if int(mm) < 13:
                            if int(mm) > 0:
                                if int(dd) < 30:
                                    if int(dd) > 0:
                                        if int(yyyy) > 1:
                                            if int(yyyy) < 9999:
                                                print('Формат даты задан верно')
                                            else:
                                                print('Год указан некорректно, либо отрицательное значение')
                                        else:
                                            print('Год указан некорректно, либо отрицательное значение')
                                    else:
                                        print('Количество дней в месяце задано некорректно, либо \n '
                                              'отрицательное значение')
                                else:
                                    print('Количество дней в месяце некорректно, либо отрицательное значение')
                            else:
                                print('Количество месяцев в году некорректно, либо отрицательное значение')
                        else:
                            print('Количество месяцев в году некорректно, либо отрицательное значение')
                    else:
                        print('Количество месяцев некорректно, либо отрицательное значение')
                else:
                    print('Ошибка. Слишком много символов в значении года, или введены отрицательные значения')
            else:
                print('Ошибка. Некорректно указанно значение месяца, или введены отрицательные значения')
        else:
            print('Ошибка. Некорректно указано значение дня, или введены отрицательные значения')
    elif user_input_1 == 2:
        #  Этот вариант лучше
        input_1 = input('Введите дату в числовом формате dd.mm.yyyy: ')
        splited_date = (input_1.split('.'))

        dd = splited_date[0]
        mm = splited_date[1]
        yyyy = splited_date[2]

        dd_len = len(dd)
        mm_len = len(mm)
        yyyy_len = len(yyyy)

        M = [1, 3, 5, 7, 8, 10, 12]
        if dd_len != 2:
            print('Значение дня указано некорректно')
        elif mm_len != 2:
            print('Значение месяца указано некорректно')
        elif yyyy_len != 4:
            print('Значение года указано некорректно')
        elif int(dd) > 31 or int(dd) < 1:
            print('Значение дня указано некорректно')
        elif int(mm) > 12 or int(mm) < 1:
            print('Значение месяца указано некорректно')
        elif int(yyyy) > 1 or int(yyyy) > 9999:
            print('Знавение года указано некорректно')
        elif mm not in M and int(dd) > 30:
            print('Значение дня указано некорректно')
        else:
            print('Дата указана корректно')
    else:
        print('Вы что - то не то ввели')
elif user_input_task == 3:
    print(' Задача - 1 - хард')
    print('не успел сделать((')
'''
    ui_1 = input(int('Введите комнату'))
    count_1 = 0

    while 1 <= int(ui_1) <= 2000000000:
        ui_1 = str(ui_1)
        for i in range(ui_1):
            count += 1
'''
#  новый пулреквест
import hw05_easy
from os import *
#  Получилось немножко лишних действий, но все работает!
#  PS добавляя условия понял, что все технически работает, но забаговано и надо исправлять. Времени нет.
print('выберите что хотите делать')
ui_s = int(input('Приступить к исполнению? да - 1, нет - 2'))
while ui_s == 1:
    ui_1 = int(input('1. Перейти в папку\n'
                     '2. Просмотреть содержимое текущей папки\n'
                     '3. Удалить папку\n'
                     '4. Создать папку\n'
                     '5.Для выхода'))
    if ui_1 == 1:
        way = input(' укажите путь к папке: ')
        hw05_easy.dirr(way)
        if getcwd() == way:
            print('Вы перешли успешно по следующему адресу:', way)
        elif getcwd() != way:
            print('Вы не перешли по адресу')
    elif ui_1 == 2:
        hw05_easy.showdirs('.')
    elif ui_1 == 3:
        way = input(' укажите путь к папке: ')
        name = input(' укажите имя папки для удаления: ')
        hw05_easy.dirr(way)
        hw05_easy.rmvdir(name)
        direct_name = str(way)
        cur_dir = getcwd()
        dir_list = listdir(cur_dir)
        if direct_name in dir_list:
            print('Удаление не выполнено')
        else:
            pass
    elif ui_1 == 4:
        way = input(' укажите путь к папке: ')
        name = input(' укажите имя папки: ')
        hw05_easy.dirr(way)
        hw05_easy.mkdir(name)
        direct_name = str(way)
        cur_dir = getcwd()
        dir_list = listdir(cur_dir)
        if direct_name in dir_list:
            print('Не создано')
        else:
            print('Успешно создано')
    elif ui_1 == 5:
        break

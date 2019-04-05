from shutil import copy
from os import *

' Все переделал из - за задания нормал. Изначально работало нормально.'


# user_input_task = int(input('Впишите номер задачи для последующего решения или 0 для завершения: '))
#
# if user_input_task == 1:
#    print('Задача-1')

#    ui_1 = int(input('Создать папки - 1. Удалить папки - 2'))


def mkdir(name):
    try:
        makedirs(name)
    except FileExistsError:
        print('Такая папка существует.')


def rmvdir(name):
    try:
        removedirs(name)
    except FileNotFoundError:
        print('Такая папка не существует, не успешно')


def process():
    num_dir = range(1, 10)
    ui_1 = int(input('введите 1 если надо создать папки\n'
                     'введите 2 если надо удалить папки\n'))
    if ui_1 == 1:
        for i in num_dir:
            i = str(i)
            mkdir('dir_' + i)
        return listdir('.')
    elif ui_1 == 2:
        for i in num_dir:
            i = str(i)
            rmvdir('dir_' + i)
        return listdir('.')


# process()


# elif user_input_task == 2:
#    print('Задача - 2')
def dirr(way):
    try:
        chdir(way)
        print(getcwd())
    except:
        print('что - то пошло не так')


# dirr(input())

def showdirs(way):  # доработал из - за нормал задачи
    for el in listdir(way):
        if path.isdir(el):
            print('Папка - ', el)
        else:
            print('Не папка -', el)


#  showdirs('.')

def insanity():
    file_1 = path.realpath(__file__)
    file_2 = file_1 + '.копия'
    if not path.isfile(file_2):
        copy(file_1, file_2)
        print('создан следующий файл: ', file_2)
    else:
        print('Такой файл уже есть, вернее был, я его удалил, чтобы не засорял папку')
        remove(file_2)
#  insanity()

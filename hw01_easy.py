__author__ = 'Лукичев А.В.'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
import random

user_input = random.randint(1, 9999999999)

for i in user_input:
    print(int(i))

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

user_input_1 = input('Введите первую переменную: ')
user_input_2 = input('Введите вторую переменную: ')

var_1 = user_input_1
user_input_1 = user_input_2
user_input_2 = var_1

print(user_input_1, user_input_2)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

user_input = input('Введите, пожалуйста Ваш возраст: ')

if int(user_input) >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')

from random import *

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""


class Card:
    def __init__(self, name):
        bag = [i for i in range(0, 90)]
        self.card = [
            __class__.gen_string(bag),
            __class__.gen_string(bag),
            __class__.gen_string(bag)
        ]
        self.name = name
        self.count_barrels = 15

    @staticmethod
    def gen_string(bag):
        string = ['' for _ in range(9)]
        for i in range(8, 3, -1):
            dig = randint(0, i)
            while string[dig] != '':
                dig += 1
            string[dig] = bag.pop(randint(0, len(bag) - 1))
        return string

    def __str__(self):
        res = '{:-^26}\n'.format(self.name)
        for i in range(3):
            res += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}' \
                       .format(*self.card[i]) + '\n'
        return res + '\n**************************\n'


player = Card(' Игрок ')
computer = Card(' Компьютер ')

bag = [i for i in range(0, 90)]  # Мешок с бочками.
while True:
    if len(bag) < 1:
        print('Бочонки закончились. Результат:\n'
              'у компьютера осталось {} числа/чисел,\n'
              'у игрока осталось {} числа/чисел.'.format(
            computer.count_barrels, player.count_barrels))
        break
    barrels = bag.pop(randint(0, len(bag) - 1))
    print('\nНовый бочонок: {} (осталось {})'.format(barrels, len(bag)))
    print(computer)
    print(player)
    ui_1 = input('Зачеркнуть цифру? (y/n/q)')
    ui_1 = ui_1.lower()
    while len(ui_1) == 0 or ui_1 not in 'ynq':
        print('\n\nНезивестный ввод\n')
        print('Новый бочонок: {} (осталось {})'.format(barrels, len(bag)))
        print(computer)
        print(player)
        ui_1 = input('Зачеркнуть цифру? (y/n/q)')
        ui_1 = ui_1.lower()

    if ui_1 == 'q':
        print('Выход')
        break
    elif ui_1 == 'y':
        test = False
        for i in range(3):
            if barrels in player.card[i]:
                test = True
                player.card[i][player.card[i].index(barrels)] = 'X'
                player.count_barrels -= 1
            if barrels in computer.card[i]:
                computer.card[i][computer.card[i].index(barrels)] = 'X'
                computer.count_barrels -= 1
        if test:
            if player.count_barrels < 1:
                print('Вы победили.')
                break
            elif computer.count_barrels < 1:
                print('Компьютер победил.')
                break
        else:
            print('Такого числа в вашей карточке нет, вы проиграли. ')
            break
    elif ui_1 == 'n':
        test = False
        for i in range(3):
            if barrels in player.card[i]:
                print('Проворонили число! Вы проиграли. ')
                test = True
                break
            if barrels in computer.card[i]:
                computer.card[i][computer.card[i].index(barrels)] = 'X'
                computer.count_barrels -= 1
        if test:
            break
        if player.count_barrels < 1:
            print('Вы выиграли')
            break
        elif computer.count_barrels < 1:
            print('Компьютер выиграл')
            break
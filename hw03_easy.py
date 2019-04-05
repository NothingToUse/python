import random
import math
user_input_task = int(input('Впишите номер задачи для последующего решения или 0 для завершения: '))

if user_input_task == 1:
        print("Задача-1: ")

        def my_round(number, ndigits):
            number = number * (10 ** ndigits) + 0.4
            number = number // 1
            return number / (10 ** ndigits)


        print(my_round(2.1234567, 5))
        print(my_round(2.1999967, 5))
        print(my_round(2.9999967, 5))

elif user_input_task == 2:
    print("Задача-2")
#  простите, захотелось чет написать длинно((


    def lucky_ticket(ticket_number):
        sub5 = math.floor(ticket_number % 10)
        sub4 = math.floor((ticket_number / 10) % 10)
        sub3 = math.floor((ticket_number / 100) % 10)
        sub2 = math.floor((ticket_number / 1000) % 10)
        sub1 = math.floor((ticket_number / 10000) % 10)
        sub0 = math.floor((ticket_number / 100000) % 10)

        lucky_1 = sub0 + sub1 + sub2
        lucky_2 = sub3 + sub4 + sub5

        if lucky_1 == lucky_2:
            return 'счастливый'
        else:
            return 'не счастлиый'


    print(lucky_ticket(123006))
    print(lucky_ticket(12321))
    print(lucky_ticket(436751))
    print(lucky_ticket(374357))



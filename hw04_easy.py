import random
import math
user_input_task = int(input('Впишите номер задачи для последующего решения или 0 для завершения: '))

if user_input_task == 1:
    print("Задача-1: ")

    first_list = [random.randint(-100, 100) for _ in range(20)]
    second_list = [a ** 2 for a in first_list]
    print(second_list)


elif user_input_task == 2:
    print("Задача-2")

    fruits_1 = ['apple', 'banana', 'watermelon', 'blackberry', 'fruit_number_six']
    fruits_2 = ['banana', 'pineapple', 'fruit_number_three', 'fruit_number_four']

    new_list = list(set(fruits_1) & set(fruits_2))
    print(new_list)

elif user_input_task == 3:
    print("Задача - 3")

    first_list = [random.randint(-100, 100) for _ in range(15)]
    second_list = [el for el in first_list if el % 3 == 0 and el >= 0 and el % 4 != 0]
    print(first_list)
    print(second_list)


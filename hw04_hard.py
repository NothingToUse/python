user_input_task = int(input('Впишите номер задачи для последующего решения или 0 для завершения: '))

if user_input_task == 1:
    print('Задача-1')
    matrix = [[1, 0, 8],
              [3, 4, 1],
              [0, 4, 2]]
    print(list(map(list, zip(*matrix))))


elif user_input_task == 2:
    print('Сорри, не сделал')


elif user_input_task == 3:
    print('Сорри, не сделал')

elif user_input_task == 4:
    pass

#  Хард не успеваю, простите, сделаю в след раз.
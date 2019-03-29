import random
import math

user_input_task = int(input('Впишите номер задачи для последующего решения или 0 для завершения: '))

if user_input_task == 1:
    print('Задача-1')


    def whataboutlist(lenth):  # создаем список чисел фибоначчи
        if lenth == 0:
            return [1]
        elif lenth == 1:
            return [1, 1]
        else:
            flist = whataboutlist(lenth - 1)
            flist.append(flist[-1] + flist[-2])
        return flist


    #  я тут пытался сначала через две функции, работает только эта^^.
    #   разберусь потом
    n = int(input('Введите начальный номер элемента списка фибоначчи'))
    m = int(input('Введите второй номер элемента списка фибоначчи'))


    def fibonacci(n, m):
        fibon_list = []
        a, b = 1, 1
        for num in range(m):
            fibon_list.append(b)
            a, b = b, a + b
        n -= 1
        result = [fibon_list[i] for i in range(n, m)]
        del fibon_list
        return result


    print(fibonacci(n, m))
    print(whataboutlist(99)[n], 'Независимая проверка начального числа фибоначчи')
    print(whataboutlist(99)[m], 'Независимая проверка финального числа фибоначчи')
elif user_input_task == 2:
    print('Задача - 2')
    #  origin_list = float(input()
    origin_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]


    def sort_to_max(origin_list):
        def m_num(l):
            m_el = float('inf')
            for el in l:
                if el < m_el:
                    m_el = el
            return m_el

        action = [x for x in origin_list]
        result = []
        while len(action):
            for el in action:
                if el == m_num(action):
                    result.append(el)
                    action.remove(el)
        return result


    print(sort_to_max(origin_list))

elif user_input_task == 3:
    print('Задача - 3')

    def func_filter(func, itr):
        newitr = [el for el in itr if func(el)]
        if type(itr) is str:
            newitr = str(newitr)
        elif type(itr) is int:
            newitr = int(newitr)
        elif type(itr) is float:
            newitr = float(newitr)
        elif type(itr) is set:
            newitr = set(newitr)
        elif type(itr) is tuple:
            newitr = tuple(newitr)
        return newitr

elif user_input_task == 4:
    print('Задача - 4')

    xA = float(input('Введите x первой вершины'))
    yA = float(input('Введите y первой вершины'))
    xB = float(input('Введите x второй вершины'))
    yB = float(input('Введите y второй вершины'))
    xC = float(input('Введите x третьей вершины'))
    yC = float(input('Введите y третьей вершины'))
    xD = float(input('Введите x четвертой вершины'))
    yD = float(input('Введите y четвертой вершины'))

    A = float(xA), float(yA)
    B = float(xB), float(yB)
    C = float(xC), float(yC)
    D = float(xD), float(yD)

    def par(A, B, C, D):  #  проверки по этому правилу, полагаю, достаточно
        AB = math.sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2)
        AD = math.sqrt((D[0] - A[0]) ** 2 + (D[1] - A[1]) ** 2)
        BC = math.sqrt((B[0] - C[0]) ** 2 + (B[1] - C[1]) ** 2)
        CD = math.sqrt((D[0] - C[0]) ** 2 + (D[1] - C[1]) ** 2)

        if AB == CD and BC == AD:
            print('Cумма квадратов диагоналей параллелограмма \n'
                  'равна сумме квадратов его сторон, соответственно, \n'
                  'заданные вершины являются вершинами параллелограмма')
        else:
            print('Эти вершины - не вершины параллелограмма')
    par(A, B, C, D)
#  Хард не успеваю, простите, сделаю в след раз.
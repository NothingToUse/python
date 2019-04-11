from math import *

user_input_task = int(input('Впишите номер задачи для последующего решения или 0 для завершения: '))

if user_input_task == 1:
    print('Задача 1')


    #  с математикой и геометрией не в ладах, но вот что - то считает, и это хорошо.
    class Triangle:

        def __init__(self, ax, ay, bx, by, cx, cy):
            self.ax = ax
            self.ay = ay
            self.bx = bx
            self.by = by
            self.cx = cx
            self.cy = cy
            self.ab = round(sqrt(int(fabs((by - ay) ** 2) + ((bx - ax) ** 2))))
            self.ca = round(sqrt(int(fabs((ay - cy) ** 2) + ((ax - cx) ** 2))))
            self.bc = round(sqrt(int(fabs((cy - by) ** 2) + ((cx - bx) ** 2))))

        def perimeter(self):
            perimeter = self.ab + self.bc + self.ca
            return perimeter

        def square(self):
            square = round(sqrt(((self.ab + self.bc + self.ca) / 2) * (
                    ((self.ab + self.bc + self.ca) / 2) - self.ab) * (((self.ab + self.bc + self.ca) / 2) - self.bc)
                                * (((self.ab + self.bc + self.ca) / 2) - self.ca)))
            return square

        def height(self):
            height = round((sqrt(((self.ab + self.bc + self.ca) / 2) * (
                    ((self.ab + self.bc + self.ca) / 2) - self.ab) * (((self.ab + self.bc + self.ca) / 2) - self.bc)
                                 * (((self.ab + self.bc + self.ca) / 2) - self.ca))) * 2) / self.ca
            return height


    triangle_1 = Triangle(2, 2, 3, 6, -2, 4)
    print('Длина стороны AB: ', triangle_1.ab)
    print('Длина стороны CA: ', triangle_1.ca)
    print('Длина стороны BC: ', triangle_1.bc)
    print('Периметр треугольника: ', triangle_1.perimeter())
    print('Площадь треугольника: ', triangle_1.square())
    print('Высота треугольника: ', triangle_1.height())

elif user_input_task == 2:
    print('Задача 2')


    class Trapezium:

        def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):

            self.ax = ax
            self.ay = ay

            self.bx = bx
            self.by = by

            self.cx = cx
            self.cy = cy

            self.dx = dx
            self.dy = dy

            self.a = int((self.bx - self.ax) + (self.by - self.ay))
            self.b = int((self.cx - self.bx) + (self.cy - self.by))
            self.c = int((self.dx - self.cx) + (self.dy - self.cy))
            self.d = int((self.ax - self.dx) + (self.ay - self.dy))

        def check_trap(self):
            if ((self.a == self.c) and ((dx - ax) / self.d) == ((cx - bx) / self.b)) or ((self.b == self.d) and
                                                                                         ((cx - dx) / self.c) ==
                                                                                         ((bx - ax) / self.a)):
                print('Трапеция равносторонняя')
                return True
            elif ((self.a == self.c) and (self.b == self.d)) or ((self.b == self.d) and (self.c == self.a)):
                print('Трапеция равносторонняя')
                return True
            else:
                print('Трапеция не равносторонняя')
                return False

        def midline(self):
            mid = (self.a + self.b) / 2
            return mid

        def height(self):
            height = sqrt((((self.c ** 2) - (((self.a - self.b) ** 2) + (self.c ** 2) - (self.d ** 2)) / (2 *
                                                                                                self.a - self.b))) ** 2)
            return height

        def square_trap(self):
            square = ((self.a + self.b) / 2 * (sqrt((((self.c ** 2) - (((self.a - self.b) ** 2) + (self.c ** 2) -
                                                                       (self.d ** 2)) / (2 * self.a - self.b))) ** 2)))
            return square


    trap_1 = Trapezium(3, 2, 5, 2, 9, 6, 6, 6)
    print(' Сторона а: ', trap_1.a)
    print(' Сторона b: ', trap_1.b)
    print(' Сторона c: ', trap_1.c)
    print(' Сторона d: ', trap_1.d)
    print(' Мидлайн: ', trap_1.midline())
    print(' Высота: ', trap_1.height())
    print(' Площадь: ', trap_1.square_trap())
    print(trap_1.check_trap())

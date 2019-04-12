'''class Class:
    def __init__(self, class_room):
        self.class_room = {'class_n': int(class_room.split()[0]), 'class_liter': class_room.split()[1]}

    def get_name(self):
        return str(self.class_room['class_n']) + ' ' + self.class_room['class_liter']


class Personal:
    def __init__(self, name, surname, father_n, birth):
        self.name = name
        self.surname = surname
        self.father_n = father_n
        self.birth = birth

    def specifications(self):
        return self.surname + ' ' + self.name[:1] + '.' + self.father_n[:1] + '.'


class Pupil(Personal):
    def __init__(self, name, surname, father_n, birth, class_room, father, mother):
        Personal.__init__(self, name, surname, father_n, birth)
        self.class_room = class_room
        self.mother = mother
        self.father = father

    def get_class_room(self):
        return self.class_room

    def get_parents(self):
        return self.father.specifications(), self.mother.specifications()


class Teacher(Personal):
    def __init__(self, name, surname, father_n, birth, classes, subject):
        Personal.__init__(self, name, surname, father_n, birth)
        self.classes = classes
        self.subject = subject

    def get_subj(self):
        return self.subject

    def get_cls(self):
        return self.classes


class_rooms = ['7 B', '3 A', '9 A']
parents = [Personal("name1", "surname1", "fathname1", "01.01.1980"),
           Personal("name2", "surname2", "fathname2", "01.02.1980"),
           Personal("name3", "surname3", "fathname3", "01.03.1980"),
           Personal("name4", "surname4", "fathname4", "01.04.1980"),
           Personal("name4", "surname4", "fathname4", "01.05.1980"),
           Personal("name4", "surname4", "fathname4", "01.06.1980")]
pupils = [Pupil("name1-1", "surname1-1", "fathname1-1", '01.01.2000', class_rooms[0], parents[2], parents[3]),
          Pupil("name2-1", "surname1-2", 'fathname1-1', '01.02.2000', class_rooms[2], parents[0], parents[1]),
          Pupil("name3-1", "surname1-3", 'fathname1-1', '01.03.2000', class_rooms[1], parents[2], parents[3])]
teachers = [Teacher("teach1", "teach1-1", "teach2-1", "01.01.1975", [class_rooms[0], class_rooms[1]], 'subj1'),
            Teacher("teach2", "teach1-2", "teach2-2", "01.02.1975", [class_rooms[2], class_rooms[1]], 'subj2'),
            Teacher("teach3", "teach1-3", "teach2-3", "01.03.1975", [class_rooms[0], class_rooms[2]], 'subj3')]

print(' ')
pup = set([i.get_class_room() for i in pupils])
print(class_rooms)
print(pup)
print(' ')
print(' ')
cls_room = '7 B'
pup_list = [i.specifications() for i in pupils if i.get_class_room() == cls_room]
print(pup_list)
print(' ')
print(' ')

print(' ')
print(' ')
par = pupils.get_parents()
print(par)
print(' ')
print(' ')
teach_list = [i.specifications for i in teachers if cls_room in i.get_cls]
print(teach_list)'''


class People:
    def __init__(self, Name):
        self.Name = Name

    def full_name(self):
        sname = self.Name.split(' ')
        return sname[0] + ' ' + sname[1][0] + '.' + sname[2][0] + '.'

class Teacher(People):
    def __init__(self, Name, Subject):
        super().__init__(Name)
        self.Subject = Subject
        self.teachers_sub = {self.Name: self.Subject}

class Students(People):
    def __init__(self, Name, mother, father, classnum):
        super().__init__(Name)
        self.mother = mother
        self.father = father
        self.classnum = classnum

class classes():
    def __init__(self, classnum, *Name):
        self.Name = Name
        self.classnum = classnum

stud = [Students('Blah, Hoo, Www', 'JDsa Adasf Lfjdgj', 'Asafg Jgkdf Olglh', '5A'),
        Students('Blahsada, Hoo2, Www2', 'JDsa1 Adasf Lfjdgj', 'Asafgeg Jgkdf Olglh', '5A'),
        Students('Blahdasd, Hoo3, Www3', 'JDsa12 Adascdb Lfjdgjmmm', 'Asafgwe Jgkdf Olglh', '6A'),
        Students('Blahczx, Hoo4, Www4', 'JDsa3 Adasfef Lfjdgjcn', 'Asafg Jgkdfeq Olglhc', '6A'),
        Students('Blahasd, Hoo5, Www5', 'JDsa4 Adasfee Lfjdgjzz', 'Asafgyh Jgkdf Olglh45', '5B'),
        Students('Blahrqr, Hoo6, Www6', 'JDsa5 Adasfeerr Lfjdgjsd', 'Asafgdg Jgkdfxc Olglh', '5B'),
        Students('Blah22, Hoo7, Www7', 'JDsa6 Adasfy Lfjdgjeqw', 'Asafgc Jgkdf Olglhc', '7A'),
        Students('Blah, Hoo, Www', 'JDsa Adasf Lfjdgj', 'Asafg Jgkdf Olglh', '5A'),
        Students('Blahsada, Hoo2, Www2', 'JDsa1 Adasf Lfjdgj', 'Asafgeg Jgkdf Olglh', '5A'),
        Students('Blahdasd, Hoo3, Www3', 'JDsa12 Adascdb Lfjdgjmmm', 'Asafgwe Jgkdf Olglh', '6A'),
        Students('Blahczx, Hoo4, Www4', 'JDsa3 Adasfef Lfjdgjcn', 'Asafg Jgkdfeq Olglhc', '6A'),
        Students('Blahasd, Hoo5, Www5', 'JDsa4 Adasfee Lfjdgjzz', 'Asafgyh Jgkdf Olglh45', '5B'),
        Students('Blahrqr, Hoo6, Www6', 'JDsa5 Adasfeerr Lfjdgjsd', 'Asafgdg Jgkdfxc Olglh', '5B'),
        Students('Blah22, Hoo7, Www7', 'JDsa6 Adasfy Lfjdgjeqw', 'Asafgc Jgkdf Olglhc', '7A'),
        Students('Blah, Hoo, Www', 'JDsa Adasf Lfjdgj', 'Asafg Jgkdf Olglh', '5A'),
        Students('Blahsada, Hoo2, Www2', 'JDsa1 Adasf Lfjdgj', 'Asafgeg Jgkdf Olglh', '5A'),
        Students('Blahdasd, Hoo3, Www3', 'JDsa12 Adascdb Lfjdgjmmm', 'Asafgwe Jgkdf Olglh', '6A'),
        Students('Blahczx, Hoo4, Www4', 'JDsa3 Adasfef Lfjdgjcn', 'Asafg Jgkdfeq Olglhc', '6A'),
        Students('Blahasd, Hoo5, Www5', 'JDsa4 Adasfee Lfjdgjzz', 'Asafgyh Jgkdf Olglh45', '5B'),
        Students('Blahrqr, Hoo6, Www6', 'JDsa5 Adasfeerr Lfjdgjsd', 'Asafgdg Jgkdfxc Olglh', '5B'),
        Students('Blah22, Hoo7, Www7', 'JDsa6 Adasfy Lfjdgjeqw', 'Asafgc Jgkdf Olglhc', '7A'),
        Students('Blah, Hoo, Www', 'JDsa Adasf Lfjdgj', 'Asafg Jgkdf Olglh', '5A'),
        Students('Blahsada, Hoo2, Www2', 'JDsa1 Adasf Lfjdgj', 'Asafgeg Jgkdf Olglh', '5A'),
        Students('Blahdasd, Hoo3, Www3', 'JDsa12 Adascdb Lfjdgjmmm', 'Asafgwe Jgkdf Olglh', '6A'),
        Students('Blahczx, Hoo4, Www4', 'JDsa3 Adasfef Lfjdgjcn', 'Asafg Jgkdfeq Olglhc', '6A'),
        Students('Blahasd, Hoo5, Www5', 'JDsa4 Adasfee Lfjdgjzz', 'Asafgyh Jgkdf Olglh45', '5B'),
        Students('Blahrqr, Hoo6, Www6', 'JDsa5 Adasfeerr Lfjdgjsd', 'Asafgdg Jgkdfxc Olglh', '5B'),
        Students('Blah22, Hoo7, Www7', 'JDsa6 Adasfy Lfjdgjeqw', 'Asafgc Jgkdf Olglhc', '7A')]


teach = [Teacher('Teach1 Gasd Tgsdg', 'Python'),
         Teacher('Teacher2 Ksdfkg Nnbd', 'C++'),
         Teacher('Teacher3 Jfdjj Ldkff', 'C#'),
         Teacher('Teacher4 Kaksfdk Ldasd', 'Java'),
         Teacher('Teach1 Gasd Tgsdg', 'Python'),
         Teacher('Teacher2 Ksdfkg Nnbd', 'C++'),
         Teacher('Teacher3 Jfdjj Ldkff', 'C#'),
         Teacher('Teacher4 Kaksfdk Ldasd', 'Java')]

class_sb = [classes('5', teach[3], teach[4], teach[5]),
            classes('6', teach[3], teach[4], teach[5], teach[6], teach[0]),
            classes('7', teach[3], teach[4], teach[5], teach[6], teach[0], teach[1], teach[2])]

print(' Выберите действие: \n 1. Получить полный список классов школы \n 2. Получить полный список учеников в указанном'
      ' классе \n 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы), \n'
      '4. Узнать ФИО родителей указанного ученика \n Получить список всех Учителей, преподающих в указанном классе')
try:

    operation = '!'
    while operation != 0:
        operation = int(input('Введите номер операции: '))
        if operation == 1:
            clas_list = []
            i = 0
            while i < len(stud):
                clas_list.append(stud[i].classnum)
                i += 1
            print(set(clas_list))
        elif operation == 2:
            cls = input('Введите номер класса: ')
            print('Список учащихся в данном классе: ')
            for line in stud:
                if line.classnum == cls:
                    print(line.full_name())
        elif operation == 3:
            name = input('Укажите ФИО ученика: ')
            for line in stud:
                if name == line.Name:
                    print('{}, учащийся {} класса \nИзучает предметы: '.format(name, classnum))
                    for tch in clas_sb:
                        if tch.classnum == line.classnum[0]:
                            for nameClas in tch.Name:
                                for nameTeach in teach:
                                    if nameClas.Name == nameTeach.Name:
                                        print(nameTeach.teachers_sub[nameTeach.Name])
        elif operation == 4:
            name = input('Укажите имя ученика:')
            for line in stud:
                if name == line.Name:
                    print('Mom: ', line.mother, 'Dad: ', line.father)
        elif operation == 5:
            clas = input('Укажите класс, для получения списка учителей: ')
            print('Учительский состав класса {}'.format(clas))
            for line in clas_sb:
                if clas[0] == line.classnum:
                    for i in line.classnum:
                        print(i.Name)
        elif operation == 0:
            break
        else:
            print('Неверная команда')

except ValueError:
    print('Неверная команда')
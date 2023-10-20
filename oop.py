class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
        
class Student(Mentor):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in course in self.courses_in_progress and course in lecturer.lecturer_courses:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'
        


# print(some_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование

    def average_grade(self):
        total_grades = 0
        total_count = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            total_count += len(grades)
        if total_count == 0:
            return 0
        return round(total_grades / total_count, 2)

    
    def __str__(self):
        completed_courses = ", ".join(self.finished_courses)
        in_progress_courses = ", ".join(self.courses_in_progress)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {in_progress_courses}\nЗавершенные курсы: {completed_courses}"

    def __lt__(self, other):
        return self.average_grade < other.average_grade

    # def lt(self, other):
    #     if aver_stud(self) >= aver_stud(other):
    #         return
    #     return aver_stud(self) < aver_stud(other)
        
    # def __str__(self):
    #     res =f"Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за домашние задания:{self.mean_grade}\nКурсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_courses = []
        self.lecturer_grades = {}


    def average_grade(self):
        total_grades = 0
        total_count = 0
        for grades in self.lecturer_grades.values():
            total_grades += sum(grades)
            total_count += len(grades)
        if total_count == 0:
            return 0
        return round(total_grades / total_count, 2)

# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9
    # def __str__(self):
    #     res =f"Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции:{self.average_grade}"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}"

    def __lt__(self, other):
        return self.average_grade < other.average_grade

    
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
# print(some_reviewer)
# Имя: Some
# Фамилия: Buddy
    def __str__(self):
        res = f"Имя:{self.name}\nФамилия:{self.surname}"
        return res
        
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']
best_student.grades = {'Python': [9,8], 'Git': [10, 9] } 

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.lecturer_courses += ['Python']
cool_lecturer.lecturer_grades = {'Python': [9, 10]}

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)



cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)

print(best_student.grades)
print(cool_lecturer.lecturer_grades)



print(cool_reviewer)
print(cool_lecturer)
print(best_student)

student1 = Student('John', 'Doe', 'Мужской')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']
student1.grades = {'Python': [9, 8], 'Git': [10, 9]}

student2 = Student('Alice', 'Smith', 'Женский')
student2.courses_in_progress += ['Python', 'JavaScript']
student2.finished_courses += ['Английский']
student2.grades = {'Python': [10, 9], 'JavaScript': [8, 7]}



lecturer1 = Lecturer('John', 'Doe')
lecturer1.lecturer_courses += ['Python']
lecturer1.lecturer_grades = {'Python': [9, 10]}

lecturer2 = Lecturer('Alice', 'Smith')
lecturer2.lecturer_courses += ['Python', 'JavaScript']
lecturer2.lecturer_grades = {'Python': [10, 9], 'JavaScript': [8, 7]}

print(student1.average_grade() > student2.average_grade())

print(lecturer1.average_grade() > lecturer2.average_grade())


def average_hw_grade(students, course):
    total_grades = 0
    total_count = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_count += len(student.grades[course])
    if total_count == 0:
        return 0
    return round(total_grades / total_count, 2)


def average_lecture_grade(lecturers, course):
    total_grades = 0
    total_count = 0
    for lecturer in lecturers:
        if course in lecturer.lecturer_grades:
            total_grades += sum(lecturer.lecturer_grades[course])
            total_count += len(lecturer.lecturer_grades[course])
    if total_count == 0:
        return 0
    return round(total_grades / total_count, 2)


course_name = 'Python'
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

average_hw = average_hw_grade(students, course_name)
average_lecture = average_lecture_grade(lecturers, course_name)

print(f'Средняя оценка за домашние задания по курсу "{course_name}": {average_hw}')
print(f'Средняя оценка за лекции по курсу "{course_name}": {average_lecture}')





# Задание № 1. Наследование
# Исходя из квиза к предыдущему занятию, у нас уже есть класс преподавателей и класс студентов (вы можете взять этот код за основу или написать свой). Студентов пока оставим без изменения, а вот преподаватели бывают разные, поэтому теперь класс Mentor должен стать родительским классом, а от него нужно реализовать наследование классов Lecturer (лекторы) и Reviewer (эксперты, проверяющие домашние задания). Очевидно, имя, фамилия и список закрепленных курсов логично реализовать на уровне родительского класса. А чем же будут специфичны дочерние классы? Об этом в следующих заданиях.

# Задание № 2. Атрибуты и взаимодействие классов.
# В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки за домашние задания. Теперь это могут делать только Reviewer (реализуйте такой метод)! А что могут делать лекторы? Получать оценки за лекции от студентов :) Реализуйте метод выставления оценок лекторам у класса Student (оценки по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer, в котором ключи – названия курсов, а значения – списки оценок). Лектор при этом должен быть закреплен за тем курсом, на который записан студент.
# Задание № 3. Полиморфизм и магические методы
# Перегрузите магический метод __str__ у всех классов.
# У проверяющих он должен выводить информацию в следующем виде:

# print(some_reviewer)
# Имя: Some
# Фамилия: Buddy
# У лекторов:

# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9
# А у студентов так:

# print(some_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование
# Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.
# Задание № 4. Полевые испытания
# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:

# для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);
# для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса).

class Student:
    def __init__(self, name, surname, age, sex, student_id):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.student_id = student_id

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Возраст: {self.age}
Пол: {self.sex}
Номер студента: {self.student_id}
'''


def students_bubble_sort_by_age(students_list):
    for i in range(len(students_list)-1):
        for j in range(len(students_list)-i-1):
            if students_list[j].age > students_list[j+1].age:
                buff = students_list[j]
                students_list[j] = students_list[j+1]
                students_list[j+1] = buff


def binary_search_by_age(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while start <= end:
        step = step + 1
        mid = (start + end) // 2

        if element == array[mid].age:
            return mid

        if element < array[mid].age:
            end = mid - 1
        else:
            start = mid + 1
    return -1


students = [
    Student('ИВАН', 'ИВАНОВ', 20, 'М', '123123'),
    Student('ДАРЬЯ', 'КОЛЕСНИКОВА', 22, 'Ж', '456456'),
    Student('ИГОРЬ', 'АБЫШЕВ', 18, 'М', '789'),
    Student('КСЕНИЯ', 'САМОХИНА', 21, 'Ж', '456789'),
    Student('МАРИЯ', 'СВАРЩИКОВА', 19, 'Ж', '789123'),
    Student('АЛЕШАНДРЕ', 'МАЛУНГУ', 18, 'М', '852963')
]

for student in students:
    print(student)

students_bubble_sort_by_age(students)
print('-------------------------------------------------\n')

for student in students:
    print(student)

print(binary_search_by_age(students, 18))

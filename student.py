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


students = [
    Student('ИВАН', 'ИВАНОВ', 20, 'М', '123123'),
    Student('ДАРЬЯ', 'КОЛЕСНИКОВА', 22, 'Ж', '456456'),
    Student('ИГОРЬ', 'АБЫШЕВ', 18, 'М', '789'),
    Student('КСЕНИЯ', 'САМОХИНА', 21, 'Ж', '456789'),
    Student('МАРИЯ', 'СВАРЩИКОВА', 19, 'Ж', '789123'),
]

for student in students:
    print(student)
